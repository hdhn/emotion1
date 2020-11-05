#open file
name = 'regex_sum_834794.txt'
fh = open(name)
import re
numberlist = list()
#read line
for line in fh:
	line = line.rstrip()
	number = re.findall('([0-9]+)',line)
#minus blank line
	if len(number) < 1:
		continue
#add number into the empty list
	numberlist.append(number)
	print(numberlist)

sum = 0
for num in numberlist:
	sum += int(num[0])
print(sum)



