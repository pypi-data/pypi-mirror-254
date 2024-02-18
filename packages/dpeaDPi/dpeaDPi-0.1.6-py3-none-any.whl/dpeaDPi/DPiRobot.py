#      ******************************************************************
#      *                                                                *
#      *                         DPiRobot Libary                        *
#      *                                                                *
#      *            Stan Reifel                     8/24/2022           *
#      *                                                                *
#      ******************************************************************

from dpeaDPi.DPiNetwork import DPiNetwork
dpiNetwork = DPiNetwork()


#
# DPiNetwork DPiRobot commands  
#
_CMD_DPiROBOT__PING                                            = 0x00   
_CMD_DPiROBOT__INITIALIZE                                      = 0x01 
_CMD_DPiROBOT__GET_ROBOT_STATE                                 = 0x02    # robot_GetRobotState
_CMD_DPiROBOT__DISABLE_ROBOT_MOTORS                            = 0x03    # enable / disable the stepper motors
_CMD_DPiROBOT__HOME_ROBOT                                      = 0x04    # robot_prepareForMotion / HomeRobot
_CMD_DPiROBOT__ADD_WAYPOINT                                    = 0x05    # robot_AddWaypoint
_CMD_DPiROBOT__ADD_WAYPOINT_ROBOT_COORDS                       = 0x06    # robot_AddWaypoint_RobotCoords
_CMD_DPiROBOT__CALCULATE_CURRENT_POSITION                      = 0x07    # robot_GetCurrentPosition
_CMD_DPiROBOT__CALCULATE_CURRENT_POSITION_ROBOT_COORDS         = 0x08    # robot_GetCurrentPosition_RobotCoords
_CMD_DPiROBOT__GET_CURRENT_POSITION                            = 0x09
_CMD_DPiROBOT__BUFFER_WAYPOINTS_BEFORE_STARTING                = 0X0a

_CMD_DPiROBOT__SET_ROBOT_TYPE                                  = 0x11    # robot_SetRobotType
_CMD_DPiROBOT__SET_ROBOT_DEFAULT_ACCELERATION                  = 0x12    # robot_SetRobotDefaultAcceleration
_CMD_DPiROBOT__SET_ROBOT_DEFAULT_JUNCTION_DEVIATION            = 0x13    # robot_SetRobotDefaultJunctionDeviation
_CMD_DPiROBOT__SET_ROBOT_MIN_MAX_X                             = 0x14    # robot_SetRobotMinMaxX
_CMD_DPiROBOT__SET_ROBOT_MIN_MAX_Y                             = 0x15    # robot_SetRobotMinMaxY
_CMD_DPiROBOT__SET_ROBOT_MIN_MAX_Z                             = 0x16    # robot_SetRobotMinMaxZ
_CMD_DPiROBOT__SET_HOMING_SPEED                                = 0x17    # robot_SetHomingSpeed
_CMD_DPiROBOT__SET_HOMING_METHOD                               = 0x18    # robot_SetHomingMethod
_CMD_DPiROBOT__SET_MAX_HOMING_DISTANCE_DEG_OR_MM               = 0x19    # robot_SetMaxHomingDistanceDegOrMM

_CMD_DPiROBOT__LIN_DELTA_SET_STEPS_PER_MM                      = 0x21    # robot_LinDelta_SetStepsPerMM
_CMD_DPiROBOT__LIN_DELTA_SET_ARM_LENGTH                        = 0x22    # robot_LinDelta_SetArmLength
_CMD_DPiROBOT__LIN_DELTA_SET_TOWER_AND_END_EFFECTOR_RADIUS     = 0x23    # robot_LinDelta_SetTowerAndEndEffectorRadius
_CMD_DPiROBOT__LIN_DELTA_SET_MAX_JOINT_POS                     = 0x24    # robot_LinDelta_SetMaxJointPos

