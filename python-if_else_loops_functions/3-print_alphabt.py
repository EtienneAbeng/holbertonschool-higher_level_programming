#usr/bin/python3

#Use the number ascii (97 = a & 123 = z)
for ascii in range(97, 123):
    #Use a loop to increment and if the number is 101 and 113 don't print
    if(ascii != 101 and ascii != 113):
        print("{:c}".format(ascii), end=""))
