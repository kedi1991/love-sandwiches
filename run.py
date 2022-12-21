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
    """get data from the terminal
    """
    while True:
        print("Enter in the format (x,y,z,a,b,c)")
        data = input("\nPlease enter the sales: ")
        split_data = data.split(",")
        
        if validate_data(split_data):
            break
    return split_data    


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
        return False

    return True  


def update_sales_worksheet(data):
    """
    update the worksheet with a new row of data
    """
    print("Updating the sales worksheet")
    sales_worksheet = sales
    sales_worksheet.append_row(data)
    print("Success...")


def calculate_stock_data():
    """
    calculate the stock data
    Positive means surplus, negative means less
    """
    print("Calculating the stock ...")
    stock_data = SHEET.worksheet("stock").get_all_values()
    stock_row = stock_data[-1]

    return stock_row


def calculate_surplus_data():
    """
    Calculate the surplus data after sales for the day
    """
    sales_data = get_Sales_data()
    stock_data = calculate_stock_data()

    print(sales_data)
    print(stock_data)
    surplus_data = [int(sale) - int(stock) for sale, stock in zip(sales_data, stock_data)]
    
    return surplus_data


def main():
    """
    Call all the methods in teh program
    """
    calculate_stock_data()
    
    data = get_Sales_data()
    calculate_surplus_data()
    int_data = [int(num) for num in data]
    update_sales_worksheet(int_data)


print("welcome to the love sandwiches automation program")
main()