#coding=utf-8
from sys import prefix

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from fabric import Connection

# env.shell = "/bin/bash -l -c -i"
# conn = Connection('192.168.10.10','vagrant',connect_kwargs={"password": "vagrant"})
conn = Connection('192.168.10.10','vagrant',connect_kwargs={"password": "vagrant"})


# result = conn.run('source ~/.bashrc ', pty=True)
# print(result)
conn.run('source ~/.bashrc')
result = conn.run('mgrep "senti" /etc/redis')
print(result)



