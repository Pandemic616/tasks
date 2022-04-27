# new_file=open("File_one.txt", "w+", encoding="UTF-8")
# new_file.write("Строка номер раз. \nСтрока номер два. \nСтрока номер три.")
# new_file.close()
# with open("File_one.txt", "a", encoding="UTF-8") as new_file:
#     new_file.write("\nНовая строка в с новым кодом.")
with open("File_one.txt", "a+", encoding="UTF-8") as new_file:
    new_file.seek(0)
    for line in new_file:
        print(line.strip())
    new_file.write("\nСтрока 5")