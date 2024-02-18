#      ******************************************************************
#      *                                                                *
#      *                           DPi Network                          *
#      *                                                                *
#      *            Stan Reifel                     8/19/2022           *
#      *                                                                *
#      ******************************************************************

#
# Protocol for RS485 serial communication between the Master and a Slave module:
# 
# Commands are sent from the Master to a Slave.  The slave on the RS485 network is
# identified by the Slave's address.  Each Slave must have a unique 6 bit SlaveAddress.
#
# Commands from the Master include a CommandByte and up to 15 bytes of additional 
# data.  The Slave must acknowledge that it received the Master's command and that 
# the data it received is intact.  The Master can send commands to have the Slave 
# do things, or it can send commands requesting data from the Slave.
#
# When the Slave receives a command from the Master, it must acknowledge the command.
# This acknowledgement is used to let the Master know the command was received
# successfully.  When the Master sends a command requesting data from the Slave, the 
# Slave sends the data by adding it to the acknowledgement (which can include up
# to 15 bytes of data from the Slave).
#
# After the Master sends a command, it waits for an acknowledgement from the Slave.
# If the Master doesn't receive the acknowledgement within a few milliseconds, it
# resends the command (up to n times).  If the Slave receives a command with corrupted 
# data, the Slave simply ignores the command by not executing it or sending any 
# acknowledgement (causing the Master to resend). 
# 
# All data transfers are initiated by the Master.  The Slave can not asynchronously
# transmit data that wasn't requested by a command from the Master.
#
# Byte format of command packets sent from the Master to Slave:
#   * HeaderByte: Always 0xaa
#   * SlaveAddress: 6 bits, note bit 7 must be 1, bit 6 must be 0. 
#   * CommandByte
#   * DataCount: Count of bytes in the DataField (0 - 15):
#      - The value's low nibble = DataCount
#      - The value's high nibble = (~DataCount) << 4   (one's complment of the DataCount)
#   * DataField: Between 0 and 15 bytes of additional data sent by the Master
#   * Checksum: The 8 bit sum of all bytes in the packet including the HeaderByte, 
#              DataCount value, SlaveAddress value, CommandByte, and all bytes in 
#              the DataField.
#
# There are two packet formats the Slave uses when acknowledging the Master's commands.
# If the Master isn't requesting data from the Slave, the acknowledgement format is:
#   * HeaderByte: 0x77
#   * Checksum: (will always be 0x77)
# If the Master is requesting data from the Slave, the format is:
#   * HeaderByte: 0x78
#   * DataCount: Count of bytes in the DataField (1 - 15):
#      - The value's low nibble = DataCount
#      - The value's high nibble = (~DataCount) << 4   (one's complment of the DataCount)
#  * DataField: Between 1 and 15 bytes of data sent from the Slave
#  * Checksum: The 8 bit sum of all bytes in the acknowledgement packet including the 
#              HeaderByte, DataCount value, and all bytes in the DataField.
#

from time import time
import serial
serialPort = serial


#
# Master/Slave communication constants
#
_RS485_BAUDRATE = 115200
_RS485_RETRY_ATTEMPTS = 3
_COMMAND_PACKET_HEADER = 0xaa
_ACKNOWLEDGEMENT_PACKET_HEADER_WITH_NO_DATA = 0x77
_ACKNOWLEDGEMENT_PACKET_HEADER_WITH_DATA = 0x78

#
# state values for: receivePacketState
#
_RECEIVE_PACKET_STATE__WAITING_FOR_HEADER = 0
_RECEIVE_PACKET_STATE__WAITING_FOR_DATA_COUNT = 1
_RECEIVE_PACKET_STATE__WAITING_DATA = 2
_RECEIVE_PACKET_STATE__WAITING_FOR_CHECKSUM = 8

#
# vars global to this module
#
_dataTransmitBuffer = bytearray(16)
_dataTransmitIndex = 0
_dataReceiveBuffer = bytearray(16)
_dataReceiveIndex = 0

