# Where each editorial request is answered (second revision)

| Editor point | Manuscript | Files in this release |
|---|---|---|
| 1, 36, 39, 49 — post-exposure external reassessment | 3.9, 4.5, Table 4, Fig. 6 | `manifests/external_*.csv`, `predictions/external/*_all_models.csv` |
| 2–5, 30–32, 47 — masking: terminology, sufficiency, paired Δ, all backbones | 3.7, 4.4, Table 3, Fig. 4 | `predictions/shortcut_cv/*_oof_predictions.csv`, `predictions/round3/masking_oof_*.csv`, `results/round3/tables/MA1_masking_paired.csv` |
| 6, 32, 35 — masking QA | 4.4, Table S9, Figs S2–S4 | `results/round3/tables/Q0_masking_qa_per_image.csv`, `results/round3/tables/Q1_detection_rates.csv`, `manifests/masking_QA_expert_review_form.csv` |
| 7, 8, 41, 42 — metadata-only diagnostic and class-wise metadata | 3.8, 4.4, Table 3, Fig. 5, Tables S10–S11, Fig. S12 | `predictions/round3/metadata_features.csv`, `results/round3/tables/MD3_metadata_baseline.csv` |
| 9 — near-duplicate adjudication | 3.2, 4.1, Table S3, Fig. S11 | `results/round3/tables/ND1_near_duplicate_adjudication.csv`, `results/round3/tables/ND2_near_duplicate_sensitivity.csv` |
| 10 — additional benign cases | 3.1, 4.1, Table S4 | `results/round3/tables/S_provenance_sensitivity.csv` |
| 11 — TN3K label-inversion history | 3.10 | — |
| 12, 50 — reconciliation with the published article | 4.6, Table S1 | `results/tables/A7_prior_paper_reconciliation.csv` |
| 13, 28, 29 — split design | 3.6, 4.3, Table 3, Fig. 3 | `predictions/imagelevel_cv/*_oof_predictions.csv`, `predictions/round3/splitdesign_oof_*.csv` |
| 15, 17 — TN3K uncertainty and calibration | 3.9, 3.11, 4.5, Table 4, Fig. 6B, Table S13 | `results/round3/tables/T4_post_exposure_reassessment.csv` |
| 18 — release contents | Declarations | `SHA256SUMS.txt`, `checkpoints/checkpoint_sha256.csv`, `checkpoints/CHECKPOINTS.md`, `CITATION.cff`, `tools/check_release.py` |
| 19 — case-identifier schema | 3.1, Table S17 | `manifests/04_frozen_manifest_v2_case_keys.csv`, `docs/CASE_ID_SCHEMA.md` |
| 20 — reproducibility index | Table S16 | `docs/REPRODUCIBILITY_INDEX.md` |
| 21–55 — figures and tables | Figs 1–6, Tables 1–4, Additional files 1–2 | `results/round3/figures/*`, `docs/supplementary/*` |

The reviewer map for the first revision is preserved in `docs/REVIEWER_MAP_round1.md`.
