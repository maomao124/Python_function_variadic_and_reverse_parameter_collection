"""
 * Project name(项目名称)：Python函数可变参数
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/25 
 * Time(创建时间)： 20:19
 * Version(版本): 1.0
 * Description(描述)： 
 """


def f1(*num):
    """
    累加
    :param num:
    :return:
    """
    max1 = 0
    for i in num:
        max1 = max1 + i
    return max1


def f2(data, *num):
    """
    累加
    :param data:
    :param num:
    :return:
    """
    max1 = 0
    for i in num:
        max1 = max1 + i
    return max1 * data


def f3(first, last, **user_info):
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


if __name__ == '__main__':
    print(f1(1, 2))
    print(f1(1, 2, 5, 6))
    print(f1(1))
    print(f1(1, 2, -3))
    print(f1(1, 2, 7, 8, 9, 3, 1, 7))

    # 函数接收任意数量的非关键字实参
    # 如果函数参数中既要接收已知数量的实参，又要接收任意数量的实参，则必须遵循一个原则，即将接纳任意数量实参的形参放在最后。
    print(f2(3))
    print(f2(2, 1, 1))
    print(f2(2, 4, 5, 3))

    # 函数接收任意数量的关键字实参
    # 如果在调用函数时是以关键字参数的形式传入实参，且数量未知，则需要使函数能够接收任意数量的键值对参数。
    print(f3('albert', 'einstein', location='princeton', field='physics'))
