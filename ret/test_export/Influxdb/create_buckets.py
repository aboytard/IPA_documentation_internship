#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 13:01:32 2021

@author: student
"""

import requests
#url = 'https://us-west-2-1.aws.cloud2.influxdata.com/api/v2/bucket'
# or if you’re using InfluxDB OSSr
url = 'http://localhost:8088'
headers = {'Authorization': 'Token G6ZzYAdenIqWISWvfmHd0QIIL-DUcvREJWzCMMDLSF5aZonOwE2etwh22d4OwjTPAxGo1UtzDhsOs6EJCK0ppA=='}
payload = {
"orgID": "ec4a5f5fee6ed685",
"name": "bucket",
"description": "create a bucket",
"rp": "db_rp",
"retentionRules":[
{
"type": "expire",
"everySeconds": 86400
}
]
}
#r = requests.get('http://localhost:8086/api/v2/authorizations/', headers=headers)
r = requests.post(url, headers=headers, json=payload)
print(r.text)