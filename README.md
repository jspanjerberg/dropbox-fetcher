# Dropbox file fetcher

Fetch all files from your dropbox

## Usage

This guide assumes you have python3 installed.

1. Create a dropbox API token via https://www.dropbox.com/developers/apps
1. Run the following commands in terminal from the root of this repository:

```
TOKEN=db_copypasteyourtokenhere
mkdir -p ~/tokens
mkdir -p ~/storage/dropbox
echo $TOKEN > ~/tokens/.dropbox.secret
pip3 install dropbox
~/repos/dropbox-fetcher/dropbox_fetcher.py
```
