

# some_file = open("file.txt", "r")
# print(some_file.read())
#
# list_number = []
# for line in some_file:
#     print(line, end="")
#     print(type (line))
#     list_number.append(int (line))
# print(list_number)
#
#
# result = sum(list_number)/len(list_number)
# print(round(result, 2))
# some_file.close()

file_write = open("file.txt", "w")
for i in range(50000,100000,25):
        file_write.write(f'{i}\n')

file_write.write('9999999')
file_write.close()