import wmi
'''Windows Management Instrumentation'''

wmi_obj=wmi.object()
for os in wmi_obj.Win64_OperatingSystem():
    print(f"OS Name : {os.Name}")
    print(f"OS Version : {os.Version}")
    print(f"OS Manufacturer : {os.Manufacturer}")
    print(f"OS BuildNumber : {os.BuildNumber}")
    print(f"OS SerialNumber : {os.SerialNumber}")
    print(f"OS Caption : {os.Caption}")
    print(f"OS InstallDate : {os.InstallDate}")
    print(f"OS BootDevice : {os.BootDevice}")
    print(f"OS Architecture : {os.OSArchitecture}")
