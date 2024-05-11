#!/usr/bin/env python3
import bottle
@bottle.route('/')
def index():
     return bottle.template('index')
@bottle.route('/<name>')
def message(name):
    the_message = f'Hello {name}!'
    return bottle.template('message_template', message=the_message)
