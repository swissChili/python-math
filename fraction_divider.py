import gcf
import sys

num1 = int(sys.argv[1])
den1 = int(sys.argv[2])
num2 = int(sys.argv[3])
den2 = int(sys.argv[4])

newnum = num1 * den2
newden = den1 * num2

gcf = gcf.get_gcf(newnum, newden)


print("Work:")
print(newnum  )
print("-----")
print(newden )


print("Greatest Common Factor: %d" % gcf)
print(newnum / gcf )
print("-----")
print(newden / gcf)
