# 根据用户输入的三条边的数值, 判断三角形的种类
# 要求: 只判断普通三角形/等边三角形/等腰三角形/不是三角形即可
# 提示: 满足三角形的最基本条件是, 任意两条边之和要大于第三条边

# 定义三角形的三条边 a b c
a = int(input('请输入三角形的三条边长:\n''a:'))
b = int(input('b:'))
c = int(input('c:'))
# 判断：结果有四种：普通三角形/等边三角形/等腰三角形/不是三角形
# 先判断是不是三角形
if a+b > c and a+c > b and c+b > a:
    # 在是三角形的情况下判断是什么三角形
    if a == b == c:
        print('这是等边三角形')
    elif a == b or a == c or b == c:
        print('这是等腰三角形')
    else:
        print('这是普通三角形')
else:
    print('这不是三角形')