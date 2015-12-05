#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Christopher C. Strelioff <chris.strelioff@gmail.com>
#
# Distributed under terms of the MIT license.

"""
consumer_key.py
=================

A Python 3 example of using the discogs-client with a consumer key and secret.
"""
import discogs_client as dc

try:
    # make sure there is a config.py file
    import config
except:
    raise Exception('Could not import config.py -- please create this file!')


# try to access the consumer key and secret
ckey = config.consumer_key
csecret = config.consumer_secret
default_ckey = (ckey == 'your-consumer-key-here')
default_csecret = (csecret == 'your-consumer-secret-here')

if default_ckey and default_csecret:
    raise Exception('Please set variables consumer_key and '
                    'consumer_secret in config.py!\n'
                    '--obtain consumer key and secret at:'
                    ' https://www.discogs.com/settings/developers')

uagent = ('ConsumerKeyExample/0.1 '
         '+https://github.com/cstrelioff/discogs-python3-examples')

print('\n===\n'
      'user agent: {0}\n'
      'consumer key: {1}\n'
      'consumer secret: {2}\n'
      '==='.format(uagent, ckey, csecret))

# set key, secret when initializing Client
d = dc.Client(uagent, consumer_key=ckey, consumer_secret=csecret)

# use OOB flow to authorize
request_token, request_secret, authorize_url = d.get_authorize_url()
print('\n===\n'
      'request_token: {0}\n'
      'request_secret: {1}\n'
      '==='.format(request_token, request_secret))

# - user verifies at specified url
print('\n** Please browse to the following URL:\n\n'
      '\t{0}\n\n'.format(authorize_url))

# request verfication code from user
oauth_verifier = input('** Please enter verification code: ')
access_token, access_secret = d.get_access_token(oauth_verifier)

print('\n===\n'
      ' * oauth_token: {0}\n'
      ' * oauth_secret: {1}\n\n'
      'Authentication complete. Future requests for this user '
      'can be signed with the above tokens--\n'
      'written to access_tokens.py.'.format(access_token, access_secret))

# write tokens to file
with open('access_tokens.py', 'w') as f:
    f.write('# oauth token and secret\n')
    f.write('access_token=\'{}\'\n'.format(access_token))
    f.write('access_secret=\'{}\''.format(access_secret))

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
