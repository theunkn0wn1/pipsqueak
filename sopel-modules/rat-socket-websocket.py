# coding: utf8
"""
rat-socket-websocket.py - Fuel Rats Rat Tracker module.
reimplemented against the `websocket` package

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
import websocket
# Sopel imports
from sopel.formatting import bold, color, colors
from sopel.module import commands, NOLIMIT, priority, require_chanmsg, rule
from sopel.tools import Identifier, SopelMemory
import ratlib.sopel
from sopel.config.types import StaticSection, ValidatedAttribute

from ratlib.api.v2compatibility import convertV1RescueToV2, convertV2DataToV1
import threading
import collections
# ratlib imports
import ratlib.api.http
from ratlib.api.names import *

urljoin = ratlib.api.http.urljoin


# # Start Config Section ##
class SocketSection(StaticSection):
    websocketurl = ValidatedAttribute('websocketurl', str, default='1234')
    websocketport = ValidatedAttribute('websocketport', str, default='9000')


def configure(config):
    """
    called during Sopel Configure
    :param config:
    :return:
    """
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


def setup(bot):
    """
    called during Sopel setup
    :param bot: Sopel bot handle
    :return:
    """
    ratlib.sopel.setup(bot)
    bot.memory['ratbot']['log'] = (threading.Lock(), collections.OrderedDict())
    bot.memory['ratbot']['socket'] = Socket()


class Socket:
    def __enter__(self):
        return self._lock.__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._lock.__exit__(exc_type, exc_val, exc_tb)

    def __init__(self):
        self._lock = threading.RLock()
        # print("Init for socket called!")


class RatSocket(Thread):
    # define class var bot, for external usage
    socket = None  # lets keep with the convention shall we?
    started = False
    # we are not yet connected
    connected = False

    def __init__(self, bot=None, url="dev.api.fuelrats.com"):
        # call the super
        super().__init__()
        # setup the Socket lock
        self.socket = Socket()
        self.token = None
        self.url = url
        self.bot = bot
        RatSocket.socket = self

    def _on_recv(self, socket, message):
        print("got message: data is {}".format(message))

    def _on_open(self, socket):
        print("[Ratsocket] Connection to API established.")
        # Api.my_websocket = socket

    def _on_error(self, socket, error):
        print("[Ratsocket] some error occured!\n{}".format(error))

    def _on_close(self, socket):
        print("[Ratsocket] ####\tsocket closed\t####")

    def run(self):
        if RatSocket.started:
            raise RuntimeError("[Rattracker] something tried spawning a sceond API instance!")
        print("[Ratsocket] Thread started.")
        # thread started.
        RatSocket.started = True
        print("[Ratsocket] using {} as connnection URL".format(self.url))
        self.socket = websocket.WebSocketApp(url=self.url.format(token=self.api_token),
                                             on_close=self._on_close,
                                             on_error=self._on_error,
                                             on_message=self._on_recv)
        self.socket.on_open = self._on_open
        print("running client....")
        self.socket.run_forever()
        print("Exiting thread...")

    async def send_message(self, message):
        # self.socket: ws_client.WebSocketApp
        await self.socket.send(message)
        # await self.socket.close()


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


