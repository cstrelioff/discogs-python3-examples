# discogs-python3-examples

Simple examples of accessing discogs with Python 3, using the official
discog-client Python library. More information is available here:

* The discog-client repository: https://github.com/discogs/discogs_client

* The discogs developer page: https://www.discogs.com/developers/

* Python 2 examples: https://github.com/jesseward/discogs-oauth-example

The above resources were also very helpful putting the examples in this
repository together.

## Install

The scripts in this repository assume that you are using Python 3, probably
Python 3.4+ at this point. I'd suggest making a virtual environment with 
Python 3 and installing the discogs-client using pip:

```bash
$ pip install discogs-client
```

This should also install *oauthlib*, *requests*, and *six* automatically.

## Scripts

### config_example.py

Copy this script to *config.py* and add your tokens/keys here-- hopefully this
helps (me and you) avoid the posting of tokens/keys to public repositories.

### user_token.py

If you only want to access *your own data* on discogs, you can get a user token
and authenticate as shown in this script.

### consumer_token.py

Soon...
