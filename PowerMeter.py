import copy

import pyvisa
import  anritsu_pwrmtr
class PowerMeter:

    def __init__(self,ip):
        return

    def setAverageOnly(self):
        pass
    def setBoth(self):
        pass

class AnritsuMeter(PowerMeter):
    pm = None
    def __init__(self,ip):
        self.rm = pyvisa.ResourceManager()
        self.visa = self.rm.open_resource(f"GPIB::{ip}")
        self.visa.write("*CLS")
        #self.pm = anritsu_pwrmtr.PWRMTR["ML2437A"](self.visa)
        return


    def setBoth(self):
        self.visa.write('PMMEAS 1,2')

    def setReadAvg(self):
        self.visa.write('PMMEAS 1,1')

    def setChannel(self,value):
        self.visa.write(f'CHACTIV {value}')

    def setChannelInput(self,channel,input):
        self.visa.write(f'CHCFG {channel} ,{input}')

    def setAveraging(self,channel,n):
        self.visa.write(f'CWAVG {channel}, RPT ,{n}')

    def queryValue(self):
        mn, mx = self.visa.query(f"GMNMX {1}")
        return (float(mn), float(mx))

    def read(self, samples=1, timeout=10, settle=False):
        #res = self.pm.ch1.read(samples, timeout, settle)
        original_timeout = self.visa.timeout
        self.visa.timeout = 1000 * timeout
        self.visa.write(f"PMRDO {1}")
        """
        if not settle:
            self.visa.write(f"ON {1},{samples}")
        else:
            self._visa.write(f"TR2 {self._ch}")
        """
        values = self.visa.read_ascii_values(converter='s')
        self.visa.timeout = original_timeout
        if len(values) == 1:
            return values[0]
        return values
        return res
