from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()  # You can also use other drivers like Firefox, Edge, etc.

try:
    # Open the URL
    driver.get("https://jqueryui.com/droppable/")

    # Wait for the iframe to be present and switch to it
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, ".demo-frame"))
    )

    # Locate the draggable and droppable elements
    draggable = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "draggable"))
    )
    droppable = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "droppable"))
    )

    # Perform drag and drop
    actions = ActionChains(driver)
    actions.drag_and_drop(draggable, droppable).perform()

    # Optionally, wait for a few seconds to see the result
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.ID, "droppable"), "Dropped!")
    )

finally:
    # Close the driver
    driver.quit()