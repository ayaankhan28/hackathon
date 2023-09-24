from flask import Flask, render_template, url_for, request
import sys
import subprocess
import uuid
import json
import ast
import datetime
import gspread
app = Flask(__name__)
import pandas as pd
import os
import signal
###########################################  Wifi bssid
def get_connected_wifi_name():
  output = subprocess.check_output(["netsh", "wlan", "show", "interfaces"]).decode("utf-8")
  for line in output.splitlines():
    if "BSSID" in line:
      ssid = line.split(": ")[1].strip()
      return ssid
  return None
wifi_name = get_connected_wifi_name()
########################## MAC ADRESS
def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ':'.join([mac[i:i+2] for i in range(0, 12, 2)])[:-3]
mac_address = get_mac_address()
######################### OPENS LINK 
import webbrowser
url = "http://127.0.0.1:5000/" 
######################### GOOGL SHEET CONNECTION
import gspread

timeh = datetime.datetime.now().hour

def mark_attd(Email,name,batch):
    time = datetime.datetime.now().date()
    timeadd = datetime.datetime.now().strftime('%H:%M:%S')
    ac = gspread.service_account()
    ob = ac.open("attendance")
    check = f"{time}"
    #timeh = datetime.datetime.now().hour
    vericon = verf_cred(Email)
    if vericon=="verified":
        if check in [worksheet.title for worksheet in ob.worksheets()]:
            wks = ob.worksheet(f"{time}")
            cell = wks.find(Email)
            if cell:
        
                return "Already Marked"

            else:
                if timeh>9:
                    return "Unmarked"
            
                
                path = "D:\c language\WEB_DEV\counter4.0\email.xlsx"
                df = pd.read_excel(path,engine='openpyxl')
                email_exists = df[df['Email'] == Email]
                if not email_exists.empty:
                    
                    ##########
                    
                
                    data = [name, batch, timeadd, Email]
                    wks.append_row(data)
                    return "Marked"
                else:
                
                    return "Wrong email,check again!!"
                            


                    '''print("not contains")
                    data=[name,batch,timeadd,Email]
                    wks.append_row(data)
                    return "Marked"'''
            

        else:
        
            path = "D:\c language\WEB_DEV\counter4.0\email.xlsx"
            df = pd.read_excel(path,engine='openpyxl')
            email_exists = df[df['Email'] == Email]
            if not email_exists.empty:
            
            
                datai=["Name","Batch","Time","Email"]
                ob.add_worksheet(f"{time}",50,50)
                wks = ob.worksheet(f"{time}")
                data=[name,batch,timeadd,Email]
                wks.append_row(datai)
                wks.append_row(data)
                return "Marked"
            else:
            
                return "Wrong email,check again!!"
    else:
        return "Fake email address"
      





##################################GET credential
def get_cred(Email):
    mylist=[]
    path = "D:\c language\WEB_DEV\counter4.0\email.xlsx"
    dt = pd.read_excel(path,engine='openpyxl')
    email_exists = dt[dt['Email'] == Email]
    if not email_exists.empty:
        
       
        macR = dt[dt["Email"]==f"{Email}"].iloc[0]["MAC"]
        wifiR = dt[dt["Email"]==f"{Email}"].iloc[0]["WIFI"]
        batchR = dt[dt["Email"]==f"{Email}"].iloc[0]["Batch"]
        nameR = dt[dt["Email"]==f"{Email}"].iloc[0]["Name"]
        mylist.append(Email)
        mylist.append(nameR)
        mylist.append(batchR)
        mylist.append(macR)
        mylist.append(wifiR)
        return mylist
    else:
        return "Wrong email,check again!!"
###############################################VERIY CREDENTIAL

def verf_cred(Email):
    Edata = get_cred(Email)
    E_mac = Edata[3]
    E_wifi = Edata[4]
    if(wifi_name==E_wifi) and (mac_address==E_mac):
        return "verified"
    else:
        return "fake"




     




   
   
###########################################
webbrowser.open(url)

@app.route("/")
@app.route('/home')
def home():
    return render_template("index.html")


@app.route("/result",methods=['POST',"GET"])

def result():
   
    output=request.form.to_dict()
    email = output["email"]
    
    timem=datetime.datetime.now().minute
    #timeh=datetime.datetime.now().hour
    cred = get_cred(email)
   
    if cred!="Wrong email,check again!!":
       
        con = mark_attd(cred[0],cred[1],str(cred[2]))

        if timeh==9:
           
            return render_template("index.html",email=con)
        elif timeh>9:
            
            return render_template("index.html",email=f"Time over{con}")
        elif timeh<9:
           
            return render_template("index.html",email=f"window will open at 9 am")
    else:

        
        return render_template("index.html",email=cred)
       
    #return render_template("index.html",email=wifi_name+" mac:"+mac_address)

if __name__ == "__main__":
    app.run(debug=True,port=5000)
    #webbrowser.open(url)
    