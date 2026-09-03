import importlib.util
import json
import re
import unittest
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = PACKAGE_ROOT / "scientific-article-writing"


def load_script(name):
    path = SKILL_ROOT / "scripts" / name
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SkillStructureTests(unittest.TestCase):
    def test_runtime_skill_has_required_files(self):
        required = {
            "SKILL.md",
            "agents/openai.yaml",
            "references/evidence-contract.md",
            "references/workflow.md",
            "references/sections.md",
            "references/exemplar-model.md",
            "references/prose-quality.md",
            "references/style-guide.md",
            "references/reporting-standards.md",
            "references/submission-checklist.md",
            "assets/contribution-brief.md",
            "assets/manuscript-skeleton.md",
            "assets/figure-legend-template.md",
            "assets/exemplar-journal-model.json",
            "scripts/prose_diagnostics.py",
            "scripts/check_draft_invariants.py",
            "scripts/validate_writing_model.py",
        }
        present = {
            path.relative_to(SKILL_ROOT).as_posix()
            for path in SKILL_ROOT.rglob("*")
            if path.is_file() and "__pycache__" not in path.parts
        }
        self.assertTrue(required.issubset(present), required - present)

    def test_frontmatter_is_valid(self):
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        match = re.match(r"---\n(.*?)\n---\n", skill, re.DOTALL)
        self.assertIsNotNone(match)
        frontmatter = match.group(1)
        self.assertIn("name: scientific-article-writing", frontmatter)
        self.assertRegex(frontmatter, r"description: Use when ")
        self.assertLessEqual(len(frontmatter), 1024)

    def test_skill_references_only_existing_files(self):
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        for relative in re.findall(r"`((?:references|assets|scripts)/[\w./-]+)`", skill):
            self.assertTrue((SKILL_ROOT / relative).is_file(), relative)

    def test_exemplar_model_validates_and_stores_no_prose(self):
        validator = load_script("validate_writing_model.py")
        model = json.loads(
            (SKILL_ROOT / "assets" / "exemplar-journal-model.json").read_text(encoding="utf-8")
        )
        self.assertEqual(validator.validate_model(model), [])
        self.assertEqual(len(model["sources"]), 4)
        for section in model["sections"].values():
            for function in section["functions"]:
                self.assertLess(len(function["name"]), 200)
                self.assertTrue(function["evidence"])


class ProseDiagnosticsTests(unittest.TestCase):
    def setUp(self):
        self.module = load_script("prose_diagnostics.py")

    def test_flags_intensifiers_promotional_and_throat_clearing(self):
        text = (
            "It is worth noting that the effect was very large and dramatic. "
            "This novel finding is groundbreaking."
        )
        report = self.module.analyze_text(text)
        summary = report["summary"]
        self.assertEqual(summary["throat_clearing_total"], 1)
        self.assertEqual(summary["intensifier_total"], 2)
        self.assertEqual(summary["promotional_total"], 2)

    def test_clean_paragraph_has_no_flags(self):
        text = (
            "Theta stimulation increased capacity relative to arrhythmic stimulation. "
            "Response time did not differ between conditions. "
            "These results suggest a frequency-specific effect on prioritization."
        )
        report = self.module.analyze_text(text)
        summary = report["summary"]
        self.assertEqual(summary["intensifier_total"], 0)
        self.assertEqual(summary["promotional_total"], 0)
        self.assertEqual(summary["throat_clearing_total"], 0)
        self.assertEqual(summary["sentences"], 3)

    def test_detects_nominalization_and_monotone_cadence(self):
        text = (
            "We performed an examination of the data. "
            "We performed an evaluation of the model. "
            "We performed a validation of the result. "
            "We performed an analysis of the effect. "
            "We performed a comparison of the groups."
        )
        report = self.module.analyze_text(text)
        self.assertGreaterEqual(report["summary"]["nominalization_total"], 4)
        self.assertTrue(report["summary"]["monotone_cadence"])

    def test_sentence_splitter_keeps_abbreviations_and_statistics(self):
        text = "Capacity increased (t(19) = 2.38, p = 0.028, d = 0.53; Fig. 2B). Reaction time did not differ."
        paragraph = self.module.split_paragraphs(text)[0]
        self.assertEqual(len(self.module.split_sentences(paragraph)), 2)

    def test_style_signals_detect_exemplar_moves(self):
        text = (
            "We next asked whether stimulation frequency changed capacity. "
            "We reasoned that if entrainment mattered, then matched stimulation should help. "
            "There was a significant interaction such that capacity was higher for matched stimulation "
            "(F(1, 19) = 5.66, p = 0.028). "
            "Together, these findings suggest a frequency-specific effect.\n\n"
            "Reaction time was measured on every trial. "
            "It did not differ between conditions. "
            "The main effect of site was not significant (F(1, 19) = 0.59, p = 0.45)."
        )
        report = self.module.analyze_text(text)
        style = report["summary"]["style"]
        self.assertEqual(style["question_openers"], 1)
        self.assertEqual(style["stated_reasoning"], 1)
        self.assertEqual(style["directional_effects"], 1)
        self.assertEqual(style["summative_closers"], 1)
        self.assertEqual(style["paragraphs_ending_on_statistic"], [2])
        self.assertEqual(style["multi_sentence_paragraphs_without_closer"], [2])

    def test_exemplar_model_includes_language_style_section(self):
        model = json.loads(
            (SKILL_ROOT / "assets" / "exemplar-journal-model.json").read_text(encoding="utf-8")
        )
        self.assertIn("language_style", model["sections"])
        self.assertGreaterEqual(len(model["sections"]["language_style"]["functions"]), 15)

    def test_skips_headings_and_tables(self):
        text = "# Results\n\n| a | b |\n|---|---|\n\nThe effect was present."
        report = self.module.analyze_text(text)
        self.assertEqual(report["summary"]["paragraphs"], 1)


class InvariantScriptTests(unittest.TestCase):
    def test_bundled_invariant_checker_detects_changed_number(self):
        module = load_script("check_draft_invariants.py")
        audit = module.audit_texts("The estimate was 1.31.", "The estimate was 1.13.", [])
        self.assertFalse(audit["passed"])

    def test_bundled_invariant_checker_flags_strengthened_claim(self):
        module = load_script("check_draft_invariants.py")
        audit = module.audit_texts(
            "Stimulation was associated with recovery.",
            "Stimulation caused recovery.",
            [],
        )
        self.assertTrue(audit["claim_strength_changed"])


if __name__ == "__main__":
    unittest.main()
