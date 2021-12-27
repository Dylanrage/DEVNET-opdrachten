#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install netmiko
print('Installation necessary')


# In[14]:


from netmiko import ConnectHandler
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="192.168.56.106",
    port="22",
    username="cisco",
    password="cisco123!"
    )
output=sshCli.send_command("show ip int br")
print(output)


# In[9]:


config_commands = (
    'int loopback 1' ,
    'ip address 1.1.1.1 255.255.255.0',
    'description LO1'
    )
output=sshCli.send_config_set(config_commands)
config_commands = (
    'int loopback 2' ,
    'ip address 2.2.2.2 255.255.255.0',
    'description LO2'
    )
output=sshCli.send_config_set(config_commands)
#
output=sshCli.send_command("show ip int br")
print(output)


# In[10]:


config_commands = (
    'int loopback 2' ,
    'no ip address',
    'exit',
    'no interface loopback 2'
    )
output=sshCli.send_config_set(config_commands)
output=sshCli.send_command("show ip int br")
print(output)


# In[13]:


config_commands = (
    'int loopback 1' ,
    'no ip address',
    'exit',
    'no interface loopback 1'
    )
output=sshCli.send_config_set(config_commands)
output=sshCli.send_command("show ip int br")
print(output)


# In[11]:


from netmiko import ConnectHandler
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="192.168.56.106",
    port="22",
    username="cisco",
    password="cisco123!"
    )
output=sshCli.send_command("show ver")
print(output)


# In[12]:


from netmiko import ConnectHandler
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="192.168.56.106",
    port="22",
    username="cisco",
    password="cisco123!"
    )
output=sshCli.send_command("show running-config")
print(output)

