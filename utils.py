import gspread, os
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

load_dotenv()
CREDENTIALS_JSON = os.getenv('CREDENTIALS_JSON')



def load_ammo_chart() -> None:
    # scopes needed to access Google Spreadsheets and Google Drive API
    scope = ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive']
    
    # Use private service account key file for service account credentials
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_JSON, scope)

    # Use the created credentials to access Google Drive/Spreadsheets
    gc = gspread.authorize(credentials)

    wks = gc.open("EFT 0.12 Ammo Chart").sheet1

    print(wks)
    

def load_map_images(map_name: str) -> str:
    pass

if __name__ == '__main__':
    load_ammo_chart()
