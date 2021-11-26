import os
from twilio.rest import Client

# account_sid = 'ACd126ff90ad474dce221c63911edfb281'
# auth_token = '8fc6b15f67df19fc9c8213e9ef4449dd'
# client = Client(account_sid, auth_token)

# service = client.verify.services.create(
#                                      friendly_name='My First Verify Service'
#                                  )

# print(service.sid)
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure


def sendOTP(mobile):
    number="+91"+str(mobile)
    print(number)
    account_sid = 'ACd126ff90ad474dce221c63911edfb281'
    auth_token = '8fc6b15f67df19fc9c8213e9ef4449dd'
    client = Client(account_sid, auth_token)

    verification = client.verify \
        .services('VA8e84d57f593f9f38f9828552f3e601f1') \
        .verifications \
        .create(to=number, channel='sms')

    print(verification.status)
    return verification.status


def varifyOTP(mobile,otp):
    number="+91"+str(mobile)
    print(number)
    account_sid = 'ACd126ff90ad474dce221c63911edfb281'
    auth_token = '8fc6b15f67df19fc9c8213e9ef4449dd'
    client = Client(account_sid, auth_token)

    verification_check = client.verify \
        .services('VA8e84d57f593f9f38f9828552f3e601f1') \
        .verification_checks \
        .create(to=number, code=otp)

    print(verification_check.status)
    if verification_check.status=='approved':
        print("Truecheck")
        return True
    else:
        return False
    
