a,b,c,d = map(int,input().split())
total = a+b+c+d
percent = float((total/400)*100)
print(total)
print(f"{percent:.2f}")
if percent > 75:
	print("Distinction")
elif percent >= 60 and percent < 75:
	print("First Division")
elif percent >=50 and percent < 60:
	print("Second Division")
elif percent >= 40 and percent< 60:
	print("Third Division")
else:
	print("Fail")
