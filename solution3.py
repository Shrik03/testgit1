#The corrected code is

#testcase1: if all numbers are equal mymax(4, 4, 4)
#testcase2: if two numbers equal and max is the third(2,2,4)

#testcase3: if two numbers equal and max (4,4,2)

#testcase4: if max is negative(-10,-20,-5)

#testcase5: if max is found from mix of negative and positive (-3,10,-10)

def mymax(x,y,z):
  max = x
  if y > max:
    max = y
  if z > max:
    max = z
  return max
print(mymax(4,4,4))
print(mymax(2,2,4))
print(mymax(4,4,2))
print(mymax(-10,-20,-5))
print(mymax(-3,10,-10))

