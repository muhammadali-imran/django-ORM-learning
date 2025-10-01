import random
from faker import Faker
from myapp.models import Student, Teacher, Course, Department, Enrollment
import os
import django



fake = Faker()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

def seed_database():

    Enrollment.objects.all().delete()
    Course.objects.all().delete()
    Teacher.objects.all().delete()
    Student.objects.all().delete()
    Department.objects.all().delete()

    departments = []
    dept_names = ["Computer Science", "Mathematics", "Physics"]
    for code, name in enumerate(dept_names, start=1):
        dept = Department.objects.create(name=name, code=f"DEP{code:02d}")
        departments.append(dept)

    teachers = []
    for i in range(12):
        dept = random.choice(departments)
        teacher = Teacher.objects.create(
            name=fake.name(),
            email=fake.unique.email(),
            department=dept
        )
        teachers.append(teacher)

    courses = []
    for i in range(20):
        dept = random.choice(departments)
        teacher = random.choice(teachers)
        course = Course.objects.create(
            title=f"{fake.word().capitalize()} {random.choice(['101','201','301'])}",
            code=f"C{i+1:03d}",
            description=fake.sentence(nb_words=10),
            teacher=teacher,
            department=dept
        )
        courses.append(course)

    students = []
    for i in range(100):
        dept = random.choice(departments)
        student = Student.objects.create(
            name=fake.name(),
            age=random.randint(18, 25),
            email=fake.unique.email(),
            department=dept
        )
        students.append(student)

    for student in students:
        enrolled_courses = random.sample(courses, random.randint(3, 6))
        for course in enrolled_courses:
            Enrollment.objects.create(
                student=student,
                course=course,
                enrollment_date=fake.date_this_decade()
            )

    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()
