from kavenegar import *
from .env import kavehnegar_api_key

def sms_otp_code(phone_number, code):
    api = KavenegarAPI(kavehnegar_api_key)
    params = {'sender': '1000689696', 'receptor': phone_number, 'message': f'کد تایید شما -{code}'}
    response = api.sms_send( params)
    return response

