---
name: neuroscience-database-lookup
description: Search and retrieve public neuroscience datasets and educational anatomy resources. Covers OpenNeuro BIDS datasets, OSF neuroscience projects/files, general repositories such as Figshare, Dryad, Harvard Dataverse, Science Data Bank, and Zenodo, data descriptor article fallback via journals such as Scientific Data, clinical EEG and TDBRAIN resources, Human Connectome Project data, BRAVA brain arterial reconstruction data, NITRC ICBM MRA atlas data, Oliva Lab visual cognition and neuroimaging datasets, standardized visual stimuli, eye-tracking resources, TEMCA2/FAFB fly brain EM connectomics data, and BrainFacts 3D Brain anatomy pages. Use when looking up neuroscience datasets, EEG/fMRI/MEG/MRA/EM data, visual cognition stimulus datasets, brain anatomy teaching material, or dataset download/access instructions.
metadata:
  skill-author: local
---

# Neuroscience Database Lookup

Use this skill to find, inspect, and retrieve neuroscience datasets or brain anatomy resources. It mirrors the `database-lookup` workflow, but is focused on neuroscience resources that are not all clean REST databases. Some are API-first, some are structured HTML download catalogs, some require registration or data-use agreements, and some are educational interactive sites.

## Core Workflow

1. **Understand the query** - Identify the requested data type: EEG, fMRI, MEG, MRA/NIfTI, structural/diffusion MRI, connectomics, vascular reconstructions, EM connectomics, visual cognition stimuli, eye tracking, OSF project files, or brain anatomy education.
2. **Select resource(s)** - Use the selection guide below. Query multiple resources when the user asks broadly.
3. **Read the reference file** - Each resource has a file in `references/` with access patterns, endpoints, examples, and limitations.
4. **Make the call or scrape the page** - Prefer JSON/GraphQL APIs where available. For older HTML catalogs, use `curl` plus structured parsing.
5. **Return results** - Always include:
   - The resources queried
   - The exact endpoint/page/download link used
   - Raw JSON when available, or a concise structured extraction from HTML
   - Any access, license, citation, or manual-download restriction

Priority rule: direct dataset/database links outrank articles. If no direct dataset record is found, use data descriptor or primary articles as an `Article fallback`, especially Scientific Data Data Descriptors, and extract data availability statements, repository DOIs, accession IDs, and usage/citation notes.

## Resource Selection Guide

| User is asking about... | Primary resource(s) | Also consider |
|---|---|---|
| BIDS neuroimaging datasets | OpenNeuro | OSF |
| EEG, MEG, MRI, fMRI, iEEG, PET datasets | OpenNeuro | OSF, Oliva Lab |
| Clinical EEG, psychiatric EEG, EEG biomarkers, TDBRAIN | Clinical EEG and Big Data | OpenNeuro, Narayanan Lab, MSU EEG links |
| Parkinson disease EEG, timing, cognitive control, frontal theta | Narayanan Lab via Clinical EEG and Big Data | OpenNeuro, OSF |
| A specific OpenNeuro accession such as `ds004584` | OpenNeuro | OSF if linked by paper/project |
| General project materials, preregistrations, files, protocols | OSF | OpenNeuro for BIDS imaging |
| Broad repository search, paper-linked datasets, DOI lookup, uncertain source | General Data Repositories and Data Articles | OSF, OpenNeuro, Scientific Data |
| Figshare, Dryad, Harvard Dataverse, Science Data Bank, Zenodo | General Data Repositories and Data Articles | Data descriptor journals |
| Scientific Data or data descriptor article lookup | General Data Repositories and Data Articles | Direct repository search first |
| Human connectomics, structural/diffusion MRI, HCP data | Human Connectome Project | OpenNeuro, EBRAINS |
| Brain arterial trees or vascular morphology | BRAVA | NITRC ICBM MRA |
| Human magnetic resonance angiography atlas, NIfTI MRA data | NITRC ICBM MRA | BRAVA |
| Visual cognition, natural scenes, memorability, Algonauts, fMRI/MEG image datasets | Oliva Lab datasets | OpenNeuro |
| Standardized object photos, BOSS stimuli | Visual Stimulus and Eye-Tracking | Oliva Lab |
| Emotional faces, ABCD fMRI task stimuli, Emotional N-back | Visual Stimulus and Eye-Tracking | ABCD data sharing pages |
| Image memorability, LaMem, MemNet | Visual Stimulus and Eye-Tracking | Oliva Lab |
| Eye fixations, saliency, FIGRIM, contextual scene search | Visual Stimulus and Eye-Tracking | Oliva Lab |
| Drosophila full adult fly brain EM/connectomics | TEMCA2/FAFB | Virtual Fly Brain, CATMAID tools |
| Interactive brain anatomy explanation, teaching, region names | BrainFacts 3D Brain | General web search for deeper citations |

