# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 22:25:18 2019

@author: lenovo
"""

"""
Code Challenge:
    
http://forsk.in/images/Forsk_logo_bw.png"

Download the image from the url above and store in your workking diretory with the same
name as the image name.

Do not hardcode the name of the image

"""

import requests 
image_url = "http://forsk.in/images/Forsk_logo_bw.png"
 
r = requests.get(image_url) 

with open("Forsk_logo_bw.png",'wb') as f: 

	f.write(r.content)
