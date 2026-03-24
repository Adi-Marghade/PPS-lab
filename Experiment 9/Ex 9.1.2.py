s = input()
l = len(s)
flag = True
for i in range(l):
	if s[i] != s[l-1-i]:
		flag = False

if flag:
	print("Palindrome")
else:
	print("Not a Palindrome")
