# -- coding: utf-8 --
X="There are %d types of people" % 10
#%d�a�J���Y���Ʀr10
binary ="binary"
do_not ="don't"
Y="Those who know %s and those who %s ." % (binary,do_not)
                                        #�n���J�h���ܼ� �ݭn�� () �]�_�� �A�ϥ� , �j�} 
#%s �a�J �ܼ� binary   do_not
print X
#����ܼ�X
print Y
#����ܼ�Y
print "I said : %r " %X

print "I also said %s" %Y

hilarious = False

joke_evaluation = "Isn't that joke so funny !? %r"

print joke_evaluation  % hilarious

w = "This is the left side of..."

e = "a string with a right side."

print w + e
#�r�굲�X �ϥ� + ��
