def check_output():
    # maps personal info keys to their respective regex patterns
    stored_answers = dict()
    f = open('/home/bgg646/feedback/stored_answers.txt', 'r')
    import re
    for line in f.readlines():
        key, regex_value = re.split("~~~", line)
        stored_answers[key] = (False, regex_value)

    # Check their output
    # TODO unhardcode feedback paths
    f = open("/home/bgg646/feedback/answers.txt", 'r')
    import helper_functions as hf
    for line in f.readlines():
        if not output:
            return
        expected = line
        output = hf.cleared(expected, output)
    f.close()