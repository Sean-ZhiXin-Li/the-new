import json

def main():
    with open("metrics.json", "r") as f:
        metrics = json.load(f)

    with open("analysis/failure_counts.json", "r") as f:
        counts = json.load(f)

    failed_total = sum(1 for rec in metrics if rec.get("passed") is False)
    counts_total = sum(counts.values())
        # contract 1: counts must be a dict
    if not isinstance(counts, dict):
        print("ERROR: failure_counts is not a dict")
        raise SystemExit(1)

    # contract 2: all values must be non-negative integers
    for v in counts.values():
        if not isinstance(v, int) or v < 0:
            print("ERROR: failure_counts contains non-integer or negative value")
            raise SystemExit(1)

    # contract 3: total count must match number of failed records
    if counts_total != failed_total:
        print(
            f"ERROR: count mismatch "
            f"(failed_total={failed_total}, counts_total={counts_total})"
        )
        raise SystemExit(1)

    # all contracts satisfied
    print(f"VERIFY OK: failed_total={failed_total} counts_total={counts_total}")



if __name__ == "__main__":
    main()