# gets input from the user
student_height = input("Input a list of student heights: ").split()

# converts each input in the list to an integer
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

sum = 0
length = 0

for i in student_height:
    sum += i

for j in student_height:
    length += 1

print(round(sum / length))