def score_exam(correct_answers, student_answers):
    score = 0
    for correct, student in zip(correct_answers, student_answers):
        if student == correct:
            score += 4
        elif student != "" and student != correct:
            score -= 1
    return max(score, 0)