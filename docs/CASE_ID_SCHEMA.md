# Case identifiers

| Field | Meaning | Status |
|---|---|---|
| `case_key` | Authoritative case identifier: class folder + file-name case number (e.g. `PTC_0085`; `85.jpg`, `85_003.tif`) | Added in `manifests/04_frozen_manifest_v2_case_keys.csv` |
| `source_group` | Analytical group within a modality (`modality::label::group<case number>`); one-to-one with `case_key` within a modality | Unchanged; used for case-level grouping in every analysis |
| `component_id` | Connected component of source groups joined by duplicate links; the CV and bootstrap grouping unit | Unchanged |
| `case_id` (legacy) | Sequential ID inherited from earlier metadata; disagrees with the file-name case number in 39.7% of rows and repeats across classes | Renamed `legacy_case_id_unused`; never used for grouping |
| `patient_id` (legacy) | Label inherited from earlier metadata (e.g. `CYTOLOGY_001`) | Renamed `legacy_patient_label_unused`; never used |

`manifests/04_frozen_manifest.csv` is kept byte-for-byte so that its SHA-256 (`83e656ef…`) still verifies; `04_frozen_manifest_v2_case_keys.csv` is the same table with the corrected fields. `tools/check_release.py` verifies that `case_key` and `source_group` agree.
