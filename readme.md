markdown
Copy code
# Face Gesture Recognition System for Controlling PC

A professional Python-based Human Computer Interface application designed to perform cursor functions using face movements and gestures, featuring built-in face detection and recognition for enhanced security. The application utilizes the built-in webcam for input, and it allows saving the faces of authorized users while operating in the **-allow_grow** mode.

## Prerequisites

- Windows Operating System
- Python 3.6.x

## Installation

### Step 1: Install Python 3.6.8

1. Download Python 3.6.8 from the following link: [Python 3.6.8](https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe).
2. Run the installer.
3. **Important:** Check the `Add Python 3.6 to PATH` box.
4. Select `Install Now`.

### Step 2: Install Required Libraries

1. Open `cmd.exe` from the `proj2` directory.
2. Run the following commands:

```sh
pip install -U pip
pip install -U setuptools
pip install -U wheel
pip install -r requirements.txt
pip install Xlib
pip install matplotlib
pip install openvino==2021.4.0
pip install python3-xlib==0.15
pip install PyAutoGUI==0.9.38
Running the Code
Running with a Video File
To run the code with a video file, use the following command:

sh
Copy code
python main.py --input demo.mp4 --debug --show-bbox --enable-mouse --mouse-precision low --mouse-speed fast
Running with a Camera Input
To run the code with camera input, use the following command:

sh
Copy code
python main.py --input cam --debug --show-bbox --enable-mouse --mouse-precision low --mouse-speed fast
Notes
Please ensure you are in the proj2 directory when running the commands.


This README provides a clear and concise guide for users to set up and run your project.



