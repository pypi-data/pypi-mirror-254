#      ******************************************************************
#      *                                                                *
#      *                        DPiStepper Libary                       *
#      *                                                                *
#      *            Stan Reifel                     8/21/2022           *
#      *                                                                *
#      ******************************************************************

#
# This library is used to drive the DPiStepper board which can control up to 3
# stepper motors.  The motors are accelerated and decelerated as they travel 
# to the final position.  This driver supports changing the target position, 
# speed or rate of acceleration while moving.
#
# Running just one stepper motor, DPiStepper can generate a maximum of about 35K  
# steps per second.  Running one motor with 8X microstepping, the maximum rotation  
# rate is about 22 RPS or 1300 RPM.  Running multiple motors at the same time will 
# reduce the maximum speed.  For example running two motors will reduce the step 
# rate by a bit more than half.
# 
#
# Usage:
#    Near the top of the program, add:
#        from DPiStepper import DPiStepper
#
#    Declare a global object for the DPiStepper board functions as: 
#        dpiStepper = DPiStepper()
#
#    Jumpers on the DPiStepper board allow you to have up to 4 boards on the same
#    RS485 network. Call this function to tell the library which DPi stepper board 
#    you want to talk to.  In this example board 0 is selected:
#        dpiStepper.setBoardNumber(0)
#
#    Each DPiStepper board can control up to 3 stepper motors.  This example will setup
#    and move "Motor 0":
#        #
#        # enable the stepper motors, when disabled the motors are turned off and spin freely
#        #
#        dpiStepper.enableMotors(True)
#
#        #
#        # set the microstepping to 1, 2, 4, 8, 16 or 32. 8 results in 1600 steps per
#        # revolution of the motor's shaft
#        #
#        dpiStepper.setMicrostepping(8)
#
#        #
#        # set the speed in steps/second and acceleration in steps/second/second
#        #
#        stepperNum = 0
#        dpiStepper.setSpeedInStepsPerSecond(stepperNum, 1600)
#        dpiStepper.setAccelerationInStepsPerSecondPerSecond(stepperNum, 1600)
#
#        #
#        # move 1600 steps in the backward direction, this function will return after the
#        # motor stops because "wait_to_finish_moving_flg" is set to True
#        #
#        wait_to_finish_moving_flg = True
#        dpiStepper.moveToRelativePositionInSteps(stepper_num, -1600, wait_to_finish_moving_flg)
#
#        #
#        # move to an absolute position of 1600 steps
#        #
#        dpiStepper.moveToAbsolutePositionInSteps(stepperNum, 1600, wait_to_finish_moving_flg)
#
#
#    There are 3 different units that can be used to control the stepper motors: (steps, 
#    millimeters or revolutions).  Choose the one that's most intuitive for your 
#    application.  This example will move "Motor 1" using units of Revolutions:
#        #
#        # set the number of steps per revolutions, 200 with no microstepping, 
#        # 800 with 4x microstepping
#        #
#        stepperNum = 1
#        dpiStepper.setStepsPerRevolution(stepperNum, 800)
#
#        #
#        # set the speed in rotations/second and acceleration in 
#        # rotations/second/second
#        #
#        dpiStepper.setSpeedInRevolutionsPerSecond(stepperNum, 1.0)
#        dpiStepper.setAccelerationInRevolutionsPerSecondPerSecond(stepperNum, 1.0)
#
#        #
#        # move backward 1.5 revolutions, this function will return after the
#        # motor stops because "wait_to_finish_moving_flg" is set to True
#        #
#        wait_to_finish_moving_flg = True
#        dpiStepper.moveToRelativePositionInRevolutions(stepperNum, -1.5, wait_to_finish_moving_flg)
#
#        #
#        # move to an absolute position of 3.75 revolutions
#        #
#        dpiStepper.moveToAbsolutePositionInRevolutions(stepperNum, 3.75, wait_to_finish_moving_flg)
#
#
#    For linear mechanisms, controlling the stepper motors with units in millimeters
#    often makes the most sense.  This example is driving "Motor 2" in millimeters:
#        #
#        # set the number of steps per millimeter
#        #
#        stepperNum = 2
#        dpiStepper.setStepsPerMillimeter(stepperNum, 25.0)
#
#        #
#        # set the speed in millimeters/second and acceleration in 
#        # millimeters/second/second
#        #
#        dpiStepper.setSpeedInMillimetersPerSecond(stepperNum, 20.0)
#        dpiStepper.setAccelerationInMillimetersPerSecondPerSecond(stepperNum, 20.0)
#
#        #
#        # move backward 15.5 millimeters
#        #
#        wait_to_finish_moving_flg = True
#        dpiStepper.moveToRelativePositionInMillimeters(stepperNum, -15.5, wait_to_finish_moving_flg)
#
#        #
#        # move to an absolute position of 125 millimeters
#        #
#        dpiStepper.moveToAbsolutePositionInMillimeters(stepperNum, 125, wait_to_finish_moving_flg)
#


