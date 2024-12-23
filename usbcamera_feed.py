from flask import Flask, Response
import cv2
import argparse

def returnCameraIndexes():
    # check the first 10 indices
    index = 0
    arr = []
    i = 10
    while i > 0:
        cap = cv2.VideoCapture(index)
        if cap.read()[0]:
            arr.append(index)
            cap.release()
        index += 1
        i -= 1
    return arr