#--coding utf-8--
from sys import argv

script,input_file =argv

def print_all(f):
	print f.read()

def rewind(f):
	print f.seek(0)
	#seek移動讀取指針到指定位置

def print_a_line(line_count,f):
	print line_count,f.readline()

current_file = open(input_file)
#打開檔案

print "First let's print the whole file:\n"

print_all(current_file)
#讀取檔案
print "Now let's rewind , kind of like a tape."

rewind(current_file)
#檔案從第0個位置開始讀取
print "Let's print three lines:"

current_line = 1
#設定行數變數為1
print_a_line (current_line , current_file)
#行數1 讀取第一行
current_line=current_line+1

print_a_line (current_line,current_file)

current_line=current_line+1

print_a_line (current_line,current_file)
print_a_line (current_line,current_file)