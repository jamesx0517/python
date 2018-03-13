#--coding utf-8--
def cheese_and_crackers(cheese_count , boxes_of_crackers):
	print "You have %d cheese!" % cheese_count
	print "You have %d boxes of crackers!" %boxes_of_crackers
	print "Man that's enough for a party"
	print "Get a blanket.\n"
	#設定函數工作
print "We can just give the function number directly:"
cheese_and_crackers(20 , 30)
#給變數值

print "Or , we can use variable from our script:"

amount_of_cheese = 10

amount_of_crackers = 50

cheese_and_crackers (amount_of_cheese , amount_of_crackers)
#更換變數名稱
print "We can even do math inside too:"
cheese_and_crackers(10 + 20 , 5 + 6)
#執行數學運算
print "And we can combine the two ,variable and math"
cheese_and_crackers(amount_of_cheese+100 , amount_of_crackers+10000)
#變數的數學運算