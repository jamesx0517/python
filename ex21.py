#--coding utf-8--
def  add(a,b):
    print "ADDING %d + %d" %( a, b)
    return a + b
	
	
def subtract(a , b):
	print"SUBTRACT %d - %d" % (a,b)
	return a-b

def multiply(a , b):
	print "MULTIPLY %d * %d" %(a,b)
	return a*b

def divide(a , b):
	print "DIVIDE %d / %d " % (a,b)
	return a/b
	
print "Let's do some math with just functions!"

age=add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq= divide(100,2)

print "Age: %d , height: %d , Weight: %d , IQ: %d" %(age , height , weight , iq)

print"Here is puzzle."

what = add(age, subtract(height,multiply(weight,divide(iq,2))))

print "That becomes", what, "Can you do it hand?"
#iq=50->divide->25
#weight=180 *25 =4500
#height=74 -4500=-4426