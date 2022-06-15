def check_output():
    # TODO unhardcode feedback paths
    f = open("/home/bgg646/feedback/answers.txt", 'r')
    import help
    for line in f.readlines():
        if not help.output:
            if len(help.output) == 0:
                print("Your current output is acceptable, however you haven't outputted everything yet.")
            return
        help.output = help.cleared(line, help.output)
    f.close()
    print("Output is acceptable.")