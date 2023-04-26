from testPlanManager import *
from time import sleep
from  PowerMeter import  *
class Autotest:
    power_meter = None
    chamber = None
    def __init__(self,test_type,path,chamber):
        if test_type == "WIFI":
            self.test_plan_manager = WifiTestPlanManager()
            self.test_plan_manager.loadTestPlan(path)
            self.test_plan = self.test_plan_manager.test_plan
            self.chamber = chamber

        # to be continue for other test


    def start_test(self):
        for channel in self.test_plan:
            dict_rest = self.test_channel(channel)
            self.test_plan_manager.writeRes(channel,dict_rest)
        return
    def test_channel(self,signal:Channel):
        res_pass = False
        while not res_pass:
            print("Testing: {}".format(signal.note))

            sleep(1)
        return

    def check_pass(self):
        return
    def connect_power_meter(self):
        return
    def connect_dut_controller(self):
        return
    def send_signal_and_wait(self):
        return
    def read_power_result(self,ap):
        return
