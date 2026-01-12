def find_common_participants(str_1, str_2, divider = ","):
    set_1 = set(str_1.split(divider))
    set_2 = set(str_2.split(divider))
    return sorted(list(set_1.intersection(set_2)))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, divider="|"))