#      ******************************************************************
#      *                                                                *
#      *                       DPiDigitalIn Libary                      *
#      *                                                                *
#      *            Stan Reifel                     11/13/2023          *
#      *                                                                *
#      ******************************************************************

from dpeaDPi.DPiNetwork import DPiNetwork
dpiNetwork = DPiNetwork()


#
# DPiNetwork DPiDigitalIn commands  
#
_CMD_DPi_DIGITAL_IN__PING                    = 0x00
_CMD_DPi_DIGITAL_IN__INITIALIZE              = 0x01
_CMD_DPi_DIGITAL_IN__READ_ALL_INPUTS         = 0x02
_CMD_DPi_DIGITAL_IN__READ_ALL_LATCHES        = 0x03
_CMD_DPi_DIGITAL_IN__CLEAR_ALL_LATCHES       = 0x04
_CMD_DPi_DIGITAL_IN__READ_INPUT              = 0x20
_CMD_DPi_DIGITAL_IN__SET_LATCH_ACTIVE_LOW    = 0x30
_CMD_DPi_DIGITAL_IN__SET_LATCH_ACTIVE_HIGH   = 0x40
_CMD_DPi_DIGITAL_IN__READ_LATCH              = 0x50


#
# other constants used by this class
#
_NUMBER_OF_DIGITAL_INPUTS = 16
_DPiNETWORK_TIMEOUT_PERIOD_MS = 8
_DPiNETWORK_BASE_ADDRESS = 0x28



class DPiDigitalIn:
    #
    # constructor for the DPiDigitalIn class
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
    # Send a command to the DPiDigitalIn board, command's additional data must have already  
    # been "Pushed".  After this function returns, data from the device is retrieved by "Popping"
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
    # set the DPiDigitalIn board number
    #    Enter:  boardNumber = DPiDigitalIn board number (0 - 3)
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
        return self.__sendCommand(_CMD_DPi_DIGITAL_IN__PING)


    #
    # initialize the board to its "power on" configuration
    #    Exit:   True returned on success, else False
    #
    def initialize(self):
        return self.__sendCommand(_CMD_DPi_DIGITAL_IN__INITIALIZE)


    #
    # read all digital inputs
    #    Exit:   [0]: True returned on success, else False
    #            [1]: list of booleans:
    #                   the first boolean in the list is True if input 0 is HIGH
    #                   the second is True if input 1 is HIGH
    #                   ...
    #                   the 15th is True if input 15 is HIGH
    #           
    def readAllInputs(self):      
        if self.__sendCommand(_CMD_DPi_DIGITAL_IN__READ_ALL_INPUTS) != True:
            return False, 0
    
        input_values = dpiNetwork.popUint16()
        
        inputs = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        
        for input_num in range(0, _NUMBER_OF_DIGITAL_INPUTS):
            if ((input_values & (1 << input_num)) != 0):
                inputs[input_num] = True;
        
        return True, inputs


    #
    # read all latched inputs
    #    Exit:   [0]: True returned on success, else False
    #            [1]: list of booleans:
    #                   the first boolean in the list is True if latched input 0 is Set
    #                   the second is True if latched input 1 is set
    #                   ...
    #                   the 15th is True if latched input 15 is set
    #           
    def readAllLatches(self):      
        if self.__sendCommand(_CMD_DPi_DIGITAL_IN__READ_ALL_LATCHES) != True:
            return False, 0
    
        input_values = dpiNetwork.popUint16()
        
        inputs = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        
        for input_num in range(0, _NUMBER_OF_DIGITAL_INPUTS):
            if ((input_values & (1 << input_num)) != 0):
                inputs[input_num] = True;
        
        return True, inputs


    #
    # reset all the input latches to their "UnLatched" state
    #    Exit:   True returned on success, else False
    #
    def clearAllLatches(self):
        return self.__sendCommand(_CMD_DPi_DIGITAL_IN__CLEAR_ALL_LATCHES)


    #
    # configure the latch for the given input number to be Set when its digital input goes LOW
    #    Enter:  inputNumber = input number (0 - 15)
    #    Exit:   True returned on success, else False
    #
    def setLatchActiveLow(self, inputNumber: int):      
        if (inputNumber < 0) or (inputNumber >= _NUMBER_OF_DIGITAL_INPUTS):
            return False

        command = _CMD_DPi_DIGITAL_IN__SET_LATCH_ACTIVE_LOW + inputNumber
        if self.__sendCommand(command) != True:
            return False
        return True


    #
    # configure the latch for the given input number to be Set when its digital input goes HIGH
    #    Enter:  inputNumber = input number (0 - 15)
    #    Exit:   True returned on success, else False
    #
    def setLatchActiveHigh(self, inputNumber: int):      
        if (inputNumber < 0) or (inputNumber >= _NUMBER_OF_DIGITAL_INPUTS):
            return False

        command = _CMD_DPi_DIGITAL_IN__SET_LATCH_ACTIVE_HIGH + inputNumber
        if self.__sendCommand(command) != True:
            return False
        return True


    #
    # read a digital input
    #    Enter:  inputNumber = input number (0 - 15)
    #    Exit:   [0]: True returned on success, else False
    #            [1]: True returned if input is HIGH, else False
    #
    def readDigitalInput(self, inputNumber: int):      
        if (inputNumber < 0) or (inputNumber >= _NUMBER_OF_DIGITAL_INPUTS):
            return False, False

        command = _CMD_DPi_DIGITAL_IN__READ_INPUT + inputNumber
        if self.__sendCommand(command) != True:
            return False, False

        if (dpiNetwork.popUint8()):
            return True, True
        else:
            return True, False
    
        
    #
    # read the latch for a digital input, checking if the input has been Set since the  
    # last time the latch was read, if it is Set then this call will automatically unlatch it
    #    Enter:  inputNumber = input number (0 - 15)
    #    Exit:   [0]: True returned on success, else False
    #            [1]: True returned if input has been Active, else False
    #
    def readLatch(self, inputNumber: int):      
        if (inputNumber < 0) or (inputNumber >= _NUMBER_OF_DIGITAL_INPUTS):
            return False, False

        command = _CMD_DPi_DIGITAL_IN__READ_LATCH + inputNumber
        if self.__sendCommand(command) != True:
            return False, False

        if (dpiNetwork.popUint8()):
            return True, True
        else:
            return True, False


    #
    # get the count of communication errors
    #    Exit:   0 return if no errors, else count of errors returned
    #
    def getCommErrorCount(self):
        return self._commErrorCount

