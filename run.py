#!/usr/bin/env python3
import bottle
@bottle.route('/')
def index():
     return bottle.template('index')