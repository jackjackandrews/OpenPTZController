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
    :mod:`openptzcontroller.core.protocols.generic_exceptions`
    
    Provides some standard error definitions which are common to all protocols.
    
'''

class ProtocolError(Exception):
    '''Basic exception class for any protocol errors'''
    def __init__(self, msg=None):
        if msg is None:
            msg = 'A protocol error occurred'
        super(ProtocolError, self).__init__(msg)

class ParameterOutOfRangeError(ProtocolError, ValueError):
    '''Raised when parameter passed to a command is outside the acceptable range defined by the protocol'''

    def __init__(self, parameter_name, parameter_value, parameter_max, parameter_min):
        super(ParameterOutOfRangeError, self).__init__(parameter_name + ' is outside the range defined by the protocol. Parameter value was: {}, must be in range: {} to {}'.format(parameter_value, parameter_min, parameter_max))
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value
        self.parameter_max = parameter_max
        self.parameter_min = parameter_min
        