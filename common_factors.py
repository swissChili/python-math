import sys
import math 
import gcf
first_num = int(sys.argv[1])
second_num = int(sys.argv[2])

gcf = gcf.get_gcf(first_num, second_num)

print("Greatest Common Factor: %d" % gcf)
print(first_num / gcf )
print("-----")
print(second_num / gcf)
