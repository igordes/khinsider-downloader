# khinsider-downloader
## Automatic khinsider album downloader made in **Python**
Poorly made automatic Khinsider site music downloader just for personal use, but If you'll like it - that's fine I guess.

For now it **supports only MP3** format and uses selenium.

By default it's set up to use **Edge** as default browser that could be easly swapped with other chromium based browsers (I'm not sure if every browser option will work on other ones [like Firefox for example]).

In the future I'm planning to ditch out selenium completely in the sake of using only requests packet.

### Usage

Just put an URL as an argument to the script

```cmd
.\khinsider-downloader.py <your link>
```

for example:

```cmd
.\khinsider-downloader.py https://downloads.khinsider.com/game-soundtracks/album/among-us
```
after that, the script should create the directory called as the title of the provided OST link and start downloading all of the mp3 files.

### Changing selenium browser

Simply change "edge" phrase with browser of your choice:

in row 8
```python
from selenium.webdriver.edge.options import Options
```
and row 16
```python
driver = webdriver.Edge(options=chromium_options)
```
