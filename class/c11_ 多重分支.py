# 案例：对考试成绩进行分级处理
# 1. 定义 score 变量记录考试分数
score = 90
# 2. 如果分数是 大于等于 90分 应该显示 优
if score >= 90:
    print('优')
# 3. 如果分数是 大于等于 80分 并且 小于 90分 应该显示 良
elif score >= 80 and score < 90:
    print('良')
# 4. 如果分数是 大于等于 70分 并且 小于 80分 应该显示 中
elif score >= 70 and score < 80:
    print('中')
# 5. 如果分数是 大于等于 60分 并且 小于 70分 应该显示 差
elif score >= 60 and score < 70:
    print('差')
# 6. 其它分数显示 不及格
else:
    print('不及格')


# 代码优化
# 1. 定义 score 变量记录考试分数
score = 90
# 2. 如果分数是 大于等于 90分 应该显示 优
if score >= 90:
    print('优')
# 3. 如果分数是 大于等于 80分 并且 小于 90分 应该显示 良
# elif score >= 80 and score < 90:
elif 80 <= score < 90:
    print('良')
# 4. 如果分数是 大于等于 70分 并且 小于 80分 应该显示 中
# elif score >= 70 and score < 80:
elif 70 <= score < 80:
    print('中')
# 5. 如果分数是 大于等于 60分 并且 小于 70分 应该显示 差
# elif score >= 60 and score < 70:
elif 60 <= score < 70:
    print('差')
# 6. 其它分数显示 不及格
else:
    print('不及格')
