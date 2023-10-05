from robocorp.tasks import task
from robocorp import browser

from RPA.HTTP import HTTP
from RPA.Excel.Files import Files

@task
def order_robots_from_RobotSpareBin():
    """
    Orders robots from RobotSpareBin Industries Inc.
    Saves the order HTML receipt as a PDF file.
    Saves the screenshot of the ordered robot.
    Embeds the screenshot of the robot to the PDF receipt.
    Creates ZIP archive of the receipts and the images.
    """
    open_browser()
    download_excel()
    read_excel()

def open_browser():
    """Navigates to the given URL"""
    browser.goto("https://robotsparebinindustries.com/#/")    

def download_excel():
    """Downloads excel file from the given URL"""
    http = HTTP()
    http.download(url="https://robotsparebinindustries.com/orders.csv", overwrite=True)

def read_excel():
    """Read data from excel"""
    file = Files()
    file.open_workbook("orders.csv")
    worksheet = file.read_worksheet_as_table("data", header=True)
    file.close_workbook()