#basic_info.py
import platform
def  print_system_info():
    python_v = platform.python_version()
    platforma = str(platform.system())+ ", " + str(platform.architecture()[0])
    print("Używasz", python_v, "na platformie xd", platforma)

#print_system_info()