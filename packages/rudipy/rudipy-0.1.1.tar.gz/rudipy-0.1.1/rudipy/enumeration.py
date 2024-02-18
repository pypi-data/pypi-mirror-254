import rudipy
import logging
import serial
import serial.tools.list_ports

def find_devices(type=None,name=None):

    devices=[] # start with an empty list of devices

    if ("M5Stack" in type):

        logging.info("Enumerating serial ports...")
        ports = serial.tools.list_ports.comports()
        for p in ports:
            logging.info("Found port:"+str(p))

        logging.info("Ports with the right UART:")
        # check for ports with the right hwid, available through [2] of the SysFS object
        UART_correct= [p for p in ports if 'VID:PID=10C4:EA60' in p[2]]
        for p in UART_correct:
            logging.info(str(p[0]))

        # Note: M5Stack detection is based only on the device having the right UART.
        # This might lead to false positives, but prevents having to probe all serial
        # ports for a response, interfering with possible operation of other devices.

        for p in UART_correct:
            m=rudipy.devices.M5.M5Stack()
            # SysFS-object [0] contains the port name.
            m.portname=p[0]
            devices.append(m)


    if ("BLE" in type):
        pass

    if ("CCD" in type):
        pass

    if ("IOT" in type):
        pass

    return(devices)

