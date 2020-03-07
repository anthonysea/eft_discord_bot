import gspread, os, pprint
from collections import defaultdict
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

load_dotenv()
CREDENTIALS_JSON = os.getenv('CREDENTIALS_JSON')



def get_ammo_data() -> None:
    # scopes needed to access Google Spreadsheets and Google Drive API
    scope = ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive']
    
    # Use private service account key file for service account credentials
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_JSON, scope)

    # Use the created credentials to access Google Drive/Spreadsheets
    gc = gspread.authorize(credentials)

    sheet = gc.open("EFT 0.12 Ammo Chart")
    wks = sheet.worksheet("Sheet2")

    # debugging
    pp = pprint.PrettyPrinter(indent=4)
    
    chart_data = wks.get_all_values()[1:]

    # pp.pprint(chart_data)

    # use nested default dict to create items that are being accessed but have not been created
    ammo_chart_dict = defaultdict(lambda: defaultdict(list))

    for row in chart_data[0:5]:
        ammo_chart_dict[row[0]][row[1]] = [val for val in row[2:12]]

    pp.pprint(ammo_chart_dict)



    

def load_map_images(map_name: str) -> str:
    pass

if __name__ == '__main__':
    get_ammo_data()
