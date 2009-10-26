# -*- coding: utf-8 -*-
from quinn.server.plugins import QuinnPlugin

class ControlsocketPlugin(QuinnPlugin):
    def __init__(self):
        print "init ControlsocketPlugin"