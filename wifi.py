import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

for i in profiles:  # <-- Fix: changed 'profile' to 'profiles'
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    result = [b.split(":")[1][1:-1] for b in results if "Key Content" in b] 
    try:
        print("{:<30}|  {:<}".format(i, result[0]))
    except IndexError:
        print("{:<30}|  {:<}".format(i, ""))
input("\n\nPress enter to continue...")
