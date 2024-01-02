score = input("Please enter a score: ")

try:
    sc = float(score)
except:
    print("Please enter a numeric value!")
    quit()

if sc >= 0.9:
    grade = "A"
elif sc >= 0.8:
    grade = "B"
elif sc >= 0.7:
    grade = "C"
elif sc >= 0.6:
    grade = "D"
elif sc < 0.6:
    grade = "F"

if 1.0 > sc > 0.0:
    print("Your grade is", grade)
else:
    print("Enter a score between 0.0 and 1.0")
    
