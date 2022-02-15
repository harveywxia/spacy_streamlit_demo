#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File       :  utils.py    
@Contact    :  harvey.wxia@gmail.com
@License    :  (C)Copyright 2020-2021
-------------------------------------
@Modify Time:  2022/2/15 2:26 PM
@Author     :  xiawei
@Version    :  1.0
@Description :  None
"""
import configparser


def check_login(username: str, password: str):
    config = configparser.ConfigParser()
    config.read('user_info.ini')
    # print(config['USER_INFO']['username'])
    # print(config['USER_INFO']['password'])

    if username == config['USER_INFO']['username'] and password == config['USER_INFO']['password']:
        return True
    return False

if __name__ == '__main__':
    print(check_login('xiawei', 'xiawei1qaz'))
