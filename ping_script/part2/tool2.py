#!/usr/bin/env python
"""
    Copyright 2016 Cisco Systems All rights reserved.

 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions are
 met:

     * Redistributions of source code must retain the above copyright
 notice, this list of conditions and the following disclaimer.

 The contents of this file are licensed under the Apache License, Version 2.0
 (the "License"); you may not use this file except in compliance with the
 License. You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 License for the specific language governing permissions and limitations under
 the License.
"""
import os


# Verifies your os type
OS_TYPE = os.name
# Sets the count modifier to the os type
count = '-n' if OS_TYPE == 'nt' else '-c'

def create_ip_list():
    """Creates an ip address list
        return: Return the ip_list
        rtype: list
    """
    ip_list = []
    with open("ip_file.txt", "r") as file:
        for line in file:
            ip_list.append(line.strip())
    return ip_list


def ping_device(ip_list):
    """Ping ip_list and return results
        return: None
        rtype: None
    """
    results_file = open("results.txt", "w")
    for ip in ip_list:
        response = os.popen(f"ping {ip} {count} 1").read()
        if "Received = 1" and "Approximate" in response:
            print(f"UP {ip} Ping Successful")
            results_file.write(f"UP {ip} Ping Successful" + "\n")
        else:
            print(f"Down {ip} Ping Unsuccessful")
            results_file.write(f"Down {ip} Ping Unsuccessful" + "\n")
    results_file.close()


if __name__ == "__main__":
    ping_device(create_ip_list())
