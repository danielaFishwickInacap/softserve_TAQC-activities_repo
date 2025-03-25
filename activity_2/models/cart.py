from playwright.sync_api import Page

class Cart():
    def __init__(self, page : Page):
        self.page = page
        self.container = page.locator("div[data-test='header-container']")
        self.menu_button = self.container.locator("button[id='react-burger-menu-btn']")
        self.logout_sidebar_link = self.container.locator("a[data-test='logout-sidebar-link']")

    async def openMenu(self):
        assert self.menu_button, "menu button NOT found"
        await self.menu_button.click()

    async def logout(self):
        assert self.logout_sidebar_link, "logout link NOT found"
        await self.logout_sidebar_link.click()