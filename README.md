# WAFuzzer - some kind of tool for whatsapp bots pentesting
Works very simple - sends messages from txt file to specified whatsapp user by phone number

## Installing:
ChromeDriver (you can also change to firefox in the source code) suitable for your system and browser version
```sh
git clone https://github.com/TheQmaks/WAFuzzer
```
```sh
cd WAFuzzer
```
```sh
pip install -r requirements.txt
```

## Running:
|Arguments                       |Short                          |Full                         |Type   |Required |Default|
|--------------------------------|-------------------------------|-----------------------------|-------|---------|-------|
|Number in international format  |`-n`                           |`--number`                   |string |true     |None   |
|Path to wordlist                |`-w`                           |`--wordlist`                 |string |true     |None   |
|Delay in seconds                |`-d`                           |`--delay`                    |integer|false    |1      |

#### Example:
```sh
python3 main.py --number +12025550188 --wordlist /usr/share/seclists/Fuzzing/XSS/XSS-Cheat-Sheet-PortSwigger.txt --delay 1
```
