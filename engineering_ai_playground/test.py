import json
from datetime import datetime
import os

FAILURE_PARAM_LE_1 = "param_le_1"
FAILURE_LEGACY_MISSING_REASON = "legacy_missing_reason"
passed = False
failure_reason = None
param =float( input())
a = 12
b = 123
c = 135
if param > 1:
	print(abs(param - 1))
	passed = True
else:
	failure_reason = FAILURE_PARAM_LE_1

if passed:
	print("Hello Engineering World!!!")
else:
	print("ENTER FAILURE MODE")
timestamp = datetime.now().isoformat()
metrics ={
	"param": param,
	"value": abs(param - 1),
	"passed": passed,
	"timestamp": timestamp,
	"bad": [1, 2, 3],
	"failure_reason": failure_reason
}

metrics_path = "metrics.json"

if os.path.exists(metrics_path):
	with open(metrics_path, 'r') as f:
		history = json.load(f)
else:
	history = []

if not isinstance(history, list):
	history = []

for rec in history:
	if "failure_reason" not in rec:
		rec["failure_reason"] = None if rec["passed"] else FAILURE_LEGACY_MISSING_REASON

history.append(metrics)

with open(metrics_path, 'w') as f:
	json.dump(history, f, indent = 2)
