
#9.Find the student with the highest score using max() and the key argument
highest_score_student = max(scores, key=scores.get)
highest_score = scores[highest_score_student]

print("The Highest Score is", highest_score)
print("Achieved by", highest_score_student)
