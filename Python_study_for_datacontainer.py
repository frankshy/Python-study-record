#菜单
menu = """
#################################################[菜单]#############################################
#  1.添加学生信息 2.修改学生信息 3.删除学生信息 4.查询学生信息 5.列出所有学生 6.统计班级成绩 7.退出系统  #
###################################################################################################
"""
#定义学生信息词典
student_card = {}

print("欢迎使用教务管理系统")

while True:
    print(menu)
    choice = input("请输入:")
    match choice:
        case '1':
            student_name = input("请输入学生名字:")
            grade_chinese = float(input("请输入学生语文成绩:"))
            grade_math = float(input("请输入学生数学成绩:"))
            grade_english = float(input("请输入学生英语成绩:"))
            if student_name in student_card:
                print("该学生已录入系统，如需修改请按2，请重新输入")
                continue
            else :
                student_card[student_name] = {"chinese":grade_chinese,"math":grade_math,"english":grade_english}
                print("添加成功~")

        case '2':
            student_name = input("请输入学生名字:")
            if student_name not in student_card:
                print("该学生未录入系统，如需添加请按1，请重新输入")
                continue
            grade_chinese = float(input("请输入学生语文成绩:"))
            grade_math = float(input("请输入学生数学成绩:"))
            grade_english = float(input("请输入学生英语成绩:"))

            student_card[student_name] = {"chinese":grade_chinese,"math":grade_math,"english":grade_english}
            print("修改成功~")

        case '3':
            student_name = input("请输入学生名字:")
            if student_name not in student_card:
                print("该学生未录入系统，不可删除，请重新输入")
                continue
            else :
                del student_card[student_name]
        case '4':
            find_name = input("请输入要查找的学生姓名")
            if find_name not in student_card:
                print("未查找到该学生，该学生为录入系统")
            else :
                student_grade = student_card[find_name]
                print(f"学生成绩:语文：{student_grade['chinese']},数学：{student_grade['math']},英语：{student_grade['english']}")
        case '5':
            for student_name in student_card:
                student_grade = student_card[student_name]
                print(f"学生姓名:{student_name},学生成绩:语文：{student_grade['chinese']},数学：{student_grade['math']},英语：{student_grade['english']}")
        case '6':

            grade_list = {"chinese":[],"math":[],"english":[]}
            for student_name,student_scores in student_card.items():
                for subject in grade_list:
                    grade_list[subject].append(student_scores[subject])
            #最高分统计
            max_score_chinese = max(grade_list["chinese"])
            max_score_math = max(grade_list["math"])
            max_score_english = max(grade_list["english"])

            #最低分统计
            min_score_chinese = min(grade_list["chinese"])
            min_score_math = min(grade_list["math"])
            min_score_english = min(grade_list["english"])

            #平均分统计
            avg_score_chinese = sum(grade_list["chinese"])/len(grade_list["chinese"])
            avg_score_math = sum(grade_list["math"])/len(grade_list["math"])
            avg_score_english = sum(grade_list["english"])/len(grade_list["english"])

            #遍历各科学生成绩并找到最高分
            chinese_max_student = [name for name,score in student_card.items() if score["chinese"] == max_score_chinese]
            math_max_student = [name for name,score in student_card.items() if score["math"] == max_score_math]
            english_max_student = [name for name,score in student_card.items() if score["english"] == max_score_english]

            #遍历各科学生成绩并找到最低分
            chinese_min_student = [name for name,score in student_card.items() if score["chinese"] == min_score_chinese]
            math_min_student = [name for name,score in student_card.items() if score["math"] == min_score_math]
            english_min_student = [name for name,score in student_card.items() if score["english"] == min_score_english]

            #输出各科最高分，最低分，平均分
            print(f"语文最高分:{max_score_chinese}"
                  f"数学最高分:{max_score_math}"
                  f"英语最高分:{max_score_english}")
            print(f"语文最低分:{min_score_chinese}"
                  f"数学最低分:{min_score_math}"
                  f"英语最低分:{min_score_english}")
            print(f"语文平均分:{avg_score_chinese:.2f}"
                  f"数学平均分:{avg_score_math:.2f}"
                  f"英语平均分:{avg_score_english:.2f}")

            #输出各科最高分，最低分的学生姓名
            print(f"语文最高分的学生是 {chinese_max_student}"
                  f"数学最高分的学生是 {math_max_student}"
                  f"英语最高分的学生是 {english_max_student}")
            print(f"语文最低分的学生是 {chinese_min_student}"
                  f"数学最低分的学生是 {math_min_student}"
                  f"英语最低分的学生是 {english_min_student}")

        case '7':
            break
        case _ :
            print("输入错误")
