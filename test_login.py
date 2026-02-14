from pages.login_page import LoginPage
from utils.excel_utils import ExcelUtils


def test_login_ddtf(page):
    excel = ExcelUtils("data/login_data.xlsx")
    login_page = LoginPage(page)

    for data in excel.get_data():
        login_page.load()

        login_page.login(data["username"], data["password"])

        if login_page.is_login_success():
            excel.write_result(data["row"], "PASS")
        else:
            excel.write_result(data["row"], "FAIL")

        page.context.clear_cookies()
