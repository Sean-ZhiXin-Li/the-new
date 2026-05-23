from pathlib import Path
import subprocess
import datetime as dt
import json
import shutil

REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = REPO_ROOT / "phase_b" / "config" / "day18.json"
with open(CONFIG_PATH, 'r') as f:
    config = json.load(f)
STDIN_VALUE = config["stdin_value"]

def timestamp() -> str:
    return dt.datetime.now().strftime("%Y%m%d_%H%M%S")

ts = timestamp()

print(REPO_ROOT)
PHASE_A_ENTRY = REPO_ROOT / "scripts" / "run_failure_aggregation_v1.sh"
EXP_DIR = (REPO_ROOT / "phase_b" / "experiments" / f"day17_call_{ts}")
EXP_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(CONFIG_PATH, EXP_DIR / "config_snapshot.json")

proc = subprocess.run(
    ["bash", str(PHASE_A_ENTRY)],
    input = (STDIN_VALUE + '\n').encode("utf-8"),
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE,
    cwd = str(REPO_ROOT),
)

# 2) after proc: build minimal manifest dict
manifest = {
    "timestamp": ts,
    "phase_a_entry": "scripts/run_failure_aggregation_v1.sh",
    "config_snapshot": "config_snapshot.json",
    "returncode": proc.returncode,
}

# 3) dump to EXP_DIR/run_manifest.json
with open(EXP_DIR / "run_manifest.json","w") as f:
          json.dump(manifest, f)

print("returncode: ", proc.returncode)
(EXP_DIR / "returncode.txt").write_text(str(proc.returncode))
(EXP_DIR / "stdout.txt").write_bytes(proc.stdout)
(EXP_DIR / "stderr.txt").write_bytes(proc.stderr)
