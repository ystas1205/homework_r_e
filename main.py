import re
import csv

with open("phonebook.csv", encoding="utf-8", ) as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pattern = r"(\+7|8)\W*(\d{3})\W*(\d{3})(\W*)(\d{2})\W*(\d{2})\s*\(*([доб.]*)" \
          r"*(2*0*9*7*9*2*6*)\)*"
replace = r"+7(\2)-\3-\5-\6 \7\8 "
new_list = []
for data in contacts_list:
    full_name = ' '.join(data[:3]).split(' ')
    result = [full_name[0], full_name[1], full_name[2], data[3], data[4],
              re.sub(pattern, replace, data[5]),
              data[6]]
    new_list.append(result)
for contact in new_list:
    first_name = contact[0]
    last_name = contact[1]
    for new_contact in new_list:
        new_first_name = new_contact[0]
        new_last_name = new_contact[1]
        if first_name == new_first_name and last_name == new_last_name:
            if contact[2] == "": contact[2] = new_contact[2]
            if contact[3] == "": contact[3] = new_contact[3]
            if contact[4] == "": contact[4] = new_contact[4]
            if contact[5] == "": contact[5] = new_contact[5]
            if contact[6] == "": contact[6] = new_contact[6]
result = []
for i in new_list:
    if i not in result:
        result.append(i)
with open("phonebook_1.csv", "w", encoding="utf-8", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(result)
    