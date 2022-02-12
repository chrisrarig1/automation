import re
import shutil

file = "assets/potential-contacts.txt"
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)? # separator
    (\d{3}) # first 3 digits
    (\s|-|\.) # separator
    (\d{4}) # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
    )''', re.VERBOSE)
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+       # Username
@                       # @Symbol
[a-zA-Z0-9.-]+          # Domain Name
(\.[a-zA-Z]{2,})       # dot-something
)''', re.VERBOSE)

cell_list=[]
email_list=[]
with open(file) as f:
	for line in f:
		text=line
		for i in phoneRegex.findall(text):
			cell_list.append(i[0])
        
with open(file) as f:
	for line in f:
		text=line
		for i in emailRegex.findall(text):
			email_list.append(i[0])

print(email_list)