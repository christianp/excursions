# For a given time after midnight, pair it with the same time before midnight.
# Find all pairs which have both elements prime
def digits(n):
	if n=='':
		return None
	digits=[int(x) for x in list(str(n))]
	digits = [0]*(4-len(digits))+digits
	return digits

def to_time(n):
	a,b,c,d=digits(n)
	hour = a*10+b
	minutes = c*10+d
	return hour,minutes

def valid_time(time):
	hour,minutes=time
	return minutes<60 and (hour<12 or (hour==12 and minutes<31))

def prime_time(hour,minutes):
	return (hour*100+minutes) in primes


primes=[int(n) for n in open('primes.txt').read().split('\n') if len(n)>0]

primetimes=[to_time(p) for p in primes if valid_time(to_time(p))]

twoway_primetimes = [[(hour,minutes),(23-hour,60-minutes)] for hour,minutes in primetimes if prime_time(23-hour,60-minutes)]

def display_time(time):
	hour,minutes = time
	return '%s:%s' % (str(hour).zfill(2),str(minutes).zfill(2))

for t1,t2 in twoway_primetimes:
	print('%s -- %s' % (display_time(t1),display_time(t2)))
print('%i pairs of two-way prime times' % len(twoway_primetimes))
