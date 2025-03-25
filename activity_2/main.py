import asyncio
from playwright.async_api import async_playwright
from models.home_page import Login
from models.inventory_page import Inventory_page
from models.product_page import Product_page
from models.cart import Cart

# the problem
'''
Abre un driver y navega a https://www.saucedemo.com/

Inicia sesión utilizando las credenciales proporcionadas:

Nombre de usuario: standard_user
Contraseña: secret_sauce

Valida que el inicio de sesión fue exitoso comprobando que se carga la página de productos.

Busca un producto (por ejemplo, "Sauce Labs Backpack") y verifica que aparece.

Agregar el producto al carrito y verificar que se haya agregado correctamente.

Cierra sesión de la aplicación. (no es lo mismo que salir del driver) 
'''

URL = "https://www.saucedemo.com"

# context manager (the keyword "with" is used to wrap the execution of a block of code)
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False) # headless=False to see the browser. if true, the browser will be hidden.
        page = await browser.new_page()
        print("webpage loading...")
        await page.goto(URL, wait_until="domcontentloaded")
        print("webpage loaded\n")

        print("***1. Login***")
        login = Login(page)
        username = "standard_user"
        password = "secret_sauce" # caution: hard-coded values
        await login.loginForm(username, password) 
        await page.screenshot(path="activity_2/screenshots/1.login_successful.png")
        print("Login successful + screenshot\n")

        print("***2. Search product***")
        product_name = "Sauce Labs Backpack" # caution: hard-coded values
        inventory = Inventory_page(page)
        await inventory.findProductByName(product_name)
        await page.screenshot(path="activity_2/screenshots/2.product_found.png")
        print("Product found + screenshot\n")

        print("***3. Add product to cart***")
        product = Product_page(page)
        await product.addProductToCart()
        print("Product added to cart")
        await product.goToShoppingCart()
        await page.screenshot(path="activity_2/screenshots/3.product_in_cart.png")
        print("Product in cart + screenshot\n")

        print("***4. Logout***")
        cart = Cart(page)
        await cart.openMenu()
        await cart.logout()
        await page.screenshot(path="activity_2/screenshots/4.logout_successful.png")
        print("Logout successful + screenshot\n")

        await asyncio.sleep(2) # wait for 2 seconds
        await browser.close()
        print("Browser closed\n")

asyncio.run(main()) # run the main function