# General Data Repositories and Data Articles

Use this reference when domain-specific neuroscience repositories do not contain a direct match, when a user gives only a paper title/DOI, or when the requested data may have been archived in a general-purpose repository.

## Search Priority

1. Search specialized neuroscience repositories first when the user asks for clear modality/domain data: OpenNeuro, OSF, TDBRAIN/Synapse, HCP, NITRC, BRAVA, Oliva Lab, TEMCA2/FAFB, or other reference-specific sources.
2. Search general-purpose data repositories next: Figshare, Dryad, Harvard Dataverse, Science Data Bank, Zenodo.
3. If no direct dataset record is found, search data descriptor journals and article metadata. The article is a fallback route to locate a data availability statement, repository DOI, accession, or supplementary file.
4. Return the direct dataset/database link as the top result whenever available. Article links are secondary unless the article is the only stable route to the data.

## General Repositories

| Repository | Best for | Search/access pattern |
|---|---|---|
| Figshare | Datasets, filesets, code, figures, media, institutional repository deposits, publisher-linked data | Web search at `https://figshare.com/search`; public API at `https://api.figshare.com/v2/articles/search` |
| Dryad Digital Repository | Curated research data, often associated with journal articles, strong life-science/ecology coverage | Web search at `https://datadryad.org/search`; API at `https://datadryad.org/api/v2/search` |
| Harvard Dataverse | Multidisciplinary datasets, social/behavioral science, biomedical and institutional dataverses | Web/API search at `https://dataverse.harvard.edu`; API path `/api/search` |
| Science Data Bank / ScienceDB | General-purpose scientific data, especially China/CAS and Springer Nature recommended generalist deposits | Web search at `https://www.scidb.cn/`; verify current UI/API behavior before scripting |
| Zenodo | Datasets, software, code, preregistration material, community deposits, DOI-versioned research objects | Web search at `https://zenodo.org/search`; API at `https://zenodo.org/api/records` |

## API Examples

### Figshare

Figshare API search uses POST:

```bash
curl -s -X POST -H "Content-Type: application/json" \
  -d '{"search_for":"neuroscience EEG","page_size":5}' \
  "https://api.figshare.com/v2/articles/search"
```

Filter returned records to `defined_type_name == "dataset"` or `defined_type_name == "fileset"` when the user needs downloadable data.

Useful fields:

- `title`
- `doi`
- `url_public_html`
- `url_public_api`
- `defined_type_name`
- `published_date`
- `resource_title`
- `resource_doi`

### Dryad

```bash
curl -s \
  "https://datadryad.org/api/v2/search?q=neuroscience%20EEG&page=1&per_page=5"
```

Useful fields:

- `identifier`
- `title`
- `abstract`
- `authors`
- `keywords`
- `relatedWorks`
- `sharingLink`
- `license`
- `_links.stash:download.href`

Dryad search supports phrase search, wildcard endings, negation, and filters in the web UI. Dryad can filter by journal, institution, publication date, file extension, and subject keywords.

### Harvard Dataverse

```bash
curl -s \
  "https://dataverse.harvard.edu/api/search?q=neuroscience&type=dataset&per_page=5"
```

Useful fields:

- `name`
- `url`
- `global_id`
- `description`
- `citation`
- `subjects`
- `fileCount`
- `publicationStatuses`
- `authors`

Dataverse Search API supports the same general searching, sorting, and faceting operations as the web interface for published data.

### Zenodo

```bash
curl -s \
  "https://zenodo.org/api/records?q=neuroscience%20EEG&type=dataset&size=5"
```

Useful fields:

- `metadata.title`
- `doi`
- `doi_url`
- `links.self_html`
- `metadata.description`
- `metadata.creators`
- `metadata.resource_type`
- `metadata.license`
- `files`
- `stats`

Zenodo supports UI and REST API search. Use `type=dataset` when the user wants data rather than papers, posters, or code.

### Science Data Bank / ScienceDB

Start with:

```text
https://www.scidb.cn/
```

Search strategy:

- Try the dataset title, paper title, author name, DOI, and modality keywords.
- Search both English and likely translated terms if a China-based dataset is expected.
- Verify dataset DOI, CSTR, license, file list, and access status on the dataset landing page.
- If scripted access is unclear, do not invent an API; report the web search route and exact landing page.

## DOI Patterns

| Pattern | Usually indicates |
|---|---|
| `10.6084/m9.figshare...` | Figshare |
| `10.5061/dryad...` | Dryad |
| `10.7910/DVN/...` | Harvard Dataverse |
| `10.5281/zenodo...` | Zenodo |
| `10.11922/sciencedb...` or ScienceDB landing page DOI/CSTR | Science Data Bank / ScienceDB |

Do not rely only on DOI prefix. Always resolve the DOI or inspect the landing page.

## Data Article Fallback

Use data articles when direct repository search fails or returns ambiguous results. Good targets include:

- Scientific Data: `https://www.nature.com/sdata/`
- Data in Brief: `https://www.sciencedirect.com/journal/data-in-brief`
- GigaScience/GigaByte and GigaDB for large life-science datasets.
- Journal-specific data availability statements in the primary article.

Scientific Data guidance:

- Scientific Data publishes open-access descriptions of research datasets.
- Its main article type, the Data Descriptor, is designed to describe reusable datasets rather than test hypotheses.
- Scientific Data pages often include validated links to related repository records.
- Use the article to extract repository links, accession numbers, dataset DOIs, data availability details, usage notes, validation details, and citation requirements.

Search patterns:

```bash
# Broad web search query to use with web search tools
"Scientific Data" neuroscience EEG dataset DOI

# Site-restricted search query
site:nature.com/articles/s41597 neuroscience dataset EEG
```

## Result Ranking Rules

Rank results in this order:

1. Direct dataset/database landing page with files or official access instructions.
2. Repository DOI landing page that points to files, restricted access, or request workflow.
3. Data descriptor article that contains repository links or accession numbers.
4. Primary research article with a data availability statement.
5. Lab/project page that says data are available on request.

## Output Requirements

For repository results, return:

- Repository searched.
- Query used.
- Dataset title.
- Direct dataset URL and DOI/accession.
- File availability and file types when visible.
- License/access status.
- Associated paper/article DOI when available.
- Why this result matched the user's query.

If only a data article is found, explicitly label it as `Article fallback`, extract any data availability statement or repository identifiers, and say that no direct repository record was found in the searched sources.
