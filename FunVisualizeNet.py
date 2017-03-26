#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 14:54:38 2017

@author: guangwei
"""

import numpy as np
import matplotlib.pyplot as plot

def  VisualizeNet(weightCurrent, currentError, weightT):
    
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(6,10))
    
    ax1.imshow(weightCurrent[0], extent=[0,100,0,1])
    ax1.set_title('Default')
    
    ax2.imshow(grid, extent=[0,100,0,1], aspect='auto')
    ax2.set_title('Auto-scaled Aspect')
    
    ax3.imshow(grid, extent=[0,100,0,1], aspect=100)
    ax3.set_title('Manually Set Aspect')
    
    plt.tight_layout()
    plt.show()