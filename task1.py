# Given an array of user connections. You need to implement a function,
# which takes three arguments as input: link information, as a tuple
# tuples, first name (str), second name (str). The function should return True if
# a relationship exists between any two given users, for example, if
# two users have friends in common or their friends have friends in common, etc. otherwise
# False.


def check_relation(net, first, second):
    identifier = None
    count = 0
    while count <= len(net):
        for tuple_names in net:
            if first in tuple_names:
                if tuple_names.index(first) == 0:
                    first = tuple_names[1]
                    if first == second:
                        identifier = True
                else:
                    first = tuple_names[0]
                    if first == second:
                        identifier = True
        count += 1
    return True if identifier else False


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша"),
    )
    assert check_relation(net, 'Петя', 'Стёпа') is True
