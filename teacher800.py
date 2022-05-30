#!/usr/bin/env python

import helper_functions as hf
import sys
import subprocess
import re

#global variables
# TODO: fill in correct usr
usr = "bgg646"

def test():
    # check if user is in the right directory
    their_pwd, = hf.bytes_to_string(subprocess.check_output(['pwd']))
    correct_pwd = "/home/" + usr + "/lab0-part2"
    nested_directory = "/home/" + usr + "/.+/lab0-part2.*"

    # do they have a nested directory
    if(hf.match(nested_directory, their_pwd)):
        commands = ["cp -r " + their_pwd + " ~", "rm -r ~/lab0"] 
        command_message("You have a directory nested inside of your directory", commands)
        return
    elif(hf.match(correct_pwd, their_pwd)):
        print("cleared. Your directories are looking good")
    else:   
        hf.ask_ray("Your directories are messed up")
        return

    import error
    error.handle_errors()    

    import output
    output.check_output()

test()

# syntax tips:
    # for each open parenthesi \"(\", you have a closing parenthesi \")\"