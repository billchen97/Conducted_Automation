# This is a sample Python script.
import PowerMeter
import const_value
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.




import Autotest

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    PM = PowerMeter.AnritsuMeter()
    PM.setAverageOnly()
    chamber = const_value.DICT_CHAMBER[int(input("Hello, Please choose chamber:\n1:CS1\n2:CS2\n3:CS3\n4:CS4\n5:CS5\n"))]
    test_type = const_value.DICT_TYPE[int(input("Hello, Please choose chamber:\n1:WIFI\n2:BT\n3:LTE\n4:FR1\n5:FR2\n"))]
    comport = input("Please Enter Comport:")
    test_plan_path = input("Please Enter Test Plan Path:")
    Autotest(test_type,test_plan_path,chamber,comport)









# See PyCharm help at https://www.jetbrains.com/help/pycharm/
