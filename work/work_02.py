# 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
# 2. 电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码功能
# 3. 比较胜负
# 导包
import random
# 定义变量
player = int(input('请出拳石头（1）／剪刀（2）／布（3）:'))
# 使用随机函数
computer = random.randint(1, 3)
if computer:
    print(f'电脑出的是{computer}')
# 总共的结果有三种：玩家赢，电脑赢，平局
# 不管谁赢都有三种出拳方法：石头1-剪刀2/剪刀2-布3/布3-石头1
if ((player == 1 and computer == 2) or
        (player == 1 and computer == 2) or
        (player == 1 and computer == 2)):
    print('电脑弱爆了')
elif player == computer:
    print('想到一起了,再来一局')
else:
    print('No!!!,我要跟你决战到天明！')
