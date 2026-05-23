import json
from collections import Counter

METRICS_PATH = "metrics.json"
OUTPUT_PATH = "analysis/failure_counts.json"

with open(METRICS_PATH, "r") as f:
    data = json.load(f)

reasons = []
for rec in data:
    passed = rec.get("passed", None)
    if passed is False:
        reasons.append(rec.get("failure_reason", None))

counts = Counter(reasons)
counts_dict = dict(counts)

for reason, cnt in counts.items():
    print(f"{reason}: {cnt}")

with open(OUTPUT_PATH, "w")as f:
    json.dump(counts_dict, f, indent = 2)