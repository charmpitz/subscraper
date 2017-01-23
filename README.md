# Subscraper
Use this to download subtitles for movies/series.

##### Installation:
```
sudo apt-get install python-pip python-qt4
sudo pip install bs4 requests subscraper
```

##### Usage:
```
subscraper /path/to/the/movie/file.mkv
```
A QT interface will open and now you can search and download the appropriate subtitle.

### Install in Nemo context menu for Linux Mint
This will only work if you are using Nemo. Right-clicking a video will give you the option to `Download subtitle`.

```
# Download file and restart Nemo
wget -N https://raw.githubusercontent.com/charmpitz/subscraper/master/subscraper/download-subtitle.nemo_action -P ~/.local/share/nemo/actions/ && nemo --quit
```