from array import *
from time import sleep
from dpeaDPi.DPiNetwork import DPiNetwork
dpiNetwork = DPiNetwork()

#
# DPiNetwork DPiStepper commands  
#
_CMD_DPiSTEPPER__PING                                  = 0x00
_CMD_DPiSTEPPER__INITIALIZE                            = 0x01
_CMD_DPiSTEPPER__ENABLE_MOTORS                         = 0x02
_CMD_DPiSTEPPER__DISABLE_MOTORS                        = 0x03
_CMD_DPiSTEPPER__SET_MICROSTEPPING                     = 0x04
_CMD_DPiSTEPPER__ALL_MOTORS_STOPPED                    = 0x05
_CMD_DPiSTEPPER__SET_CURRENT_P0SITION_IN_STEPS         = 0x10
_CMD_DPiSTEPPER__GET_CURRENT_POSITION_IN_STEPS         = 0x20
_CMD_DPiSTEPPER__SET_SPEED_IN_STEPS_PER_SEC            = 0x30
_CMD_DPiSTEPPER__SET_ACCEL_IN_STEPS_PSPS               = 0x40
_CMD_DPiSTEPPER__MOVE_TO_ABS_POSITION_IN_STEPS         = 0x50
_CMD_DPiSTEPPER__MOVE_TO_REL_POSITION_IN_STEPS         = 0x60
_CMD_DPiSTEPPER__DECELERATE_TO_A_STOP                  = 0x70
_CMD_DPiSTEPPER__EMERGENCY_STOP                        = 0x80
_CMD_DPiSTEPPER__GET_CURRENT_VELOCITY_IN_STEPS_PER_SEC = 0x90
_CMD_DPiSTEPPER__MOTION_COMPLETE                       = 0xa0
_CMD_DPiSTEPPER__GET_STEPPER_STATUS                    = 0xb0


#
# bits returned by CMD_DPiSTEPPER__GET_STEPPER_STATUS
#
_STEPPER_STATUS_MOTOR_STOPPED  = 0x01
_STEPPER_STATUS_MOTORS_ENABLED = 0x02
_STEPPER_STATUS_AT_HOME_SWITCH = 0x04


#
# other constants used by this class
#
_NUMBER_OF_DPi_STEPPER_DRIVERS = 3
_DPiNETWORK_TIMEOUT_PERIOD_MS = 8                # 3/9/2023 changed from 6 to 8ms
_DPiNETWORK_BASE_ADDRESS = 0x20



