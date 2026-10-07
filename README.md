# Case-level audit of thyroid ultrasound and cytology deep learning

Analysis release for the manuscript *Case-level audit of thyroid ultrasound and cytology deep learning: label conflicts, split design, and shortcut-sensitive performance in a public archive* (Kiani Kalejahi B, Rajabi MJ; BMC Medical Imaging, second revision).

**Release v2.1 is the complete release cited by the manuscript.** Release v2.0 was an incomplete snapshot of this repository; it lacks the cross-validation, split-design and masking predictions and the Round 3 results, and should not be used. Every number in the manuscript can be regenerated from the files here together with the three public datasets listed below, and `python tools/check_release.py` verifies the release. No medical images are redistributed.

> **Previous repository.** The repository cited in the first submission (github.com/b-kiani/Thyroid-Cancer-Classification-2026) held only figure exports and is superseded. The first submission's external TN3K and DDTI analyses were invalid and have been withdrawn (manuscript Section 3.10).

## Contents

| Folder | What it contains | Manuscript |
|---|---|---|
| `code/` | Conflict audit (`00c`), frozen split (`01e`), frozen-split training (`02`), grouped cross-validation (`03b`), its two single-change variants (`03b_imagelevel_cv`, `03b_shortcut_cv`), inference (`r2_gpu_tasks.py`), and the analysis notebook that regenerates every table and figure | Methods 3.2–3.10 |
| `manifests/` | Source image metadata; the original frozen case-level manifest (SHA-256 verified) and `04_frozen_manifest_v2_case_keys.csv` with the authoritative `case_key` (see `docs/CASE_ID_SCHEMA.md`); excluded label-conflict images; exact-duplicate groups; perceptual-hash pairs; cross-validation fold assignment; external manifests listing every evaluated TN3K and DDTI image and its label; masking-QA review form | Table 1, Fig. 1, Sections 3.1–3.3 and 3.9, Tables S1–S5 |
| `predictions/frozen_split/` | Per-image validation and test probabilities for all five backbones and the ensemble, both modalities, image and case level, with `metrics.json` | Table 2, Fig. 2C–D, Tables S7–S8 |
| `predictions/grouped_cv/` | Out-of-fold probabilities for every backbone and the ensemble (`*_all_models_oof.csv`, `per_model/`), inner-validation predictions used for thresholds (`inner_validation/`), fold metrics and summaries | Table 2, Fig. 2, Table S6 |
| `predictions/imagelevel_cv/`, `predictions/shortcut_cv/` | Out-of-fold probabilities for the split-design experiment and for the masking control of all five backbones (sector removed, sector only) | Table 3, Figs 3–4 |
| `predictions/round3/` | Paired masking and split-design files, metadata features and metadata-only predictions | Table 3, Figs 3–5 |
| `results/round3/` | Second-revision tables and figures (vector PDF/SVG and PNG) | Tables 1–4, Figs 1–6, Additional files |
| `predictions/external/` | Per-image probabilities of the frozen ultrasound models on TN3K (test, trainval) and DDTI | Table 4, Fig. 6, Table S13 |
| `thresholds/` | Every operating threshold, and the data it was selected on | Sections 3.4–3.5 |
| `results/` | First-revision result tables (CSV), `RESULTS.md`, figures and figure source data | Supplementary tables |
| `environment/` | Training environment, full `pip freeze` and GPU details | Section 3.11 |
| `checkpoints/` | SHA-256 of all 120 checkpoints and their storage location (`checkpoints/CHECKPOINTS.md`) | — |
| `docs/` | Reviewer maps, reproducibility index, case-identifier schema, Additional files 1–2 | Tables S16–S17 |

## Data (obtain from the distributors)

| Dataset | Source | Place at |
|---|---|---|
| Pang et al. ultrasound and cytology archive | Mendeley Data, https://doi.org/10.17632/dp7zp2pb2v.1 (CC BY 4.0) | `<ROOT>/data/` with the four released class folders |
| TN3K images | TRFE-Net repository, https://github.com/haifangong/TRFE-Net-for-thyroid-nodule-segmentation | `<ROOT>/Thyroid Dataset/tn3k/` (`test-image/`, `trainval-image/`) |
| TN3K classification labels | ACL repository data release, https://github.com/chenghui-666/ACL (`label4test.csv`, `label4trainval.csv`; 0 = benign, 1 = malignant) | same `tn3k/` folder |
| Original DDTI with XML annotations | CIM@LAB, Universidad Nacional de Colombia; mirror: Kaggle `dasmehdixtr/ddti-thyroid-ultrasound-images` | `<ROOT>/Thyroid Dataset/DDTI_original/` |

Do not use preprocessed DDTI redistributions whose `category.csv` is documented as invalid for classification, or image-folder repackagings of TN3K whose `label` field is a folder name.

## Reproducing the results

1. Create the environment: Python 3.10, then `pip install -r requirements.txt` (PyTorch 2.5.1 with CUDA 12.1; see `environment/`).
2. Place the data as above under a project root. The scripts use `ROOT = Path(r"D:\Thyroid-BHI-26")` near the top of each file; change that one line to your root, or use the same path. Manifests store absolute paths from the original machine; `python tools/relocate_paths.py --old "D:\Thyroid-BHI-26" --new <your root>` rewrites them in a copy.
3. Verify the frozen manifest: `python tools/verify_manifest.py` (expected SHA-256 `83e656eff33e272020d85f8faf4004285a67768d3ef79e040c59ee13ea1575f5`).
4. Run, in order:
   - `code/00c_audit_cross_label_duplicates.py` — label-conflict audit
   - `code/01e_rebuild_FINAL_split_70_15_15.py` — frozen case-level 70/15/15 split
   - `code/02_experiment1b_retrain_five_backbones.py` — five backbones and ensemble on the frozen split
   - `code/Revision_Round2_Runs.ipynb` — grouped cross-validation of all backbones (via `03b`), split-design experiment, external reassessment, calibration, feature-space comparison
   - `code/Revision_Round3_Runs.ipynb` — masking control for all backbones and the ensemble with masking QA, paired ΔAUROC, metadata-only diagnostic, near-duplicate adjudication, shared-scale Grad-CAM, and every manuscript table and figure

   The notebook is resumable, and verifies the manifest hash and cross-validation fold reproduction before training.
5. Training settings: timm ImageNet weights, single linear logit head, 224 × 224 input, AdamW (lr 3 × 10⁻⁴, weight decay 10⁻⁴), 40 epochs, batch 16, seed 2026, class-weighted BCE plus weighted sampler, checkpoint by validation AUROC, Youden threshold on validation.

Fold membership of `StratifiedGroupKFold` depends on the scikit-learn version. The notebook checks that `03b` reproduces `manifests/cv_fold_assignment.csv` exactly before reusing any earlier run.

## Reviewer comments

`docs/REVIEWER_MAP.md` maps every point of the second editorial review to the manuscript and to files here; `docs/REVIEWER_MAP_round1.md` does the same for the first review. `docs/REPRODUCIBILITY_INDEX.md` links each manuscript result to its source files, code, checkpoints and expected output.

## Licence and citation

Code: MIT (`LICENSE`). Derived data (manifests, predictions, tables): CC BY 4.0 (`DATA_LICENSE.md`), consistent with the development archive. Please cite the manuscript (`CITATION.cff`) and the three datasets.
