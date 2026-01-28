import csv

# with open ("file.csv", "w") as file:
#     write_on = csv.writer(file)
#     write_on.writerow(["Name", "Age", "City"])
#     write_on.writerow (["Alice", 30, "New York"])

with open("file.csv", "r") as file:
    read_from = csv.reader (file, delimiter="\n")
    for row in read_from:
        print(row)
        for item in row:
            # print(item)
            if 'ppsu' in item:
                print(row)

            with open("new_file.txt", "a", newline='') as new_file:
                write_to = csv.writer(new_file, dilimetr=',')
                write_to.writerow(row)