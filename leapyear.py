xyz=int(input())
if (xyz%4==0 and xyz%100!=0) or (xyz%400==0 and xyz%100==0):
	print("yes")
else:
	print("no")
