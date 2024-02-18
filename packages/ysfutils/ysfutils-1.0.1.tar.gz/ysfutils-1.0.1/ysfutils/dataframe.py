import re


def pd_float_format(x):
    """ df取消科学计数法显示, 根据xxxE-zz和xxxE+zz进行自动选择小数部分的精度

    Notes:
        实际使用时先import该函数, 然后执行pd.options.display.float_format=pdFloatFormat即可取消df的科学计数法显示

    """
    li1 = re.split('E+', str(x), flags=re.IGNORECASE)
    li2 = re.split('E-', str(x), flags=re.IGNORECASE)
    if len(li1) > 1 or len(li2) > 1:
        if len(li1) > 1:
            n1 = len(li1[0].replace('.', ''))-1
            n2 = int(li1[1])
            nx = n2-n1
            n = 0 if nx > 0 else nx
        else:
            n1 = len(li2[0].replace('.', '')) - 1
            n2 = int(li2[1])
            n = n1 + n2
        x2 = ('{:.'+str(n)+'f}').format(x)
    else:
        x2 = str(x)
    return x2
