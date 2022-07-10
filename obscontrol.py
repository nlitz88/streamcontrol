"""
Module: obscontrol.py

This module is a collection of functions to abstract away the interaction with the OBS instance via OBSwebsockets
using the simpleobsws package.
"""

import simpleobsws
import asyncio
import json
# import logging
# logging.basicConfig(level=logging.DEBUG)

# Parameters for making obsws connection (optional).
parameters = simpleobsws.IdentificationParameters(ignoreNonFatalRequestChecks = False)
# Websocket client that we'll use to the connect and interface with the OBSWebsocket server on our OBS instance.
wsclient = simpleobsws.WebSocketClient(url = 'ws://localhost:4455', password = 'jOwVaOSG68HEWaMm', identification_parameters = parameters)

# Sample request function pulled from simpleobsws request sample. This will be used as the core for making obsws
# requests, as it abstracts away some of the common operations involved in making requests (like connecting, etc.).
async def make_request(request: simpleobsws.Request):
    await wsclient.connect() # Make the connection to obs-websocket
    await wsclient.wait_until_identified() # Wait for the identification handshake to complete

    request = simpleobsws.Request('GetVersion') # Build a Request object

    response = await wsclient.call(request) # Perform the request
    if response.ok(): # Check if the request succeeded
        print("Request succeeded! Response data:")
        print(json.dumps(response.responseData, indent=2))

    await wsclient.disconnect() # Disconnect from the websocket server cleanly

def switch_scene(new_scene):
    """Switch to provided scene with with name new_scene"""
    pass


if __name__ == "__main__":
    # Temporary for testing.
    loop = asyncio.get_event_loop()
    loop.run_until_complete(make_request(None)) 