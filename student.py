# Create  Student class
class Student():
    # Constructor method
    def __init__(self, age, name, gender, grades):
        self.age = age
        self.name = name
        self.gender = gender
        self.grades  = grades
   
    #  Method to calculate average grade
    def compute_average(self):
        average = sum(self.grades)/len(self.grades)
        print("The average for student " + self.name + " is " + str(average))

 #  Method to calculate student highest grade
    def highest_student_grade(self):
        highest_grade = max(self.grades)
        print("The highest grade for student " + self.name + " is " + str(highest_grade))

# Create Student objects
philani  = Student(20, "Philani Sithole", "Male", [64,65])
sarah = Student(19, "Sarah Jones", "Female", [82,58])
peter= Student(21, "Peter Moyo", "Male", [76,90])
claire = Student(19, "Claire Brooks", "Female", [45,80])
kelly = Student(20, "Kelly Rodgers", "Female", [89,97])


# Method call
claire.compute_average()

# Add in new objects and logic here, and above to test your understanding.
#Call method to find highest grade for student
peter.highest_student_grade()
