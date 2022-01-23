# Dropbox file fetcher

Fetch all files from your dropbox via API

This guide assumes you have python3 installed.

## Installation

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
```

## Usage examples

```
cd ~/repos/dropbox-fetcher/

# download all files in your dropbox, skip existing
./dropbox_fetcher.py

# download all files, overwrite existing
./dropbox_fetcher.py -f

# specify source and destination
./dropbox_fetcher.py -s "mydropbox/subfolder" -d "~/temp/dbx-download"

# specify path to token secret
./dropbox_fetcher.py -t "~/mytokens/.dropbox.secret"
```
