import win32service
import win32event
import win32serviceutil
import servicemanager
import sys
import socket


class AppServerSvc(win32serviceutil.ServiceFramework):
    _svc_name_ = "WindowsMonitor"
    _svc_display_name_ = "Windows Monitor"

    def __init__(self, args):
        print("INIT")
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        print("STOP")
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        exit(1)

    def SvcDoRun(self):
        print("RUN")
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def main(self):
        f = open("HelloWorld.txt", "a")
        f.write("Hello World!")
        f.close()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(AppServerSvc)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(AppServerSvc)
