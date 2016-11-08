# 判断一个函数是不是回数，回数的意思就是把数倒过来后和以前一样，比如 909，,1881,12344321等等
def is_palindrome(s):
    # 先把数字转成字符串，这样，才有长度，才可以对每个位置的数进行索引
    s_str = str(s)
    # 求出这个数字的位数，也就是字符串的长度
    l = len(s_str)
    # 判断长度是奇数还是偶数，分别进行讨论，第一种情况是偶数，第二种情况是奇数
    if l % 2 == 0:
        a = True
        # 只有每个对称的位置的数都相等时，才返回TRUE，不然就是FALSE
        # 经过debug后，它表示下面这一行有问题，前面没有问题
        for i in range(l / 2):
            if s_str[i] == s_str[l - i - 1]:
                a = a and True
            else:
                a = a and False
            return a
    else:
        for i in range((l - 1) / 2):
            b = True
            if s_str[i] == s_str[l - i - 1]:
                b = b and True
            else:
                b = b and False
            return b

print(is_palindrome(9009))



