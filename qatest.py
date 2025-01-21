from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import openai
import time


# Configure browser options
options = Options()
options.headless = False  # Disable headless mode to see the browser
options.add_argument("start-maximized")  # Open browser in maximized window

# Set up WebDriver
service = Service('/opt/homebrew/bin/chromedriver')  # Replace with the path to your WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Example: Navigate to a website
driver.get("https://coveycenter.csstix.com/customer.php")
print("Page Title:", driver.title)

# Close the browser

driver.quit()
def generate_script(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate Python Selenium code to: {prompt}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

def run_test(script):
    exec(script)

prompt = "Log into https://coveycenter.csstix.com/customer.php with username 'khaag' and password 'Yellow21!', click 'Login'"
generated_code = generate_script(prompt)
print("Generated Code:\n", generated_code)

try:
    run_test(generated_code)
except Exception as e:
    print("Test failed:", e)

# Testing this out
# now I am testing from the other side

