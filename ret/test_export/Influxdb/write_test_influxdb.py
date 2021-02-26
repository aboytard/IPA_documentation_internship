#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 11:21:28 2021

@author: student
"""
import influxdb
from influxdb import InfluxDBClient
import datetime

def create_switch_influxdb(client):
    client.create_database('test_influxdb_export')
    client.switch_database('test_influxdb_export')
    return client

def write_data_influxdb(client):
    json_body_A = [
        {
            "measurement": "test_A",
            "tags": {
                "requestName": "All_Information",
                "requestType": "GET"
            },
            "time": datetime.datetime.utcnow(),#datetime.datetime.utcnow(),
             "fields": {
                "Btn_name": "coco", 
                "Action": "coco",
                "In_Time_Interval": "coco", 
                "end_effector_position_entering_button_area": "coco",
                "end_effector_position_received_socket_message_pressed": "coco",
                "end_effector_position_leaving_button_area": "coco"
                        }
        }
    ]
    json_body_B = [
        {
            "measurement": "test_B",
            "tags": {
                "requestName": "Error_Message",
                "requestType": "GET"
            },
            "time": datetime.datetime.utcnow(),#datetime.datetime.utcnow(),
             "fields": {
                "Btn_name": "kaka", 
                "Action": "kaka",
                "In_Time_Interval": "kaka", 
                "end_effector_position_entering_button_area": "kaka",
                "end_effector_position_received_socket_message_pressed": "kaka",
                "end_effector_position_leaving_button_area": "kaka"
                        }
        }
    ]
    client.write_points(json_body_A,batch_size=1000)
    client.write_points(json_body_A,batch_size=1000)
    client.write_points(json_body_B,batch_size=1000)
    
if __name__=="__main__":
    client = InfluxDBClient(host = 'localhost' , port ='8086', username='alban', password='asdf')
    create_switch_influxdb(client)
    write_data_influxdb(client)
    

