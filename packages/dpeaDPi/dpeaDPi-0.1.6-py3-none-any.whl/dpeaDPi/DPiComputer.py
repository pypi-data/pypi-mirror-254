#      ******************************************************************
#      *                                                                *
#      *   DPiComputer Libary - For using the DPiComputer's onboard IO  *
#      *                                                                *
#      *            Stan Reifel                     9/20/2022           *
#      *                                                                *
#      ******************************************************************

from smbus import SMBus
from time import sleep
import RPi.GPIO as GPIO

#
# DPiComputer commands issued to the onboard Pico
#
_CMD_DPiCOMPUTER_PICO__INITIALIZE                         = 0x01
_CMD_DPiCOMPUTER_PICO__SET_ENCODER_CLOCK_DIVISOR          = 0x02
_CMD_DPiCOMPUTER_PICO__WRITE_RGB_BUTTON_COLOR             = 0x10
_CMD_DPiCOMPUTER_PICO__READ_RGB_BUTTON_SWITCH             = 0x18
_CMD_DPiCOMPUTER_PICO__READ_ANALOG                        = 0x20
_CMD_DPiCOMPUTER_PICO__RESET_ENCODER                      = 0x28
_CMD_DPiCOMPUTER_PICO__READ_ENCODER                       = 0x30
_CMD_DPiCOMPUTER_PICO__WRITE_NEOPIXEL_REPEAT_ONE_COLOR    = 0x38
_CMD_DPiCOMPUTER_PICO__WRITE_NEOPIXEL_REPEAT_THREE_COLORS = 0x40
_CMD_DPiCOMPUTER_PICO__WRITE_NEOPIXEL_ARRAY               = 0x48
_CMD_DPiCOMPUTER_PICO__ADD_TO_NEOPIXEL_ARRAY              = 0x50
_CMD_DPiCOMPUTER_PICO__WRITE_SERVO                        = 0x58
_CMD_DPiCOMPUTER_PICO__WRITE_DIGITAL_OUT_HIGH             = 0x60
_CMD_DPiCOMPUTER_PICO__WRITE_DIGITAL_OUT_LOW              = 0x68
_CMD_DPiCOMPUTER_PICO__WRITE_PWM_OUT                      = 0x70

#
# other constants used by this class
#
_PICOS_I2C_ADDRESS = 0x50
_I2C_RETRY_ATTEMPTS = 4
_NUMBER_OF_RGB_BUTTONS = 2
_NUMBER_OF_ANALOG_INPUTS = 2
_NUMBER_OF_ENCODERS = 2
_NUMBER_OF_NEOPIXELS = 2
_NUMBER_OF_SERVOS = 2
_NUMBER_OF_PI_OUTS = 4
_NUMBER_OF_PI_INS = 4
_NUMBER_OF_PICO_OUTS = 8
_PWM_FREQUENCY = 1000


#
# pin numbers used on the Raspberry Pi
#
_OUT_0_PIN       = 13
_OUT_1_PIN       = 16
_OUT_2_PIN       = 18
_OUT_3_PIN       = 19
_IN_0_PIN        = 23
_IN_1_PIN        = 24
_IN_2_PIN        = 25
_IN_3_PIN        = 7
_PI_SHUTDOWN_PIN = 21


