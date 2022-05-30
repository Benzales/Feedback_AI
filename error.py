import helper_functions as hf
import subprocess
import re

def handle_errors():
    usr = "bgg646"
    correct_pwd = "/home/" + usr + "/lab0-part2"
    script_path = correct_pwd + "/Your_script/your_script.py"
    p = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    o, e = p.communicate() 
    output, error = hf.bytes_to_string(o, e)
    if(p.returncode == 1):
        print("\n\nYou have an error in your code\n")
        lines = re.split("\n", error)
        line_num = -1
        error_message = lines[len(lines) - 1]
        found = False
        i = 1
        regex = ".*" + script_path + ".*"
        while i < len(lines) and line_num == -1 and not found:
            if hf.match(regex, lines[i]):
                line_num = i
            elif line_num == -1:
                found = True
            i+=2
        
        error_line = lines[line_num + 1].strip()
        line_num = re.sub(", in.*", "", re.sub(".*, line ", "", lines[line_num]))
        error_line, error_message, line_num
        print("Line number:", str(line_num))
        # print(error_message)
        # TODO handle error
            # run-time
            # NameError
                # mispelled python function name - print, numpy, str, type, sqrt, power, exp
                # mispelled their own function name
                # mispelled variable name
            # SyntaxError TODO different format than other error messages
                # parenthesis
        return
    else:
        print("No errors")

# syntax tips:
    # for each open parenthesi \"(\", you have a closing parenthesi \")\"