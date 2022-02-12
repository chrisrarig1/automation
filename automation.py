import re
import shutil

file = "assets/potential-contacts.txt"
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? 
    (\s|-|\.)? 
    (\d{3}) 
    (\s|-|\.) 
    (\d{4}) 
    (\s*(ext|x|ext.)\s*(\d{2,5}))? 
    )''', re.VERBOSE)
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+       
@                      
[a-zA-Z0-9.-]+         
(\.[a-zA-Z]{2,})       
)''', re.VERBOSE)



cell_list=[]
email_list=[]
final_email=[]
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

for i in email_list:
    if i not in final_email:
        final_email.append(i)

final_cell =[]
for i in cell_list:
    new_cell = i.replace("(","")
    dot_cell = new_cell.replace(".","-")
    dash_cell = dot_cell.replace(")","-")
    newer_cell = dash_cell.split("x",1)
    final_cell.append(newer_cell[0])

res = []
for i in final_cell:
    if i not in res:
        res.append(i)

res.sort()
final_email.sort()
print(final_email)
print(res)

with open("assets/phone_numbers.txt", "w+") as f:
    for i in res:
        f.write(f'{i}\n')

with open("assets/email.txt", "w+") as f:
    for i in final_email:
        f.write(f'{i}\n')