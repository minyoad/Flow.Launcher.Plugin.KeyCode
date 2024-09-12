# -*- coding: utf-8 -*-

import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher
from plugin.keycode import *
import pyperclip


class KeyCodeLauncher(FlowLauncher):
    
    def query(self, query):        
        key_items=find_keys(key=query)
        full_items=[]
        
        for item in key_items:
            if "=>" in item:
                key, value = item.split("=>")
                full_items.append(
                    {
                        "Title": "KeyCode: {}, value: {}".format(key,value),
                        "SubTitle": "Press enter to copy adb shell command to clipboard",
                        "IcoPath": "Images/app.png",
                        "JsonRPCAction": {
                            "method": "copy_value",
                            "parameters": [value]
                        }
                    }
                )
            else:
                full_items.append(
                    {
                        "Title": "{}".format(item),
                        "SubTitle": "",
                        "IcoPath": "Images/app.png"                        
                    }
                )
        
        
        return full_items
        
    def context_menu(self, data):
        return [    
        ]

    def copy_value(self, text):
        cmd="adb shell input keyevent {}".format(text)
        pyperclip.copy(cmd)

if __name__ == "__main__":
    KeyCodeLauncher()
