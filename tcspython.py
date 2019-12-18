for i in range(2,16):
	k=0
	for j in range(2,i):
		if i%j==0:
			k=1
			break
	if k==1:
		print(i,"not prime")
	else:
		print(i,"prime")
