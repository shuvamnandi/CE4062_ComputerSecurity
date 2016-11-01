import os
import sys

user_list = ['alice', 'charlie', 'dennis', 'eve', 'fong']
if len(sys.argv) != 2:
        print 'Usage: python', sys.argv[0], 'username'
else:
        charlie_passwd = 'charliethree'
        user_input = sys.argv[1].strip()

        if user_input in user_list:
                command = '/home/bob/Public/user-secret charlie/../' + user_input + ' ' + charlie_passwd
                os.system(command)
        else:
                print 'User', user_input, 'not found.'