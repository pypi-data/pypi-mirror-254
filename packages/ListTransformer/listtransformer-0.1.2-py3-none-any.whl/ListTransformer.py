from enums import *


def lister(str_list: str, typ: Typ | None = Typ.auto) -> list:
    """
    The str_list is a string with a list separated by a comma or a space, for example.
    The type does not have to be specified because this is done automatically.
    :param str_list:
    :param typ:
    :return: list
    """
    if typ == Typ.auto:
        if " " in str_list and "," not in str_list:
            typ = Typ.space
        elif "," in str_list:
            typ = Typ.comma
    if typ == Typ.space:
        str_list = str_list.replace(" ", ",")
        str_list = str_list.split(",")
    elif typ == Typ.comma:
        if ", " in str_list:
            str_list = str_list.split(", ")
        else:
            str_list = str_list.split(",")
    return str_list


def str_list(list_list: list, split: Splits | None = Splits.comma) -> str:
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
        str_list += f"{split if (split and index != 0) else nothing}" + element
    return str_list
