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
        list.append(b.decode('UTF-8').rstrip('\n'))
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
    if(expected == "\n"):
        p_expected = "a blank line"
    if(cur_line == "\n"):
        p_cur_line = "a blank line"
    else:
        p_expected = "\"" + expected.strip() + "\""
        p_cur_line = "\"" + cur_line.strip()     + "\""

    if(match(expected, cur_line)):                
        output = output[len(cur_line):]
        print("cleared. You successfully outputted", p_expected)
        return output
    else:
        # TODO make regex expression human readable.
            # consider using an array to store what the regex is supposed to represent
        print("\n\n" + p_expected + " must be printed.")
        print(p_cur_line + " is what you're printing\n\n")
        return False