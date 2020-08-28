# -*- coding: utf-8 -*-

##########################################################################
# Open PTZ Controller - An Open Source PTZ Camera Controller             #
# ---------------------------------------------------------------------- #
# Copyright (c) 2008-2020 Jack Andrews                                   #
# ---------------------------------------------------------------------- #
# This program is free software: you can redistribute it and/or modify   #
# it under the terms of the GNU General Public License as published by   #
# the Free Software Foundation, either version 3 of the License, or      #
# (at your option) any later version.                                    #
#                                                                        #
# This program is distributed in the hope that it will be useful,        #
# but WITHOUT ANY WARRANTY; without even the implied warranty of         #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
# GNU General Public License for more details.                           #
#                                                                        #
# You should have received a copy of the GNU General Public License      #
# along with this program.  If not, see <https://www.gnu.org/licenses/>. #
##########################################################################

'''
    :mod:`ptzcontroller.core.protocols.serial.sonyvisca_exceptions`
    
    Provides error classes for cameras using the Sony VISCA (tm) protocol connected over serial or UDP/IP.
    
'''

from openptzcontroller.protocols.generic_exceptions import ProtocolError

class SonyViscaError(ProtocolError):
    '''Basic exception class for any VISCA protocol errors'''
    def __init__(self, msg):
        if msg is None:
            msg = 'A VISCA protocol error occurred'
        super(SonyViscaError, self).__init__(msg)

class ResponseTimeout(SonyViscaError):
    '''Raised when a response is not received within the configured timeout period'''
    def __init__(self, camera_serialport, camera_address, command, configured_timeout_milliseconds):
        msg = 'Camera at address: {} on serial port: '.format(camera_address) + camera_serialport + ' failed to send a response to command: ' + command + ' within {} milliseconds'.format(configured_timeout_milliseconds)
        super(ResponseTimeout, self).__init__(msg)
        self.camera_serialport = camera_serialport
        self.camera_address = camera_address
        self.command = command
        self.configured_timeout_milliseconds = configured_timeout_milliseconds

class CommandSyntaxError(SonyViscaError):
    def __init__(self, camera_serialport, camera_address, command):
        msg = 'Camera at address: {}'.format(camera_address) + ' on serial port: ' + camera_serialport + ' responded with syntax error to command: ' + command
        super(CommandSyntaxError, self).__init__(msg)
        self.camera_serialport = camera_serialport
        self.camera_address = camera_address
        self.command = command

class CommandBufferFullError(SonyViscaError):
    def __init__(self, camera_serialport, camera_address, command):
        msg = 'Camera at address: {}'.format(camera_address) + ' on serial port: ' + camera_serialport + ' responded with command buffer full error to command: ' + command
        super(CommandBufferFullError, self).__init__(msg)
        self.camera_serialport = camera_serialport
        self.camera_address = camera_address
        self.command = command

class CommandCancelledError(SonyViscaError):
    def __init__(self, camera_serialport, camera_address, command):
        msg = 'Camera at address: {}'.format(camera_address) + ' on serial port: ' + camera_serialport + ' responded with command cancelled error to command: ' + command
        super(CommandBufferFullError, self).__init__(msg)
        self.camera_serialport = camera_serialport
        self.camera_address = camera_address
        self.command = command
        
class NoSocketError(SonyViscaError):
    def __init__(self, camera_serialport, camera_address, command):
        msg = 'Camera at address: {}'.format(camera_address) + ' on serial port: ' + camera_serialport + ' responded with command cancelled error to command: ' + command
        super(CommandBufferFullError, self).__init__(msg)
        self.camera_serialport = camera_serialport
        self.camera_address = camera_address
        self.command = command

class CommandNotExecutableError(SonyViscaError):
    def __init__(self, camera_serialport, camera_address, command):
        msg = 'Camera at address: {}'.format(camera_address) + ' on serial port: ' + camera_serialport + ' responded with command not executable error to command: ' + command
        super(CommandBufferFullError, self).__init__(msg)
        self.camera_serialport = camera_serialport
        self.camera_address = camera_address
        self.command = command
        