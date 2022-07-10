# streamcontrol
A collection of services to control an OBS live stream

## Object detection controlled stream planning
Here's how I'd like this to work ideally:
- Write a python module that contains an always-on, MQTT subscriber that just subscribes to each camera's MQTT channel. It will invoke the [obscontrol] functions according to what shows up on each camera channel (I.e., cam2 detects a bird--switch to that scene).
- Write another python module that will have a function that can be invoked for each camera device. Basically, this script will launch the gstreamer pipeline, object detection (not sure if that's in a separate pipeline or just in the python script), and then publishing data according to the output of the object detection.
- In the middle of all this is an MQTT broker of some sort, I guess mosquitto.