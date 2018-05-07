# https://fivethirtyeight.com/tag/the-riddler/

for i in range(100000,999999):
	num = str(i)
	# check if number fits criteria
	if num[2] == num[3] and str(4 * i) == num[::-1]:
		print i


