# Dropbox file fetcher

Fetch all files from your dropbox

## Usage

This guide assumes you have python3 installed.


1. Clone this repo locally:

```
mkdir -p ~/repos
cd ~/repos
git clone git@github.com:jspanjerberg/dropbox-fetcher.git
```

2. Create a dropbox API token via https://www.dropbox.com/developers/apps
3. Store token and run script:

```
TOKEN=db_copypasteyourtokenhere
mkdir -p ~/tokens
mkdir -p ~/storage/dropbox
echo $TOKEN > ~/tokens/.dropbox.secret
pip3 install dropbox
~/repos/dropbox-fetcher/dropbox_fetcher.py
```
