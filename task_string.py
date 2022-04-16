# "ghjhghjyfjfjjikutufjugjgjgu" четные в uppercase; не четные в lowercase
string = "ghjhghjyfjfjjikutufjugjgjgu"
string_new = ""
for i in range(len(string)):
    if i % 2 == 0:
        string_new += string[i].upper()
    else:
        string_new += string[i].lower()
print(string_new)
