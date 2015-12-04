#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Christopher C. Strelioff <chris.strelioff@gmail.com>
#
# Distributed under terms of the MIT license.

"""
user_token.py
=================

A Python 3 example of using the discogs-client with a user token.
"""
import discogs_client as dc

try:
    # make sure there is a config.py file
    import config
except:
    raise Exception('Could not import config.py -- please create this file!')

# try to access the user token
utoken = config.user_token
if utoken == 'your-user-token-here':
    raise Exception('Please set variaible user_token in config.py!\n'
                    '--obtain token at:'
                    ' https://www.discogs.com/settings/developers')

uagent = ('UserTokenExample/0.1 '
         '+https://github.com/cstrelioff/discogs-python3-examples')

print('\n===\n'
      'user agent: {0}\n'
      'user token: {1}\n'
      '==='.format(uagent, utoken))

# Following the example here:
#
#    https://github.com/discogs/discogs_client#user-token-authentication
#
d = dc.Client(uagent, user_token=utoken)

me = d.identity()
print('\n* Identity')
print('I\'m {0} ({1}) from {2}.'.format(me.name, me.username, me.location))
print('My wantlist has {} items.'.format(len(me.wantlist)))

print('\n* Fetching data')
results = d.search('Stockholm By Night', type='release')
print('results.pages:', results.pages)
artist = results[0].artists[0]
print('artist.name:', artist.name)

print('\n* Artist ID')
artist_id = artist.id
print('artist.id: {}'.format(artist_id))
print('d.artist({}): {}'.format(artist_id, d.artist(artist_id)))

print('\n* Drill down')
releases = d.search('Bit Shifter', type='artist')[0].releases[1].\
    versions[0].labels[0].releases
print('len(releases): {}'.format(len(releases)))
