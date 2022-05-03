#!/usr/bin/env python

import sys
import subprocess
import re

#helper functions
def match(regex, str):
    match_obj = re.search(regex, str)
    if(match_obj != None):
        beg, end = match_obj.span()
        if(end - beg == len(str)):
            return True
    return False

def bytes_to_string(*args):
    list = [] 
    for b in args:
        list.append(b.decode('UTF-8').rstrip('\n'))
    return tuple(list)

def command_message(issue, commands):
    print("\n", issue, "\n\nRun the following commands:")
    for command in commands:
        print(command)
    print()

def ask_ray(issue):
    print(issue + ", but I'm not sure how to fix it so ask Ray.")

def cleared(expected, output):
    # TODO handle new lines
    cur_line = output[:len(expected) if len(output) >= len(expected) else len(output)]
    if(expected == "\n"):
        p_expected = "a blank line"
    if(cur_line == "\n"):
        p_cur_line = "a blank line"
    else:
        p_expected = "\"" + expected.strip() + "\""
        p_cur_line = "\"" + cur_line.strip()     + "\""
    if(cur_line == expected):
        output = output[len(expected):]
        print("\tcleared. You successfully outputted", p_expected)
        return output
    else:
        print("\n\n" + p_expected + " must be printed.")
        print(p_cur_line + " is what you're printing\n\n")
        return False




def test():
    # TODO: fill in correct usr
    usr = "bgg646"





    # check if user is in the right directory
    their_pwd, = bytes_to_string(subprocess.check_output(['pwd']))
    correct_pwd = "/home/" + usr + "/lab0-part2.*"
    nested_directory = "/home/" + usr + "/.+/lab0-part2.*"





    # do they have a nested directory
    if(match(nested_directory, their_pwd)):
        commands = ["cp -r " + their_pwd + " ~", "rm -r ~/lab0"] 
        command_message("You have a directory nested inside of your directory", commands)
        return
    elif(match(correct_pwd, their_pwd)):
        print("\tcleared. Your directories are looking good")
    else:   
        ask_ray("Your directories are messed up")
        return
    




    # Check for syntax errors
    script_path = correct_pwd[0:len(correct_pwd) - 2] + "/Your_script/your_script.py"
    p = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    o, e = p.communicate() 
    output, error = bytes_to_string(o, e)
    if(p.returncode == 1):
        print("You have an error in your code")
        lines = re.split("\n", error)
        line_num = -1
        error_message = lines[len(lines) - 1]
        found = False
        i = 1
        regex = ".*" + script_path + ".*"
        while i < len(lines) and line_num == -1 and not found:
            if match(regex, lines[i]):
                line_num = i
            elif line_num == -1:
                found = True
            i+=2
        
        error_line = lines[line_num + 1].strip()
        line_num = int(re.sub(", in.*", "", re.sub(".*, line ", "", lines[line_num])))
        # error_line, error_message, line_num
        # TODO handle error
            # run-time
            # syntax
        return


    

    # Check their output
    f = open("/home/bgg646/feedback/answers.txt", 'r')
    for line in f.readlines():
        if not output:
            return
        expected = line
        output = cleared(expected, output)
    f.close()

test()





# QUESTIONS:
# THEME: make scalable

# answers.txt
# Can they have extra new lines
# Should I get their name?

# syntax tips:
    # for each open parenthesi \"(\", you have a closing parenthesi \")\"