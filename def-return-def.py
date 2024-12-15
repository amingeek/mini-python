def a(n):
	if 2<n:
		return a(n-1) + 5*a(n-2)
		
	elif n == 2:
		return 4
	elif n==1:
		return 1
		
for k in range(1,11):
	print(a(k))
