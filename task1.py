# Дан массив связей пользователей. Вам необходимо реализовать функцию,
# которая принимает на вход три аргумента: информация о связях, как кортеж (tuple)
# кортежей, первое имя (str), второе имя (str). Функция должна возвращать True, если
# связь между любыми двумя заданными пользователями существует, например, если у
# двух пользователей есть общие друзья или у их друзей есть общие друзья и т.д., иначе
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
    print(check_relation(net, 'Ваня', 'Дима'))