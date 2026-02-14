from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("input[name='username']")
        self.password = page.locator("input[name='password']")
        self.login_btn = page.locator("button[type='submit']")
        self.dashboard = page.locator("text=Dashboard")

    def load(self):
        self.page.goto(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        )

    def login(self, user, pwd):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_btn.click()

    def is_login_success(self):
        try:
            expect(self.dashboard).to_be_visible(timeout=5000)
            return True
        except:
            return False