class DPiComputer:
    #
    # connectors constants for the writeDigitalOut() and writePWMOut() functions
    #
    OUT_CONNECTOR__OUT_0         = 0   # DPiComputer connector labeled "OUT 0"
    OUT_CONNECTOR__OUT_1         = 1   # DPiComputer connector labeled "OUT 1"
    OUT_CONNECTOR__OUT_2         = 2   # DPiComputer connector labeled "OUT 2"
    OUT_CONNECTOR__OUT_3         = 3   # DPiComputer connector labeled "OUT 3"
    OUT_CONNECTOR__NEOPIXEL_0    = 10  # DPiComputer connector labeled "NEOPIXEL 0"
    OUT_CONNECTOR__NEOPIXEL_1    = 11  # DPiComputer connector labeled "NEOPIXEL 1"
    OUT_CONNECTOR__RGB_BUTTON0_R = 12  # DPiComputer connector labeled "RGB BUTTON 0 - R"
    OUT_CONNECTOR__RGB_BUTTON0_G = 13  # DPiComputer connector labeled "RGB BUTTON 0 - G"
    OUT_CONNECTOR__RGB_BUTTON0_B = 14  # DPiComputer connector labeled "RGB BUTTON 0 - B"
    OUT_CONNECTOR__RGB_BUTTON1_R = 15  # DPiComputer connector labeled "RGB BUTTON 1 - R"
    OUT_CONNECTOR__RGB_BUTTON1_G = 16  # DPiComputer connector labeled "RGB BUTTON 1 - G"
    OUT_CONNECTOR__RGB_BUTTON1_B = 17  # DPiComputer connector labeled "RGB BUTTON 1 - B"

    #
    # connectors constants for the readDigitalIn() function
    #
    IN_CONNECTOR__IN_0 = 0  # DPiComputer connector labeled "IN 0"
    IN_CONNECTOR__IN_1 = 1  # DPiComputer connector labeled "IN 1"
    IN_CONNECTOR__IN_2 = 2  # DPiComputer connector labeled "IN 2"
    IN_CONNECTOR__IN_3 = 3  # DPiComputer connector labeled "IN 3"

    #
    #  initialize the GPIO pins
    #
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(_OUT_0_PIN, GPIO.OUT)
    GPIO.setup(_OUT_1_PIN, GPIO.OUT)
    GPIO.setup(_OUT_2_PIN, GPIO.OUT)
    GPIO.setup(_OUT_3_PIN, GPIO.OUT)

    GPIO.setup(_IN_0_PIN, GPIO.IN)
    GPIO.setup(_IN_1_PIN, GPIO.IN)
    GPIO.setup(_IN_2_PIN, GPIO.IN)
    GPIO.setup(_IN_3_PIN, GPIO.IN)

    _out0PWM = GPIO.PWM(_OUT_0_PIN, _PWM_FREQUENCY)
    _out1PWM = GPIO.PWM(_OUT_1_PIN, _PWM_FREQUENCY)
    _out2PWM = GPIO.PWM(_OUT_2_PIN, _PWM_FREQUENCY)
    _out3PWM = GPIO.PWM(_OUT_3_PIN, _PWM_FREQUENCY)

    _out0PWM_Flg = False
    _out1PWM_Flg = False
    _out2PWM_Flg = False
    _out3PWM_Flg = False

    GPIO.output(_OUT_0_PIN, GPIO.LOW)
    GPIO.output(_OUT_1_PIN, GPIO.LOW)
    GPIO.output(_OUT_2_PIN, GPIO.LOW)
    GPIO.output(_OUT_3_PIN, GPIO.LOW)

    #
    # constructor for the DPiSolenoid class
    #
    def __init__(self):
        self.i2cbus = SMBus(1)

    # ---------------------------------------------------------------------------------
    #                                 Private functions
    # ---------------------------------------------------------------------------------

    #
    # send a command to the DPiComputer's Pico, along with variable amount of data
    #    Enter:  command = command byte
    #            data = list of additional data bytes to send
    #    Exit:   True returned on success, else False
    #
    def __sendCommand(self, command: int, data: list = []) -> bool:
        try:
            if data:
                self.i2cbus.write_i2c_block_data(_PICOS_I2C_ADDRESS, command, data)
            else:
                self.i2cbus.write_byte(_PICOS_I2C_ADDRESS, command)
            return True
        except OSError:
            return False

    #
    # send a command to the DPiComputer's Pico requesting data
    #    Enter:  command = command byte
    #            bytesToReceive = number of bytes to read
    #    Exit:   byte list of size 'bytesToReceive' on success, else empty list
    #
    def __requestDataCommand(self, command: int, bytesToReceive: int) -> list:
        for _retry_num in range(_I2C_RETRY_ATTEMPTS):
            try:
                data = self.i2cbus.read_i2c_block_data(_PICOS_I2C_ADDRESS, command, bytesToReceive)
            except OSError:
                data = []

            if len(data) == bytesToReceive:
                return data
            else:
                sleep(.002)  # communication failed, retry after 2ms
        return []

    # ---------------------------------------------------------------------------------
    #                                Public functions
    # ---------------------------------------------------------------------------------

    #
    # initialize the board to its "power on" configuration
    #
    def initialize(self):

        if (self._out0PWM_Flg):
            self._out0PWM.stop()
            self._out0PWM_Flg = False

        if (self._out1PWM_Flg):
            self._out1PWM.stop()
            self._out1PWM_Flg = False

        if (self._out2PWM_Flg):
            self._out2PWM.stop()
            self._out2PWM_Flg = False

        if (self._out3PWM_Flg):
            self._out3PWM.stop()
            self._out3PWM_Flg = False

        GPIO.output(_OUT_0_PIN, GPIO.LOW)
        GPIO.output(_OUT_1_PIN, GPIO.LOW)
        GPIO.output(_OUT_2_PIN, GPIO.LOW)
        GPIO.output(_OUT_3_PIN, GPIO.LOW)

        self.__sendCommand(_CMD_DPiCOMPUTER_PICO__INITIALIZE)

    #
    # set the RGB Button color
    #    Enter:  buttonNumber = RGB Button number (0 - 1)
    #            R = red value (0 - 255)
    #            G = green value (0 - 255)
    #            B = blue value (0 - 255)
    #
    def writeRGBButtonColor(self, buttonNumber: int, R: int, G: int, B: int):
        if (buttonNumber < 0) or (buttonNumber >= _NUMBER_OF_RGB_BUTTONS):
            return

        if (R < 0) or (R > 255) or (G < 0) or (G > 255) or (B < 0) or (B > 255):
            return

        command = _CMD_DPiCOMPUTER_PICO__WRITE_RGB_BUTTON_COLOR + buttonNumber
        self.__sendCommand(command, [R, G, B])

    #
    # read the RGB Button switch
    #    Enter:  buttonNumber = RGB Button number (0 - 1)
    #    Exit:   True returned if button pressed, else False
    #
    def readRGBButtonSwitch(self, buttonNumber: int):
        if (buttonNumber < 0) or (buttonNumber >= _NUMBER_OF_RGB_BUTTONS):
            return False

        command = _CMD_DPiCOMPUTER_PICO__READ_RGB_BUTTON_SWITCH + buttonNumber
        if ((self.__requestDataCommand(command, 1)[0]) & 0x7f):
            return True
        else:
            return False

    #
    # read an analog input pin
    #    Enter:  analogNumber = 0 or 1
    #    Exit:   analog value returned (0 = 0V  -  1023 = 3.3V)
    #
    def readAnalog(self, analogNumber: int):
        if (analogNumber < 0) or (analogNumber >= _NUMBER_OF_ANALOG_INPUTS):
            return 0

        command = _CMD_DPiCOMPUTER_PICO__READ_ANALOG + analogNumber
        results = self.__requestDataCommand(command, 2)
        return ((results[0] & 0x0f) << 8) + results[1]

    #
    # set the clock divisor used by both Encoder0 and Encoder1's state machines.
    #
    # NOTE: This function must be called before the first call to readEncoder()
    #
    # The Clock Divisor is used to lower the clock rate of the encoder processor, thus
    # reducing its bandwidth.  Setting the value to 1 gives the full bandwidth, providing
    # a maximum count rate of about 10 million encoder_counts/second. Setting the divisor
    # to 10 reduces the bandwidth to ~1 million counts/sec.  A value of 1000 sets the
    # max rate to ~10K/sec.
    #
    # The default Clock Divisor is 10, allowing the encoder counter to count up to ~1M
    # counts/second.
    #
    # Reducing the bandwidth has the advantage of making the encoder more resistant to
    # electrical noise.  For example: an encoder with 400 counts/revolution that's rotated
    # by a human's hand, might have a maximum speed of 20 revolutions/second, resulting in
    # a top speed of 8000 counts/second.  Setting the Clock Divisor to 1000 might make
    # sense here.
    #
    #    Enter:  clockDivisor = 1 for full clock rate, larger values slows the clock down (1 - 10000)
    #
    def setEncoderClockDivisor(self, clockDivisor):
        if (clockDivisor < 1) or (clockDivisor > 10000):
            return

        command = _CMD_DPiCOMPUTER_PICO__SET_ENCODER_CLOCK_DIVISOR
        self.__sendCommand(command, [(clockDivisor >> 8) & 0xff, clockDivisor & 0xff])

    #
    # reset the encoder's position to 0
    #    Enter:  encoderNumber = 0 or 1
    #
    def resetEncoder(self, encoderNumber: int):
        if (encoderNumber < 0) or (encoderNumber >= _NUMBER_OF_ENCODERS):
            return

        command = _CMD_DPiCOMPUTER_PICO__RESET_ENCODER + encoderNumber
        self.__sendCommand(command)

    #
    # read an encoder's position
    #    Enter:  encoderNumber = 0 or 1
    #    Exit:   32 bit signed encoder position returned
    #
    def readEncoder(self, encoderNumber: int):
        if (encoderNumber < 0) or (encoderNumber >= _NUMBER_OF_ENCODERS):
            return 0

        command = _CMD_DPiCOMPUTER_PICO__READ_ENCODER + encoderNumber
        #         results = self.__requestDataCommand(command, 5)
        #         encoderValue = (results[1] << 24) + (results[2] << 16) + (results[3] << 8) + results[4]

        for _retry in range(4):
            results = self.__requestDataCommand(command, 6)
            if (results[0] == 0) and (results[1] == 0):
                encoderValue = (results[2] << 24) + (results[3] << 16) + (results[4] << 8) + results[5]
                if encoderValue > 0x7FFFFFFF:
                    encoderValue -= 0x100000000
                return encoderValue
        return 0

    #
    # set the neopixel LEDs by repeating one color (with blanking before and after)
    #    Enter:  neopixelNumber = neopixel number (0 - 1)
    #            blankFirstCount = number of LEDs to set black at the beginning of the string (0 - 255)
    #            repeatColorCount = after the black LEDs, set this number of LEDs to the given color (0 - 255)
    #            blankLastCount = after the colored LEDs, set this many black at the end of the string (0 - 255)
    #            R = red value (0 - 255)
    #            G = green value (0 - 255)
    #            B = blue value (0 - 255)
    #
    def writeNeopixelByRepeatingOneColor(self, neopixelNumber: int, blankFirstCount: int, repeatColorCount: int,
                                         blankLastCount: int, R: int, G: int, B: int):
        if (neopixelNumber < 0) or (neopixelNumber >= _NUMBER_OF_NEOPIXELS):
            return

        if (blankFirstCount < 0) or (blankFirstCount > 255) or (repeatColorCount < 0) or (repeatColorCount > 255) or (
                blankLastCount < 0) or (blankLastCount > 255):
            return

        if (R < 0) or (R > 255) or (G < 0) or (G > 255) or (B < 0) or (B > 255):
            return

        command = _CMD_DPiCOMPUTER_PICO__WRITE_NEOPIXEL_REPEAT_ONE_COLOR + neopixelNumber
        self.__sendCommand(command, [blankFirstCount, repeatColorCount, blankLastCount, R, G, B])

    #
    # set the neopixel LEDs by repeating a 3 color sequence (with blanking before and after)
    #    Enter:  neopixelNumber = neopixel number (0 - 1)
    #            blankFirstCount = number of LEDs to set black at the beginning of the string (0 - 255)
    #            repeatColorCount = after the black LEDs, set this number of LEDs using color sequence (0 - 255)
    #            blankLastCount = after the colored LEDs, set this many black at the end of the string (0 - 255)
    #            R1, G1, B1 = first color to repeat (each value 0 - 255)
    #            R2, G2, B2 = next color to repeat
    #            R3, G3, B3 = third color to repeat
    #
    def writeNeopixelByRepeatingThreeColors(self, neopixelNumber: int, blankFirstCount: int, repeatColorCount: int,
                                            blankLastCount: int, R1: int, G1: int, B1: int, R2: int, G2: int, B2: int,
                                            R3: int, G3: int, B3: int):
        if (neopixelNumber < 0) or (neopixelNumber >= _NUMBER_OF_NEOPIXELS):
            return

        if (blankFirstCount < 0) or (blankFirstCount > 255) or (repeatColorCount < 0) or (repeatColorCount > 255) or (
                blankLastCount < 0) or (blankLastCount > 255):
            return

        if (R1 < 0) or (R1 > 255) or (G1 < 0) or (G1 > 255) or (B1 < 0) or (B1 > 255):
            return

        if (R2 < 0) or (R2 > 255) or (G2 < 0) or (G2 > 255) or (B2 < 0) or (B2 > 255):
            return

        if (R3 < 0) or (R3 > 255) or (G3 < 0) or (G3 > 255) or (B3 < 0) or (B3 > 255):
            return

        command = _CMD_DPiCOMPUTER_PICO__WRITE_NEOPIXEL_REPEAT_THREE_COLORS + neopixelNumber
        self.__sendCommand(command,
                           [blankFirstCount, repeatColorCount, blankLastCount, R1, G1, B1, R2, G2, B2, R3, G3, B3])

    #
    # write to neopixels by passing in an array of RGB values to the neopixels
    #   Enter:  neopixelNumber = neopixel number (0 - 1)
    #           NeoPixelRGBValues = array of RGB values to write to the neopixels (either a set of tuples or individual R, G, B values)
    #
    def writeNeopixelByArray(self, neopixelNumber: int, NeoPixelRGBValues: list):
        if (neopixelNumber < 0) or (neopixelNumber >= _NUMBER_OF_NEOPIXELS):
            return

        # Check if the list is empty
        if not NeoPixelRGBValues:
            return

        # Check if the list is a list of ints
        if isinstance(NeoPixelRGBValues[0], int):
            # Refactor the list to be a list of tuples
            NeoPixelRGBValues = list(zip(NeoPixelRGBValues[0::3], NeoPixelRGBValues[1::3], NeoPixelRGBValues[2::3]))

        # Make sure the list is a list of tuples
        if not isinstance(NeoPixelRGBValues[0], tuple):
            return

        # Iterate through the list sending the RGB values to the neopixels array
        for RGBValue in NeoPixelRGBValues:
            R, G, B = RGBValue

            command = _CMD_DPiCOMPUTER_PICO__ADD_TO_NEOPIXEL_ARRAY + neopixelNumber
            self.__sendCommand(command, [R, G, B])

        # Send the command to write the neopixels
        command = _CMD_DPiCOMPUTER_PICO__WRITE_NEOPIXEL_ARRAY + neopixelNumber
        self.__sendCommand(command, [])

    #
    # write to a servo setting its angular position
    #    Enter:  servoNumber = servo port number (0 - 1)
    #            angle = angle to set the servo to (0 - 180, with 90 centering the servo)
    #
    def writeServo(self, servoNumber: int, angle: int):
        if (servoNumber < 0) or (servoNumber >= _NUMBER_OF_SERVOS):
            return

        if (angle < 0):
            angle = 0
        if (angle > 180):
            angle = 180

        command = _CMD_DPiCOMPUTER_PICO__WRITE_SERVO + servoNumber
        self.__sendCommand(command, [angle])

    #
    # write to a digital output connector
    #    Enter:  connectorNum = connector to write to:
    #                  OUT_CONNECTOR__OUT_0, OUT_CONNECTOR__OUT_1, OUT_CONNECTOR__OUT_2, OUT_CONNECTOR__OUT_3,
    #                  OUT_CONNECTOR__NEOPIXEL_0, OUT_CONNECTOR__NEOPIXEL_1, OUT_CONNECTOR__RGB_BUTTON0_R,
    #                  OUT_CONNECTOR__RGB_BUTTON0_G, OUT_CONNECTOR__RGB_BUTTON0_B, OUT_CONNECTOR__RGB_BUTTON1_R,
    #                  OUT_CONNECTOR__RGB_BUTTON1_G, OUT_CONNECTOR__RGB_BUTTON1_B
    #            value = True to set the pin HIGH, False to set it LOW
    #
    def writeDigitalOut(self, connectorNum: int, value: int):
        #
        # check if connector connects directly to the Raspberry Pi
        #
        if (connectorNum >= 0) and (connectorNum < _NUMBER_OF_PI_OUTS):
            if (value == True):
                pinValue = GPIO.HIGH
            else:
                pinValue = GPIO.LOW

            if (connectorNum == self.OUT_CONNECTOR__OUT_0):
                if (self._out0PWM_Flg):
                    self._out0PWM.stop()
                    self._out0PWM_Flg = False
                pinNumber = _OUT_0_PIN

            elif (connectorNum == self.OUT_CONNECTOR__OUT_1):
                if (self._out1PWM_Flg):
                    self._out1PWM.stop()
                    self._out1PWM_Flg = False
                pinNumber = _OUT_1_PIN

            elif (connectorNum == self.OUT_CONNECTOR__OUT_2):
                if (self._out2PWM_Flg):
                    self._out2PWM.stop()
                    self._out2PWM_Flg = False
                pinNumber = _OUT_2_PIN

            elif (connectorNum == self.OUT_CONNECTOR__OUT_3):
                if (self._out3PWM_Flg):
                    self._out3PWM.stop()
                    self._out3PWM_Flg = False
                pinNumber = _OUT_3_PIN
            else:
                return

            GPIO.output(pinNumber, pinValue)
            return

        #
        # check if connector is attached to the Pico
        #
        connectorNum -= 10  # remove offset so connectorNum numbers are 0 - 7
        if (connectorNum >= 0) and (connectorNum < _NUMBER_OF_PICO_OUTS):
            if (value):
                command = _CMD_DPiCOMPUTER_PICO__WRITE_DIGITAL_OUT_HIGH + connectorNum
                self.__sendCommand(command)
                return

            else:
                command = _CMD_DPiCOMPUTER_PICO__WRITE_DIGITAL_OUT_LOW + connectorNum
                self.__sendCommand(command)
                return

    #
    # write to a pwm output connector
    #    Enter:  connectorNum = connector to write to:
    #                  OUT_CONNECTOR__OUT_0, OUT_CONNECTOR__OUT_1, OUT_CONNECTOR__OUT_2, OUT_CONNECTOR__OUT_3,
    #                  OUT_CONNECTOR__NEOPIXEL_0, OUT_CONNECTOR__NEOPIXEL_1, OUT_CONNECTOR__RGB_BUTTON0_R,
    #                  OUT_CONNECTOR__RGB_BUTTON0_G, OUT_CONNECTOR__RGB_BUTTON0_B, OUT_CONNECTOR__RGB_BUTTON1_R,
    #                  OUT_CONNECTOR__RGB_BUTTON1_G, OUT_CONNECTOR__RGB_BUTTON1_B
    #            value = pwm value (0 - 255)
    #
    def writePWMOut(self, connectorNum: int, pwmValue: int):
        if (pwmValue < 0) or (pwmValue > 255):
            return
        pwmValue = (pwmValue * 100.0) / 256.0

        #
        # check if connector connects directly to the Raspberry Pi
        #
        if (connectorNum >= 0) and (connectorNum < _NUMBER_OF_PI_OUTS):
            if (connectorNum == self.OUT_CONNECTOR__OUT_0):
                if (self._out0PWM_Flg == False):
                    self._out0PWM.start(pwmValue)
                    self._out0PWM_Flg = True
                    return
                self._out0PWM.ChangeDutyCycle(pwmValue)

            elif (connectorNum == self.OUT_CONNECTOR__OUT_1):
                if (self._out1PWM_Flg == False):
                    self._out1PWM.start(pwmValue)
                    self._out1PWM_Flg = True
                    return
                self._out1PWM.ChangeDutyCycle(pwmValue)

            elif (connectorNum == self.OUT_CONNECTOR__OUT_2):
                if (self._out2PWM_Flg == False):
                    self._out2PWM.start(pwmValue)
                    self._out2PWM_Flg = True
                    return
                self._out2PWM.ChangeDutyCycle(pwmValue)

            elif (connectorNum == self.OUT_CONNECTOR__OUT_3):
                if (self._out3PWM_Flg == False):
                    self._out3PWM.start(pwmValue)
                    self._out3PWM_Flg = True
                    return
                self._out3PWM.ChangeDutyCycle(pwmValue)
            return

        #
        # check if connector attaches to the Pico
        #
        connectorNum -= 10  # remove offset so connector numbers are 0 - 7
        if (connectorNum >= 0) and (connectorNum < _NUMBER_OF_PICO_OUTS):
            command = _CMD_DPiCOMPUTER_PICO__WRITE_PWM_OUT + connectorNum
            self.__sendCommand(command, [pwmValue])

    #
    # read a digital input connector
    #    Enter:  connectorNum = connector to read from:
    #                  IN_CONNECTOR__IN_0, IN_CONNECTOR__IN_1, IN_CONNECTOR__IN_2, IN_CONNECTOR__IN_3
    #    Exit:   True returned if pin HIGH, else False
    #
    def readDigitalIn(self, connectorNum: int):
        if (connectorNum == self.IN_CONNECTOR__IN_0):
            return (GPIO.input(_IN_0_PIN))

        elif (connectorNum == self.IN_CONNECTOR__IN_1):
            return (GPIO.input(_IN_1_PIN))

        elif (connectorNum == self.IN_CONNECTOR__IN_2):
            return (GPIO.input(_IN_2_PIN))

        elif (connectorNum == self.IN_CONNECTOR__IN_3):
            return (GPIO.input(_IN_3_PIN))

        else:
            return (False)

