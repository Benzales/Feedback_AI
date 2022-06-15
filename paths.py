def check_directories():
    # check if user is in the right directory
    import help
    import subprocess
    their_pwd, = help.bytes_to_string(subprocess.check_output(['pwd']))
    their_pwd = their_pwd.rstrip('\n')
    correct_pwd = "/home/" + help.usr + "/lab0-part2"
    nested_directory = "/home/" + help.usr + "/.+/lab0-part2.*"

    # do they have a nested directory
    if(help.match(nested_directory, their_pwd)):
        commands = ["cp -r " + their_pwd + " ~", "rm -r ~/lab0"] 
        help.command_message("You have a directory nested inside of your directory", commands)
        return
    elif(help.match(correct_pwd, their_pwd)):
        print("Directories are acceptable.")
    else:   
        print(correct_pwd)
        print(their_pwd)
        print(correct_pwd == their_pwd)
        help.ask_ray("Your directories are messed up")
        return