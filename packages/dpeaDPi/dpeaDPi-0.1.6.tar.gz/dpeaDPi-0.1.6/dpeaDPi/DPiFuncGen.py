#      ******************************************************************
#      *                                                                *
#      *                        DPiFuncGen Libary                       *
#      *                                                                *
#      *            Stan Reifel                     8/21/2022           *
#      *                                                                *
#      ******************************************************************

from dpeaDPi.DPiNetwork import DPiNetwork
dpiNetwork = DPiNetwork()


#
# DPiNetwork DPiFuncGen commands  
#
_CMD_DPi_FUNCGEN__PING                  = 0x00
_CMD_DPi_FUNCGEN__INITIALIZE            = 0x01
_CMD_DPi_FUNCGEN__SET_FREQENCY_AND_WAVE = 0x02
_CMD_DPi_FUNCGEN__SET_VOLUME            = 0x03
_CMD_DPi_FUNCGEN__MUTE                  = 0x04


#
# other constants used by this class
#
_DPiNETWORK_TIMEOUT_PERIOD_MS = 8      # 3/10/2023 changed from 5 to 8ms
_DPiNETWORK_BASE_ADDRESS = 0x18



class DPiFuncGen:
    #
    # audio wave shapes
    #
    SINE_WAVE       = 0
    TRIANGLE_WAVE   = 1
    SQUARE_WAVE     = 2


    #
    # constructor for the DPiFuncGen class
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
    # send a command to the DPiFuncGen, command's additional data must have already been "Pushed". 
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
    # set the DPiFuncGen board number
    #    Enter:  boardNumber = DPiFuncGen board number (0 - 3)
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
        return self.__sendCommand(_CMD_DPi_FUNCGEN__PING)


    #
    # initialize the board to its "power on" configuration
    #    Exit:   True returned on success, else False
    #
    def initialize(self):
        return self.__sendCommand(_CMD_DPi_FUNCGEN__INITIALIZE)


    #
    # set the function generator's frequency and waveshape 
    #    Enter:  frequency = cycles per second (10Hz - 25000Hz)
    #            waveShape = AD9833_SINE_WAVE, AD9833_TRIANGLE_WAVE or AD9833_SQUARE_WAVE
    #    Exit:   True returned on success, else False
    #
    def setFrequency(self, frequency: int, waveShape: int):
        if (frequency < 10) or (frequency > 25000):
            return False

        if not ((waveShape == self.SINE_WAVE) or (waveShape == self.TRIANGLE_WAVE) or (waveShape == self.SQUARE_WAVE)):
            return False

        dpiNetwork.pushUint16(frequency)
        dpiNetwork.pushUint8(waveShape)
        return self.__sendCommand(_CMD_DPi_FUNCGEN__SET_FREQENCY_AND_WAVE)


    #
    # set the function generator's volume
    #    Enter:  volume = volume (0 - 63)
    #    Exit:   True returned on success, else False
    #
    def setVolume(self, volume: int):
        if (volume < 0) or (volume > 63):
            return False

        dpiNetwork.pushUint8(volume)
        return self.__sendCommand(_CMD_DPi_FUNCGEN__SET_VOLUME)


    #
    # mute/un-mute the function generator
    #    Enter:  muteFlg = True to mute, False to un-mute
    #    Exit:   True returned on success, else False
    #
    def mute(self, muteFlg: bool):
        dpiNetwork.pushUint8(muteFlg)
        return self.__sendCommand(_CMD_DPi_FUNCGEN__MUTE)
 

    #
    # get the count of communication errors
    #    Exit:   0 return if no errors, else count of errors returned
    #
    def getCommErrorCount(self):
        return self._commErrorCount
