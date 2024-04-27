class Student:
    def __init__(
        self, studentid: str, firstName: str, lastName: str, gradeLevel: int
    ) -> None:

        self.studentid = studentid
        self.firstName = firstName
        self.lastName = lastName
        self.gradeLevel = gradeLevel

    def getStudentInfo(self) -> str:
        return (
            self.studentid
            + ": "
            + self.firstName
            + " "
            + self.lastName
            + "("
            + str(self.gradeLevel)
            + "gr"
            + ")"
        )


student1 = Student("AC-343424", "James", "Smith", 6)
student2 = Student("AC-343428", "Maria", "Garcia", 5)
student3 = Student("AC-343434", "Robert", "Johnson", 3)

print(student1.getStudentInfo())
print(student2.getStudentInfo())
print(student3.getStudentInfo())
