# -*- coding: utf-8 -*-

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
    :mod:`ptzcontroller.core.protocols.packet`
    
    Provides a standard packet descriptor and operations class which can be used by communication protocols.
    
"""

class GenericPacket(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.bytes = bytearray()
        
    def init(self):
        
        self.bytes = bytearray()
        
    def append_byte(self, byte):
        
        self.bytes.append(byte)
        
    def get_length(self):
        
        return len(self.bytes)
        
        