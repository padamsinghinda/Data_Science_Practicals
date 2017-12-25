first = input("Enter first name : ")
last = input("Enter last name : ")
name = first + ' ' + last

#print("Name : %s " % name)

rev_name = []
for i in range(0,len(name)):
    rev_name.append(name[len(name)-1-i])
	
reverse_name = ''.join(rev_name)

print("Name in reversed order separated with space : %s " %reverse_name)