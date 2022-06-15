# helper methods
import re
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
        list.append(b.decode('UTF-8'))
    return tuple(list)

def command_message(issue, commands):
    print("\n", issue, "\n\nRun the following commands:")
    for command in commands:
        print(command)
    print()

def ask_ray(issue):
    print(issue + ", but I'm not sure how to fix it so ask Ray.")

def get_line(str):
    index = str.find("\n")
    if index == -1:
        print(str)
    return str if index == -1 else str[:index + 1]

def extract(answer, cur_line, k, key):

    # store the regex pattern that matches the expected answer
    (a ,iso_re) = stored_answers[key]

    # find span of key in answer
    match_obj = re.search(k, answer)
    beg, end = match_obj.span()

    # isolate the the student's info
    # missing case when end in .* (not needed right now thought)

    # personal info that we are trying to extract is surrounded by .*
    if beg <= len(answer) and answer[beg - 2:beg] == ".*" and end + 2 <= len(answer) and answer[end: end + 2]:
        left = re.sub(iso_re + answer[end:], "", cur_line)
        right = re.sub(answer[:beg] + iso_re, "", cur_line)
        result = re.sub(left, "", re.sub(right, "", cur_line))
    else:
        # accounting for the case when the personal info is at the beg or end of the string
        result = cur_line
        if answer[:beg]: result = re.sub(answer[:beg], "", result)
        if answer[end:]: result = re.sub(answer[end:], "", result)

    return result

# maps personal info keys to their respective regex patterns
stored_answers = dict()
f = open('/home/bgg646/feedback/stored_answers.txt', 'r')
import re
for line in f.readlines():
    key, regex_value = re.split("~~~", line)
    stored_answers[key] = (False, regex_value)

def use_stored_answer(answer, cur_line):
    keys = re.findall("<r>.*?</r>", answer)
    for k in keys:
        # get rid of the tags
        key = re.sub("<r>", "", k)
        key = re.sub("</r>", "", key)
        # unpack: boolean and stored_answer
        (stored, stored_answer) = stored_answers[key]
        if(not stored):
            stored_answer = extract(answer, cur_line, k, key)
            stored_answers[key] = True, stored_answer
        answer = re.sub(k, stored_answer, answer)
    return answer

def cleared(expected, output):
    cur_line = get_line(output)
    # TODO: ensure they are outputting a valid output
    expected = use_stored_answer(expected, cur_line)
    if(match(expected, cur_line)):                
        output = output[len(cur_line):]
        return output
    else:
        if(expected == "\n"):
            expected = "a blank line"
        if(cur_line == "\n"):
            cur_line = "a blank line"
        # TODO make regex expression human readable.
            # consider using an array to store what the regex is supposed to represent
        print("\n\nYour output preceding this line is correct.\n")
        print("But now you must fix this issue:")
        print("\"" + expected.rstrip("\n") + "\" must be printed.")
        print("\"" + cur_line.rstrip("\n") + "\" is what you're printing\n\n")
        return False

# global variables
# TODO: fill in correct usr
usr = "bgg646"
correct_pwd = "/home/" + usr + "/lab0-part2"
script_path = correct_pwd + "/Your_script/your_script.py"
import subprocess
p = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
o, e = p.communicate() 
output, error = bytes_to_string(o, e)