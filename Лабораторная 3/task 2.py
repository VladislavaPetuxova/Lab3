def find_common_participants(str_1, str_2, k=','):
    a = list(set(list(str_1.split(k))).intersection(list(str_2.split(k))))
    a.sort()
    return a

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))