## Included References

- `references/openneuro.md` - OpenNeuro GraphQL, openneuro-cli, DataLad, and ds004584 example.
- `references/osf.md` - OSF API v2 nodes, files, registrations, and public project lookup.
- `references/general-data-repositories-and-data-articles.md` - Figshare, Dryad, Harvard Dataverse, Science Data Bank, Zenodo, DOI patterns, and Scientific Data/article fallback workflow.
- `references/clinical-eeg-and-big-data.md` - TDBRAIN, MSU EEG links, Narayanan Lab datasets, and 5 V dataset evaluation guidance from the big-data review article.
- `references/human-connectome-project.md` - Human Connectome Project, ConnectomeDB, access routes, and citation/access notes.
- `references/brava.md` - BRAVA all-subject browser, subject pages, SWC download, vascular metrics.
- `references/nitrc-icbmmra.md` - NITRC Magnetic Resonance Angiography Atlas Dataset.
- `references/oliva-lab.md` - MIT Oliva Lab datasets and visual cognition/neuroimaging resources.
- `references/visual-stimulus-and-eyetracking.md` - BOSS, ABCD fMRI tasks and emotional stimuli, LaMem, contextual guidance eye-tracking data, and FIGRIM fixation data.
- `references/temca2-fafb.md` - TEMCA2/FAFB adult fly brain EM image volume and tools.
- `references/brainfacts-3d-brain.md` - BrainFacts 3D Brain educational anatomy resource.

## Identifier Patterns

| Identifier | Example | Resource |
|---|---|---|
| OpenNeuro dataset accession | `ds004584` | OpenNeuro |
| OpenNeuro DOI | `10.18112/openneuro.ds004584.v1.0.0` | OpenNeuro |
| OSF node/project ID | `q4mez`, `sfbpx` | OSF |
| Figshare DOI | `10.6084/m9.figshare.32336397.v1` | Figshare |
| Dryad DOI | `10.5061/dryad.76hdr7t80` | Dryad |
| Harvard Dataverse DOI | `10.7910/DVN/2RKAQP` | Harvard Dataverse |
| Zenodo DOI | `10.5281/zenodo.6860680` | Zenodo |
| ScienceDB DOI/CSTR | `10.11922/sciencedb...` | Science Data Bank |
| TDBRAIN DOI/Synapse ID | `10.70303/syn25671079`, `syn25671079` | TDBRAIN/Synapse |
| NITRC group ID | `1113` | NITRC ICBM MRA |
| NITRC file ID | `9725` | NITRC ICBM MRA |
| BRAVA subject page ID | `query_subject.php?id=1` | BRAVA |
| FAFB volume/version | `FAFBv14` | TEMCA2/FAFB |
| HCP project/cohort | `HCP Young Adult`, `HCP Lifespan` | Human Connectome Project |

## API and Access Notes

