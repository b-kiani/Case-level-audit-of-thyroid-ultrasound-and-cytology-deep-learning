"""Verify this release: checksums, frozen-manifest hash, case-key schema, checkpoint list, and that every file referenced in the documentation exists.

    python tools/check_release.py          (exit code 0 = all checks passed)
"""
import glob, hashlib, re, sys, csv
from pathlib import Path
REPO = Path(__file__).resolve().parents[1]; ok = True
def fail(msg):
    global ok; ok = False; print("FAIL:", msg)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
# 1. checksums
listed = {}
for line in (REPO / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
    h, f = line.split("  ", 1); listed[f] = h
for f, h in listed.items():
    p = REPO / f
    if not p.exists(): fail(f"listed in SHA256SUMS but missing: {f}")
    elif sha(p) != h: fail(f"checksum mismatch: {f}")
present = {p.relative_to(REPO).as_posix() for p in REPO.rglob("*") if p.is_file() and ".git" not in p.parts and p.name != "SHA256SUMS.txt"}
for f in sorted(present - set(listed)): fail(f"file not covered by SHA256SUMS: {f}")
print(f"checksums: {len(listed)} files")
# 2. frozen manifest
if sha(REPO / "manifests/04_frozen_manifest.csv") != "83e656eff33e272020d85f8faf4004285a67768d3ef79e040c59ee13ea1575f5": fail("frozen manifest SHA-256")
else: print("frozen manifest SHA-256: OK")
# 3. case keys
with open(REPO / "manifests/04_frozen_manifest_v2_case_keys.csv", newline="", encoding="utf-8") as fh:
    bad = [r["case_key"] for r in csv.DictReader(fh) if int(re.search(r"group(\d+)", r["source_group"]).group(1)) != int(r["case_key"][4:])]
print("case_key vs source_group:", "OK" if not bad else fail(f"{len(bad)} disagreements"))
# 4. checkpoints
with open(REPO / "checkpoints/checkpoint_sha256.csv", newline="") as fh: n = sum(1 for _ in csv.DictReader(fh))
print("checkpoints listed:", n) if n == 120 else fail(f"expected 120 checkpoints, found {n}")
# 5. every referenced path exists
docs = ["README.md", "docs/REVIEWER_MAP.md", "docs/REPRODUCIBILITY_INDEX.md", "docs/CASE_ID_SCHEMA.md", "checkpoints/CHECKPOINTS.md"]
TOP = ("manifests/", "predictions/", "results/", "code/", "docs/", "tools/", "checkpoints/", "environment/", "thresholds/")
refs = 0
for d in docs:
    for tok in re.findall(r"`([^`]+)`", (REPO / d).read_text(encoding="utf-8")):
        for t in re.split(r",\s*", tok):
            t = t.strip()
            if not t.startswith(TOP) and t not in ("SHA256SUMS.txt", "CITATION.cff", "requirements.txt", "LICENSE", "DATA_LICENSE.md"): continue
            if "<" in t or " " in t: continue
            refs += 1
            if not glob.glob(str(REPO / t)): fail(f"{d} references a missing path: {t}")
print(f"documentation references checked: {refs}")
print("\nALL CHECKS PASSED" if ok else "\nSOME CHECKS FAILED"); sys.exit(0 if ok else 1)
