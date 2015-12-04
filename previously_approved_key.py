#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Christopher C. Strelioff <chris.strelioff@gmail.com>
#
# Distributed under terms of the MIT license.

"""
previously_approved_key.py
=================

A Python 3 example of using the discogs-client with a consumer key and secret,
as well as access tokens from previous user validation of app/script.
"""
import discogs_client as dc

try:
    # make sure there is a config.py file
    import config
except:
    raise Exception('Could not import config.py -- please create this file!')

try:
    # try to access the consumer key and secret
    ckey = config.consumer_key
    csecret = config.consumer_secret
except:
    raise Exception('Please set variables consumer_key and '
                    'consumer_secret in config.py!\n'
                    '--obtain consumer key and secret at: \n'
                    '  https://www.discogs.com/settings/developers')

try:
    # make sure there is a access_tokens.py file
    import access_tokens
    access_token = access_tokens.access_token
    access_secret = access_tokens.access_secret
except:
    raise Exception('Could not import access_tokens.py -- please create this '
                    'file using the script consumer_key.py!')

uagent = ('PreviousKeyExample/0.1 '
         '+https://github.com/cstrelioff/discogs-python3-examples')

print('\n===\n'
      'user agent: {0}\n'
      'consumer key: {1}\n'
      'consumer secret: {2}\n'
      'access key: {3}\n'
      'access secret: {4}\n'
      '==='.format(uagent, ckey, csecret, access_token, access_secret))

# set key, secret when initializing Client
# -- also user access token & secret from previous validation
d = dc.Client(uagent, consumer_key=ckey, consumer_secret=csecret,
              token=access_token, secret=access_secret)

# Again, following the example here (sanme as user_token.py):
#
#    https://github.com/discogs/discogs_client#user-token-authentication
#
user = d.identity()
print('\n* Identity')
print('You are {0} ({1}) from {2}.'.format(user.name, user.username,
                                           user.location))
print('Your wantlist has {} items.'.format(len(user.wantlist)))

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
