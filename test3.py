"""
 * Project name(项目名称)：Python函数可变参数
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/25 
 * Time(创建时间)： 20:43
 * Version(版本): 1.0
 * Description(描述)： 逆向参数收集
 """


def f1(a, b, c):
    """
    逆向参数收集
    :param a:
    :param b:
    :param c:
    :return:
    """
    print(a)
    print(b)
    print(c)


def f2(a, b, c):
    """
    逆向参数收集
    :param a:
    :param b:
    :param c:
    :return:
    """
    print(a)
    print(b)
    print(c)


if __name__ == '__main__':
    v = (3, 6, 7)
    f1(*v)
    l = [4, 2, 1]
    f1(*l)

    d = {'a': 4, 'b': 0, 'c': 88}
    f2(**d)
