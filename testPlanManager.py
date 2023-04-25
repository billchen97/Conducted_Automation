import csv
from const_value import  DICT_RU_LENGTH
from testChannel import *
from pathlib import Path
class TestPlanManager:
    col_avg_res = 0
    col_pek_res = 0
    col_pwr_res = 0
    col_ap = 0
    col_target_power = 0
    col_duty_cycle = 0
    col_max_power = 0
    test_plan = []
    plan_file_path = ""
    col_time = 0
    def __init__(self):
        return
    def readTestPlan(self,path):
        pass

    def writeCell(self,row=0,column=0,value="Not Define"):
        in_file = open(self.plan_file_path, "rb")
        reader = csv.reader(in_file)
        out_file = open(self.plan_file_path, "wb")
        writer = csv.writer(out_file)
        for i,Row in enumerate(reader):
            if i == row:
                Row[column] = value
                writer.writerow(row)
                return
    def writeRes(self,channel:Channel,dict_res):
        for k,v in dict_res:
            if 'avg' in k:
                self.writeCell(row=channel.row,column=self.col_avg_res,value=v)
            elif 'pk' in k:
                self.writeCell(row=channel.row,column=self.col_pek_res,value=v)
            elif 'pwr' in k:
                self.writeCell(row=channel.row, column=self.col_pwr_res, value=v)
            else:
                self.writeCell(row=channel.row, column=self.col_time, value=v)



class WifiTestPlanManager(TestPlanManager):
    def __init__ (self):
        self.col_avg_res,self.col_pek_res,self.col_pwr_res,self.col_time = 11,12,13,14
        self.col_ap, self.col_duty_cycle,self.col_max_power, self.col_target_power = 7, 8, 9,10

    def channel_describtion(self,channel):
        return "Signal# {}:\n Mode: {} bandwidth: {}MHz Chn: {} Rate: {} {}".format(channel.row,
                                                                                    channel.signal_parameter['Mode'],
                                                                                    channel.signal_parameter["Bandwidth"],
                                                                                    channel.signal_parameter["Channel"],
                                                                                    channel.signal_parameter["Rate"],
                                                                                    channel.signal_parameter["Length"])
    def loadTestPlan(self,path):
        self.plan_file_path = path
        col_channel, col_bandwidth, col_ant, col_MCS, col_mode, col_ru_index, col_ru_length = 0, 1, 2, 3, 4, 5, 6
        with open(path, newline='') as csvfile:
            plan_file = csv.reader(csvfile, delimiter=' ', quotechar='|')
            dict_signal = {}
            startReading = False
            for i ,row in enumerate(plan_file):
                if "Start" in row:
                    startReading = True
                if "Stop" in row:
                    return
                if not startReading:
                    continue
                dict_signal['Channel'] = row[col_channel]
                dict_signal['Bandwidth'] = row[col_bandwidth]
                dict_signal['Core'] = row[col_ant]
                dict_signal['Rate'] = row[col_MCS]
                dict_signal['Mode'] = row[col_mode]
                dict_signal['Power'] = row[self.col_max_power]
                if 'ru' in row[col_mode].lower():
                    dict_signal['Index'] = str(row[col_ru_index])
                    dict_signal['Length'] = str(DICT_RU_LENGTH[row[col_ru_index]])
                else:
                    dict_signal['Index'] = ""
                    dict_signal['Length'] = ""
                signal = Channel(signal=dict_signal, n_row=i, ap=row[self.col_ap], target=row[self.col_target_power])
                signal.note = self.channel_describtion(signal)
                if signal.dict_signal["Length"] != "":
                    signal.note += row[col_ru_index]
                self.test_plan.append(signal)



















