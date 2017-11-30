# coding: utf8
"""
rat-socket-websocket.py - Fuel Rats Rat Tracker module.

Copyright (c) 2017 The Fuel Rats Mischief,
All rights reserved.

Licensed under the BSD 3-Clause License.

based on rat-socket.py
Copyright originally by  Peter "Marenthyu" Fredebold <marenthyu@marenthyu.de> (2016),
under the Eiffel Forum License, version 2

This module is built on top of the Sopel system.
http://sopel.chat/
"""
# Python imports
import sys
from threading import Thread
import json
import time
import traceback

# Sopel imports
from sopel.formatting import bold, color, colors
from sopel.module import commands, NOLIMIT, priority, require_chanmsg, rule
from sopel.tools import Identifier, SopelMemory
import ratlib.sopel
from sopel.config.types import StaticSection, ValidatedAttribute

from ratlib.api.v2compatibility import convertV1RescueToV2, convertV2DataToV1

log.startLogging(sys.stdout)
defer.setDebugging(True)

# ratlib imports
import ratlib.api.http
from ratlib.api.names import *

urljoin = ratlib.api.http.urljoin

import threading
import collections


## Start Config Section ##
class SocketSection(StaticSection):
    websocketurl = ValidatedAttribute('websocketurl', str, default='1234')
    websocketport = ValidatedAttribute('websocketport', str, default='9000')

def configure(config):
    ratlib.sopel.configure(config)
    config.define_section('socket', SocketSection)
    config.socket.configure_setting(
        'websocketurl',
        (
            "Websocket url"
        )
    )
    config.socket.configure_setting(
        'websocketport',
        (
            "Web Socket Port"
        )
    )


def shutdown(bot=None):
    # Ignored by sopel?!?!?! - Sometimes.
    print('[Websocket] shutdown for socket')
    reactor.stop()



def setup(bot):
    ratlib.sopel.setup(bot)
    bot.memory['ratbot']['log'] = (threading.Lock(), collections.OrderedDict())
    bot.memory['ratbot']['socket'] = Socket()

    if not hasattr(bot.config, 'socket') or not bot.config.socket.websocketurl:
        websocketurl = '123'
        websocketport = '9000'
    else:
        websocketurl = bot.config.socket.websocketurl
        websocketport = bot.config.socket.websocketport
    debug_channel = bot.config.ratbot.debug_channel or '#mechadeploy'

        # ---> Does not work as te board is not nessesarily set up yet! func_connect(bot)


