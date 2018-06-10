import fitbit
import gather_keys_oauth2 as Oauth2
import pandas as pd
import datetime

CLIENT_ID = '22CTCF'
CLIENT_SECRET = 'fc4b857f2a57f05f87c46c41f319e8b4'

server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()

ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])

auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

def get_heartrate(base_date):
	hr = auth2_client.intraday_time_series('activities/heart', base_date=base_date, detail_level='1min')

def get_steps(dateTime)
	steps = auth2_client.time_series('activites/steps', user_id=None, base_date =base_date, period='1d')

def get_sleep(dateTime)
	efficiency = auth2_client.time_series('sleep/efficiency', user_id=None, base_date=base_date, period='1d')
	starttime = auth2_client.time_series('sleep/startTime', user_id=None, base_date=base_date, period='1d')	
	minutesasleep = auth2_client.time_series('sleep/minutesAsleep', user_id=None, base_date=base_date, period='1d')	