class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.attendance = False

    def mark_attendance(self):
        self.attendance = True


class AttendanceBook:
    def __init__(self):
        self.students = []
        self.student_ids = set()

    def add_student(self, name, number):
        if number not in self.student_ids:
            student = Student(name, number)
            self.students.append(student)
            self.student_ids.add(number)
            print("{} 학생이 등록되었습니다.".format(name))
        else:
            print("학생 번호가 중복됩니다.")

    def mark_student_attendance(self, student_number):
        for student in self.students:
            if student.number == student_number:
                student.mark_attendance()
                print("{} 학생의 출석을 마크했습니다.".format(student.name))
                return
        print("해당 학생 번호가 존재하지 않습니다.")

    def get_attendance_summary(self):
        attendance_summary = {"출석": 0, "결석": 0}
        for student in self.students:
            if student.attendance:
                attendance_summary["출석"] += 1
            else:
                attendance_summary["결석"] += 1
        return attendance_summary

    def get_student_list(self):
        student_list = []
        for student in self.students:
            status = "출석" if student.attendance else "결석"
            student_list.append(f"이름: {student.name}, 번호: {student.number}, 상태: {status}")
        return student_list



#################################################################




attendance_book = AttendanceBook()    # 출석부 테스트


attendance_book.add_student("김대열", 2019111111)      # 학생 추가
attendance_book.add_student("김대은", 2020112429)
attendance_book.add_student("김파이썬", 2020335873)
attendance_book.add_student("김너무어려워요", 2024558282)


attendance_book.mark_student_attendance(2019111111) # 출석 체크
attendance_book.mark_student_attendance(2020112429)
attendance_book.mark_student_attendance(2020112429) #중복?

print("출석 요약:", attendance_book.get_attendance_summary()) # 출석 요약 및 출석한 학생 목록 출력
print("출석한 학생 목록:", attendance_book.get_student_list())