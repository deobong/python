# Ping Script, ping a network device to verify if the device is up or down

This is a script that leverages the [os library](https://docs.python.org/3/library/os.html) to ping a network device to verify if the device is up or down and output the status to `results.txt`. Use this script to learn the basics of python.

## Download the Code

To get started: Download the code and cd the `ping_script` directory

```bash
git clone https://github.com/labeveryday/ping_script.git
cd ping_script
```

## Python Virtual Environment

When executing python code or installing python applications you should get into the practice of creating and managing python virtual environments.
This will allow you to run different versions of a python library while avoiding version conflicts. My preferred tool for python virtual environments is `venv`
There are tools out there. Remember to find what works best for you.

**On Linux or Mac**

```python
python3 -m venv venv
source venv/bin/activate
```

**On Windows**

```cmd
python3 -m venv venv
.\venv\Scripts\activate.bat
```

## Example: Script in action

Now that you have everything installed and updated you can execute the script

```bash
(venv) duan@ubuntu ping_script$ python tool.py
Down 192.168.23.1 Ping Unsuccessful
Down 192.168.23.2 Ping Unsuccessful
Up 192.168.23.142 Ping successful
Up 192.168.23.143 Ping successful
Up 192.168.23.144 Ping successful

```

>NOTE: To modify the subnets and the range change the starting digit and the ending digit in line 18.

![ping_range](https://github.com/labeveryday/Notes/blob/main/images/ping_range.png)

## Walk through

Here is a video walk through of the `ping_script` in action.

[![Watch the video](https://github.com/labeveryday/Notes/blob/main/images/ping.png)](https://youtu.be/PTUhiDnYrbs)

### About me

Introverted Network Automation Engineer that is changing lives as a Developer Advocate for Cisco DevNet. Pythons scripts are delicious. Especially at 2am on a Saturday night.

My hangouts:

- [LinkedIn](https://www.linkedin.com/in/duanlightfoot/)

- [Twitter](https://twitter.com/labeveryday)