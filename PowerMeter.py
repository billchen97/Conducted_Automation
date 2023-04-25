import pyvisa

class PowerMeter:

    def __init__(self):
        self.rm = pyvisa.ResourceManager()

        return
    def setAverageOnly(self):
        pass
    def setBoth(self):
        pass

class AnritsuMeter(PowerMeter):
    def __init__(self):
        self.rm = pyvisa.ResourceManager('/Users/spiritairline/Desktop/Conducted_Automation/venv/lib/python3.10/site-packages/pyvisa/__init__.py ')
        self.instr = self.rm.get_instrument('TCPIP::192.168.0.1::INST')

    def setAverageOnly(self):
        self.instr.write('CONF:POW:AVER')
        self.instr.write('TRIG:SOUR IMM')
        self.instr.write('SAMP:COUN 10')
        self.instr.write('INIT:IMM')
        avg_power = float(self.instr.query('FETCH?'))
        print(f'Average Power: {avg_power} dBm')
