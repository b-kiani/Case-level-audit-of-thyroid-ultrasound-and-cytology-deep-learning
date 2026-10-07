# Model checkpoints

- `checkpoint_sha256.csv` identifies all 120 checkpoints used in the manuscript (10 frozen-split models, 50 grouped-CV fold models, 10 split-design fold models, 50 masking fold models) by path, size, modification time and SHA-256.
- **Storage.** The 10 frozen-split checkpoints, used for the frozen test set and all external reassessments, are attached to GitHub release v2.1 as `ThyroFuse_frozen_split_checkpoints.zip` (0.95 GB). The 110 fold checkpoints are held by the corresponding author and are available on request; any copy can be verified against `checkpoint_sha256.csv`.
- Each file is a PyTorch dictionary with `model_state_dict` for `timm.create_model(<name>, pretrained=False, num_classes=1)`; see `code/r2_gpu_tasks.py`, function `build_model`.
