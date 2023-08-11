# ------------------------------------------------------------------------------------
#|  ==============================================================================    |
#| | Security Scanner                                                               | |
#| | Author: HARIS                                                                  | |
#| | Instagram: @risss_min1_chemistry                                               | | 
#| |                                                                                | |
#| | Description: This script performs security scans for common vulnerabilities!   | |
#|  ==============================================================================    |
# ------------------------------------------------------------------------------------

"""Scanner"""


import requests
import re

def scan_xss(url):
    with open('payload_xss.txt') as payload_file:
    payload_content = payload_file.read()
    
    response = requests.post(url, data={"input_field": payload})
    if "XSS!" in response.text:
        print("XSS vulnerability found!")

def scan_csrf(url):
    headers = {"Referer": url}
    response = requests.get(url, headers=headers)
    csrf_token = re.search(r"<input type=\"hidden\" name=\"csrf_token\" value=\"(.*?)\">", response.text).group(1)
    payload = {"csrf_token": csrf_token, "action": "transfer_funds", "amount": 100}
    response = requests.post(url, data=payload, headers=headers)
    if "Transfer successful" in response.text:
        print("CSRF vulnerability found!")

def scan_open_redirect(url):
    payload = {"next": "http://evil.com"}
    response = requests.get(url, params=payload)
    if "evil.com" in response.url:
        print("Open redirect vulnerability found!")

def scan_all(url):
    scan_xss(url)
    scan_csrf(url)
    scan_open_redirect(url)

# Meminta URL dari pengguna
target_url = input("Masukkan URL situs web yang ingin Anda pindai: ")
scan_all(target_url)
