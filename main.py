import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from open_browser import open_blast
from submit_query import fill_values, refresh_page, submit_query
from redirect_page import redirect_page
from download_seq import download_sequences, check_file



'''
EXAMPLE SEQUENCE AND ORGANISM FOR TESTING

test_seq = 'GCCTTATCTGCTTCTCTCTCTCCAGTGGTCTCAAATCTCTCTGTGTGATCCCACTTGTCATCCTCCTCCACAACATAAAGCTTGAGACCATAACCCTTTAGCGTTTTCGGCTAAAGCTTTCGCTGACTACTACAACAATGGCGTCCTCATCCCTTTCCCCTGCTACTCAGGTTCACTCTTGATCGTTCGAATCGAAACAATCGGGTCTCTTCGTATAGGAATTTGGGTTTTTGAAAGTTTGGTTTTTTTTTTTGGTGGCAGCTTGGTTCTAGCAGAAGTGCTTTGATGGCGATGTCAAGTGGGTTGTTTGTGAAGCCAACGAAGATGAATCATCAAATGGTTAGAAAAGAGAAGATTGGATTGAGAATTTCTTGTCAAGCGTCGAGTATTCCAGCAGACAGAGTTCCAGATATGGAAAAGAGGAAGACTTTGAATCTTCTTCTTCTTGGGGCTCTTTCTCTACCTACTGGCTACATGCTTGTCCCTTACGCTACCTTCTTTGTTCCTCCTGGAACCGGAGGTGGAGGTGGTGGTACTCCAGCCAAGGATGCCCTTGGAAACGATGTAGTTGCAGCGGAATGGCTTAAGACTCATGGTCCCGGTGACCGAACCTTGACCCAAGGATTAAAGGGAGATCCGACTTACCTAGTTGTAGAGAACGACAAGACTCTAGCGACATACGGTATCAACGCAGTGTGCACTCATCTTGGATGTGTTGTGCCATGGAACAAAGCTGAGAACAAGTTTCTATGTCCTTGCCATGGATCCCAATACAACGCCCAAGGAAGAGTCGTTAGAGGTCCAGCCCCATTGTCGCTAGCGTTGGCTCACGCGGATATAGATGAAGCTGGGAAGGTTCTTTTTGTTCCATGGGTGGAAACTGACTTCAGGACTGGTGATGCTCCATGGTGGTCTTAAGACTCTTCAACAAGAAAAAGAGAAAGATTTGGTCTTTTTGTGTAAGACTTGTTTGAATGTTCTTATAATGTATAAGCTACATTTCATCGCAATTACTCTGTCTATGAAATATTATGTTCATTCACTTCCCA'

test_org = 'arabidopsis thaliana'
'''


def main():

    web_browser = open_blast()

    submit_query(web_browser, test_seq, test_org)
    redirect_page(web_browser)
    download_sequences(web_browser)

    web_browser.close()

if __name__ == '__main__':
    main()
