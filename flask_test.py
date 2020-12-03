from flask import Flask, render_template
import requests
import json
from auth.vmanage_auth import login

app = Flask(__name__)

def get_devicecontrollers():
    session = login()

    baseurl = "https://10.100.99.28:8443"

    controller_endpoint = "/dataservice/system/device/controllers"
    url = f"{baseurl}{controller_endpoint}"
    print('Exectuing following URL:\n',url ,'\n')
    response_controller = session.get(url, verify=False)

    devices = response_controller.json()['data']

    #for device in devices:
    #    if device['deviceType']=='vmanage':
    #        print('success - we have a vmanage')
    #    print(f"Device controller => {device['deviceType']} with System IP address {device['deviceIP']}")
    
    return devices


@app.route('/')
#def index():
#    h1_variable = 'Lewis'
#    h1_list = list(h1_variable)
#    h2_dict = {'Name':'Lewis'}
#    return render_template('basic2.html',h1_variableh1=h1_variable,h1_list=h1_list, h2_dict=h2_dict)
def index():
    get_devicecontrollers()
    return render_template('basic_flask.html',devices=devices)

if __name__ == "__main__":
    app.run()