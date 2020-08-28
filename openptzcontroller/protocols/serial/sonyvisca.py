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
    :mod:`ptzcontroller.core.protocols.serial.sonyvisca`
    
    Provides interface functions for cameras using the Sony VISCA (tm) protocol connected over serial.
    
'''

import logging

from openptzcontroller.protocols.generic_packet import GenericPacket

import openptzcontroller.protocols.generic_exceptions
import openptzcontroller.protocols.serial.sonyvisca_exceptions

class SonyVisca(object):
    '''
    classdocs
    '''

    def __init__(self, camera_serialport, camera_address, timeout_milliseconds):
        '''
        Constructor
        '''
        self.packet = GenericPacket
        self.packet.init()
        
        self.serialport = camera_serialport
        self.address = camera_address
        self.broadcast = 0
        
        try:
            self.set_timeout(timeout_milliseconds)
        except ValueError as e:
            raise e
    
    # This should really be off in it's own module along with other common serial functions
    def set_timeout(self, timeout_milliseconds):
        '''Configure timeout for responses: -1 = wait indefinitely, 0 = no timeout (ie. don't wait), positive values are timeout in milliseconds'''
        if timeout_milliseconds < -1:
            self.timeout = 0
            raise ValueError('Timeout value out of range. Use timeout_milliseconds = -1 to wait indefinitely, = 0 for no timeout, or a positive integer for timeout in milliseconds.')
        self.timeout = timeout_milliseconds
        
    def send_packet(self):
        pass
    
    def build_packet(self):
        pass
    
    def parse_response(self):
        pass

    # Camera initialisation procedure
    def initialise_camera(self):
        '''Perform any initialisation functions here - eg. IF_Clear'''
        pass

    # Commands
    # Broadcast set commands
    def set_address(self):
        
        backup = self.broadcast
        self.broadcast = 1
        raise
        
        self.packet.init()
        self.packet.append_byte(0x30)
        self.packet.append_byte(0x01)
        
    # Set commands
    
    # Get commands

        

        