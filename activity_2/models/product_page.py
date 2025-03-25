from playwright.sync_api import Page

class Product_page():
    def __init__(self, page : Page):
        self.page = page
        self.container = page.locator("div[data-test='inventory-item']")
        self.add_to_cart_button = page.locator("button[data-test='add-to-cart']")
        self.shopping_cart_link = page.locator("a[data-test='shopping-cart-link']")

    async def addProductToCart(self):
        assert self.add_to_cart_button, "add to cart button NOT found"
        await self.add_to_cart_button.click()

    async def goToShoppingCart(self):
        assert self.shopping_cart_link, "shopping cart link NOT found"
        await self.shopping_cart_link.click()