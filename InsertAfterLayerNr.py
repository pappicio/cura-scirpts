# Copyright (c) 2020 Ultimaker B.V.
# Cura is released under the terms of the LGPLv3 or higher.
# Created by Wayne Porter

from ..Script import Script

import re

class InsertAfterLayerNr(Script):
    def __init__(self):
        super().__init__()

    def getSettingDataString(self):
        return """{
            "name": "Insert After layer nr",
            "key": "InsertAfterLayerNr",
            "metadata": {},
            "version": 2,
            "settings":
            {
                "insert_location":
                {
                    "label": "Layer nr where insert",
                    "description": "Whether to insert code after layer Nr.",
                    "type": "int",
                    "default_value": "0"
                },
                "gcode_to_add":
                {
                    "label": "G-code to insert.",
                    "description": "G-code to insert after layer nr.",
                    "type": "str",
                    "default_value": ""
                }
            }
        }"""
    def getValue(self, line):
        list_split = re.split(":", line)  # Split at ":" so we can get the numerical value
        return int(list_split[1])  # Convert the numerical portion to a int
  
  
    def execute(self, data):
        gcode_to_add = self.getSettingValueByKey("gcode_to_add") + "\n"
        insert_location = self.getSettingValueByKey("insert_location") 
        for layer in data:
            # Check that a layer is being printed
            lines = layer.split("\n")
            for line in lines:
                if ";LAYER:" in line:
                    actual_layer = self.getValue(line)
                    index = data.index(layer)
                    if actual_layer == insert_location:
                        layer = layer + gcode_to_add 
                    data[index] = layer
                    break
        return data





