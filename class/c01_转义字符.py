print('你好')
# # 注意：print函数在执行时，默认附带换行效果（\n:换行）
print('我是',end='\n')
print('朋友')
print('白日依山尽,黄河入海流')
print('白日依山尽,\n黄河入海流')
# 要求打印不换行
print('你好',end='')
print('我是',end='')
print('朋友')
# 其它转义字符：\t: 空格或制表符（tab键）可以连续使用多个
print('你好',end='\t')
print('我是',end='\t')
print('朋友')
print('你好',end='\t\t')
print('我是',end='\t')
print('朋友')