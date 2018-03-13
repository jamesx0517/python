#--coding utf-8--
print "Let's practice everything"

print 'You\'d need to know \' bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love 
nor comprehend passion from intuition 
and requires an explanation
\n\t\twhere there is none.
"""
#可愛的世界
#邏輯如此牢固
#無法辨別
#  愛的需要
#也不從直覺領悟激情
#並需要解釋

#沒有的地方。
print"------------"
print poem
print"------------"

five=10 - 2 + 3 - 6

print "This should be five: %s" % five

def secret_formula(started):
	beans = started * 500
	jars = beans / 1000
	crates = jars / 100
	return beans,jars,crates
	
start_point = 10000

beans , jars , crates = secret_formula(start_point)


print "With a starting point of: %d" % start_point

print "We'd have %d beans , %d jars and %d crates . " % (beans , jars , crates)

start_point= start_point/10

print"We can also do that this way:"

print "We'd have %d beans , %d jars and %d crates . " %secret_formula(start_point)