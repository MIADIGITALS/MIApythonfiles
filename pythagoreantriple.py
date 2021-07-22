def pytriple(side1,side2,hypotenuse):
    return side1,side2,hypotenuse
m=int(input('m = '))
n=int(input('n = '))
side1=int((m**2)-(n**2))
side2=int(2*(m*n))
hypotenuse=int((m**2)+(n**2))
print('side1 = {} ' .format(side1))
#print(side1) 
print('side2 = {} ' .format(side2))
#print(side2)
print('hypotenuse = {}' .format(hypotenuse))
#print(hypotenuse)
