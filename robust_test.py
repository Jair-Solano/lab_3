from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
# robust_test.py — agregar al final del archivo
if __name__ == "__main__":
    pass 

try:
    # --- CASO 1: Login Seguro ---
    driver.get("https://saucedemo.com")
    user_input = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    user_input.send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    print("✅ Caso 1: Login exitoso.")

    # --- CASO 2: Agregar al Carrito ---
    btn_add = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    btn_add.click()
    badge = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    print(f"✅ Caso 2: Carrito tiene {badge.text} producto(s).")

    # --- CASO 3: Login Fallido ---
    driver.get("https://saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    error_container = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']")))
    print(f"✅ Caso 3: Error validado: {error_container.text}")

finally:
    driver.quit()
