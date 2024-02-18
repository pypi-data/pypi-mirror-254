#      ******************************************************************
#      *                                                                *
#      *                       DPiPowerDrive Libary                     *
#      *                                                                *
#      *            Stan Reifel                     8/20/2022           *
#      *                                                                *
#      ******************************************************************

from dpeaDPi.DPiNetwork import DPiNetwork
dpiNetwork = DPiNetwork()


#
# DPiNetwork DPiPowerDrive commands  
#
_CMD_DPi_POWERDRIVE__PING                  = 0x00
_CMD_DPi_POWERDRIVE__INITIALIZE            = 0x01
_CMD_DPi_POWERDRIVE__TURN_ALL_DRIVERS_OFF  = 0x02
_CMD_DPi_POWERDRIVE__SET_PWM_FREQUENCY     = 0x03
_CMD_DPi_POWERDRIVE__SET_DRIVER_PWM        = 0x10
_CMD_DPi_POWERDRIVE__TURN_DRIVER_OFF       = 0x20
_CMD_DPi_POWERDRIVE__TURN_DRIVER_ON        = 0x30
_CMD_DPi_POWERDRIVE__PULSE_DRIVER_OFF      = 0x40
_CMD_DPi_POWERDRIVE__PULSE_DRIVER_ON       = 0x50

#
# other constants used by this class
#
_NUMBER_OF_DPi_POWERDRIVE_DRIVERS = 4
_DEFAULT_DPi_POWERDRIVE_PWM_FREQUENCY = 500
_DPiNETWORK_TIMEOUT_PERIOD_MS = 8            #3/9/2023 changed from 6 to 8ms
_DPiNETWORK_BASE_ADDRESS = 0x1C


class DPiPowerDrive:
    #
    # constructor for the DPiPowerDrive class
    #
    def __init__(self):
        #
        # attribute variables local to one instance of this class
        #
        self._slaveAddress = _DPiNETWORK_BASE_ADDRESS
        self._commErrorCount = 0
       

    # ---------------------------------------------------------------------------------
    #                                 Private functions 
    # ---------------------------------------------------------------------------------

    #
    # send a command to the DPiPowerDrive, command's additional data must have already been "Pushed". 
    # After this function returns data from the device is retrieved by "Popping"
    #    Enter:  command = command byte
    #    Exit:   True returned on success, else False
    #
    def __sendCommand(self, command: int):
        (results, failedCount) = dpiNetwork.sendCommand(self._slaveAddress, command, _DPiNETWORK_TIMEOUT_PERIOD_MS)
        self._commErrorCount += failedCount;
        return results

 
    # ---------------------------------------------------------------------------------
    #                                Public functions 
    # ---------------------------------------------------------------------------------

    #
    # set the DPiPowerDrive board number
    #    Enter:  boardNumber = DPiPowerDrive board number (0 - 3)
    #
    def setBoardNumber(self, boardNumber: int):
        if (boardNumber < 0) or (boardNumber > 3):
            boardNumber = 0
        self._slaveAddress = _DPiNETWORK_BASE_ADDRESS + boardNumber


    #
    # ping the board
    #    Exit:   True returned on success, else False
    #
    def ping(self):
        return self.__sendCommand(_CMD_DPi_POWERDRIVE__PING)


    #
    # initialize the board to its "power on" configuration
    #    Exit:   True returned on success, else False
    #
    def initialize(self):
        return self.__sendCommand(_CMD_DPi_POWERDRIVE__INITIALIZE)


    #
    # switch a driver on or off
    #    Enter:  driver number = driver number (0 - 3)
    #            onOffValue = True to turn on, False to turn off
    #    Exit:   True returned on success, else False
    #
    def switchDriverOnOrOff(self, driverNumber: int, onOffValue: bool):      
        if (driverNumber < 0) or (driverNumber >= _NUMBER_OF_DPi_POWERDRIVE_DRIVERS):
            return False

        if onOffValue:
            command = _CMD_DPi_POWERDRIVE__TURN_DRIVER_ON + driverNumber
        else:
            command = _CMD_DPi_POWERDRIVE__TURN_DRIVER_OFF + driverNumber

        return self.__sendCommand(command)


    #
    # pulse a driver On for the given period of time
    #    Enter:  driver number = driver number (0 - 3)
    #            pulseDurationMS = pulse length in milliseconds (1 to 65000)
    #    Exit:   True returned on success, else False
    #
    def pulseDriverOn(self, driverNumber: int, pulseDurationMS: int):
        if (driverNumber < 0) or (driverNumber >= _NUMBER_OF_DPi_POWERDRIVE_DRIVERS):
            return False

        if (pulseDurationMS < 1) or (pulseDurationMS > 65000):
            return False

        dpiNetwork.pushUint16(pulseDurationMS)
        return self.__sendCommand(_CMD_DPi_POWERDRIVE__PULSE_DRIVER_ON + driverNumber)


    #
    # pulse a driver Off for the given period of time
    #    Enter:  driver number = driver number (0 - 3)
    #            pulseDurationMS = pulse length in milliseconds (1 to 65000)
    #    Exit:   True returned on success, else False
    #
    def pulseDriverOff(self, driverNumber: int, pulseDurationMS: int):
        if (driverNumber < 0) or (driverNumber >= _NUMBER_OF_DPi_POWERDRIVE_DRIVERS):
            return False

        if (pulseDurationMS < 1) or (pulseDurationMS > 65000):
            return False

        dpiNetwork.pushUint16(pulseDurationMS)
        return self.__sendCommand(_CMD_DPi_POWERDRIVE__PULSE_DRIVER_OFF + driverNumber)


    #
    # switch all drivers off
    #    Exit:   True returned on success, else False
    #
    def switchAllDriversOff(self):
        return self.__sendCommand(_CMD_DPi_POWERDRIVE__TURN_ALL_DRIVERS_OFF)


    #
    # get the count of communication errors
    #    Exit:   0 return if no errors, else count of errors returned
    #
    def getCommErrorCount(self):
        return self._commErrorCount


    #
    # set a driver's PWM value
    #    Enter:  driver number = driver number (0 - 3)
    #            pwmValue = 0 for off, 255 max on
    #    Exit:   True returned on success, else False
    #
    def setDriverPWM(self, driverNumber: int, pwmValue: int):
        if (driverNumber < 0) or (driverNumber >= _NUMBER_OF_DPi_POWERDRIVE_DRIVERS):
            return False

        if (pwmValue < 0) or (pwmValue > 255):
            return False

        dpiNetwork.pushUint8(pwmValue)
        return self.__sendCommand(_CMD_DPi_POWERDRIVE__SET_DRIVER_PWM + driverNumber)


    #
    # set the frequency use for PWM
    #    Enter:  pwmFrequency = PWM cycles/second (100 to 100000)
    #    Exit:   True returned on success, else False
    #
    def setPWMFrequency(self, pwmFrequency: int):
        if (pwmFrequency < 100) or (pwmFrequency > 100000):
            return False

        dpiNetwork.pushUint32(pwmFrequency)
        return self.__sendCommand(_CMD_DPi_POWERDRIVE__SET_PWM_FREQUENCY)
