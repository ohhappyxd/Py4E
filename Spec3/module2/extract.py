import re

handle = open('regex_sum_2149766.txt')
allNumsStr = list()
allNum = list()
for line in handle:
    line.rstrip()
    nums = re.findall('[0-9]+', line)
    allNumsStr += nums

for number in allNumsStr:
    allNum.append(int(number))

print(sum(allNum))
