PASS_MARK = 50
REVAL_WINDOW_MARK = 45  # candidates within 5 marks of passing


def grade(score):
    if score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= PASS_MARK:
        return "C"
    return "F"


def is_pass(score):
    return score >= PASS_MARK


def revaluation_eligible(score):
    """A failed candidate close to the pass mark can apply for re-evaluation."""
    return REVAL_WINDOW_MARK <= score < PASS_MARK


def evaluate(candidate_id, score):
    return {
        "id": candidate_id,
        "score": score,
        "grade": grade(score),
        "result": "PASS" if is_pass(score) else "FAIL",
        "reval_eligible": revaluation_eligible(score),
    }


if __name__ == "__main__":
    for cid, sc in [("S101", 91), ("S102", 47), ("S103", 30)]:
        print(evaluate(cid, sc))