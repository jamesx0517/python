# -- coding: utf-8 --
cars = 100
space_in_a_car = 4.0
#�@�x���i���h�H��
drivers = 30
#�q��
passengers = 90
#����
cars_not_driven= cars - drivers
#������}
car_driven = drivers
carpool_capacity=car_driven * space_in_a_car
#�@���H��
average_passengers_per_car = passengers / car_driven
#�C�������������ȼ�
print "There are " , cars ,"cars available "
#�o�̦�X���T���i��
print "There are only ", drivers , "drivers available"
print "The will be" , cars_not_driven ,"empty cars today"
#���ѱN�|��X���Ũ�
print "We can transport", carpool_capacity, "people today"
#�ڭ̤��ѥi�H�B�eX�H
print "We have", passengers ,"to carpool today"
#carpool �@��
print "We need to put about " , average_passengers_per_car ,"in each car "
#�ڭ̻ݭn�⡧�C�������������ȼơ���b�C������
