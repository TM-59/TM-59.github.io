# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 13:02:47 2023

@author: taichi.mitsuhashi
"""

from jinja2 import Template
tmp_s = 'Hello {{ name }}!'
template = Template(tmp_s)
ren_s = template.render(name='名前')
print(ren_s)


