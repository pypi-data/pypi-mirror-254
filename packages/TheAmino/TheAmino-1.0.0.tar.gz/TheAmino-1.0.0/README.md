# An API for amino bot using Python

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)                 
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)   

## Follow us
- Telegram Channel [Click](https://t.me/the_code_24)
- YouTube channel  [Click](https://youtube.com/@the_code692)
- Discord Server   [Click](https://discord.com/invite/jEcCwE8cte)

## Usage

- Make sure you have Python installed in your system.
- Run Following command in the CMD.
 ```
  pip install TheAmino
  ```
## Example

- It works like the Amino.py's API but with added features like commands or answer for example:

 ```
from TheAmino import TheAmino

client = TheAmino("Your Email", "Your Password") # Or you use login.json
client.prefix = "!"  # set the prefix default is /



@client.command("check")
def ping(data):
    data.subClient.send_message(data.chatId, message="𝗕𝗼𝘁 𝗮𝗰𝘁𝗶𝘃𝗲 ✓")



client.launch()
print("Bot is running")
  ```

## Note 
- I have tried to implement all the functionality, it might have some bugs also. Ignore that or please try to solve that bug.

## Credits
- Credits goes to BotAmino
- Big shout out to Phoenix
