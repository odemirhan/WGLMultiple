# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 12:17:20 2022

@author: Engineering
"""

import shutil
import glob
import os


rawfiles=glob.glob("raw"+"\*")

for cnt0 in range(len(rawfiles)):
    
    filename=str(rawfiles[cnt0]).split("\\")
    filename=filename[1]
    print(filename)
    os.makedirs(os.path.dirname(os.path.join("TC-COH", filename, "selam")), exist_ok=True)
    shutil.copy(rawfiles[cnt0], os.path.join("TC-COH", filename))
