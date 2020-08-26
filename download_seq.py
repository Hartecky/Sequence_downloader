from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os
import time

file_path_1 = 'C:\\Users\\amplicon\\Downloads\\downloaded_sequences.txt'
file_path_2 = 'C:\\Users\\amplicon\\Downloads\\seqdump.txt'
desktop_path = 'C:\\Users\\amplicon\\Desktop'

def check_file(file_to_check, path_1, path_2):
    """Checks if a file 'seqdump.txt' is in a directory, otherwise it waits untill it will appear
    
    :param file_to_check: path to a file which we want to download and we are waiting for
    """
    
    while not os.path.exists(file_to_check):
        time.sleep(1)

    if os.path.isfile(file_to_check):
        os.rename(file_to_check, file_path_1)
    else:
        raise ValueError("%s is not a file" % file_to_check)

def download_sequences(driver):
    """Download all avalaible sequences returned in a query search provided by function submit_values() in a submit_query.py file

    :param driver: webdriver defined by function open_blast() in a open_browser.py file
    """

    # On a redirected page find and choose download option
    download_button = driver.find_element_by_id("btnDwnld")
    download_button.click()

    download_fasta = driver.find_element_by_id("dwFSTAl")
    download_fasta.click()

    # Function call to check downloading file existing
    check_file(file_path_2, file_path_1, desktop_path)

    return(driver)

