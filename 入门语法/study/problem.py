# 从标准输入读取两行，用空格分隔的整数
input_line1 = input()
input_line2 = input()

# 将两个输入行合并成一个列表
numbers = input_line1.split() + input_line2.split()

# 将字符串转换为整数
numbers = list(map(int, numbers))

# 按照降序排序
numbers.sort(reverse=True)

# 输出结果
print(numbers)
