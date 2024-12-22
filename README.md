# PiCamera2Stream

Basic script to run PiCamera2 as a streaming device.

## Resources & Guides

* ["Beginner Tutorial: How to Stream Video from Raspberry Pi Camera to Local Computer (P3 - piCamera2)" by Shilleh](https://www.youtube.com/watch?v=NOAY1aaVPAw)

## Dependencies

* Flask
* OpenCV-Python
* PiCamera2

## Installation

It is expected that you are running this on a Rasberry Pi with a PiCamera module attached to the `Camera` pin.

1. Make sure to update your app libraries:

```bash
sudo apt update
```

2. Install the following via sudo:

```bash
sudo apt install -y python3-flask python3-opencv python3-picamera2
```

## How to Run

There are several considerations... consider, before you proceed:

* This exposes the video feed to devices only on the same LAN as your Rasberry Pi. The stream will be inaccessible to devices not connected to your local network.
* At this current moment, the PiCamera2 by default engages in auto-exposure and auto-focus. This may lag your feed.

The current script that controls the magic is `test-picamera2.py`. To run it, simply call:

```bash
python3 test-picamera2.py
```

This will create a Flask application that acts as a server. The camera feed is accessible via port 5000 and with url `/video_feed`. To access the feed, you must know your Rasberry Pi's IP address. This is printed out for you at the start of the server's operation in the Terminal, so make sure to read that first.

Here's an example of how to access the camera feed:

```
http://<RP's IP ADDRESS>:5000/video_feed
```