| Resource | Access style | Authentication |
|---|---|---|
| OpenNeuro | GraphQL, openneuro-cli, DataLad, browser | Public browse/download without account for public datasets |
| OSF | JSON:API REST API, browser | Public read without token; token for private/write access |
| Figshare | Web search, POST search API, public item API | Public metadata/download for open records; license varies |
| Dryad | Web search, JSON API | Public metadata/download for published datasets; license usually visible |
| Harvard Dataverse | Web search, Search API | Public metadata/download for released datasets; restricted files vary |
| Science Data Bank / ScienceDB | Web search; verify current scripting options | Public/restricted varies; verify DOI/CSTR and access status |
| Zenodo | Web search, REST records API | Public metadata/download for open records; restricted/embargoed records may require request |
| Scientific Data and data descriptor journals | Article pages, data availability statements, repository links | Article is fallback; repository link remains priority |
| TDBRAIN | Brainclinics/Synapse downloads, code repository | Registration and Data Use Agreement |
| Human Connectome Project | ConnectomeDB, HCP Data Archive, LONI/NDA routes depending on cohort | Registration and data-use terms; restricted data require approval |
| Narayanan Lab | HTML catalog linking to OSF, OpenNeuro, PubMed, Dropbox, Bitly | Varies by linked resource |
| MSU EEG links | Older HTML catalog and dataset pages | Public pages observed; verify dataset pages |
| BRAVA | HTML/PHP pages and ZIP download | Public HTML/download |
| NITRC ICBM MRA | NITRC HTML and direct file download | Public download observed; NITRC account may be needed for some files on NITRC generally |
| Oliva Lab | HTML catalog and linked dataset pages/forms | Varies by dataset; some direct, some form-gated |
| Visual stimulus/eye-tracking resources | HTML pages, Google Drive, GitHub, direct ZIP downloads, task ZIPs | Varies; some academic/research-only restrictions |
| TEMCA2/FAFB | HTML catalog, CATMAID browser, tile downloads | Public browse/download; respect license |
| BrainFacts 3D Brain | Interactive web page | Public educational page; not a research dataset API |

## Making Requests

Use `curl` or the available web fetch tool. For OpenNeuro and OSF, prefer structured API calls:

```bash
# OpenNeuro GraphQL dataset metadata
curl -s -H "Content-Type: application/json" \
  --data '{"query":"query { dataset(id: \"ds004584\") { id name public metadata { datasetName modalities species studyDomain studyDesign } latestSnapshot { tag size description { Name License DatasetDOI Authors } } } }"}' \
  https://openneuro.org/crn/graphql

# OSF title search
curl -s -H "Accept: application/vnd.api+json" \
  "https://api.osf.io/v2/nodes/?filter%5Btitle%5D=neuroscience&page%5Bsize%5D=5"
```

For HTML resources, fetch the page and extract links/tables:

```bash
curl -L -s "http://cng.gmu.edu/brava/all_subjects.php?clear=1" |
  rg "query_subject.php|swc_files.zip|metrics.php"
```

For general repository search, read `references/general-data-repositories-and-data-articles.md` and run several repository queries before falling back to articles. Example:

```bash
curl -s "https://zenodo.org/api/records?q=neuroscience%20EEG&type=dataset&size=5"
curl -s "https://dataverse.harvard.edu/api/search?q=neuroscience&type=dataset&per_page=5"
```

## Output Format

Use this shape:

- `## Resources Queried`
- `## Results`
- One subsection per resource, with raw JSON in a fenced `json` block when available.
- `## Access Notes`, including license, citation, download method, and file formats.
- `## Article Fallback`, only when no direct dataset link was found; include the article DOI, data availability statement, and any repository/accession clues.

For large file lists, summarize the first page and include pagination or recursive download instructions.

When a user asks for recommendations across datasets, add a compact `## Big Data Fit` note covering volume, variety, velocity/update status, veracity/quality-control signals, and scientific value. This is especially useful for clinical, multimodal, or AI/ML use cases.

## Error Recovery

- If OpenNeuro GraphQL rejects a field, introspect the type first or remove the field. OpenNeuro field names are case-sensitive.
- If OSF filters return broad/noisy results, try `filter[title]`, `filter[description]`, `filter[tags]`, and the `/v2/search/` endpoint.
- If an older HTTP resource fails over plain HTTP, retry HTTPS if available, then try with `curl -L`.
- For resources that are not APIs, do not invent JSON. Return extracted page metadata and direct links.
- Always preserve license/citation warnings, especially for TEMCA2/FAFB and older lab-hosted datasets.
