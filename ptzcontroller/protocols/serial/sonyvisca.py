# -*- coding: utf-8 -*-
import serial

##########################################################################
# PTZ Controller - An Open Source PTZ Camera Controller                  #
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

"""
    :mod:`ptzcontroller.core.protocols.serial.sonyvisca`
    
    Provides interface functions for cameras using the Sony VISCA (tm) protocol connected over serial.
    
"""

import logging

from ptzcontroller.protocols.generic_packet import GenericPacket
from ptzcontroller.protocols import generic_exceptions

class SonyVisca(object):
    '''
    classdocs
    '''

    def __init__(self, serialport, address):
        '''
        Constructor
        '''
        self.packet = GenericPacket
        self.packet.init()
        
        self.serialport = serialport
        self.address = address
        self.broadcast = 0 
    
    
    def set_address(self):
        
        backup = self.broadcast
        self.broadcast = 1
        
        self.packet.init()
        self.packet.append_byte(0x30)
        self.packet.append_byte(0x01)

        
    def send_packet(self):
        None
        
    def get_reply(self):
        None
        
    def get_packet(self):
        pass
        
class Error(Exception):
    pass

class ViscaResponseTimeout(Error):
    pass

class ViscaSyntaxError(Error):
    pass

class ViscaCommandBufferFullError(Error):
    pass

class ViscaCommandCancelledError(Error):
    pass

class ViscaNoSocketError(Error):
    pass

class ViscaCommandNotExecutableError(Error):
    pass
        