# -- coding: utf-8 --
X="There are %d types of people" % 10
#%d帶入後頭的數字10
binary ="binary"
do_not ="don't"
Y="Those who know %s and those who %s ." % (binary,do_not)
                                        #要插入多個變數 需要用 () 包起來 再使用 , 隔開 
#%s 帶入 變數 binary   do_not
print X
#顯示變數X
print Y
#顯示變數Y
print "I said : %r " %X

print "I also said %s" %Y

hilarious = False

joke_evaluation = "Isn't that joke so funny !? %r"

print joke_evaluation  % hilarious

w = "This is the left side of..."

e = "a string with a right side."

print w + e
#字串結合 使用 + 號
