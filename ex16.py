#--coding utf-8--

from sys import argv

script , filename = argv

print "We're going to erase %r " %filename

print "If you don't want that ,hit ctrl+C (^C)"

print "If you do want that , hit RETURN"

raw_input("?")

print "Opening the file..."

traget = open(filename,'w')
#開啟一個文件 只用於寫入

print "Truncating the file Goodbye!!"

traget.truncate()

print "Now I'm going to ask you for three lines"

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file "

traget.write(line1+line2+line3)
#traget.write("\n")
#traget.write(line2)
#traget.write("\n")
#traget.write(line3)
#traget.write("\n")
print "And finally , we close it."
traget.close()