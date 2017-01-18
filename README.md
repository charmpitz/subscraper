# Subscraper
Use this to download subtitles for movies/series.

##### Installation:
```
sudo apt-get install python-pip python-dev libxext-dev python-qt4 qt4-dev-tools build-essential

pip install subscraper
```

##### Usage:
```
subscraper /path/to/the/movie/file.mkv
```
A QT interface will open and now you can search and download the appropriate subtitle.

### Install in Nemo context menu for Linux Mint
This will only work if you are using Nemo. Right-clicking a video will give you the option to `Download subtitle`.

```
# Download file
wget https://raw.githubusercontent.com/charmpitz/subscraper/master/subscraper/download-subtitle.nemo_action

# Move file into ~/.local/share/nemo/actions
mv download-subtitle.nemo_action ~/.local/share/nemo/actions

# Then restart Nemo:
nemo --quit
```