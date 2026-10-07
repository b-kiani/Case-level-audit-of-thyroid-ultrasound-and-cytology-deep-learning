# Publishing release v2.1

The GitHub web uploader is limited to 100 files and skips hidden files, so use GitHub Desktop (or git).

1. Install GitHub Desktop, sign in, and clone `b-kiani/Case-level-evaluation-of-thyroid-ultrasound-and-cytology-deep-learning` to a local folder.
2. In that folder, delete every file and folder **except** the hidden `.git` folder.
3. Copy the full contents of this release package into the folder, including the hidden `.gitignore`.
4. In GitHub Desktop: summary "Release v2.1: complete analysis release" → Commit to main → Push origin.
5. Check: `python tools/check_release.py` must print `ALL CHECKS PASSED`.
6. On GitHub: Releases → Draft a new release → tag `v2.1` → title "v2.1 — complete analysis release". In the description, write that v2.1 supersedes the incomplete v2.0. Attach `ThyroFuse_frozen_split_checkpoints.zip` (the renamed `revision_round3\zenodo_frozen_split_checkpoints.zip`) as a release asset. Publish.
7. Zenodo archives v2.1 automatically as a new version of the same record. Copy the new version DOI from the Zenodo record page; it goes into the manuscript's Data and Code availability statements.
