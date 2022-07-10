"""
Module: obscontrol.py

This module is a collection of functions to abstract away the interaction with the OBS instance via OBSwebsockets
using the simpleobsws package.
"""

from multiprocessing.connection import wait
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
    response = await wsclient.call(request) # Perform the request
    await wsclient.disconnect() # Disconnect from the websocket server cleanly
    return response

# Function to switch the current program scene in OBS. Uses "make_request" to actually perform the request.
# Functions like this are just wrappers for different types of actions.
async def switch_scene(new_scene):
    """Switch to provided scene with with name new_scene"""

    request = simpleobsws.Request("SetCurrentProgramScene", {
        "sceneName": new_scene
    })
    response = await make_request(request)
    if response.ok(): # Check if the request succeeded
        print(f"Request succeeded! Switched to {new_scene}")
    else:
        print(f"Request to switch to {new_scene} failed!")

if __name__ == "__main__":
    # Temporary for testing.
    loop = asyncio.get_event_loop()
    loop.run_until_complete(switch_scene("Scene2"))