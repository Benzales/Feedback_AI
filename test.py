import subprocess
def tup(*args):
    print(args)
    list = [] 
    for b in args:
        print(type(b))
        list.append(b.decode('UTF-8').rstrip('\n'))
    return tuple(list)

script_path = "/home/bgg646/feedback/output_test_script.py"
p = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(p.returncode)

print("\nasd;lkfjdskf j"[1:])
str = "\n"
print(str[0:1] == "\n")