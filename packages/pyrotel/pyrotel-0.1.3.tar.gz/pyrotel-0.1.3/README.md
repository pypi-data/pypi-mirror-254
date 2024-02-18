## pyrotel 0.1.2v

<h3 align="center">pyrotel is a library for telegram bots.</h3>

> ## Install and Update:
```python
pip install pyrotel
```

> ## START:
```python
from pyrotel import *

bot = client("TOKEN")

last_update = bot.get_updates()

while True:
	update = bot.get_last_update()
	if update != last_update:
		msg = message(update)
		if msg.text() == "/start":
			bot.send_message(msg.chat_id(), "wellcome to my bot.")
```

> ## Social Media:
<a href="https://t.me/persian_py">TELEGRAM</a><br>
<a href="https://github.com/Erfan-Bafandeh/pyrotel">GITHUB</a>
