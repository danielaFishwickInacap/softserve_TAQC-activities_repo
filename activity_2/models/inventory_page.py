from playwright.sync_api import Page

class Inventory_page:
    def __init__(self, page : Page):
        self.page = page
        self.container = page.locator("div[data-test='inventory-item']")
        self.inventory_item_name = self.container.locator(f"a:has(div[data-test='inventory-item-name'])")
    
    async def findProductByName(self, productName : str):
        product_locator = self.inventory_item_name.locator(f"div:has-text('{productName}')")
        assert product_locator, f"Product with name {productName} not found"
        await product_locator.click()