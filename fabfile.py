# -*- coding: utf-8 -*-

from fabric import Connection
from fabric import task
import io, sys


@task
def hello(c):
    c_pi = Connection(host='pi@raspberrypi.', connect_kwargs={"password": "raspberry"})
    c_pi.run('sudo raspi-config nonint do_change_locale en_US')
    c_pi.run('sudo raspi-config nonint do_configure_keyboard jp')
    c_pi.run('sudo raspi-config nonint do_change_timezone Asia/Tokyo')
    c_pi.run('sudo apt-get update -y')
    c_pi.run('sudo apt-get upgrade -y')
