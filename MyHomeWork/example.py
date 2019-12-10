class Student():
    def __init__(self, student_id, student_name, seleted_course = []):
        self.id = student_id
        self.name = student_name
        self.selected_course = seleted_course


    @property
    def course_detail(self):
        return self.selected_course


    def add_course(self, course_info):
        self.selected_course.append(course_info)


    def __str__(self):
        print('姓名：{}， 学号：{}。'.format(self.name, self.id))



class Teacher():
    def __init__(self, teacher_id, teacher_name, teacher_phone):
        self.id = teacher_id
        self.name = teacher_name
        self.phone = teacher_phone


    def __str__(self):
        print('教师姓名{}，教师编号{}。'.format(self.name, self.id))



class Course():
    def __init__(self, course_id, course_name, teacher = None):
        self.id = course_id
        self.name = course_name
        self.teacher = teacher


    def binding(self, teacher):
        if isinstance(teacher, Teacher):
            self.teacher = teacher
            return {'课程名称':self.name, '教师名称':teacher.name}
        else:
            print('this is not a teacher')
            return None



