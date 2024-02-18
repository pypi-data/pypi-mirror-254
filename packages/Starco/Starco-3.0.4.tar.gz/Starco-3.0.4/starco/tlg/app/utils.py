import re
def get_number(txt):
    txt = str(txt)
    numbers =re.findall(r'\d+', txt)
    if numbers:
        sn = ''.join(numbers)
        sn = sn.lstrip('0')
        return int(sn)

def session_number(number:int):
    return f"+{number}.session"



import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_country_code
from phonenumbers.phonenumberutil import region_code_for_number
import pycountry

def get_country_name(phone_number):
    try:
        phone_number = str(phone_number)
        if phone_number[0]!='+':phone_number=f"+{phone_number}"
        pn = phonenumbers.parse(phone_number)
        country = pycountry.countries.get(alpha_2=region_code_for_number(pn)).name
        country = country.replace(' ','_').replace(',','')
        return country
    except:return 'other'

