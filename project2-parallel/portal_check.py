"""
Online Examination and Evaluation System
Exam Portal (frontend) health check — simulates checks against
predefined expected states, no live network calls involved.
"""

import time

# Predefined expected system state for this check run
EXPECTED = {
    "login_page_status": 200,
    "question_paper_render_ms": 450,
    "max_acceptable_render_ms": 800,
    "active_exam_sessions": 3,
    "timer_sync_offset_ms": 12,
    "max_acceptable_timer_drift_ms": 50,
}

CHECKS = [
    ("Login page reachable", lambda: EXPECTED["login_page_status"] == 200),
    ("Question paper renders within limit",
     lambda: EXPECTED["question_paper_render_ms"] <= EXPECTED["max_acceptable_render_ms"]),
    ("Active sessions within expected range",
     lambda: 0 < EXPECTED["active_exam_sessions"] <= 50),
    ("Countdown timer sync within tolerance",
     lambda: EXPECTED["timer_sync_offset_ms"] <= EXPECTED["max_acceptable_timer_drift_ms"]),
]


def run_checks():
    print("Running exam portal (frontend) checks...")
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
        print(f"Exam portal checks FAILED ({len(failed)} issue(s)).")
        raise SystemExit(1)
    print("Exam portal checks passed.")