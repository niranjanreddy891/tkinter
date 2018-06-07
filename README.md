New tests should always use only one Tk window at once, like all the
current tests do. This means that you have to destroy the current window
before creating another one, and clean up after the test. The motivation
behind this is that some tests may depend on having its window focused
while it is running to work properly, and it may be hard to force focus
on your window across platforms.


To test whether tkinter is installed properly or not, use 

            import Tkinter (2.7 version)
            import tkinter (3.x version)

If you are using python-2.7 you need to use "Tkinter" (without quotes) while importing the package

If you are using python-3.x you need to use "tkinter" (without quotes) while importing the package


To install tkinter on windows, follow these steps:

  1. Install latest version of pip
  2. If you are using pip already, make sure you are using the latest version of pip
  3. If you are using Anaconda, use this command
            
            pip install tkinter
            
  4. If you are not using Anaconda, open cmd and make sure you are in Scripts folder where your python is installed and then use the command 
            
            pip install tkinter 
