import urllib3
import urllib
import requests
import pandas as pd
import datetime

# censored
url = 'https://docs.google.com/forms/'

day_to_index = {
    6 : 'SUNDAY',
    0 : 'MONDAY',
    1 : 'TUESDAY', 
    2 : 'WEDNESDAY',
    3 : 'THURSDAY',
    4 : 'FRIDAY',
    5 : 'SATURDAY'
}

ex_data = pd.read_csv('info.csv')

email = ex_data['EMAIL'].values.tolist()[0]
name = ex_data['NAME'].values.tolist()[0]
grade = ex_data['GRADE'].values.tolist()[0]
section = ex_data['SECTION'].values.tolist()[0]

day = day_to_index[datetime.datetime.today().weekday()]
subjects = ex_data[day]

for subject in subjects:
    if (subject):
        print(email, name, grade, section, subject)

        # entry nummbers censored for privacy
        form_data = {
            'entry.blabla' : name,
            'entry.blabla' : grade, 
            'entry.blabla'  : section, 
            'entry.blabla' : subject, 
            'entry.blabla' : 'Yes', 
            'emailAddress'  : email
        }

        print(form_data)
        
        s = requests.Session()
        s.get(url)
        r = s.post(url, data=form_data)
        print(r)