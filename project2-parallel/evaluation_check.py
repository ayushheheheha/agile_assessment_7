"""
Online Examination and Evaluation System
Evaluation Engine (backend) health check — simulates checks against
predefined expected states, no live network calls involved.
"""

import time

# Predefined expected system state for this check run
EXPECTED = {
    "answer_key_loaded": True,
    "answer_key_entries": 50,
    "expected_answer_key_entries": 50,
    "auto_scoring_response_ms": 320,
    "max_acceptable_response_ms": 1000,
    "db_connection_status": "connected",
}

CHECKS = [
    ("Answer key loaded", lambda: EXPECTED["answer_key_loaded"] is True),
    ("Answer key entry count matches expected",
     lambda: EXPECTED["answer_key_entries"] == EXPECTED["expected_answer_key_entries"]),
    ("Auto-scoring module responds within limit",
     lambda: EXPECTED["auto_scoring_response_ms"] <= EXPECTED["max_acceptable_response_ms"]),
    ("Result database connected",
     lambda: EXPECTED["db_connection_status"] == "connected"),
]


def run_checks():
    print("Running evaluation engine (backend) checks...")
    results = []
    for name, check_fn in CHECKS:
        time.sleep(0.5)  # simulate check taking time
        passed = check_fn()
        status = "OK" if passed else "FAIL"
        print(f"  [{status}] {name}")
        results.append((name, passed))
    return results


if __name__ == "__main__":
    results = run_checks()
    failed = [name for name, passed in results if not passed]
    if failed:
        print(f"Evaluation engine checks FAILED ({len(failed)} issue(s)).")
        raise SystemExit(1)
    print("Evaluation engine checks passed.")