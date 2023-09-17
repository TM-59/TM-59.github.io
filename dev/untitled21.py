# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 14:57:05 2023

@author: taichi.mitsuhashi
"""

import mysql.connector
from mysql.connector import Error
import pandas as pd


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

a="localhost"
b="root"
c="password"

create_server_connection(a, b, c)

