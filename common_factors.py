import sys
import math 
first_num = int(sys.argv[1])
second_num = int(sys.argv[2])

if first_num > second_num:
    larger_num = first_num
else:
    larger_num = second_num
factors = []
for i in range(math.floor(larger_num / 2)):
    if i > 0:
        factors.append(i)
    else:
        pass

gcf = 1

for i in factors:
    if (first_num % i == 0) and (second_num % i == 0):
        gcf = i
    else:
        pass

print("Greatest Common Factor: %d" % gcf)
print(first_num / gcf )
print("-----")
print(second_num / gcf)
