import rudipy
import platform
import logging
import serial
import serial.tools.list_ports


class M5Stack():
    def __init__(self):
        self.sp=None # pyserial port object
        self.portname=None
        self.connected=False

        # since it's not possible to check if non-I2C devices are connected,
        # at the moment the list of attached units is populated with all *supported* units
        self.peripherals = {}

        for obj in rudipy.peripherals.M5Units.M5Unit.__subclasses__():
            peripheral=obj(self)
            self.peripherals[peripheral.name]=peripheral


    def connect(self):
        self.sp=serial.Serial()
        self.sp.port=self.portname
        self.sp.timeout=10
        self.sp.baudrate=115200
        if (platform.system=="Windows"):
            self.sp.rts=0
            self.sp.dtr=0
        try:
            self.sp.open()
        except Exception as err:
            logging.error("Failed to open serial port:"+str(self.portname)+"!")
            logging.warning("Reason: "+str(err))
            self.connected=False
        else:
            logging.info("Succesfully connected to M5Stack on port:"+str(self.portname))
            self.sp.reset_input_buffer()
            self.sp.reset_output_buffer()
            self.connected=True


    def send_serial(self,s):
        if self.connected==True:
            infostring="Sending string: \""+s+"\" to "+self.portname
            logging.info(infostring)
            self.sp.write(s.encode('utf-8'))
        else:
            logging.error("Writing to serial port failed, not connected.")



    def receive_float_response(self):
        logging.info("Waiting for response...")
        r=self.sp.readline().decode('utf-8').replace('\n', '')
        infostring="Received string: \""+r+"\" from "+self.portname
        logging.info(infostring)
        f=None
        try:
            f=float(r)
        except:
            logging.error("Response can't be converted to a float, returning None")
        return(f)




    def __str__(self):
        return("M5Stack-object on port:"+str(self.portname))