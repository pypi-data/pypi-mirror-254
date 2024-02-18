from enums import *


def lister(str_list: str, typ: Typ | None = Typ.auto) -> list | None:
    """
    Converts strings to lists.
    :param str_list: The str_list is a string with a list separated by a comma or a space, for example.
    :param typ: The type does not have to be specified because this is done automatically.
    :return: list
    """
    _list = str_list
    if typ == Typ.auto:
        if " " in str_list and "," not in str_list:
            typ = Typ.space
        elif "," in str_list:
            typ = Typ.comma
    if typ == Typ.space:
        _list = str_list.replace(" ", ",")
        _list = _list.split(",")
    elif typ == Typ.comma:
        if ", " in str_list:
            _list = str_list.split(", ")
        else:
            _list = str_list.split(",")
    if isinstance(_list, str) and str_list != "" and str_list != " ":
        _list = [_list]
    if str_list == " ":
        return None
    return _list if isinstance(_list, list) else None


def str_list(list_list: list, split: Splits | None = Splits.comma) -> str:
    """
    Convert lists to strings.
    :param list_list: The list to be converted into a string.
    :param split: The way the entries should be separated from each other.
    :return: str
    """
    str_list = ""
    nothing = ""
    default = ", "
    if split == Splits.comma:
        split = ", "
    elif split == Splits.space:
        split = " "
    else:
        split = default
    for index, element in enumerate(list_list):
        if element != "":
            str_list += f"{split if (split and index != 0) else nothing}" + str(element)
    return str_list


def difference(list1: list, list2: list, typ: Tools | None = Tools.same) -> list | None:
    """
    Shows the differences between two lists.
    :param list1: The first list.
    :param list2: The secend list.
    :param typ: The type whether entries should occur twice. (ListTransformer.Tools.no_same) Default: ListTransformer.Tools.same
    :return: list or None
    """
    diff = []
    big_list = list1 if (len(list1) >= len(list2)) else list2
    tiny_list = list2 if (len(list2) <= len(list1)) else list1
    for entry in big_list:
        if entry not in tiny_list:
            if typ == Tools.no_same:
                if entry not in diff:
                    diff.append(entry)
            else:
                diff.append(entry)
    for entry in tiny_list:
        if entry not in big_list:
            diff.append(entry)
    return diff if diff else None


def __get_len__(liste: list, target):
    _len = 0
    for entry in liste:
        if entry == target:
            _len += 1
    return _len


def intersection(list1: list, list2: list, typ: Tools | None = Tools.same) -> list | None:
    """
    Shows the entries that are the same.
    :param list1: The first list.
    :param list2: The secend list.
    :param typ: The type whether entries should occur twice. (ListTransformer.Tools.no_same) Default: ListTransformer.Tools.same
    :return: list or None
    """
    intersection = []
    big_list = list1 if (len(list1) >= len(list2)) else list2
    tiny_list = list2 if (len(list2) <= len(list1)) else list1
    for entry in big_list:
        if entry in tiny_list:
            if entry not in intersection and typ == Tools.no_same:
                intersection.append(entry)
            elif typ == Tools.same:
                intersection.append(entry)
    return intersection if intersection else None


def combine(list1: list, list2: list, typ: Tools | None = Tools.same) -> list | None:
    """
    returns the two lists combined into one.
    :param list1: The first list to combine.
    :param list2: The secend list to combine.
    :param typ: The type whether entries should occur twice. (ListTransformer.Tools.no_same) Default: ListTransformer.Tools.same
    :return: list or None
    """
    for entry in list2:
        if typ == Tools.no_same and entry not in list1:
            list1.append(entry)
        elif typ == Tools.same:
            list1.append(entry)
    if typ == Tools.no_same:
        for entry in list1:
            entry_len = __get_len__(list1, entry)
            if entry_len > 1:
                for _ in range(1, entry_len):
                    list1.remove(entry)
    return list1 if list1 else None
