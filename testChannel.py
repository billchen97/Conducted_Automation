from copy  import  deepcopy
class Channel:
    signal_parameter = None
    row = 0
    average_peak = "Both"
    target_power = 12
    pass_pwr = 0
    note = ""
    def __init__(self,signal,n_row,ap,target):
        self.signal_parameter = signal
        self.row = n_row
        self.average_peak = ap
        self.target_power = target
        self.max_pwr = deepcopy(signal["Power"])
    def test_string(self):
        str = ""
        for k,v in self.signal_parameter:
            str = "Signal# {}"

