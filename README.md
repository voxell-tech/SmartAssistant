I have created a [playlist for this project.](https://www.youtube.com/watch?v=ncER2nHWTko&list=PLlnBGPe6GFdMxJwR8YXo_GfE1LtnTZfbk)

![Smart Assistant](./Pictures/SmartAssistant.png)

This is a basic overview of the Smart Assistant project:
![Plan](./Pictures/Plan.png)
# Smart Assistant

This project aims to create a fully functional smart assistant that is able to control your house and automate them. There are lots of features included in it.
You can look at our plan at [Milanote](https://app.milanote.com/1KPrwu1FVZ7S2G?p=UGrY3QR3ztP) and our [documentation](https://docs.google.com/document/d/1VVpCAUW7GcWCcOrWAtEkXxx1AH59J9e59fqEaYfNGSw/edit?usp=sharing).


**Planned advance features:**
- Chat with you via AI Chatbot ***(currently on going)***
- Detect faces
- Recognize faces
- Remember things / Set alarms
- Sound recognition (able to differentiate several people's sound)
- Control devices via PLC, Raspberry Pi, Arduino (I/O, IR)

*We are adding more features!!!*

## Usage

This project uses Unity (specifically the Universal Render Pipeline) as the GUI and Python as the API for the modules that users build. This project is tested on Windows 10 and is highly recommended to run in Windows OS although it is portable to Linux or Mac OS as Unity and Python are both multi-platform portable.

### Python

1. Create a virutal environment inside `./PythonAPI` and enter the virtual environement following this [tutorial](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/).
2. Run `setup.py` to install all necessary requirements.
3. Run `main.py`.

## Common Questions

**Microsoft Visual C++ is required**
- Install Visual Studio Installer via this [link](https://aka.ms/vs/16/release/vs_buildtools.exe) and install C++ build tools.

**How to solve pyttsx3 error?**
- The last line of the error should be something like this: `TypeError: item 2 in _argtypes_ passes a union by value, which is unsupported.`
- Head to [this](https://stackoverflow.com/a/60029700) thread and follow the step(s) given.

## Build Settings

- **Python**: Python 3.7.6
- **Unity URP**: 2020.2 (.0f1) *you can use any 2020.2 version but keep in mind that you will be changing the source code and out of sync from this repository*
- **Tensorflow**: v2.3.1

## Credits

- **Part of Code Structure**: [Jasper Project](https://github.com/jasperproject)