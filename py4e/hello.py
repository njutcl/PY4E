import re
fh = open(r'D:\LTC\学习\网课资料\data science\py4e\aaa.txt')
sum = 0
for line in fh:
    line = line.strip()
    a = re.findall('[0-9]+',line)
    for j in a :
        j = int(j)
        sum+=j
print(sum)
