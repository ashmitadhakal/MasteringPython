

import re

# content = "<b>content 1</b><span>test</span><b>content 2</b><div>fun</div>"

# # r= re.compile(r"<b>(.*?)</b>")
# r=re.compile(r"<b>(?P<data>.*?)</b>")

# # for match in r.finditer(content):
# #     print(match.groups())


# content = "cool 45 test"
# r=re.compile(r"(?P<str1>.*?) (?P<num>.*?) (?P<str2>.*?)")
# for match in r.finditer(content): 
#     print(match.groupdict())


# content = "cool 45 test"
# r=re.compile(r"(?P<str1>.*?)\s(?P<num>.*?)\s(?P<str2>.*?)")

# for match in r.finditer(content):
#     print(match.groupdict())

#mini lab
#write a regular expression and code extracts the command name and operatnd
#eg command: add 2
#eg command: multiply 3



#after the extraction, create a dictionary like this:
#eg 1 output: {"op_name":"add","op_value":2.0}
#eg 2 output: "op_name":"multiply","op_value":3.0}

def console_str_input(prompt):
    return input(prompt)

def get_command():
    command = console_str_input("Enter a command: ")
    
    r = re.compile(r"(?P<op_name>[a-z]+)\s+(?P<op_value>\d+)")
    #r=re.compile(r"(?P<str1>.*?)\s(?P<num>.*?)\s(?P<str2>.*?)")
    for match in r.finditer(command):
        command_dict = match.groupdict()
        command = {"op_name":command_dict["op_name"], 
                   "op_value":float(command_dict["op_value"])
                   }
    print(command)
    
while True:
    get_command()
