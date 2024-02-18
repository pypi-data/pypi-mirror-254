#      ******************************************************************
#      *                                                                *
#      *                        DPiButton Libary                        *
#      *                                                                *
#      *            Stan Reifel                      1/8/2023           *
#      *                                                                *
#      ******************************************************************

from dpeaDPi.DPiNetwork import DPiNetwork
dpiNetwork = DPiNetwork()


#
# DPiNetwork DPiButton commands  
#
_CMD_DPi_BUTTON__PING                          = 0x00
_CMD_DPi_BUTTON__INITIALIZE                    = 0x01
_CMD_DPi_BUTTON__CLEAR_ALL_RGB_BUTTON_LATCHES  = 0x02
_CMD_DPi_BUTTON__READ_ALL_RGB_BUTTON_SWITCHES  = 0x03
_CMD_DPi_BUTTON__READ_ALL_RGB_BUTTON_LATCHES   = 0x04
_CMD_DPi_BUTTON__WRITE_RGB_BUTTON_COLOR        = 0x10
_CMD_DPi_BUTTON__READ_RGB_BUTTON_SWITCH        = 0x20
_CMD_DPi_BUTTON__READ_RGB_BUTTON_LATCH         = 0x30


#
# other constants used by this class
#
_NUMBER_OF_RGB_BUTTONS = 10
_DPiNETWORK_TIMEOUT_PERIOD_MS = 8
_DPiNETWORK_BASE_ADDRESS = 0x24



class DPiButton:
    #
    # constructor for the DPiButton class
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
    # Send a command to the DPiButton board, command's additional data must have already  
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
    # set the DPiButton board number
    #    Enter:  boardNumber = DPiButton board number (0 - 3)
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
        return self.__sendCommand(_CMD_DPi_BUTTON__PING)


    #
    # initialize the board to its "power on" configuration
    #    Exit:   True returned on success, else False
    #
    def initialize(self):
        return self.__sendCommand(_CMD_DPi_BUTTON__INITIALIZE)


    #
    # reset all the buttons to their "UnLatched" state
    #    Exit:   True returned on success, else False
    #
    def clearAllButtonLatches(self):
        return self.__sendCommand(_CMD_DPi_BUTTON__CLEAR_ALL_RGB_BUTTON_LATCHES)


    #
    # read all 10 RGB Button switches
    #    Exit:   [0]: True returned on success, else False
    #            [1]: list of booleans:
    #                   the first boolean in the list is True if button 0 is pressed
    #                   the second is True if button 1 is pressed
    #                   ...
    #                   the nineth is True if button 9 is pressed
    #           
    def readAllRGBButtonSwitches(self):      
        if self.__sendCommand(_CMD_DPi_BUTTON__READ_ALL_RGB_BUTTON_SWITCHES) != True:
            return False, 0
    
        button_values = dpiNetwork.popUint16()
        
        buttons = [False, False, False, False, False, False, False, False, False, False]
        
        for button_num in range(0, _NUMBER_OF_RGB_BUTTONS):
            if ((button_values & (1 << button_num)) != 0):
                buttons[button_num] = True;
        
        return True, buttons


    #
    # read the latches for all 10 RGB Buttons, checking each button if it had been pressed since
    # the last time the latch was read, this function automatically unlatches any button that was latched
    #    Exit:   [0]: True returned on success, else False
    #            [1]: list of booleans:
    #                   the first boolean in the list is True if button 0 has been pressed
    #                   the second is True if button 1 has been pressed
    #                   ...
    #                   the nineth is True if button 9 has been pressed
    #           
    def readAllRGBButtonLatches(self):      
        if self.__sendCommand(_CMD_DPi_BUTTON__READ_ALL_RGB_BUTTON_LATCHES) != True:
            return False, 0
    
        button_values = dpiNetwork.popUint16()
        
        buttons = [False, False, False, False, False, False, False, False, False, False]
        
        for button_num in range(0, _NUMBER_OF_RGB_BUTTONS):
            if ((button_values & (1 << button_num)) != 0):
                buttons[button_num] = True;
        
        return True, buttons


    #
    # read a RGB Button switch, this tells you if the button is currently being pressed down
    #    Enter:  buttonNumber = RGB Button number (0 - 1)
    #    Exit:   [0]: True returned on success, else False
    #            [1]: True returned if button pressed, else False
    #
    def readRGBButtonSwitch(self, buttonNumber: int):      
        if (buttonNumber < 0) or (buttonNumber >= _NUMBER_OF_RGB_BUTTONS):
            return False, False

        command = _CMD_DPi_BUTTON__READ_RGB_BUTTON_SWITCH + buttonNumber
        if self.__sendCommand(command) != True:
            return False, False

        if (dpiNetwork.popUint8()):
            return True, True
        else:
            return True, False
        
        
    #
    # read the latch for a RGB Button, checking if the button had been pressed since the  
    # last time the latch was read, if it is latched then this call will automatically unlatch it
    #    Enter:  buttonNumber = RGB Button number (0 - 1)
    #    Exit:   [0]: True returned on success, else False
    #            [1]: True returned if button has been pressed, else False
    #
    def readRGBButtonLatch(self, buttonNumber: int):      
        if (buttonNumber < 0) or (buttonNumber >= _NUMBER_OF_RGB_BUTTONS):
            return False, False

        command = _CMD_DPi_BUTTON__READ_RGB_BUTTON_LATCH + buttonNumber
        if self.__sendCommand(command) != True:
            return False, False

        if (dpiNetwork.popUint8()):
            return True, True
        else:
            return True, False


    #
    # set the RGB Button color
    #    Enter:  buttonNumber = RGB Button number (0 - 1)
    #            R = red value (0 - 255)
    #            G = green value (0 - 255)
    #            B = blue value (0 - 255)
    #    Exit:   True returned on success, else False
    #
    def writeRGBButtonColor(self, buttonNumber: int, R: int, G: int, B: int):      
        if (buttonNumber < 0) or (buttonNumber >= _NUMBER_OF_RGB_BUTTONS):
            return False

        if (R < 0) or (R > 255) or (G < 0) or (G > 255) or (B < 0) or (B > 255):
            return False

        dpiNetwork.pushUint8(R)
        dpiNetwork.pushUint8(G)
        dpiNetwork.pushUint8(B)
        return self.__sendCommand(_CMD_DPi_BUTTON__WRITE_RGB_BUTTON_COLOR + buttonNumber)


    #
    # get the count of communication errors
    #    Exit:   0 return if no errors, else count of errors returned
    #
    def getCommErrorCount(self):
        return self._commErrorCount