_CMD_DPiROBOT__ROT_DELTA_SET_STEPS_PER_DEGREE                  = 0x31    # robot_RotDelta_SetStepsPerDegree
_CMD_DPiROBOT__ROT_DELTA_SET_ARM_LENGTH                        = 0x32    # robot_RotDelta_SetArmLengths
_CMD_DPiROBOT__ROT_DELTA_SET_BASE_AND_END_EFFECTOR_RADIUS      = 0x33    # robot_RotDelta_SetBaseAndEndEffectorRadius
_CMD_DPiROBOT__ROT_DELTA_SET_UPPER_ARM_HOME_ANGLE_DEGREES      = 0x34    # robot_RotDelta_SetUpperArmHomeAngleDegrees
_CMD_DPiROBOT__ROT_DELTA_SET_MIN_MAX_JOINT_ANGLES              = 0x35    # robot_RotDelta_SetMinMaxJointAngles

_CMD_DPiROBOT__MOTOR_DRIVER_SET_DRIVER_TYPE                    = 0x41    # motorDriver_SetDriverType
_CMD_DPiROBOT__MOTOR_DRIVER_SET_DRIVER_MICROSTEPPING           = 0x42    # motorDriver_SetDriverMicrostepping
_CMD_DPiROBOT__MOTOR_DRIVER_SET_REVERSE_DIRECTION_FLAG         = 0x43    # motorDriver_SetReverseStepDirectionFlag


#
# other constants used by this class
#
_DPiNETWORK_TIMEOUT_PERIOD_MS = 8       # 3/10/2023 changed from 5 to 8ms
_DPiNETWORK_BASE_ADDRESS = 0x14


