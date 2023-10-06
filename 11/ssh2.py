# SSH from Windows 10 using Python subprocess + built-in OpenSSH
#
# Alternatives to using subprocess include:
#  Fabric: http://www.fabfile.org/
#  Paramiko: http://www.paramiko.org/
#
# References:
#   OpenSSH in Windows 10: https://blogs.msdn.microsoft.com/commandline/2018/01/22/openssh-in-windows-10/
#   The only simple way to do SSH in Python today is to use subprocess + OpenSSH...: https://gist.github.com/bortzmeyer/1284249
#   Issue8557 - subprocess PATH semantics and portability: https://bugs.python.org/issue8557
#   Python does not find System32: https://stackoverflow.com/a/41631476/8670609

import os
import subprocess
import platform

PRIVATE_KEY_LOCATION = "C:/Users/johndoe/.ssh/id_rsa"  # private key location here
USER = "johndoe"                                       # username here
HOST = "192.168.1.1"                                   # address here
COMMAND="uname -a"                                     # command here
# Ports are handled in ~/.ssh/config since we use OpenSSH

# Handle execution of 32-bit Python on 64-bit Windows
system32 = os.path.join(os.environ['SystemRoot'], 'SysNative' if platform.architecture()[0] == '32bit' else 'System32')
ssh_path = os.path.join(system32, 'OpenSSH/ssh.exe')

ssh = subprocess.Popen([ssh_path, '-i', PRIVATE_KEY_LOCATION, "{}@{}".format(USER, HOST)],
                       stdin=subprocess.PIPE,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

std_data = ssh.communicate(COMMAND)
print("ssh stdout:\n{}".format(std_data[0]))
print("ssh stderr:\n{}".format(std_data[1]))