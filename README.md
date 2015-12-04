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

This should also install *oauthlib*, *requests*, and *six* automatically. If 
you want to install the exact package versions used when I developed these
scripts, I've included a *requirements.txt* file. To use this, install with:

```bash
$ pip install -r requirements.txt
```

## Scripts

**config_example.py**

Copy this script to *config.py* and add your tokens/keys here-- hopefully
this helps (me and you) avoid the posting of tokens/keys to public
repositories.

**user_token.py**

If you only want to access *your own data* on discogs, you can get a user token
and authenticate as shown in this script.

**consumer_key.py**

This script uses the OOB flow for OAuth authentication-- a url will be obtained
that allows the user to validate the script/app for access to their account
information.  The file *access_tokens.py* is written for future use of the
approved script/app using the access tokens obtained from discogs.

**previously_approved_key.py**

This script uses the access tokens obtained when the above example,
*consumer_key.py*, was run.  Because permission was already granted to the
script/app, the user information and example queries run without
interaction.
