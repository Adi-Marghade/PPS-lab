n = int(input())
ph = {}

for i in range(n):
	cm = input().split()   # FIXED

	if cm[0] == "ADD":
		ph[cm[1]] = cm[2]

	elif cm[0] == "REMOVE":   # FIXED
		ph.pop(cm[1], None)

	elif cm[0] == "DISPLAY":
		if len(ph) == 0:
			print("No contacts")
		else:
			for name in sorted(ph):
				print(f"{name}: {ph[name]}")
