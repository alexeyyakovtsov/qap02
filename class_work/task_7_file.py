test_file = open('test.txt', 'w')
stroka = ['Кодировки\n', 'Работа с файлами\n', 'Работа с внешними данными: JSON, CSV, Excel\n']
test_file.write(str(stroka))
test_file = open('test.txt', 'r')
for line in test_file:
    print(line)
test_file.close()


test_file2 = open('test2.txt', 'w')
test_file2.write(str(stroka))

test_file2 = open('test2.txt', 'r')
for li in test_file2:
    print(li)

test_file.close()
