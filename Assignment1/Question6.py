'''You are building a Python application to manage student records. Each student record is represented
as a tuple containing the student's name, age, and GPA (Grade Point Average). You need to ensure that
the student records are immutable. Explain how you can use tuples to store and manage student
records, and why immutability is essential in this scenario. Provide an example code snippet to
demonstrate the use of tuples for storing student records.'''

# you can use a the namedtuple keyword to create a tuple object that will contain all the required
# information as well as maintain it's immutability. We need that immutability so that nobody can 
# alter the records of the student once they are declared and we can maintain academic integrity.

#example code snippet
from collections import namedtuple

student = namedtuple('student', ['name', 'age', 'gpa'])

student1 = student('John', 25, 3.8)
student2 = student('Jacob', 18, 4.0)
student3 = student('Jingleheimer', 88, 2.5)
student4 = student('Schmidt', 37, 3.0)
#expected output: student(name='John Doe', age=25, gpa=3.8)

print(student1)
print(student2)
print(student3)
print(student4)