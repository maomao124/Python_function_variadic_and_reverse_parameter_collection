"""
 * Project name(项目名称)：Python函数可变参数
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/25 
 * Time(创建时间)： 20:36
 * Version(版本): 1.0
 * Description(描述)： 参数收集
 """


def f1(*n, num):
    """
    *参数收集
    :param num:
    :param n:
    :return:
    """
    print(num)
    print(n)


def f2(*n1, num1, **n, ):
    """
    **参数收集
    :param n1:
    :param num1:
    :param n:
    :return:
    """
    print(n1)
    print(num1)
    print(n)


if __name__ == '__main__':
    f1(4, 5, 6, num=3)
    f2(1, 9, 7, num1=4, a=2, b=3)
