# Instagram Login Brute Force Script

## Description
This script attempts to perform a brute-force attack on Instagram's login page using a provided username and a list of potential passwords. It sends HTTP POST requests to the Instagram login endpoint with credentials from the password list and checks for successful authentication.

**Disclaimer:** This script is for educational purposes only. Unauthorized access to accounts or systems is illegal and unethical. Use it only in environments where you have explicit permission.

---

## Features
- Uses a username and a wordlist of passwords.
- Sends POST requests with appropriate headers to mimic a legitimate browser.
- Checks the server's JSON response to determine if the password is correct.
- Handles and logs incorrect password attempts and invalid responses.

---

## Requirements
- Python 3.x
- `requests` library

Install the required library using:
```bash
pip install requests
```

---

## Usage
1. Modify the script to include your target username by replacing `"erkan_rzgc"` in the `data_dict` dictionary.
2. Provide the path to your password list file in the `open` function. Example:
   ```python
   with open("/path/to/passwords.list", "r") as wordlist_file:
   ```
3. Run the script:
   ```bash
   python brute_force_instagram.py
   ```

---

## Code Explanation
### Key Components
- **`target_url`**: The URL for Instagram's login endpoint.
- **`data_dict`**: Contains the payload sent to the server, including the username and password.
- **`headers`**: Simulates a real browser request by including necessary headers.
- **Password Loop**: Reads passwords from the wordlist and attempts each one:
  ```python
  with open("/root/Downloads/passwords.list", "r") as wordlist_file:
      for line in wordlist_file:
          word = line.strip()
          data_dict["password"] = word
  ```
- **Response Handling**: Parses the server's JSON response to determine the result of each login attempt:
  ```python
  response_json = response.json()
  if response_json.get('authenticated') == True:
      print(f"[+] Got the password --> {word}")
      exit()
  ```

---

## Example Output
```
Trying password: password123
[-] Incorrect password: password123
Trying password: admin123
[-] Incorrect password: admin123
Trying password: letmein
[+] Got the password --> letmein
```

---

## Legal Disclaimer
This script is intended for authorized testing and educational purposes only. The misuse of this script can result in severe legal consequences. Always obtain proper authorization before attempting any security testing. The author of this script is not responsible for any misuse or damage caused by this tool.

