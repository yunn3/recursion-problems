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


class Classroom:

    def __init__(self, students: Student, courseName: str, teacher: str) -> None:
        self.students = students
        self.courseName = courseName
        self.teacher = teacher

    def getClassIdentity(self) -> str:
        return self.courseName + " managed by " + self.teacher

    def getNumberOfStudents(self) -> str:
        return len(self.students)


def printHonorStudents(school: list) -> str:
    honor_grade = 10
    class_num = 0

    for classroom in school:
        for (
            student
        ) in (
            classroom.students
        ):  # student = ex) Student("AC-343424", "James", "Smith", 6)
            if student.gradeLevel >= honor_grade:
                print(
                    student.getStudentInfo()
                    + " from "
                    + classroom.teacher
                    + "'s class",
                )


classroom1 = Classroom(
    [
        Student("AC-343424", "James", "Smith", 6),
        Student("AC-343428", "Maria", "Garcia", 5),
        Student("AC-343434", "Robert", "Johnson", 3),
        Student("AC-343454", "Danny", "Robertson", 10),
    ],
    "Algebra II",
    "Emily Theodore",
)
classroom2 = Classroom(
    [
        Student("AC-340014", "Kent", "Carter", 9),
        Student("AC-340024", "Isaiah", "Chambers", 10),
        Student("AC-340018", "Leta", "Ferguson", 7),
    ],
    "English",
    "Daniel Pherb",
)

school = [classroom1, classroom2]

printHonorStudents(school)
