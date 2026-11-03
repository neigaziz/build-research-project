# Dataset provenance and licence checklist

For every dataset, retain a record of its producer, canonical landing page, persistent identifier, direct download/API route, version, release date, access date (UTC), geographic and temporal coverage, unit of observation, sampling method, variable definitions, file format and size.

## Access and licence classification

Use one of these explicit statuses:

- `OPEN_LICENSE`: a clearly identified open licence permits the intended reuse, subject to its conditions.
- `PUBLIC_DOMAIN`: the provider clearly identifies the data as public domain or an applicable public-domain basis is verified.
- `PUBLIC_DOWNLOAD_TERMS`: downloadable without payment but reuse or redistribution terms require review; do not label it open-licensed.
- `REGISTRATION_OR_APPLICATION`: access requires registration/application and the active session is authorised to access it.
- `RESTRICTED_OR_CLOSED`: do not retrieve or redistribute without valid authorisation.
- `UNKNOWN`: licence or terms could not be verified; do not redistribute and describe the limitation.

Record licence URL, attribution wording, share-alike/derivative requirements, non-commercial restrictions, database rights, privacy conditions, API terms, rate limits and any obligation to cite a publication. Do not interpret a licence on a repository platform as necessarily covering third-party data hosted there; inspect the dataset-specific terms.

## Integrity and provenance

For each local file, record relative path, byte size, SHA-256, retrieval time and source URL. Preserve original files and provider documentation where permitted. A checksum establishes byte identity, not accuracy or authenticity. Recalculate checksums after transfer and before final packaging.

## Combining datasets

Before linking files, compare entity definitions, identifiers, measurement units, time windows, geographic boundaries, coding systems and sampling processes. Document transformations and join cardinality. Avoid ecological inference, false precision from mismatched scales, and hidden selection caused by incomplete linkage.

## Minimal register columns

`dataset_id,title,producer,landing_page,download_url,doi_or_identifier,version,coverage,unit_of_observation,licence,licence_url,accessed_utc,local_path,sha256,redistribution_status,selection_decision,limitations`

Use `NOT_RETAINED` as `local_path` only when the source bytes are not included, and explain the legal or technical reason in `limitations` and the project README. Do not invent a checksum for a file that was not downloaded.
