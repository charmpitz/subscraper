# Subscraper
Use this to download subtitles for movies/series.

##### Installation
```
pip install subscraper
```

##### Usage:
```
subscraper /path/to/the/movie/file.mkv
```
A QT interface will open and now you can search and download the appropriate subtitle

### Install in Nemo context menu for Linux Mint
```
# Download file
wget https://raw.githubusercontent.com/charmpitz/subscraper/master/subscraper/download-subtitle.nemo_action

# Move file into ~/.local/share/nemo/actions
mv download-subtitle.nemo_action ~/.local/share/nemo/actions

# Then restart Nemo:
nemo --quit
```