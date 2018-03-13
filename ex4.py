# -- coding: utf-8 --
cars = 100
space_in_a_car = 4.0
#ó更ぶ
drivers = 30
#诀
passengers = 90
#
cars_not_driven= cars - drivers
#óぃ秨
car_driven = drivers
carpool_capacity=car_driven * space_in_a_car
#计
average_passengers_per_car = passengers / car_driven
#–进óキА计
print "There are " , cars ,"cars available "
#硂柑ΤX进═óノ
print "There are only ", drivers , "drivers available"
print "The will be" , cars_not_driven ,"empty cars today"
#さぱ盢穦ΤX进ó
print "We can transport", carpool_capacity, "people today"
#иさぱ笲癳X
print "We have", passengers ,"to carpool today"
#carpool 
print "We need to put about " , average_passengers_per_car ,"in each car "
#и惠璶р¨–进óキА计〃–进ó柑
