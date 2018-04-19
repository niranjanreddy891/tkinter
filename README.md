New tests should always use only one Tk window at once, like all the
current tests do. This means that you have to destroy the current window
before creating another one, and clean up after the test. The motivation
behind this is that some tests may depend on having its window focused
while it is running to work properly, and it may be hard to force focus
on your window across platforms (right now only test_traversal at
test_ttk.test_widgets.NotebookTest depends on this).


If you are using python-2.7 you need to use "Tkinter" (without quotes)

If you are using python-3.x you need to use "tkinter" (without quotes) 


To install tkinter on windows, follow these steps:

  1. Install latest version of pip
  2. If you are using pip already, make sure you are using the latest version of pip
  3. If you are using Anaconda, use this command
            
            pip install tkinter
            
  4. If you are not using Anaconda, open cmd and make sure you are in Scripts folder where your python is installed and then use the command 
            
            pip install tkinter 
