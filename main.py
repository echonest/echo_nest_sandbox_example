"""
Sandbox Example (main.py)

[The Echo Nest](the.echonest.com) 2011

This is a simple example demonstrating how to take advantage of the
Sandbox Assets in The Echo Nest API.

This example assumes that you have a basic understanding of Python.
"""

# This example uses the [web.py](http://webpy.org/) framework.
# Install it by running `sudo easy_install web.py`.
import web

# It also takes advantage of pyechonest, the official
# Python module for interfacing with The Echo Nest API.
# Install it with `sudo easy_install pyechonest`.
from pyechonest import config
from pyechonest import sandbox

# Use the `config` submodule to store your Echo Nest credentials.
# You can obtain these credentials
# by [signing up](http://developer.echonest.com/account/profile)
# as a developer for The Echo Nest API.
config.ECHO_NEST_API_KEY = "YOURAPIKEYHERE"
config.ECHO_NEST_CONSUMER_KEY = 'YOURCONSUMERKEYHERE'
config.ECHO_NEST_SHARED_SECRET = 'YOURSHAREDSECRETHERE'

urls = (
    '/', 'index', # A listing of assets available
    '/play/(.*)', 'play' # Play a specific asset
)
render = web.template.render('templates')
app = web.application(urls, globals())
sandbox_name = 'emi_bluenote'

class index:        
    def GET(self):
        """
        Sandbox/List is a paginated listing of all of the assets
        available in the sandbox.
        """
        listing = sandbox.list(sandbox_name)
        return render.index(listing=listing)

class play:
    def GET(self, item_id):
        """
        Once you have an item_id taken from the Sandbox/List, you
        can gain access to that asset with Sandbox/Access.
        You will recieve a URL for the asset which will expire
        in ten minutes.
        """

        asset = sandbox.access(sandbox_name, asset_ids=[item_id])[0]
        return render.info(asset=asset)

if __name__ == "__main__":
    # start the web.py server.
    app.run()
