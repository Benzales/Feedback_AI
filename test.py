import subprocess
import re

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

val = None
if(val):
    print("hello")

match_o1 = re.findall("[0-2]", "g6h3kdsfj3kdfj6")
print(type(match_o1))
print(match_o1)
print(match_o1 == None)

print("19\n")





# begins or ends with .*
    # 
re1 = "a 99 b"
print(re1)
re1 = re.sub("a.*", "", re1)
print(re1)
re1 = re.sub(".*b", "", re1)
print(re1)

ans_ex_1 = "longhorn_rule.*<r>name</r>.*<r>age</r>.*3\.14.*(True|False).*<class 'str'>"
mo_ex_1 = re.search(ans_ex_1, "longhorn_rule: Benjamin Gonzales 19 3.14 True <class 'str'>")
print(mo_ex_1)