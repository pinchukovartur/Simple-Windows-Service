# Simple-Windows-Service
Python script that creates a service.
The service outputs "Hello World" to the file, each time the system is started


# Installation

  1. Install Microsoft Visual C++ 2010 Redistributable Package    (https://www.microsoft.com/en-us/download/details.aspx?id=5555)
  
  2. Install python 3.6+ (https://www.python.org/downloads/)      
When installing, select the "add to PATH" and install pip.

  3. Install win32 lib. At the command prompt, type pip install pypiwin32.    
3.1 In the path variable there must be a path to .../.../Python3.*/Scripts and  ../.../Python3.* 
  
  4. Add to the PATH variable. It should have 4 ways.
 1way - .../.../Python3.*/Scripts
 2way - ../.../Python3.* 
 3way - ../../Python3.*/Lib/site-packages/win32
 4way - ../../Python3.*/Lib/site-packages/pypiwin32_system32
 
  5. Run python install.py. This script creates a service WindowsMonitor.
  After the end of the service, the HelloWorld.txt file will be created in the folder ../../Python3.*/Lib/site-packages/win32
  
  
  
  
# Using

  You can run service use "python service.py start".
  For the debug run "python service.py debug"
  For the update run "python service.py update"
  For the stop run "python service.py stop"
  
All executable code is in the script "service.py" and is in the method "main". You can use this script as a wrapper for your scripts. Just be careful, the service may not understand where the python libraries are.
