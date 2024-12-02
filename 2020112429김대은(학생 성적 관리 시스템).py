class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def calculate_average(self):
        if len(self.scores) > 0:
            return sum(self.scores) / len(self.scores)
        return 0


class GradeBook:
    def __init__(self):
        self.students = []
        self.student_ids = set()

    def add_student(self, name, student_id):
        if student_id not in self.student_ids:
            student = Student(name, student_id)
            self.students.append(student)
            self.student_ids.add(student_id)
            print(f"{name} 학생이 등록되었습니다.")
        else:
            print(f"학번 {student_id}는 이미 등록된 학생입니다.")

    def add_student_score(self, student_id, score):
        for student in self.students:
            if student.student_id == student_id:
                student.add_score(score)
                print(f"학번 {student_id} 학생의 점수 {score}가 추가되었습니다.")
                return
        print(f"학번 {student_id}에 해당하는 학생을 찾을 수 없습니다.")  # 학생을 찾을 수 없는 경우

    def get_top_students(self, n):
        sorted_students = sorted(self.students, key=lambda student: student.calculate_average(), reverse=True)
        top_students = []
        for i in range(min(n, len(sorted_students))):
            student = sorted_students[i]
            top_students.append((student.name, student.calculate_average()))  # 학생 이름과 평균 점수를 튜플로 추가
        return top_students



grade_book = GradeBook()


grade_book.add_student("김대은", 2020112429)
grade_book.add_student("황지원", 2024111537)
grade_book.add_student("조영재", 2020112426)


grade_book.add_student_score(2020112429, 88)
grade_book.add_student_score(2020112429, 92)
grade_book.add_student_score(2024111537, 75)
grade_book.add_student_score(2024111537, 80)
grade_book.add_student_score(2020112426, 95)
grade_book.add_student_score(2020112426, 90)


top_students = grade_book.get_top_students(2)
print("상위 2명 학생의 성적:", top_students)
