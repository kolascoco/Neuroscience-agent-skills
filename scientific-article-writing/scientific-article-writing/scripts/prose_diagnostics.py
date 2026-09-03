#!/usr/bin/env python3
"""Deterministic prose diagnostics for a manuscript draft.

Reports, per paragraph and overall, the signals that the prose-quality
reference asks a writer to inspect: sentence-length variation, intensifiers
and promotional words, throat-clearing phrases, nominalization candidates,
passive-voice candidates, hedge density, and very long opening sentences.

The report lists places to look. It never decides what to change; the
evidence contract governs that.
"""

import argparse
import json
import re
import statistics
from pathlib import Path


INTENSIFIERS = [
    "very", "extremely", "highly", "dramatic", "dramatically", "massive",
    "massively", "enormous", "enormously", "considerably", "substantially",
    "exceedingly", "remarkably", "strikingly", "tremendous", "huge",
    "vastly", "hugely",
]
PROMOTIONAL = [
    "groundbreaking", "novel", "unprecedented", "paradigm-shifting",
    "transformative", "breakthrough", "remarkable", "cutting-edge",
    "state-of-the-art", "first-ever", "for the first time",
]
THROAT_CLEARING = [
    "it is worth noting that", "it should be noted that", "it is important to note that",
    "it should be mentioned that", "as mentioned above", "as previously mentioned",
    "it is interesting to note that", "needless to say", "in order to",
    "the fact that", "it is well known that", "it has been shown that",
]
HEDGES = [
    "may", "might", "could", "suggests", "suggest", "appears", "appear",
    "likely", "possibly", "perhaps", "seems", "seem", "is consistent with",
    "are consistent with", "potentially",
]
ATTENTION_MARKERS = ["notably", "critically", "importantly", "of note", "interestingly"]

# Style signals inherited from the exemplar articles (see references/style-guide.md).
QUESTION_OPENERS = re.compile(
    r"^(?:we (?:first|next|then|also|finally|further)?\s*(?:tested|asked|examined|assessed|investigated|sought)|"
    r"(?:we|the (?:first|second|third|fourth|fifth|final)) (?:aim|hypothesis|requirement|implication|question)|"
    r"(?:first|next|finally),\s+we\s+(?:tested|asked|examined|assessed))",
    re.IGNORECASE,
)
REASONING = re.compile(r"\bwe (?:reasoned|predicted|hypothesi[sz]ed|expected) that\b", re.IGNORECASE)
DIRECTIONAL = re.compile(r"\b(?:such that|driven by)\b", re.IGNORECASE)
SUMMATIVE = re.compile(
    r"\b(?:together|taken together|thus|in sum|collectively|these (?:findings|results|data)|this (?:dissociation|pattern|result|finding))\b",
    re.IGNORECASE,
)
ENDS_ON_STATISTIC = re.compile(r"(?:p\s*[<=>]\s*0?\.\d+|\d)\)?\.?$")

SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z(\[\"'])")
WORD = re.compile(r"[A-Za-z][A-Za-z'-]*")
NOMINALIZATION = re.compile(
    r"\b(?:the|an?|this|these|its|their|our)\s+(\w+(?:tion|sion|ment|ance|ence|ity|ysis))\s+of\b",
    re.IGNORECASE,
)
PASSIVE = re.compile(
    r"\b(?:is|are|was|were|be|been|being)\s+(?:\w+ly\s+)?(\w+(?:ed|en|wn|own))\b(?!\s+(?:to|by\s+(?:the\s+)?(?:time|end)))",
    re.IGNORECASE,
)
ABBREVIATION_GUARD = re.compile(r"\b(?:e\.g|i\.e|et al|vs|Fig|Figs|cf|approx|no|St|Dr|Mr|Ms|Mrs)\.$")


def split_paragraphs(text):
    blocks = re.split(r"\n\s*\n", text.strip())
    paragraphs = []
    for block in blocks:
        cleaned = " ".join(line.strip() for line in block.splitlines() if line.strip())
        if not cleaned or cleaned.startswith("#") or cleaned.startswith("|"):
            continue
        paragraphs.append(cleaned)
    return paragraphs


def split_sentences(paragraph):
    raw = SENTENCE_SPLIT.split(paragraph)
    sentences = []
    for piece in raw:
        piece = piece.strip()
        if not piece:
            continue
        if sentences and ABBREVIATION_GUARD.search(sentences[-1]):
            sentences[-1] = sentences[-1] + " " + piece
        else:
            sentences.append(piece)
    return sentences


def word_count(text):
    return len(WORD.findall(text))


def find_phrases(text, phrases):
    lowered = text.lower()
    found = {}
    for phrase in phrases:
        pattern = r"(?<![\w-])" + re.escape(phrase.lower()) + r"(?![\w-])"
        count = len(re.findall(pattern, lowered))
        if count:
            found[phrase] = count
    return found


def analyze_paragraph(index, paragraph):
    sentences = split_sentences(paragraph)
    lengths = [word_count(sentence) for sentence in sentences] or [0]
    first_length = lengths[0]
    passive_hits = [match.group(0) for match in PASSIVE.finditer(paragraph)]
    nominalizations = [match.group(0) for match in NOMINALIZATION.finditer(paragraph)]
    words = max(word_count(paragraph), 1)
    hedges = find_phrases(paragraph, HEDGES)
    last_sentence = sentences[-1] if sentences else ""
    style = {
        "question_opener": bool(sentences and QUESTION_OPENERS.match(sentences[0])),
        "stated_reasoning": len(REASONING.findall(paragraph)),
        "directional_effects": len(DIRECTIONAL.findall(paragraph)),
        "summative_closer": bool(SUMMATIVE.search(last_sentence)),
        "ends_on_statistic": bool(ENDS_ON_STATISTIC.search(last_sentence.rstrip())),
    }
    return {
        "paragraph": index,
        "opening": paragraph[:80],
        "sentences": len(sentences),
        "words": words,
        "sentence_length_mean": round(statistics.mean(lengths), 1),
        "sentence_length_sd": round(statistics.pstdev(lengths), 1) if len(lengths) > 1 else 0.0,
        "sentence_length_min": min(lengths),
        "sentence_length_max": max(lengths),
        "first_sentence_words": first_length,
        "long_opening_sentence": first_length > 35,
        "intensifiers": find_phrases(paragraph, INTENSIFIERS),
        "promotional": find_phrases(paragraph, PROMOTIONAL),
        "throat_clearing": find_phrases(paragraph, THROAT_CLEARING),
        "attention_markers": find_phrases(paragraph, ATTENTION_MARKERS),
        "hedge_count": sum(hedges.values()),
        "hedges_per_100_words": round(100 * sum(hedges.values()) / words, 1),
        "nominalization_candidates": nominalizations,
        "passive_candidates": passive_hits,
        "passive_ratio": round(len(passive_hits) / max(len(sentences), 1), 2),
        "style": style,
    }


def analyze_text(text):
    paragraphs = split_paragraphs(text)
    reports = [analyze_paragraph(i + 1, p) for i, p in enumerate(paragraphs)]
    all_lengths = []
    for paragraph in paragraphs:
        all_lengths.extend(word_count(s) for s in split_sentences(paragraph))
    total_words = sum(r["words"] for r in reports) or 1
    summary = {
        "paragraphs": len(reports),
        "sentences": len(all_lengths),
        "words": total_words,
        "sentence_length_mean": round(statistics.mean(all_lengths), 1) if all_lengths else 0.0,
        "sentence_length_sd": round(statistics.pstdev(all_lengths), 1) if len(all_lengths) > 1 else 0.0,
        "monotone_cadence": bool(all_lengths) and len(all_lengths) > 3
        and statistics.pstdev(all_lengths) < 4.0,
        "intensifier_total": sum(sum(r["intensifiers"].values()) for r in reports),
        "promotional_total": sum(sum(r["promotional"].values()) for r in reports),
        "throat_clearing_total": sum(sum(r["throat_clearing"].values()) for r in reports),
        "attention_marker_total": sum(sum(r["attention_markers"].values()) for r in reports),
        "hedges_per_100_words": round(
            100 * sum(r["hedge_count"] for r in reports) / total_words, 1
        ),
        "nominalization_total": sum(len(r["nominalization_candidates"]) for r in reports),
        "passive_total": sum(len(r["passive_candidates"]) for r in reports),
        "paragraphs_with_long_opening": [
            r["paragraph"] for r in reports if r["long_opening_sentence"]
        ],
        "style": {
            "question_openers": sum(r["style"]["question_opener"] for r in reports),
            "stated_reasoning": sum(r["style"]["stated_reasoning"] for r in reports),
            "directional_effects": sum(r["style"]["directional_effects"] for r in reports),
            "summative_closers": sum(r["style"]["summative_closer"] for r in reports),
            "paragraphs_ending_on_statistic": [
                r["paragraph"] for r in reports if r["style"]["ends_on_statistic"]
            ],
            "multi_sentence_paragraphs_without_closer": [
                r["paragraph"]
                for r in reports
                if r["sentences"] >= 3 and not r["style"]["summative_closer"]
            ],
        },
    }
    return {"summary": summary, "paragraphs": reports}


def render_markdown(report):
    summary = report["summary"]
    lines = [
        "# Prose diagnostics",
        "",
        f"- Paragraphs: {summary['paragraphs']}; sentences: {summary['sentences']}; words: {summary['words']}",
        f"- Sentence length mean {summary['sentence_length_mean']} (SD {summary['sentence_length_sd']})"
        + ("; cadence looks monotone" if summary["monotone_cadence"] else ""),
        f"- Intensifiers: {summary['intensifier_total']}; promotional words: {summary['promotional_total']}; "
        f"throat-clearing: {summary['throat_clearing_total']}; attention markers: {summary['attention_marker_total']}",
        f"- Hedges per 100 words: {summary['hedges_per_100_words']}",
        f"- Nominalization candidates: {summary['nominalization_total']}; passive candidates: {summary['passive_total']}",
        f"- Paragraphs with a long opening sentence: {summary['paragraphs_with_long_opening'] or 'none'}",
        "",
        "## Style signals (see references/style-guide.md)",
        "",
        f"- Question-driven openers: {summary['style']['question_openers']}; stated reasoning (we reasoned/predicted that): {summary['style']['stated_reasoning']}",
        f"- Directional effect phrasing (such that / driven by): {summary['style']['directional_effects']}; summative closers: {summary['style']['summative_closers']}",
        f"- Paragraphs ending on a statistic: {summary['style']['paragraphs_ending_on_statistic'] or 'none'}",
        f"- Multi-sentence paragraphs without a summative closer: {summary['style']['multi_sentence_paragraphs_without_closer'] or 'none'}",
        "",
        "| Para | Sent | Mean | SD | Intens. | Promo | Throat | Hedge/100w | Nominal. | Passive |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in report["paragraphs"]:
        lines.append(
            f"| {r['paragraph']} | {r['sentences']} | {r['sentence_length_mean']} | {r['sentence_length_sd']} | "
            f"{sum(r['intensifiers'].values())} | {sum(r['promotional'].values())} | "
            f"{sum(r['throat_clearing'].values())} | {r['hedges_per_100_words']} | "
            f"{len(r['nominalization_candidates'])} | {len(r['passive_candidates'])} |"
        )
    flagged = [
        r for r in report["paragraphs"]
        if r["intensifiers"] or r["promotional"] or r["throat_clearing"]
        or r["nominalization_candidates"] or r["long_opening_sentence"]
    ]
    if flagged:
        lines += ["", "## Places to inspect", ""]
        for r in flagged:
            items = []
            if r["intensifiers"]:
                items.append("intensifiers: " + ", ".join(r["intensifiers"]))
            if r["promotional"]:
                items.append("promotional: " + ", ".join(r["promotional"]))
            if r["throat_clearing"]:
                items.append("throat-clearing: " + ", ".join(r["throat_clearing"]))
            if r["nominalization_candidates"]:
                items.append("nominalizations: " + "; ".join(r["nominalization_candidates"]))
            if r["long_opening_sentence"]:
                items.append(f"opening sentence has {r['first_sentence_words']} words")
            lines.append(f"- Paragraph {r['paragraph']} ({r['opening']}...): " + "; ".join(items))
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("draft", type=Path, help="Plain text or Markdown draft")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of Markdown")
    args = parser.parse_args()
    report = analyze_text(args.draft.read_text(encoding="utf-8"))
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(render_markdown(report))


if __name__ == "__main__":
    main()
