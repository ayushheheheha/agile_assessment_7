students = [
    {"id": "S101", "name": "Arun",   "score": 78},
    {"id": "S102", "name": "Divya",  "score": 91},
    {"id": "S103", "name": "Karthik","score": 55},
    {"id": "S104", "name": "Meera",  "score": 43},
]

PASS_MARK = 50

def grade(score):
    if score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 50:
        return "C"
    return "F"

total = sum(s["score"] for s in students)
passed = [s for s in students if s["score"] >= PASS_MARK]

with open("evaluation_report.txt", "w") as f:
    f.write("Online Examination and Evaluation System\n")
    f.write("Evaluation Report\n")
    f.write("=" * 45 + "\n")
    f.write(f"Total candidates : {len(students)}\n")
    f.write(f"Passed           : {len(passed)}\n")
    f.write(f"Failed           : {len(students) - len(passed)}\n")
    f.write(f"Average score    : {total / len(students):.2f}\n")
    f.write("-" * 45 + "\n")
    f.write("ID      NAME       SCORE  GRADE\n")
    for s in students:
        f.write(f"{s['id']:<8}{s['name']:<11}{s['score']:<7}{grade(s['score'])}\n")

print("Evaluation report generated.")