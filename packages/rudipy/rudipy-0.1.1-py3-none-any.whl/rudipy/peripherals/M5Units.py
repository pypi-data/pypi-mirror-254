import logging

class M5Unit():
    def __init__(self,host):
        pass


class TOF(M5Unit):
    def __init__(self,host):
        self.name="TOF"
        self.host=host

    def get_distance(self):
        self.host.send_serial(">Color.GetValue(red)")
        return(self.host.receive_float_response())


class Voltmeter(M5Unit):
    def __init__(self,host):
        self.name="VOLT"
        self.host=host

    def get_voltage(self):
        self.host.send_serial(">VOLT")
        return(self.host.receive_int_response())
