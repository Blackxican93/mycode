#!/usr/bin/python3
"""Alta3 Research | <your name here>
   Using an HTTP GET to determine when the ISS will pass over head"""

# python3 -m pip install requests
import requests
import time

def main():
    """your code goes below here"""
    #Weclome text
    print("Welcome to San Antonio, TX! The current rise time is 1646799020.")
    print("Oh ya you probably dont know what that means. Let me convert it to human time.")
    
    #Conversion
    unix_timestamp  = int("1646799020")
    utc_time = time.gmtime(unix_timestamp)
    local_time = time.localtime(unix_timestamp)
    
    #Print conversion
    print("The risetime is.....")
    print(time.strftime("%Y-%m-%d %H:%M:%S", local_time)) 
    print(time.strftime("%Y-%m-%d %H:%M:%S+00:00 (UTC)", utc_time))
    # print(time.ctime())
    



if __name__ == "__main__":
    main()