class DPiRobot:
    #
    # values for CMD_DPiROBOT__SET_ROBOT_TYPE
    #
    ROBOT_TYPE_ROTATIONAL_DELTA = 1
    ROBOT_TYPE_LINEAR_DELTA = 2
    ROBOT_TYPE_CARTESIAN = 3

    #
    # values for motorDriverType
    #
    MOTOR_DRIVER_TYPE_DRV8825 = 1
    MOTOR_DRIVER_TYPE_DM542T = 2

    #
    # values for CMD_DPiROBOT__SET_HOMING_METHOD
    #
    HOMING_METHOD_LIMIT_SWITCHES = 1
    HOMING_METHOD_NONE = 3

    #
    # values for CMD_DPiROBOT__GET_ROBOT_STATE
    #
    STATE_COMMUNICATION_FAILURE = 1             # getting the robot's state failed
    STATE_NOT_READY = 2                         # robot is not ready to accept commands from the host
    STATE_MOTORS_DISABLED = 3                   # motors are disabled
    STATE_NOT_HOMED = 4                         # motors enabled but robot not homed (either hasn't homed or homing failed)
    STATE_HOMING = 5                            # robot is running the homing procedure 
    STATE_STOPPED = 6                           # robot is stopped, waiting for waypoints from the host
    STATE_PREPARING_TO_MOVE = 7                 # robot has received 1 or more waypoints but hasn't started moving yet
    STATE_MOVING = 8                            # moving to next waypoint
    STATE_E_STOPPED_PRESSED = 9                 # E-Stop button is pressed
    STATE_WAYPOINT_BUFFER_FULL_FLAG = 0x80      # this bit set in status byte if waypoint buffer is full

    #
    # status values for CMD_DPiROBOT__GET_CURRENT_POSITION
    #
    GET_CURRENT_POSITION_NOT_READY = 1
    GET_CURRENT_POSITION_UNKNOWN = 2
    GET_CURRENT_POSITION_READY = 3


    #
    # constructor for the DPiRobot class
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
    # send a command to the DPiRobot, command's additional data must have already been "Pushed". 
    # After this function returns data from the device is retrieved by "Popping"
    #    Enter:  command = command byte
    #    Exit:   True returned on success, else False
    #
    def __sendCommand(self, command: int):
        (results, failedCount) = dpiNetwork.sendCommand(self._slaveAddress, command, _DPiNETWORK_TIMEOUT_PERIOD_MS)
        self._commErrorCount += failedCount;
        return results

    #
    # push a float with 0 digits right of the decimal, as an int32_t, to the transmit buffer 
    #  Enter:  float value 
    #
    def __pushFltPoint0ToInt32(self, value: float):
        dpiNetwork.pushInt32(int(round(value)))

    #
    # push a float with 3 digits right of the decimal, as an int32_t, to the transmit buffer
    #  Enter:  float value 
    #
    def __pushFltPoint3ToInt32(self, value: float):
        dpiNetwork.pushInt32(int(round(value * 1000.0)))

    #
    # push a float with 1 digit right of the decimal, as an int16_t, to the transmit buffer
    #
    def __pushFltPoint1ToInt16(self, value: float):
        dpiNetwork.pushInt16(int(round(value * 10.0)))

    #
    # pop an int16_t, to a float with 1 digits right of the decimal, from the receive buffer
    #
    def __popInt16ToFltPoint1(self):
        return float(dpiNetwork.popInt16()) / 10.0

 
    # ---------------------------------------------------------------------------------
    #                     Public setup and configuration functions 
    # ---------------------------------------------------------------------------------

    #
    # set the DPiRobot board number
    #    Enter:  boardNumber = DPiRobot board number (0 - 3)
    #
    def setBoardNumber(self, boardNumber: int):
        self._slaveAddress = _DPiNETWORK_BASE_ADDRESS + boardNumber
        

    #
    # ping the board
    #    Exit:   True returned on success, else False
    #
    def ping(self):
        return self.__sendCommand(_CMD_DPiROBOT__PING)


    #
    # initialize the board to its "power on" configuration
    #    Exit:   True returned on success, else False
    #
    def initialize(self):
        return self.__sendCommand(_CMD_DPiROBOT__INITIALIZE)


    #
    # disable the stepper motors
    #    Exit:   True returned on success, else False
    #
    def disableMotors(self):
        return self.__sendCommand(_CMD_DPiROBOT__DISABLE_ROBOT_MOTORS)


    #
    # get the count of communication errors
    #    Exit:   0 return if no errors, else count of errors returned
    #
    def getCommErrorCount(self):
        return self._commErrorCount


    # ---------------------------------------------------------------------------------
    #           Public functions for getting the robot's status and position
    # ---------------------------------------------------------------------------------

    #
    # get the robot's status
    #  Exit:   [0]: True returned on success, else False
    #          [1]: Robot status:
    #                  .STATE_NOT_READY = robot is not ready to accept commands from the host
    #                  .STATE_MOTORS_DISABLED = motors are disabled
    #                  .STATE_NOT_HOMED = motors enabled but robot not homed (either hasn't homed or homing failed)
    #                  .STATE_HOMING = robot is running the homing procedure 
    #                  .STATE_STOPPED = robot is stopped, waiting for waypoints from the hose
    #                  .STATE_PREPARING_TO_MOVE = robot has received 1 or more waypoints but hasn't started moving yet
    #                  .STATE_MOVING = moving to next waypoint
    #
    def getRobotStatus(self):
        if self.__sendCommand(_CMD_DPiROBOT__GET_ROBOT_STATE) != True:
            return False, self.STATE_COMMUNICATION_FAILURE

        return True, dpiNetwork.popUint8() & 0x7f


    #
    # get the robot's status along with waypoint buffer full flag
    #  Exit:   [0]: True returned on success, else False
    #          [1]: Robot status:
    #                  .STATE_COMMUNICATION_FAILURE = getting the robot's state failed
    #                  .STATE_NOT_READY = robot is not ready to accept commands from the host
    #                  .STATE_MOTORS_DISABLED = motors are disabled
    #                  .STATE_NOT_HOMED = motors enabled but robot not homed (either hasn't homed or homing failed)
    #                  .STATE_HOMING = robot is running the homing procedure 
    #                  .STATE_STOPPED = robot is stopped, waiting for waypoints from the hose
    #                  .STATE_PREPARING_TO_MOVE = robot has received 1 or more waypoints but hasn't started moving yet
    #                  .STATE_MOVING = moving to next waypoint
    #          [2]: True returned waypoint buffer is full
    #
    def getRobotStatusWithWaypointBufferFullFlg(self):
        if self.__sendCommand(_CMD_DPiROBOT__GET_ROBOT_STATE) != True:
            return False, self.STATE_COMMUNICATION_FAILURE, False

        status = dpiNetwork.popUint8()
        if status & 0x80 != 0:
            waypointBufferFulFlg = True
        else:
            waypointBufferFulFlg = False
            
        status = status & 0x7f
        
        return True, status, waypointBufferFulFlg


    #
    # get robot's current absolute position in the User's Cartesian Coordinates System, these values 
    # updates while in motion, values are signed with units in millimeters
    # Note: This command executes in ~3ms on a Pi4 (1.4ms with the C library)
    #  Exit:   [0]: True returned on success, false on communication error or the robot doesn't know its position
    #          [1]: X coordinate
    #          [2]: Y coordinate
    #          [3]: Z coordinate
    #
    def getCurrentPosition(self):
        #
        # start by requesting that the robot calculates its position
        #
        if self.__sendCommand(_CMD_DPiROBOT__CALCULATE_CURRENT_POSITION) != True:
            return False, 0, 0, 0

        #
        # get the position from the robot, looping until the data is ready
        #
        for _i in range(6):
            if self.__sendCommand(_CMD_DPiROBOT__GET_CURRENT_POSITION) != True:
                return False, 0, 0, 0

            X =  self.__popInt16ToFltPoint1()
            Y =  self.__popInt16ToFltPoint1()
            Z =  self.__popInt16ToFltPoint1()
            getPositionStatus = dpiNetwork.popInt8()

            if getPositionStatus == self.GET_CURRENT_POSITION_READY:
                return True, X, Y, Z

            if getPositionStatus == self.GET_CURRENT_POSITION_UNKNOWN:
                return False, 0, 0, 0

        return False, 0, 0, 0


    #
    # get robot's current absolute position in the Robot's Cartesian Coordinates System, these values 
    # updates while in motion, values are signed with units in millimeters
    # Note: This command executes in ~3ms on a Pi4 (1.4ms with the C library)
    #  Exit:   [0]: True returned on success, false on communication error or the robot doesn't know its position
    #          [1]: X coordinate
    #          [2]: Y coordinate
    #          [3]: Z coordinate
    #
    def getCurrentPosition_RobotCoords(self):
        #
        # start by requesting that the robot calculates its position
        #
        if self.__sendCommand(_CMD_DPiROBOT__CALCULATE_CURRENT_POSITION_ROBOT_COORDS) != True:
            return False, 0, 0, 0

        #
        # get the position from the robot, looping until the data is ready
        #
        for _i in range(6):
            if self.__sendCommand(_CMD_DPiROBOT__GET_CURRENT_POSITION) != True:
                return False, 0, 0, 0

            X =  self.__popInt16ToFltPoint1()
            Y =  self.__popInt16ToFltPoint1()
            Z =  self.__popInt16ToFltPoint1()
            getPositionStatus = dpiNetwork.popInt8()

            if getPositionStatus == self.GET_CURRENT_POSITION_READY:
                return True, X, Y, Z

            if getPositionStatus == self.GET_CURRENT_POSITION_UNKNOWN:
                return False, 0, 0, 0

        return False, 0, 0, 0
 

    # ---------------------------------------------------------------------------------
    #                       Public functions that control the robot
    # ---------------------------------------------------------------------------------

    #
    # add a waypoint (using the User's Cartesian Coordinate System). This will return 
    # right away unless the waypoint buffer is full (in which case it will busy-wait).
    # Note: this command executes in ~4ms on a Pi4 (2.8ms for the C version of this library)
    #    Enter:  X, Y, Z = position to move to, values are signed with units in 
    #               millimeters  (−3276.8mm to 3276.7mm)
    #            speed = speed to travel in mm/sec
    #    Exit:   True returned on success, else False
    #
    def addWaypoint(self, X: float, Y: float, Z: float, speed: float):
        #
        # verify values are in range
        #
        if (X < -3275) or (X > 3275) or (Y < -3275) or (Y > 3275) or (Z < -3275) or (Z > 3275):
            return False
        
        if (speed < 0.001) or (speed > 3275):
            return False
        
        #
        # loop if waypoint buffer is full
        #
        while True:
            #
            # get the robot's status including if the waypoint buffer is full
            #
            results, _status, waypointBufferFullFlg = self.getRobotStatusWithWaypointBufferFullFlg()
            if results != True:
                return False

            #
            # stop waiting if the waypoint buffer is not full
            #
            if waypointBufferFullFlg == False:
                break

        #
        # there is room in the buffer, send the waypoint now
        #
        self.__pushFltPoint1ToInt16(X)
        self.__pushFltPoint1ToInt16(Y)
        self.__pushFltPoint1ToInt16(Z)
        self.__pushFltPoint1ToInt16(speed)
        return self.__sendCommand(_CMD_DPiROBOT__ADD_WAYPOINT)


    #
    # add a waypoint (using the Robot's Cartesian Coordinate System). This will return 
    # right away unless the waypoint buffer is full (in which case it will busy-wait).
    # Note: this command executes in ~4ms on a Pi4 
    #    Enter:  X, Y, Z = position to move to, values are signed with units in 
    #               millimeters  (−3276.8mm to 3276.7mm)
    #            speed = speed to travel in mm/sec
    #    Exit:   True returned on success, else False
    #
    def addWaypoint_RobotCoords(self, X: float, Y: float, Z: float, speed: float):
        #
        # verify values are in range
        #
        if (X < -3275) or (X > 3275) or (Y < -3275) or (Y > 3275) or (Z < -3275) or (Z > 3275):
            return False
        
        if (speed < 0.001) or (speed > 3275):
            return False

        #
        # loop if waypoint buffer is full
        #
        while True:
            #
            # get the robot's status including if the waypoint buffer is full
            #
            results, _status, waypointBufferFullFlg = self.getRobotStatusWithWaypointBufferFullFlg()
            if results != True:
                return False

            #
            # stop waiting if the waypoint buffer is not full
            #
            if waypointBufferFullFlg == False:
                break

        #
        # there is room in the buffer, send the waypoint now
        #
        self.__pushFltPoint1ToInt16(X)
        self.__pushFltPoint1ToInt16(Y)
        self.__pushFltPoint1ToInt16(Z)
        self.__pushFltPoint1ToInt16(speed)
        return self.__sendCommand(_CMD_DPiROBOT__ADD_WAYPOINT_ROBOT_COORDS)


    #
    # in some situations buffering waypoints can result in a more "fluid" motion,
    # preventing the robot from briefly stopping between each point as it moves  
    # along a continous path; to use: 1) while the robot is stopped, call this
    # function to enable buffering  2) send the robot all the waypoints along
    # the path  3)after sending the final waypoint immediately call this function
    # again to stop buffering.
    #
    def bufferWaypointsBeforeStartingToMove(self, bufferFlg: bool):
        dpiNetwork.pushUint8(bufferFlg)
        return self.__sendCommand(_CMD_DPiROBOT__BUFFER_WAYPOINTS_BEFORE_STARTING)


    #
    # wait while the robot is moving, return when it has stopped
    #    Exit:   True returned on success, else False
    #
    def waitWhileRobotIsMoving(self):
        self.bufferWaypointsBeforeStartingToMove(False)      # stop buffering waypoints if that was enabled

        while True:
            #
            # get the robot's status
            #
            results, robotStatus = self.getRobotStatus()
            if results != True:
                return False

            #
            # return if status indicates the robot has stopped
            #
            if not ((robotStatus == self.STATE_MOVING) or (robotStatus == self.STATE_PREPARING_TO_MOVE) or
                    (robotStatus == self.STATE_HOMING)):
                return True


    #
    # home the robot, if motors are disabled then enable them first
    #    Enter:  alwaysHomeFlg = True to always run homing procedure
    #                          = False to only run homing procedure if needed
    #    Exit:   True returned on success, else False
    #
    def homeRobot(self, alwaysHomeFlg: bool):
        #
        # verify communication with the robot is working
        #
        results, robotStatus = self.getRobotStatus()
        if (results != True) or (robotStatus == self.STATE_NOT_READY):
            return False

        #
        # start the robot homing
        #
        dpiNetwork.pushUint8(alwaysHomeFlg)
        if self.__sendCommand(_CMD_DPiROBOT__HOME_ROBOT) != True:
            return False

        #
        # check the robot's status until homing is complete
        #
        while True:
            results, robotStatus = self.getRobotStatus()
            if results != True:
                return False

            if robotStatus != self.STATE_HOMING:
                break

        #
        # check if homing failed
        #
        if robotStatus != self.STATE_STOPPED:
            return False

        #
        # homing successful
        #
        return True

 

    # ---------------------------------------------------------------------------------
    #                     Public functions configuring the robot
    # ---------------------------------------------------------------------------------

    #
    # set the robot type and initialize it
    #  Enter:  typeOfRobot = ROBOT_TYPE_ROTATIONAL_DELTA, ROBOT_TYPE_LINEAR_DELTA, ROBOT_TYPE_CARTESIAN...
    #  Exit:   true returned on success, else false
    #
    def setRobotType(self, typeOfRobot: int):
        dpiNetwork.pushUint8(typeOfRobot)
        return self.__sendCommand(_CMD_DPiROBOT__SET_ROBOT_TYPE)


    # 
    # for all robot types: set default acceleration
    #   Enter:  acceleration = steps per second per second
    #   Exit:   true returned on success, else false
    # 
    def setRobotDefaultAcceleration(self, acceleration: float):
        self.__pushFltPoint0ToInt32(acceleration)
        return self.__sendCommand(_CMD_DPiROBOT__SET_ROBOT_DEFAULT_ACCELERATION)


    # 
    # for all robot types: set default junction deviation 
    # The "Junction Deviation" defines how much the motors will slow down when changing 
    # direction.  Small changes in direction typically need only a small reduction in speed, 
    # while sharp turns require a much larger reduction in speed.  For example, if the path 
    # between two waypoints are at a right angle to each other, the combined motion of all 
    # the motors must slow down significately to make this sharp turn.  Setting the
    # Junction Deviation constant controls how much the motors will slow down as they 
    # head into, and out of turns.  Effectively this sets the cornering speed.  But
    # this does not "round" corners, in that it will always complete all steps to reach 
    # the exact waypoint coordinate.  The default value is set around 1.0.  The larger
    # the value, the less it slows down when changing direction.  When moving a large
    # mass, or with a very ridge system, a smaller number may be needed.  If the number
    # is too large, it may cause a loss of steps as sharp turns are made.  Units are in 
    # steps. This value can only be changed when all motion is stopped.
    # 
    def setRobotDefaultJunctionDeviation(self, junctionDeviation: float):
        self.__pushFltPoint0ToInt32(junctionDeviation);
        return self.__sendCommand(_CMD_DPiROBOT__SET_ROBOT_DEFAULT_JUNCTION_DEVIATION)


    # 
    # for all robot types: set minimum and maximum X
    #  Enter:  minimumX, maximumX = min and max values of X in millimeters (−3276.8mm to 3276.7mm)
    #  Exit:   true returned on success, else false
    # 
    def setRobotMinMaxX(self, minimumX: float, maximumX: float):
        self.__pushFltPoint1ToInt16(minimumX)
        self.__pushFltPoint1ToInt16(maximumX)
        return self.__sendCommand(_CMD_DPiROBOT__SET_ROBOT_MIN_MAX_X)


    # 
    # for all robot types: set minimum and maximum Y
    #  Enter:  minimumY, maximumY = min and max values of Y in millimeters (−3276.8mm to 3276.7mm)
    #  Exit:   true returned on success, else false
    # 
    def setRobotMinMaxY(self, minimumY: float, maximumY: float):
        self.__pushFltPoint1ToInt16(minimumY)
        self.__pushFltPoint1ToInt16(maximumY)
        return self.__sendCommand(_CMD_DPiROBOT__SET_ROBOT_MIN_MAX_Y)


    # 
    # for all robot types: set minimum and maximum Z
    #  Enter:  minimumZ, maximumZ = min and max values of Z in millimeters (−3276.8mm to 3276.7mm)
    #  Exit:   true returned on success, else false
    # 
    def setRobotMinMaxZ(self, minimumZ: float, maximumZ: float):
        self.__pushFltPoint1ToInt16(minimumZ)
        self.__pushFltPoint1ToInt16(maximumZ)
        return self.__sendCommand(_CMD_DPiROBOT__SET_ROBOT_MIN_MAX_Z)


    # 
    # for all robot types: set homing speed
    #  Enter:  speedDegOrMMPerSec = speed in: deg/sec for rot delta robots, mm/sec for linear delta robots, 
    #                               mm/sec for cartesian robots (0 to 2000mm/sec)
    #  Exit:   true returned on success, else false
    # 
    def setHomingSpeed(self, speedDegOrMMPerSec: float):
        self.__pushFltPoint1ToInt16(speedDegOrMMPerSec)
        return self.__sendCommand(_CMD_DPiROBOT__SET_HOMING_SPEED)


    # 
    # set the homing method type
    #  Enter:  homingMethod = ROBOT_HOMING_METHOD_LIMIT_SWITCHES, ROBOT_HOMING_METHOD_STALL_DETECTION, ROBOT_HOMING_METHOD_NONE...
    #  Exit:   true returned on success, else false
    # 
    def setHomingMethod(self, homingMethod: int):
        dpiNetwork.pushUint8(homingMethod)
        return self.__sendCommand(_CMD_DPiROBOT__SET_HOMING_METHOD)


    # 
    # for all robot types: set maximum distance to move when homing
    #  Enter:  maxDistanceDegOrMM = maximum distance to move when homing (Degrees or MM)  (0 to 3276.7)
    #  Exit:   true returned on success, else false
    # 
    def setMaxHomingDistanceDegOrMM(self, maxDistanceDegOrMM: float):
        self.__pushFltPoint1ToInt16(maxDistanceDegOrMM)
        return self.__sendCommand(_CMD_DPiROBOT__SET_MAX_HOMING_DISTANCE_DEG_OR_MM)


    # 
    #  linear delta robot: set steps/mm
    #  Enter:  stepsPerMM = number of steps per MM of motion for the arm tower
    # 
    def linDelta_SetStepsPerMM(self, stepsPerMM: float):
        self.__pushFltPoint3ToInt32(stepsPerMM)
        return self.__sendCommand(_CMD_DPiROBOT__LIN_DELTA_SET_STEPS_PER_MM)


    # 
    # set linear delta robot: arm length
    #  Enter:  armLengthMM = length in mm of arm
    #  Exit:   true returned on success, else false
    # 
    def linDelta_SetArmLength(self, armLengthMM: float):
        self.__pushFltPoint3ToInt32(armLengthMM)
        return self.__sendCommand(_CMD_DPiROBOT__LIN_DELTA_SET_ARM_LENGTH)


    # 
    # set linear delta robot: raduis of the robot's tower and end effector
    #  Enter:   towerRadiusMM = radius of the tower, from its center to the rotational joints of the arms
    #           endEffectorRadiusMM = radius of the end effector, from its center to the rotational joints of the lower arm
    #  Exit:   true returned on success, else false
    # 
    def linDelta_SetTowerAndEndEffectorRadius(self, towerRadiusMM: float, endEffectorRadiusMM: float):
        self.__pushFltPoint3ToInt32(towerRadiusMM);
        self.__pushFltPoint3ToInt32(endEffectorRadiusMM)
        return self.__sendCommand(_CMD_DPiROBOT__LIN_DELTA_SET_TOWER_AND_END_EFFECTOR_RADIUS)


    # 
    # set linear delta robot: maximum arm tower position
    #  Enter:  maximumJointPos = maximum allowed pos of the arm tower
    #  Exit:   true returned on success, else false
    # 
    def linDelta_SetMaxJointPos(self, maximumJointPos: float):
        self.__pushFltPoint3ToInt32(maximumJointPos)
        return self.__sendCommand(_CMD_DPiROBOT__LIN_DELTA_SET_MAX_JOINT_POS)



    # 
    #  set rotational delta robot: steps/degree
    #  Enter:  stepsPerDegree = number of steps per degree of motion for the upper arm
    #  Exit:   true returned on success, else false
    # 
    def rotDelta_SetStepsPerDegree(self, stepsPerDegree: float):
        self.__pushFltPoint3ToInt32(stepsPerDegree)
        return self.__sendCommand(_CMD_DPiROBOT__ROT_DELTA_SET_STEPS_PER_DEGREE)


    # 
    # set rotational delta robot: arm lengths
    #  Enter:  upperArmLengthMM = length in mm of upper arm (arm connected to the motor)
    #          lowerArmLengthMM = lenght in mm of lower arm (arm connected to the end effector)
    #  Exit:   true returned on success, else false
    # 
    def rotDelta_SetArmLengths(self, upperArmLengthMM: float, lowerArmLengthMM: float):
        self.__pushFltPoint3ToInt32(upperArmLengthMM)
        self.__pushFltPoint3ToInt32(lowerArmLengthMM)
        return self.__sendCommand(_CMD_DPiROBOT__ROT_DELTA_SET_ARM_LENGTH)


    #
    # set rotational delta robot: raduis of the robot's base and end effector
    #  Enter:  baseRadiusMM = radius of the base, from its center to the rotational joints of the upper arm
    #          endEffectorRadiusMM = radius of the end effector, from its center to the rotational joints of the lower arm
    #  Exit:   true returned on success, else false
    #
    def rotDelta_SetBaseAndEndEffectorRadius(self, baseRadiusMM: float, endEffectorRadiusMM: float):
        self.__pushFltPoint3ToInt32(baseRadiusMM)
        self.__pushFltPoint3ToInt32(endEffectorRadiusMM)
        return self.__sendCommand(_CMD_DPiROBOT__ROT_DELTA_SET_BASE_AND_END_EFFECTOR_RADIUS)


    #
    # set rotational delta robot: motor angle when upper arm is homed
    #  Enter:  upperArmHomeAngleDegrees = arm angle in degress when arm in home position, such that 0 degrees 
    #            represents the arm angle when it's in the horizontal plane
    #  Exit:   true returned on success, else false
    #
    def rotDelta_SetUpperArmHomeAngleDegrees(self, upperArmHomeAngleDegrees: float):
        self.__pushFltPoint3ToInt32(upperArmHomeAngleDegrees)
        return self.__sendCommand(_CMD_DPiROBOT__ROT_DELTA_SET_UPPER_ARM_HOME_ANGLE_DEGREES)


    #
    # set rotational delta robot: minimum and maximum upper arm angles
    #  Enter:  minimumJointAngle = minimum allowed angle of the upper arm
    #          maximumJointAngle = maximum allowed angle of the upper arm
    #  Exit:   true returned on success, else false
    #
    def rotDelta_SetMinMaxJointAngles(self, minimumJointAngle: float, maximumJointAngle: float):
        self.__pushFltPoint3ToInt32(minimumJointAngle)
        self.__pushFltPoint3ToInt32(maximumJointAngle)
        return self.__sendCommand(_CMD_DPiROBOT__ROT_DELTA_SET_MIN_MAX_JOINT_ANGLES)


    #
    # set for all robot types: driver type
    #  Enter:  dtype = MOTOR_DRIVER_TYPE_DRV8825, MOTOR_DRIVER_TYPE_TMC2130, MOTOR_DRIVER_TYPE_DM542T...
    #  Exit:   true returned on success, else false
    #
    def motorDriver_SetDriverType(self, dtype: int):
        dpiNetwork.pushUint8(dtype)
        return self.__sendCommand(_CMD_DPiROBOT__MOTOR_DRIVER_SET_DRIVER_TYPE)


    #
    # set for all robot types: driver microstepping
    #  Enter:  mstepping = 16, 32, 64, 128
    #  Exit:   true returned on success, else false
    #
    def motorDriver_SetDriverMicrostepping(self, mstepping: int):
        dpiNetwork.pushUint8(mstepping)
        return self.__sendCommand(_CMD_DPiROBOT__MOTOR_DRIVER_SET_DRIVER_MICROSTEPPING)


    #
    # set for all robot types: step direction reversing flag
    #  Enter:  reverseSteppingFlg = true or false
    #  Exit:   true returned on success, else false
    #
    def motorDriver_SetReverseStepDirectionFlag(self, reverseSteppingFlg: bool):
        dpiNetwork.pushUint8(reverseSteppingFlg)
        return self.__sendCommand(_CMD_DPiROBOT__MOTOR_DRIVER_SET_REVERSE_DIRECTION_FLAG)

