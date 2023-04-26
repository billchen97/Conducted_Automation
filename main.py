# This is a sample Python script.
import PowerMeter
import const_value
from anritsu_pwrmtr import CommChannel
from Autotest import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    power_meter =AnritsuMeter(13)
    #power_meter.setBoth()
    print(power_meter.read())
    """
    with CommChannel(13) as pm:
        n = pm.ch1.read(settle = True)
        print(n)
    """
    chamber = const_value.DICT_CHAMBER[int(input("Hello, Please choose chamber:\n1:CS1\n2:CS2\n3:CS3\n4:CS4\n5:CS5\n"))]
    test_type = const_value.DICT_TYPE[int(input("Hello, Please choose chamber:\n1:WIFI\n2:BT\n3:LTE\n4:FR1\n5:FR2\n"))]
    comport = input("Please Enter Comport:")
    test_plan_path = input("Please Enter Test Plan Path:")
    Autotest(test_type,test_plan_path,chamber,comport)









# See PyCharm help at https://www.jetbrains.com/help/pycharm/
