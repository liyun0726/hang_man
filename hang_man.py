# coding:utf-8
"""chap_4-challenge1"""
"""1.编写一个函数，接受数字作为输入，并返回该数字的平方"""


# def square():
#     try:
#         a = input("type a number:")
#         a = int(a)
#         print(a ** 2)
#     except:
#         print('Invalid input')
#
#
# square()
def squared(x):
    return x**2
print(squared(2))

"""2.编写一个以字符串为参数并将其打印的函数"""


def print_string(string):
    """:param str
        打印字符串"""
    print(string)


print_string("I love you!")

"""3.编写一个接受3个必选参数，2个可选参数的函数"""
/tmp/424710044
/tmp/305923719
def add(x, y, z, a=1, b=1):
    print(x + y + z + a + b)
add(1, 2, 3, 4, 5)

"""4.编写一个带两个函数的程序。
第一个函数应该接受一个整数为参数，并返回该整数除以2的值。
第二个函数应该接受一个整数为参数，并返回该整数乘以4的值。
调用第一个函数，将结果保存至变量，并将变量作为参数传递给第二个函数
"""

def devide(x):
    """:param int"""
    try:
        num = int(num)
        return num/2
    except ValueError:
        print("Please type a number:")
def multiply(x):
    print(x*4)
y = devide(4)
z = multiply(y)
print(z)

"""5.编写一个将字符串转换为float对象并返回结果的函数。
使用异常处理来捕获可能发生的异常"""

def convert(string):
    """str to float
    :param string"""
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string to a float")
c = convert("shjjk")
print(c)

if __name__ == '__main__':

