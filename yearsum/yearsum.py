# Write a year as a sum of powers, where the powers are the year's digits.

def makeyear(year):
	digits = []
	n=year
	while n>0:
		d = int(n%10)
		digits.append(d)
		n=(n-d)/10
	digits.sort()
	digits.reverse()
	print(digits)
	coeffs=[]
	for d in digits:
		for x in range(0,year+1):
			p=x**d
			if p>=year:
				if p>year: 
					x-=1
				break
		year=year-x**d
		coeffs.append((x,d))
	return coeffs

if __name__ == '__main__':
	while 1:
		year=input('Year: ')
		coeffs=makeyear(int(year))
		print(' + '.join([str(x)+'^'+str(d) for x,d in coeffs]) +' = '+ str(sum([x**d for x,d in coeffs])) )
