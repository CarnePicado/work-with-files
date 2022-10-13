with open('text_1.txt', 'rt') as file_1:
    f1 = file_1.read().strip()
    len_f1 = len(f1)

with open('text_2.txt', 'rt') as file_2:
    f2 = file_2.read().strip()
    len_f2 = len(f2)

with open('text_3.txt', 'rt') as file_3:
    f3 = file_3.read().strip()
    len_f3 = len(f3)

dct_files_value = {len_f1: [f1, '1'], len_f2: [f2, '2'], len_f3: [f3, '3']}

with open('general_file.txt', 'a') as file_4:
    for i in range(1, len(dct_files_value) + 1):
        max_value = max(dct_files_value)
        file_4.write(f'''text_{dct_files_value[max_value][1]}.txt\n{i}\n''')
        file_4.write(dct_files_value[max_value][0] + '\n')
        del dct_files_value[max_value]
print(file_4)
