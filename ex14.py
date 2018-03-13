#--coding utf-8--
from sys import argv

script , user_name = argv

prompt= ' > '

print "Hi %s, I'm the %s script ." % (user_name  ,  script)

print "I'd like to ask you a few question."

print "Do you like me %s? " % user_name 

like= raw_input(prompt)

print "Where do you live %s? " % user_name 

lives = raw_input(prompt)

print "What kind of computer do you have ? "

computer= raw_input(prompt)

print """

Alright , so you said %s about liking me.

You live in %r . Not sure where that is .

And you have a %r computer. Nice
""" %(like , lives , computer) 

#prompt 讓問句 帶入 ">" 符號