#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time     : 2023/1/9 23:08 
# @Author   : 0xJohsnon
# @File     : test.py
# @Usage    :

import json
txt = {
    'username': 12,
    'password': 12
}
result = json.dumps(txt)
print(result)