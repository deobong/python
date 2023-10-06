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
COUNT = '-n' if OS_TYPE == 'nt' else '-c'

# Open file for saving ping results
results_file = open("results.txt", "w")

# Empty list to store ip addresses
ip_list = []

# Loop from 1 to 255
# Appends the concatenated ip to the ip_list
for ip in range(1, 255):
    ip_list.append("192.168.23." + str(ip))

# Print number of ip addresses in list
print(len(ip_list))

# Loop to ping ip_list and check if device up or down
# Outputs to results.txt file
for ip in ip_list:
    response = os.popen(f"ping {ip} {COUNT} 1").read()
    if "Received = 1" in response and "Approximate" in response:
        print(f"UP {ip} Ping Successful")
        results_file.write(f"UP {ip} Ping Successful" + "\n")
    else:
        print(f"Down {ip} Ping Unsuccessful")
        results_file.write(f"Down {ip} Ping Unsuccessful" + "\n")

# Close file when script completes
results_file.close()
