import time
from datetime import datetime as dt

#In order to run the file in background (without terminal) just change the file extention from ".py" to ".pyw"
#In task manager you would be able to see the process ruuning there you can configure it to run at startup Windows.

hosts_temp = r"C:\Users\ASUS\Desktop\IMPORTANT\Python_mega_course\Applications\Website Blocker\host" #So that no need to run cmd as administrator everytime
hosts_path = r"C:\Windows\System32\drivers\etc"                 # change hosts_temp with hosts_path everywhere when you are using this application and run process as administrator
redirect = "127.0.0.1"
web_list = ["www.facebook.com","facebook.com","youtube.com","www.youtube.com" ] #Add Additional list of website as per your choice

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8 ) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16 ): #from  8 am to 4 pm
        print("Working Hours")
        with open(hosts_temp,"r+") as file: # "r+" is used to read as well as write in the file
            content = file.read()
            for website in web_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        print("Fun Hours")
        with open(hosts_temp,"r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in web_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)
