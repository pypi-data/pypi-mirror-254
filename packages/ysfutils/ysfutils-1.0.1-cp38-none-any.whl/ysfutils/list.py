import math
from typing import Any


def chunks_list(ori_list: list, **kwargs: Any):
    """ 按片数或长度对list进行分片

    Args:
        ori_list: 原始list
        kwargs: num=任意非0整数或len=任意非0整数

    Returns:
        [[分片1], [分片2]......]或者[]

    """
    num = kwargs.get("num", None)
    chunk_len = kwargs.get("len", None)
    if ori_list and num:
        # 将list分成num指定的片数, 例如按照cpu的核数进行分片
        sub_list_len = int(math.ceil(len(ori_list) / float(num)))
        return [ori_list[i:i + sub_list_len] for i in range(0, len(ori_list), sub_list_len)]
    elif ori_list and chunk_len:
        # 将list按每个分片的长度进行分片
        return [ori_list[i:i + chunk_len] for i in range(0, len(ori_list), chunk_len)]
    else:
        return ori_list


def _compare_dicts(dict1: dict, dict2: dict):
    """ 比较字典是否相等 """
    # 检查键的数量是否相同
    if len(dict1) != len(dict2):
        return False

    # 比较每个键和值
    for key in dict1:
        if key not in dict2:
            return False
        value1 = dict1[key]
        value2 = dict2[key]
        # 递归比较嵌套字典
        if isinstance(value1, dict) and isinstance(value2, dict):
            if not _compare_dicts(value1, value2):
                return False
        else:
            if value1 != value2:
                return False
    return True


def compare_dict_in_list(list_base: list, list_wait_compare: list):
    """ 比较两个list中的dict的key是否相等

    Args:
        list_base: 作为标准的基础list
        list_wait_compare: 要比较的list

    Returns:
        一样返回True, 有差异返回False

    """
    for base_dict in list_base:
        for wait_compare_dict in list_wait_compare:
            compare_result = _compare_dicts(base_dict, wait_compare_dict)
            if not compare_result:
                return False
    return True
