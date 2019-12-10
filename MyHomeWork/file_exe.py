import example

def introduction(str):
    print('**********************{}********************'.format(str))




def prepare_course():
    course_dict = {'01':'网络爬虫',
                   '02':'数据分析',
                   '03':'人工智能',
                   '04':'机器学习',
                   '05':'云计算',
                   '06':'大数据',
                   '07':'图像识别',
                   '08':'Web开发'}
    course_list = []
    for i in course_dict:
        course_list.append(example.Course(i,course_dict[i]))
    return course_list

def create_teacher():
    t1 = [["T1", "张亮", "13301122001"],
    ["T2", "王朋", "13301122002"],
    ["T3", "李旭", "13301122003"],
    ["T4", "黄国发", "13301122004"],
    ["T5", "周勤", "13301122005"],
    ["T6", "谢富顺", "13301122006"],
    ["T7", "贾教师", "13301122007"],
    ["T8", "杨教师", "13301122008"]]

    teacher_list = []
    for i in range(len(t1)):
        teacher_list.append(example.Teacher(t1[i][0], t1[i][1], t1[i][2]))
    return teacher_list

def course_to_teacher():
    course_teacher = []
    ls_course = prepare_course()
    ls_teacher = create_teacher()
    for i in range(len(ls_course)):
        course_teacher.append(ls_course[i].binding(ls_teacher[7-i]))
    return course_teacher

def create_student():
    ls_student = ["小亮", "小明", "李红", "小丽", "Jone", "小彤", "小K", "慕慕"]
    id_limit = []
    for i in range(1000, 1008):
        id_limit.append(i)

    student_list = []
    for i in range(len(ls_student)):
        student_list.append(example.Student(id_limit[i],ls_student[7-i]))
    return student_list

if __name__ == '__main__':
    create_teacher()
    prepare_course()
    print(course_to_teacher())
    introduction('慕课学院一班学生信息')
    for i in range(len(create_student())):
        print(create_student()[i].__str__())
    introduction('慕课学院一班选课结果')
    student_list = create_student()
    print(student_list)
    course_teacher = course_to_teacher()
    for i in range(len(course_teacher)):
        student_list[i].add_course(course_teacher[i])
        print(student_list[i].course_detail)
    print(student_list[0].course_detail)

    for i in range(len(student_list)):
        print('Name:{},Selected:{}'.format(student_list[i].name, student_list[i].course_detail))
    #     # print(create_student()[i].add_course(course_to_teacher()[i]))

