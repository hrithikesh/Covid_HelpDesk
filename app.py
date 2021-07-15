from flask import Flask, render_template, request
from twilio.rest import Client
import requests
account_sid = 'AC27fd6c05cf7a90c6786544aa3fc098cfa'
auth_token = '5ee06bd7796c512330946afeb5f50430'
client = Client(account_sid,auth_token)
app = Flask(_name_, static_url_path='/static')
@app.route('/')
def registration_form():
    return render_template('test_page.html')

@app.route('/login_page',methods=['POST', 'GET'])
def login_registration_dtls():
    first_name = request.form['fname']
    last_name = request.form['lname']
    email_id = request.form['email']
    source_st = request.form['source_state']
    source_dt = request.form['source']
    destination_st = request.form['dest-state']
    destination_dt = request.form['destination']
    phoneNumer = request.form['phoneNumber']
    id_proof = request.form['idcard']
    date = request.form['trip']
    full_name = first_name + "." + last_name
    r = requests.get('https://api.covid19india.org/v4/data.json')
    json_data = r.json()
    cnt = json_data[destination_st]['districts'][destination_dt]['total']['confirmed']
    pop = json_data[destination_st]['districts'][destination_dt]['meta']['population']
    travel_pass = ((cnt/pop) * 100)
    if travel_pass < 30 and request.method == 'POST':
        status ='CONFIRMED'
        #client.messages.create(to="whatsapp:",
                               #from_='whatsapp:',
                              # body="Hello "+" "+full_name+" "+"Your Travel From" +" "+source_dt+" "+"To"+" "+destination_dt+" "
                              # +"Has "+status+" On "+date+", Apply later")
        return render_template('user_registration_dtl.html', var=full_name, var1=email_id, var2=id_proof,
                               var3=source_st, var4=source_dt, var5=destination_st, var6=destination_dt,
                               var7=phoneNumer, var8=date, var9=status)
    else:
        status = 'NOT CONFIRMED'
        #client.messages.create(to="whatsapp:",
         #                      from_='whatsapp:',
          #                     body="Hello " + " " + full_name + " " + "Your Travel From" + " " + source_dt + " " + "To" + " " + destination_dt + " "
           #                         + "Has " + status + " On " + date + ", Apply later")
        return render_template('user_registration_dtl.html', var=full_name, var1=email_id, var2=id_proof,
                               var3=source_st, var4=source_dt, var5=destination_st, var6=destination_dt,
                               var7=phoneNumer, var8=date, var9=status)

if _name_ == "_main_":
    app.run(port=5001,debug=True)
