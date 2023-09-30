import platform

def print_system_info():
    # Print system information
    print(f"System: {platform.system()}")
    print(f"Version: {platform.version()}")
    print(f"Release: {platform.release()}")
    print(f"Platform: {platform.platform()}")
    print(f"Processor: {platform.processor()}")
    print(f"Windows Version: {platform.win32_ver()}")

# Call the function to print system information
print_system_info()
