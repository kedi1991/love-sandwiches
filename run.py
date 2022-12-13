import gspread

from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwiches")
sales = SHEET.worksheet("sales")
# data = sales.get_all_values()
# print(data)

def get_Sales_data():
    """get daat from the terminal
    """
    print("Enter in the format (x,y,z,a,b,c)")
    data = input("Please enter the sales: ")
    split_data = data.split(",")
    validate_data(split_data)

def validate_data(data):
    """check the data is 6 elements and integers only"""
    try:
        [int(num) for num in data]

        if len(data) != 6:
            raise ValueError(
                print(f"We need 6 elements, you provided {len(data)}")
            )
    except ValueError as e:
        print(f"You have entered invalid data: {e}")    
get_Sales_data()
