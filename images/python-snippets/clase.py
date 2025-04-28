studentScore = []
for i in range(0, 10):
    studentScore.append(eval(input("Enter the score:")))
print("Scores: ", studentScore.copy())
print("Fourth element", studentScore[3])
print("Print from the 1st element to the 5th element", studentScore[0:5])
studentScore.insert(2, 78)
print("Add the number 78 before the fourth element of the list", studentScore)
studentScore.sort()
print("Sorted list: ", studentScore)
findScore = int(input("What score would you like to find? "))
if findScore in studentScore:
    print(f"We found {studentScore.count(findScore)}, {findScore} in your list")
else:
    print(f"We did not find a {findScore} in your list")
if 100 in studentScore:
    print("Some students got a 100")
else:
    print("No one got a 100 :(")
studentScore.pop(0)
print("Students score without the first element: ", studentScore.copy())
print("Length of the list: ", studentScore.__len__())
print("The highest score was: ", max(studentScore))
print("The lowest score was: ", min(studentScore))
studentScore.reverse()
print("Reversed list ", studentScore)
studentScore.pop()
print("Scores without las element: ", studentScore.copy())
studentScore.pop(0)
studentScore.insert(0, 85)
print("Scores with 85 in the front: ", studentScore.copy())
score1 = [99, 89]
score2 = [98, 78, 66]
score1.extend(score2)
print(studentScore)
print()
print()
print()
