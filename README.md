# Motion Based Intrusion Detection System using The Raspberry Pi

## Introduction
The Motion Based Intrusion Detection System is a computer vision application that detects the presence of a person in a designated area using motion detection algorithms. This system can be used as a security system for homes, offices, and other areas where unauthorized entry is not allowed.

#### Features
- The system detects motion in a designated area and sends a notification to the user.
- The system uses computer vision techniques to detect the presence of a person.
- The user can set up a designated area for the system to monitor.
- The user can adjust the sensitivity of the motion detection algorithm.
- The system provides a web interface for the user to monitor the detection status.

#### How it Works?
The Motion Based Intrusion Detection System uses computer vision techniques to detect the presence of a person in a designated area. The system captures a live video stream from a camera and applies a motion detection algorithm to detect any changes in the video. If the motion detection algorithm detects a change, it analyzes the video frames to determine if a person is present. If a person is detected, the system sends a notification to the user.

## Installation
To install and use the Motion Based Intrusion Detection System, follow these steps:
1. Clone this repository to your local machine.
2. Install the `telepot` module, by running
```
pip install telepot
```
3. Connect a PiCamera to your Raspberry Pi.
4. Now connect the\ GND, VCC and SIGNAL wire of the PIR Sensor to GPIO.BOARD Pins 2, 6 and 36 respectively.
5. Now open [BotFather](https://t.me/BotFather) on Telegram. Then create a New BOT and copy the `BOT_TOKEN` to the CODE. Save the code.
6. Run the system by running `python run.py`.
7. The BOT should be working now, and once motion is detected in front of the PIR Sensor, an alert will be sent to the user.

## License

This project is licensed under the MIT License.