class DPiStepper:
    #
    # constructor for the DPiStepper class
    #
    def __init__(self):
        #
        # attribute variables local to one instance of this class
        #
        self._slaveAddress = _DPiNETWORK_BASE_ADDRESS
        self._commErrorCount = 0
        self._stepsPerMillimeter = array('d', [200.0, 200.0, 200.0])
        self._stepsPerRevolution = array('d', [1600.0, 1600.0, 1600.0])
    

    # ---------------------------------------------------------------------------------
    #                                 Private functions 
    # ---------------------------------------------------------------------------------

    #
    # send a command to the DPiStepper, command's additional data must have already been "Pushed". 
    # After this function returns data from the device is retrieved by "Popping"
    #    Enter:  command = command byte
    #    Exit:   True returned on success, else False
    #
    def __sendCommand(self, command: int):
        (results, failedCount) = dpiNetwork.sendCommand(self._slaveAddress, command, _DPiNETWORK_TIMEOUT_PERIOD_MS)
        self._commErrorCount += failedCount;
        return results


    #
    # push a float with 2 digits right of the decimal, as an int32_t, to the transmit buffer
    #  Enter:  float value 
    #
    def __pushFltPoint2ToInt32(self, value: float):
        dpiNetwork.pushInt32(int(round(value * 100.0)))


    #
    # pop an int32_t, as a float with 2 digits right of the decimal, from the receive buffer
    #
    def __popInt32ToFltPoint2(self):
        return float(dpiNetwork.popInt32()) / 100.0


    # ---------------------------------------------------------------------------------
    #                     Public setup and configuration functions 
    # ---------------------------------------------------------------------------------

    #
    # set the DPiStepper board number
    #    Enter:  boardNumber = DPiStepper board number (0 - 3)
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
        return self.__sendCommand(_CMD_DPiSTEPPER__PING)


    #
    # initialize the board to its "power on" configuration
    #    Exit:   True returned on success, else False
    #
    def initialize(self):
        for i in range(_NUMBER_OF_DPi_STEPPER_DRIVERS):
            self._stepsPerMillimeter[i] = 200
            self._stepsPerRevolution[i] = 1600
        return self.__sendCommand(_CMD_DPiSTEPPER__INITIALIZE)


    #
    # enable/disable the stepper motors
    #  Exit:   True returned on success, else False
    #
    def enableMotors(self, enableFlg: bool):
        if enableFlg:
            results = self.__sendCommand(_CMD_DPiSTEPPER__ENABLE_MOTORS)
            sleep(.1);
            return results
        else:
            return self.__sendCommand(_CMD_DPiSTEPPER__DISABLE_MOTORS)


    #
    # set microstepping 
    #    Enter:  microstepping = 1, 2, 4, 8, 16, 32
    #    Exit:   True returned on success, else False
    #
    def setMicrostepping(self, microstepping: int):
        if not ((microstepping == 1) or (microstepping == 2) or (microstepping == 4) or
                (microstepping == 8) or (microstepping == 16) or (microstepping == 32)):
            return False

        dpiNetwork.pushUint8(microstepping)
        return self.__sendCommand(_CMD_DPiSTEPPER__SET_MICROSTEPPING)


    # ---------------------------------------------------------------------------------
    #                             Public status functions 
    # ---------------------------------------------------------------------------------

    #
    # check if all 3 stepper motors stopped
    #  Exit:   True returned if motion complete, else False
    #
    def getAllMotorsStopped(self):
        if self.__sendCommand(_CMD_DPiSTEPPER__ALL_MOTORS_STOPPED) != True:
            return False

        allStoppedFlg = dpiNetwork.popUint8()

        if allStoppedFlg:
            return True
        else:
            return False


    #
    # wait until motor stops
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #  Exit:   True returned on success, else False
    #
    def waitUntilMotorStops(self, stepperNum: int):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False, False

        while True:
            results, stoppedFlg = self.getMotionComplete(stepperNum)
            if results != True:
                return False
            if stoppedFlg == True:
                return True
            sleep(0.02)


    #
    # get motion complete flag, indicating that the stepper has stopped
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #  Exit:   [0]: True returned on success, else False
    #          [1]: True returned on motion complete, else False
    #
    def getMotionComplete(self, stepperNum: int):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False, False

        if self.__sendCommand(_CMD_DPiSTEPPER__MOTION_COMPLETE + stepperNum) != True:
            return False, False

        if dpiNetwork.popUint8() == False:
            return True, False
        else:
            return True, True



    #
    # get stepper status
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #  Exit:   [0]: True returned on success, else False
    #          [1]: True returned if motor is stopped
    #          [2]: True returned if motors are enabled
    #          [3]: True returned if the "Homing" switch indicates "At home"
    #
    def getStepperStatus(self, stepperNum: int):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False, False, False, False

        if self.__sendCommand(_CMD_DPiSTEPPER__GET_STEPPER_STATUS + stepperNum) != True:
            return False, False, False, False

        results = dpiNetwork.popUint8()
        if results & _STEPPER_STATUS_MOTOR_STOPPED != 0:
            stoppedFlg = True
        else: 
            stoppedFlg = False

        if results & _STEPPER_STATUS_MOTORS_ENABLED != 0:
            motorsEnabledFlg = True
        else:
            motorsEnabledFlg = False

        if results & _STEPPER_STATUS_AT_HOME_SWITCH:
            homeAtHomeSwitchFlg = True
        else:
            homeAtHomeSwitchFlg = False

        return True, stoppedFlg, motorsEnabledFlg, homeAtHomeSwitchFlg


 
    #
    # get the count of communication errors
    #    Exit:   0 return if no errors, else count of errors returned
    #
    def getCommErrorCount(self):
        return self._commErrorCount


    # ---------------------------------------------------------------------------------
    #                         Public functions with units in Steps
    # ---------------------------------------------------------------------------------

    #
    # set the maximum speed with units in steps/second, this is the maximum speed reached  
    # while accelerating
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #          speedInStepsPerSecond = speed to accelerate up to, units in steps/second
    #  Exit:   True returned on success, else False
    #
    def setSpeedInStepsPerSecond(self, stepperNum: int, speedInStepsPerSecond: float):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False

        if (speedInStepsPerSecond < 0.05) or (speedInStepsPerSecond > 30000.0):
            return False

        self.__pushFltPoint2ToInt32(speedInStepsPerSecond)
        return self.__sendCommand(_CMD_DPiSTEPPER__SET_SPEED_IN_STEPS_PER_SEC + stepperNum)


    #
    # set the rate of acceleration with units in steps/second/second
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #          accelerationInStepsPerSecondPerSecond = rate of acceleration, units in 
    #            steps/second/second
    #  Exit:   True returned on success, else False
    #
    def setAccelerationInStepsPerSecondPerSecond(self, stepperNum: int, accelerationInStepsPerSecondPerSecond: float):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False

        if (accelerationInStepsPerSecondPerSecond < 0.05) or (accelerationInStepsPerSecondPerSecond > 30000.0):
            return False

        self.__pushFltPoint2ToInt32(accelerationInStepsPerSecondPerSecond)
        return self.__sendCommand(_CMD_DPiSTEPPER__SET_ACCEL_IN_STEPS_PSPS + stepperNum)



    #
    # set the current position of the motor in Steps, this does not move the motor
    # Note: This function should only be called when the motor is stopped
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #          currentPositionInSteps = the new position of the motor in steps
    #  Exit:   True returned on success, else False
    #
    def setCurrentPositionInSteps(self, stepperNum: int, currentPositionInSteps: int):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False

        dpiNetwork.pushInt32(currentPositionInSteps)
        return self.__sendCommand(_CMD_DPiSTEPPER__SET_CURRENT_P0SITION_IN_STEPS + stepperNum)



    #
    # get the current position of the motor in Steps, this functions is updated
    # while the motor moves
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #          currentPositionInSteps -> storage to return current position in
    #  Exit:   [0]: True returned on success, else False
    #          [1]: a signed motor position in steps returned
    #
    def getCurrentPositionInSteps(self, stepperNum: int):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False, 0

        if self.__sendCommand(_CMD_DPiSTEPPER__GET_CURRENT_POSITION_IN_STEPS + stepperNum) != True:
            return False, 0

        currentPositionInSteps = dpiNetwork.popInt32()
        return True, currentPositionInSteps


    #
    # move to an absolute position, units are in Steps
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #          absolutePositionToMoveToInSteps = signed absolute position to move to  
    #            in units of steps
    #          waitToFinishFlg = True to wait before returning until motor has stops
    #  Exit:   True returned on success, else False
    #
    def moveToAbsolutePositionInSteps(self, stepperNum: int, absolutePositionToMoveToInSteps: int, waitToFinishFlg: bool):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False

        dpiNetwork.pushInt32(absolutePositionToMoveToInSteps)
        results = self.__sendCommand(_CMD_DPiSTEPPER__MOVE_TO_ABS_POSITION_IN_STEPS + stepperNum)
        if results != True:
            return False
        
        if waitToFinishFlg:
            return self.waitUntilMotorStops(stepperNum)
        else:
            return True


    #
    # move a relative distance from the current position, distance to move is in Steps
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #          distanceToMoveInSteps = signed distance to move relative to the current  
    #            position in steps
    #          waitToFinishFlg = True to wait before returning until motor has stops
    #  Exit:   True returned on success, else False
    #
    def moveToRelativePositionInSteps(self, stepperNum: int, distanceToMoveInSteps: int, waitToFinishFlg: bool):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False

        dpiNetwork.pushInt32(distanceToMoveInSteps)
        results = self.__sendCommand(_CMD_DPiSTEPPER__MOVE_TO_REL_POSITION_IN_STEPS + stepperNum)
        if results != True:
            return False
        
        if waitToFinishFlg:
            return self.waitUntilMotorStops(stepperNum)
        else:
            return True



    #
    # Get the current velocity of the motor in steps/second.  This functions is 
    # updated while it accelerates up and down in speed.  This is not the desired  
    # speed, but the speed the motor should be moving at the time the function is  
    # called.  This is a signed value and is negative when the motor is moving 
    # backwards.  Note: This speed will be incorrect if the desired velocity is set 
    # faster than this library can generate steps, or if the load on the motor is too 
    # great for the amount of torque that it can generate.
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #  Exit:   [0]: True returned on success, else False
    #          [1]: current velocity in steps/second, signed
    #
    def getCurrentVelocityInStepsPerSecond(self, stepperNum: int):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False, 0
    
        results = self.__sendCommand(_CMD_DPiSTEPPER__GET_CURRENT_VELOCITY_IN_STEPS_PER_SEC + stepperNum)
        if results != True:
            return False, 0

        currentVelocity = self.__popInt32ToFltPoint2()
        return True, currentVelocity


    #
    # decelerate the stepper motor until it stops
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #  Exit:   True returned on success, else False
    #
    def decelerateToAStop(self, stepperNum: int):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False

        return self.__sendCommand(_CMD_DPiSTEPPER__DECELERATE_TO_A_STOP + stepperNum)


    #
    # emergency stop - just stop stepping the motor, expect steps will be lost so motor should be re-homed
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #  Exit:   True returned on success, else False
    #
    def emergencyStop(self, stepperNum: int):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False
    
        return self.__sendCommand(_CMD_DPiSTEPPER__EMERGENCY_STOP + stepperNum)


    #
    # home the motor by moving until the homing sensor is activated, then set the 
    # position to zero with units in steps
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #          directionTowardHome = 1 to move in a positive direction, -1 to move in 
    #            a negative directions 
    #          speedInStepsPerSecond = speed to accelerate up to while moving toward 
    #            home, units in steps/second
    #          maxDistanceToMoveInSteps = unsigned maximum distance to move toward 
    #            home before giving up
    #  Exit:   True returned if successful, else False
    #
    def moveToHomeInSteps(self, stepperNum: int, directionTowardHome: int,
                          speedInStepsPerSecond: float, maxDistanceToMoveInSteps: int):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False

        if not ((directionTowardHome == 1) or (directionTowardHome == -1)):
            return False

        #
        # enable the motors
        #
        if self.enableMotors(True) != True:
            return False

        #
        # set the homing speed
        #
        if self.setSpeedInStepsPerSecond(stepperNum, speedInStepsPerSecond) != True:
            return False
        if self.setAccelerationInStepsPerSecondPerSecond(stepperNum, speedInStepsPerSecond) != True:
            return False
         
        #
        # if not at the home switch alread, move toward it
        #
        results, stoppedFlg, __, homeAtHomeSwitchFlg = self.getStepperStatus(stepperNum)
        if results != True:
            return False

        if homeAtHomeSwitchFlg != True:
            #
            # move toward the home switch
            #
            if self.moveToRelativePositionInSteps(stepperNum, maxDistanceToMoveInSteps * directionTowardHome, False) != True:
                return False

            #
            # while motor is moving, check if limit switch is hit, or if travels the "max" distance
            #
            while True:
                results, stoppedFlg, __, homeAtHomeSwitchFlg = self.getStepperStatus(stepperNum)
                if results != True:
                    return False
                if stoppedFlg:
                    return False
                if homeAtHomeSwitchFlg:
                    break

            self.emergencyStop(stepperNum)
            sleep(.1)


        #
        # the switch has been detected, now move away from the switch
        #
        if self.moveToRelativePositionInSteps(stepperNum, -maxDistanceToMoveInSteps * directionTowardHome, False) != True:
            return False

        #
        # while motor is moving, check if limit switch is released, or if travels the "max" distance
        #
        while True:
            results, stoppedFlg, __, homeAtHomeSwitchFlg = self.getStepperStatus(stepperNum)
            if results != True:
                return False
            if stoppedFlg:
                return False
            if homeAtHomeSwitchFlg != True:
                break
    
        self.emergencyStop(stepperNum)
        sleep(.1)


        #
        # have now moved off the switch, move toward it again but slower
        #
        if self.setSpeedInStepsPerSecond(stepperNum, speedInStepsPerSecond/8) != True:
            return False
        if self.moveToRelativePositionInSteps(stepperNum, maxDistanceToMoveInSteps * directionTowardHome, False) != True:
            return False

        while True:
            results, stoppedFlg, __, homeAtHomeSwitchFlg = self.getStepperStatus(stepperNum)
            if results != True:
                return False
            if stoppedFlg:
                return False
            if homeAtHomeSwitchFlg:
                break

        self.emergencyStop(stepperNum)
        sleep(.1)
        

        #
        # successfully homed, set the current position to 0
        #
        if self.setCurrentPositionInSteps(stepperNum, 0) != True:
            return False

        return True


    # ---------------------------------------------------------------------------------
    #                     Public functions with units in Millimeters
    # ---------------------------------------------------------------------------------
    
    #
    # set the number of steps the per millimeters of motion
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #          stepsPerMillimeter = number of motor steps per millimeter of travel
    #
    def setStepsPerMillimeter(self, stepperNum: int, motorStepsPerMillimeter: float):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return
        self._stepsPerMillimeter[stepperNum] = motorStepsPerMillimeter


    #
    # set the current position in millimeters, this does not move the motor
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #          newPositionInMillimeters = value in MM to set current position
    #  Exit:   True returned on success, else False
    #
    def setCurrentPositionInMillimeters(self, stepperNum: int, newPositionInMillimeters: float):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False

        positionInSteps = int(round(newPositionInMillimeters * self._stepsPerMillimeter[stepperNum]))
        return self.setCurrentPositionInSteps(stepperNum, positionInSteps)


    #
    # get the current position in millimeters, this functions is updated
    # while the motor moves
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #  Exit:   [0]: True returned on success, else False
    #          [1]: a signed position in millimeters
    #
    def getCurrentPositionInMillimeters(self, stepperNum: int):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False, 0.0

        results, positionInSteps = self.getCurrentPositionInSteps(stepperNum)
        if results != True:
            return False

        return True, float(positionInSteps) / self._stepsPerMillimeter[stepperNum]
   

    #
    # set the maximum speed with units in millimeters/second, this is the maximum speed  
    # reached while accelerating
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #          speedInMillimetersPerSecond = speed to accelerate up to, units in 
    #            millimeters/second
    #  Exit:   True returned on success, else False
    #
    def setSpeedInMillimetersPerSecond(self, stepperNum: int, speedInMillimetersPerSecond: float):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False

        return self.setSpeedInStepsPerSecond(stepperNum, int(speedInMillimetersPerSecond * self._stepsPerMillimeter[stepperNum]))


    #
    # set the rate of acceleration, units in millimeters/second/second
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #  Enter:  accelerationInMillimetersPerSecondPerSecond = rate of acceleration,  
    #          units in millimeters/second/second
    #  Exit:   True returned on success, else False
    #
    def setAccelerationInMillimetersPerSecondPerSecond(self, stepperNum: int, accelerationInMillimetersPerSecondPerSecond: float):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False

        return self.setAccelerationInStepsPerSecondPerSecond(stepperNum,
                    int(accelerationInMillimetersPerSecondPerSecond * self._stepsPerMillimeter[stepperNum]))


    #
    # move to an absolute position, units are in millimeters
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #          absolutePositionToMoveToInMillimeters = signed absolute position to move
    #          waitToFinishFlg = True to wait before returning until motor has stops
    #  Exit:   True returned on success, else False
    #
    def moveToAbsolutePositionInMillimeters(self, stepperNum: int, absolutePositionToMoveToInMillimeters: float, waitToFinishFlg: bool):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False

        return self.moveToAbsolutePositionInSteps(stepperNum, 
                  int(round(absolutePositionToMoveToInMillimeters * self._stepsPerMillimeter[stepperNum])), waitToFinishFlg)

 
    #
    # move a relative distance from the current position, distance to move is in millimeters
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #          distanceToMoveInMillimeters = signed distance to move relative
    #          waitToFinishFlg = True to wait before returning until motor has stops
    #  Exit:   True returned on success, else False
    #
    def moveToRelativePositionInMillimeters(self, stepperNum: int, distanceToMoveInMillimeters: float, waitToFinishFlg: bool):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False

        return self.moveToRelativePositionInSteps(stepperNum, 
                  int(round(distanceToMoveInMillimeters * self._stepsPerMillimeter[stepperNum])), waitToFinishFlg)


    #
    # Get the current velocity of the motor in Millimeters/second.  This functions 
    # is updated while it accelerates up and down in speed.  This is not the desired  
    # speed, but the speed the motor should be moving at the time the function is  
    # called.  This is a signed value and is negative when the motor is moving 
    # backwards.  Note: This speed will be incorrect if the desired velocity is set 
    # faster than this library can generate steps, or if the load on the motor is too 
    # great for the amount of torque that it can generate.
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #  Exit:   [0]: True returned on success, else False
    #          [1]: current velocity in millimeters/second, signed
    #
    def getCurrentVelocityInMillimetersPerSecond(self, stepperNum: int):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False, 0
    
        results, velocityInStepsPerSec = self.getCurrentVelocityInStepsPerSecond(stepperNum)
        if results != True:
            return False, 0

        return True, velocityInStepsPerSec / self._stepsPerMillimeter[stepperNum]


    #
    # home the motor by moving until the homing sensor is activated, then set the 
    # position to zero, with units in Millimeters
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #          directionTowardHome = 1 to move in a positive direction, -1 to move in 
    #            a negative directions 
    #          speedInMillimetersPerSecond = speed to accelerate up to while moving 
    #            toward home, units in millimeters/second
    #          maxDistanceToMoveInMillimeters = unsigned maximum distance to move 
    #            toward home before giving up
    #  Exit:   True returned on success, else False
    #
    def moveToHomeInMillimeters(self, stepperNum: int, directionTowardHome: int, 
       speedInMillimetersPerSecond: float, maxDistanceToMoveInMillimeters: float):
        
        return self.moveToHomeInSteps(stepperNum, directionTowardHome,
                                       int(speedInMillimetersPerSecond * self._stepsPerMillimeter[stepperNum]),
                                       int (maxDistanceToMoveInMillimeters * self._stepsPerMillimeter[stepperNum]))


    # ---------------------------------------------------------------------------------
    #                     Public functions with units in Revolutions
    # ---------------------------------------------------------------------------------

    #
    # set the number of steps per Revolutions
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #          motorStepPerRevolution = number of motor steps per revolution of travel
    #
    def setStepsPerRevolution(self, stepperNum: int, motorStepPerRevolution: float):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return
        self._stepsPerRevolution[stepperNum] = motorStepPerRevolution


    #
    # set the current position in revolutions, this does not move the motor
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #          newPositionInRevolutions = value in Revolutions to set current position
    #  Exit:   True returned on success, else False
    #
    def setCurrentPositionInRevolutions(self, stepperNum: int, newPositionInRevolutions: float):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False

        positionInSteps = int(round(newPositionInRevolutions * self._stepsPerRevolution[stepperNum]))
        return self.setCurrentPositionInSteps(stepperNum, positionInSteps)


    #
    # get the current position in revolutions, this functions is updated
    # while the motor moves
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #  Exit:   [0]: True returned on success, else False
    #          [1]: a signed position in revolutions
    #
    def getCurrentPositionInRevolutions(self, stepperNum: int):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False, 0.0

        results, positionInSteps = self.getCurrentPositionInSteps(stepperNum)
        if results != True:
            return False

        return True, float(positionInSteps) / self._stepsPerRevolution[stepperNum]
   

    #
    # set the maximum speed with units in revolutions/second, this is the maximum speed  
    # reached while accelerating
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #          speedInRevolutionsPerSecond = speed to accelerate up to, units in 
    #            revolutions/second
    #  Exit:   True returned on success, else False
    #
    def setSpeedInRevolutionsPerSecond(self, stepperNum: int, speedInRevolutionsPerSecond: float):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False

        return self.setSpeedInStepsPerSecond(stepperNum, int(speedInRevolutionsPerSecond * self._stepsPerRevolution[stepperNum]))


    #
    # set the rate of acceleration, units in revolutions/second/second
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #  Enter:  accelerationInRevolutionsPerSecondPerSecond = rate of acceleration,  
    #          units in revolutions/second/second
    #  Exit:   True returned on success, else False
    #
    def setAccelerationInRevolutionsPerSecondPerSecond(self, stepperNum: int, accelerationInRevolutionsPerSecondPerSecond: float):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False

        return self.setAccelerationInStepsPerSecondPerSecond(stepperNum,
                    int(accelerationInRevolutionsPerSecondPerSecond * self._stepsPerRevolution[stepperNum]))


    #
    # move to an absolute position, units are in revolutions
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #          absolutePositionToMoveToInRevolutions = signed absolute position to move
    #          waitToFinishFlg = True to wait before returning until motor has stops
    #  Exit:   True returned on success, else False
    #
    def moveToAbsolutePositionInRevolutions(self, stepperNum: int, absolutePositionToMoveToInRevolutions: float, waitToFinishFlg: bool):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False

        return self.moveToAbsolutePositionInSteps(stepperNum, 
                  int(round(absolutePositionToMoveToInRevolutions * self._stepsPerRevolution[stepperNum])), waitToFinishFlg)

 
    #
    # move a relative distance from the current position, distance to move is in revolutions
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #          distanceToMoveInRevolutions = signed distance to move relative
    #          waitToFinishFlg = True to wait before returning until motor has stops
    #  Exit:   True returned on success, else False
    #
    def moveToRelativePositionInRevolutions(self, stepperNum: int, distanceToMoveInRevolutions: float, waitToFinishFlg: bool):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False

        return self.moveToRelativePositionInSteps(stepperNum, 
                  int(round(distanceToMoveInRevolutions * self._stepsPerRevolution[stepperNum])), waitToFinishFlg)


    #
    # Get the current velocity of the motor in Revolutions/second.  This functions 
    # is updated while it accelerates up and down in speed.  This is not the desired  
    # speed, but the speed the motor should be moving at the time the function is  
    # called.  This is a signed value and is negative when the motor is moving 
    # backwards.  Note: This speed will be incorrect if the desired velocity is set 
    # faster than this library can generate steps, or if the load on the motor is too 
    # great for the amount of torque that it can generate.
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #  Exit:   [0]: True returned on success, else False
    #          [1]: current velocity in revolutions/second, signed
    #
    def getCurrentVelocityInRevolutionsPerSecond(self, stepperNum: int):
        if (stepperNum < 0) or (stepperNum >= _NUMBER_OF_DPi_STEPPER_DRIVERS):
            return False, 0
    
        results, velocityInStepsPerSec = self.getCurrentVelocityInStepsPerSecond(stepperNum)
        if results != True:
            return False, 0

        return True, velocityInStepsPerSec / self._stepsPerRevolution[stepperNum]


    #
    # home the motor by moving until the homing sensor is activated, then set the 
    # position to zero, with units in Revolutions
    #  Enter:  stepperNum = stepper driver number (0 - 2)
    #          directionTowardHome = 1 to move in a positive direction, -1 to move in 
    #            a negative directions 
    #          speedInRevolutionsPerSecond = speed to accelerate up to while moving 
    #            toward home, units in revolutions/second
    #          maxDistanceToMoveInRevolutions = unsigned maximum distance to move 
    #            toward home before giving up
    #  Exit:   True returned on success, else False
    #
    def moveToHomeInRevolutions(self, stepperNum: int, directionTowardHome: int, 
       speedInRevolutionsPerSecond: float, maxDistanceToMoveInRevolutions: float):
        
        return self.moveToHomeInSteps(stepperNum, directionTowardHome,
                                       int(speedInRevolutionsPerSecond * self._stepsPerRevolution[stepperNum]),
                                       int (maxDistanceToMoveInRevolutions * self._stepsPerRevolution[stepperNum]))

