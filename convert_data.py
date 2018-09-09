# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 19:58:01 2018

@author: gaoyufeng
"""

import numpy as np
import xml.dom.minidom as xml_dom


def parse_xml(xml_path):
    DOMTree = xml_dom.parse(xml_path)
    collection = DOMTree.documentElement
    print(collection)
    
    
if __name__=="__main__":
    parse_xml("")