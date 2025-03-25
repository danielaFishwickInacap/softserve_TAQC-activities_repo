from playwright.sync_api import Page

class Login:
    def __init__(self, page : Page):
        self.page = page
        self.container = page.locator(".login-box")
        self.username = self.container.locator("input[data-test='username']")
        self.password = self.container.locator("input[data-test='password']")
        self.login_button = self.container.locator("input[data-test='login-button']")

    async def loginForm(self, username, password):
        assert self.login_button, "login button not found"

        await self.username.fill(username)
        await self.password.fill(password)
        await self.login_button.click()