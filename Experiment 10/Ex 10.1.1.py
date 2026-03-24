st = input()
s=""


for i in st:
	if i.isalnum() or i.isspace():
		s = s +i
print(s)
