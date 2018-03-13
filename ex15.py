#--coding utf-8--

from sys import argv

script , filename = argv

txt = open(filename)
#使用open函數 打開檔案

print "Here's your file %s:" %filename

print txt.read()


#讀取檔案
print "Type the filename again"

file_again = raw_input(">")
#重新輸入檔案名稱
txt_again = open(file_again)
#打開上頭的檔案名稱 的檔案
print txt_again.read()


#讀取檔案