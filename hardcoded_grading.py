students = ["Ada", "John", "Mike"]
subjects = ["Math", "Science"]

from itertools import zip_longest 

for student in students:
    for idx, (subject, grade)in enumerate(zip_longest(subjects, range(80, 83)), start = 1 ):
        subject = subject if subject is not None else "No subject"
        grade = grade if grade is not None else "No grade"
        student = student if student is not None else "No name"
        print(f"Subject {idx}: {student} scored {grade} in {subject}")