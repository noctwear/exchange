import fitbit
from python_fitbit_master import gather_keys_oauth2 as Oauth2
import pandas as pd
import datetime

CLIENT_ID = heydontthinkyoucanhackthis
CLIENT_SECRET = heydontthinkyoucanhackthis

server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()

ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])

auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

def ts_to_df(blob_data):
	time_list = []
	val_list = []

	for i in blob_data:
		val_list.append(i['value'])
		time_list.append(i['time'])

def get_heartrate(base_date):
	blob = auth2_client.intraday_time_series('activities/heart', base_date=base_date, detail_level='1min')
	blob_data = blob['activities-heart-intraday']['dataset']
	ts_to_df(blob_data=blob_data)
	heartdf = pd.DataFrame({'Heart Rate':val_list, 'Time':time_list})

def get_steps(base_date):
	blob = auth2_client.time_series('activites/steps', user_id=None, base_date =base_date, period='1d')
	blob_data = blob['activities-steps']['dataset']
	ts_to_df(blob_data=blob_data)
	stepsdf = pd.DataFrame({'Steps':val_list, 'Time':time_list})

def get_sleep(base_date):
	efficiency = auth2_client.time_series('sleep/efficiency', user_id=None, base_date=base_date, period='1d')
	starttime = auth2_client.time_series('sleep/startTime', user_id=None, base_date=base_date, period='1d')	
	minutesasleep = auth2_client.time_series('sleep/minutesAsleep', user_id=None, base_date=base_date, period='1d')
	efficiency_data = efficiency['value']
	starttime_data = starttime['value']
	minutesasleep_data = minutesasleep['value']
	sleepdf = pd.DataFrame({'efficiency':efficiency_data, 'minutesalseep': minutesalseep_data, 'starttime': starttime_data})
