"""
Shows basic use of Sheets API. Prints values from a Google Sheet
"""
from __future__ import print_function
from httplib2 import Http
from oauth2client import file, client, tools
from pprint import pprint
from googleapiclient import discovery

# Setup the Sheets API
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
store = file.Storage('client_secret.json')
credentials = None
if not credentials or credentials.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    credentials = tools.run_flow(flow, store)
service = discovery.build('sheets', 'v4', http=credentials.authorize(Http()))

spreadsheet_body = { #Here is where to add entries to request body
}

request = service.spreadsheets().create(body=spreadsheet_body)
response = request.execute()
pprint(response)

# Call the Sheets API
"""
SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
RANGE_NAME = 'Class Data!A2:E'
result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                             range=RANGE_NAME).execute()
values = result.get('values', [])
if not values:
    print('No data found.')
else:
    print('Name, Major:')
    for row in values:
        # Print columns A and E, which correspond to indices 0 and 4.
        print('%s, %s' % (row[0], row[4]))
"""