class DPiNetwork:
    #
    # initialize the RS485 serial communication
    #
    def __init__(self):
        global serialPort
        global _dataTransmitIndex
        global _dataReceiveIndex

        serialPort = serial.Serial(
            port="/dev/serial0", 
            baudrate = _RS485_BAUDRATE,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS)

        _dataTransmitIndex = 0
        _dataReceiveIndex = 0


    #
    # send a command to a slave module via a RS485 network, command's additional data must have 
    # already been "Pushed".  After this function returns data from the slave is retrieved by "Popping"
    #    Enter:  slaveAddress = address of slave module (0 - 0x3f)
    #            command = command byte
    #            timeoutPeriodMS = number of milliseconds to wait for the slave to respond
    #    Exit:   [0]: True returned on success, else False
    #            [1]: number of failed packets (0 = no failed packets)
    #
    def sendCommand(self, slaveAddress: int, command: int, timeoutPeriodMS: int):
        global serialPort
        global _dataTransmitIndex
        global _dataTransmitBuffer
        global _dataReceiveIndex
        global _dataReceiveBuffer
        receivePacketState = _RECEIVE_PACKET_STATE__WAITING_FOR_HEADER
        timeoutPeriodSec = timeoutPeriodMS / 1000.0

        # 
        # flush the buffer of data received from the slaves, to make sure it's empty before sending the packet
        #
        serialPort.reset_input_buffer()

        #
        # setup a loop to send packet to slave, retrying if it fails
        #
        sendDataSize = _dataTransmitIndex
        _dataTransmitIndex = 0
        sendDataCountValue = (sendDataSize & 0x0f) + (((~sendDataSize) & 0x0f) << 4)
        slaveAddressValue = (slaveAddress & 0x3f) | 0x80

        for retryCount in range(0, _RS485_RETRY_ATTEMPTS):
            #
            # send packet to slave
            #
            packet = bytearray(5 + sendDataSize)
            checksum = 0
            
            packet[0] = _COMMAND_PACKET_HEADER
            checksum += _COMMAND_PACKET_HEADER
            
            packet[1] = slaveAddressValue
            checksum += slaveAddressValue
            
            packet[2] = command
            checksum += command
            
            packet[3] = sendDataCountValue
            checksum += sendDataCountValue
            
            for i in range(0, sendDataSize):
                packet[4 + i] = _dataTransmitBuffer[i]
                checksum += _dataTransmitBuffer[i]

            packet[4 + sendDataSize] = checksum % 0x100

            serialPort.write(packet)

            #
            # get acknowledgement packet from slave, timing out if it isn't received (or received corrupted)
            #
            startTime = time()
            receivePacketState = _RECEIVE_PACKET_STATE__WAITING_FOR_HEADER
            receivedDataSize = 0
            checksum = 0
            
            while(True):
                #
                # check if timed out while waiting for slave's response
                #
                elapsedTime = time() - startTime
                if (elapsedTime > timeoutPeriodSec):
                    break                                  # timed out, exit "while loop" causing packet to be resent to slave 

                #
                # check if there's a new byte of data from the slave
                #
                if serialPort.inWaiting() == 0:
                    continue
                
                c = serialPort.read()[0]
                if receivePacketState == _RECEIVE_PACKET_STATE__WAITING_FOR_HEADER:
                    checksum += c;
                    if c == _ACKNOWLEDGEMENT_PACKET_HEADER_WITH_NO_DATA:
                        receivePacketState = _RECEIVE_PACKET_STATE__WAITING_FOR_CHECKSUM;

                    if c == _ACKNOWLEDGEMENT_PACKET_HEADER_WITH_DATA:
                        receivePacketState = _RECEIVE_PACKET_STATE__WAITING_FOR_DATA_COUNT;
                
                
                elif receivePacketState == _RECEIVE_PACKET_STATE__WAITING_FOR_DATA_COUNT:
                    checksum += c
                    receivedDataSize = c & 0x0f
                    bytesReceivedCount = 0
                    _dataReceiveIndex = 0

                    if receivedDataSize == 0:
                        receivePacketState = _RECEIVE_PACKET_STATE__WAITING_FOR_HEADER
                    elif receivedDataSize != (((~c) >> 4) & 0x0f):
                        receivePacketState = _RECEIVE_PACKET_STATE__WAITING_FOR_HEADER
                    else:
                        receivePacketState = _RECEIVE_PACKET_STATE__WAITING_DATA


                elif receivePacketState == _RECEIVE_PACKET_STATE__WAITING_DATA:
                    checksum += c
                    _dataReceiveBuffer[bytesReceivedCount] = c
                    bytesReceivedCount += 1

                    if bytesReceivedCount == receivedDataSize:
                        receivePacketState = _RECEIVE_PACKET_STATE__WAITING_FOR_CHECKSUM;


                elif receivePacketState == _RECEIVE_PACKET_STATE__WAITING_FOR_CHECKSUM:
                    if c == checksum % 0x100:
                        return True, retryCount


                    receivePacketState = _RECEIVE_PACKET_STATE__WAITING_FOR_HEADER


                else:
                    receivePacketState = _RECEIVE_PACKET_STATE__WAITING_FOR_HEADER
        
        return False, retryCount+1


    #
    # push data to the transmit buffer
    #
    def pushUint8(self, value: int):
        global _dataTransmitIndex
        global _dataTransmitBuffer
        _dataTransmitBuffer[_dataTransmitIndex] = value & 0xff;
        _dataTransmitIndex += 1

    def pushInt8(self, value: int):
        global _dataTransmitIndex
        global _dataTransmitBuffer
        _dataTransmitBuffer[_dataTransmitIndex] = value & 0xff;
        _dataTransmitIndex += 1

    def pushUint16(self, value: int):
        global _dataTransmitIndex
        global _dataTransmitBuffer
        _dataTransmitBuffer[_dataTransmitIndex] = (value >> 8) & 0xff;
        _dataTransmitIndex += 1
        _dataTransmitBuffer[_dataTransmitIndex] = value & 0xff;
        _dataTransmitIndex += 1

    def pushInt16(self, value: int):
        global _dataTransmitIndex
        global _dataTransmitBuffer
        _dataTransmitBuffer[_dataTransmitIndex] = (value >> 8) & 0xff;
        _dataTransmitIndex += 1
        _dataTransmitBuffer[_dataTransmitIndex] = value & 0xff;
        _dataTransmitIndex += 1

    def pushUint32(self, value: int):
        global _dataTransmitIndex
        global _dataTransmitBuffer
        _dataTransmitBuffer[_dataTransmitIndex] = (value >> 24) & 0xff;
        _dataTransmitIndex += 1
        _dataTransmitBuffer[_dataTransmitIndex] = (value >> 16) & 0xff;
        _dataTransmitIndex += 1
        _dataTransmitBuffer[_dataTransmitIndex] = (value >> 8) & 0xff;
        _dataTransmitIndex += 1
        _dataTransmitBuffer[_dataTransmitIndex] = value & 0xff;
        _dataTransmitIndex += 1

    def pushInt32(self, value: int):
        global _dataTransmitIndex
        global _dataTransmitBuffer
        _dataTransmitBuffer[_dataTransmitIndex] = (value >> 24) & 0xff;
        _dataTransmitIndex += 1
        _dataTransmitBuffer[_dataTransmitIndex] = (value >> 16) & 0xff;
        _dataTransmitIndex += 1
        _dataTransmitBuffer[_dataTransmitIndex] = (value >> 8) & 0xff;
        _dataTransmitIndex += 1
        _dataTransmitBuffer[_dataTransmitIndex] = value & 0xff;
        _dataTransmitIndex += 1


    #
    # get data from the receive buffer
    #
    def popUint8(self) -> int:
        global _dataReceiveIndex
        global _dataReceiveBuffer
        value = _dataReceiveBuffer[_dataReceiveIndex]
        _dataReceiveIndex += 1
        return value

    def popInt8(self) -> int:
        global _dataReceiveIndex
        global _dataReceiveBuffer
        value = _dataReceiveBuffer[_dataReceiveIndex]
        if value & 0x80 > 0:
            value -= 0x100
        _dataReceiveIndex += 1
        return value

    def popUint16(self) -> int:
        global _dataReceiveIndex
        global _dataReceiveBuffer
        value = ((_dataReceiveBuffer[_dataReceiveIndex] << 8) + _dataReceiveBuffer[_dataReceiveIndex + 1])
        _dataReceiveIndex += 2
        return value

    def popInt16(self) -> int:
        global _dataReceiveIndex
        global _dataReceiveBuffer
        value = ((_dataReceiveBuffer[_dataReceiveIndex] << 8) + _dataReceiveBuffer[_dataReceiveIndex + 1])
        if value & 0x8000 > 0:
            value -= 0x10000
        _dataReceiveIndex += 2
        return value

    def popUint32(self) -> int:
        global _dataReceiveIndex
        global _dataReceiveBuffer
        value = ((_dataReceiveBuffer[_dataReceiveIndex] << 24) + 
                (_dataReceiveBuffer[_dataReceiveIndex+1] << 16) + 
                (_dataReceiveBuffer[_dataReceiveIndex+2] << 8) + 
                (_dataReceiveBuffer[_dataReceiveIndex+3]))
        _dataReceiveIndex += 4
        return value

    def popInt32(self) -> int:
        global _dataReceiveIndex
        global _dataReceiveBuffer
        value = ((_dataReceiveBuffer[_dataReceiveIndex] << 24) + 
                (_dataReceiveBuffer[_dataReceiveIndex+1] << 16) + 
                (_dataReceiveBuffer[_dataReceiveIndex+2] << 8) + 
                (_dataReceiveBuffer[_dataReceiveIndex+3]))
        if value & 0x80000000 > 0:
            value -= 0x100000000
        _dataReceiveIndex += 4
        return value
