import os
import sys
import time
import argparse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

parser = argparse.ArgumentParser(
                    prog="WAFuzzer",
                    description="Tool for fuzzing WhatsApp bots.",
                    epilog="TheQmaks (c) 2022")
parser.add_argument("-n", "--number",
                    help="Set's target phone number.",
                    type=str, required=True)
parser.add_argument("-w", "--wordlist", help="Path to wordlist.",
                    type=str, required=True)
parser.add_argument("-d", "--delay", help="Delay between sending messages in seconds.",
                    type=int, required=False, default=1)

args = parser.parse_args()

if os.path.exists(args.wordlist):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, sys.maxsize)

    try:
        print("Waiting for auth...")
        driver.get("https://web.whatsapp.com/send?phone=" + args.number)

        with open(args.wordlist, "r") as file:
            while payload := file.readline().rstrip():
                msg_field = wait.until(EC.visibility_of_element_located((
                    By.XPATH,
                    "//*[contains(@class, 'copyable-text selectable-text') and @data-tab='9']"
                )))
                msg_field.click()
                msg_field.send_keys(payload)

                wait.until(EC.visibility_of_element_located((
                    By.XPATH,
                    "//*[@data-testid='send']"
                ))).click()

                time.sleep(args.delay)
            file.close()
    except Exception as ex:
        print(ex)
    finally:
        driver.quit()
else:
    print("The file doesn't exist. Enter the correct path to the wordlist.")