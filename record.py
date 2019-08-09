#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
################################################################################
#                                                                              #
# record                                                                       #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program records weather data to database.                               #
#                                                                              #
# copyright (C) 2019 Will Breaden Madden, wbm@protonmail.ch                    #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################
"""

import time

import AWRS
import folktales

identifier = "EGPF"

folktales.create_database(filepath="weather.db")

while True:
    report_METAR = AWRS.METAR(identifier=identifier)
    folktales.insert_dictionary_into_database_table(
        dictionary      = report_METAR,
        table_name      = "METAR",
        filepath        = "weather.db"
    )
    time.sleep(2)
    report_TAF = AWRS.TAF(identifier=identifier)
    folktales.insert_dictionary_into_database_table(
        dictionary      = report_TAF,
        table_name      = "TAF",
        filepath        = "weather.db"
    )
    time.sleep(1800)
