students = [
    "Marissa",
    "Merliee",
    "Daniel",
    "Chris",
    "Chad",
    "Shane",
    "Stephen",
    "Drew",
    "Guido",
    "Porscha",
    "Carla",
    "YingRong",
    "Ian",
    "Nick",
    "Michael",
    "Hayes"
]

#Take the list of students, randomly pair 2 until all students have been paired.

# 1. Grab a random index from students
# 2. Then remove that student from the list
# 3. Repeat until the len(list) = 0

#for i in range(0, len(students)):

import random
# while students:
#     #Get a random number from the indices left in students
#     rand_num = random.randint(0, len(students) - 1)
#     #print rand_num
#     current_student = students[rand_num]
#     students.remove(current_student)
#     print current_student
#     rand_num = random.randint(0, len(students) - 1)
#     current_student = students[rand_num]
#     students.remove(current_student)
#     print (" is paired with " + current_student)


def get_student():
    rand_num = random.randint(0, len(students) - 1)
    current_student = students[rand_num]
    students.remove(current_student)
    return current_student

while students:
    student1 = get_student()
    student2 = get_student()
    print ("%s is paired with %s" % (student1, student2))