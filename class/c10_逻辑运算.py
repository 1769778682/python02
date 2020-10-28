# and，or，not

# 案例一：年龄 >= 20，并且性别为男，可以参加非常勿扰
# age = 25
# sex = '女'
# if age >= 20 and sex =='男':
#     print('欢迎来到非常勿扰')
# else:
#     print('非常抱歉，下次再来吧')

# 案例2：定义两门科目的分数（linux和mysql),只要其中一门分数>60，就算及格
# linux_score = 60
# mysql_score = 50
# if linux_score > 60 or mysql_score > 60:
#     print('恭喜通过考试')
# else:
#     print('拜拜吧，重考吧')
# 案例三：定义一个布尔类型变量值代表员工，判断是否是本公司员工,不是本公司员工不许进入
man = True
if not man:  # not是对条件取反（注意，观察此条件时，不要先带入man的值，只看条件本身）
    print('请移步')
else:
    print('工作愉快')