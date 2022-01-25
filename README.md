# Dropbox file fetcher

Fetch all files from your dropbox via API.



## Installation (Linux)

This guide assumes you have python3 installed.

1. Clone this repo locally:

```
mkdir -p ~/repos
cd ~/repos
git clone git@github.com:jspanjerberg/dropbox-fetcher.git
```

2. Create a dropbox API token
- Browse to https://www.dropbox.com/developers/apps
- Create a personal app with name of your choosing
- Select the following permissions:
    - account_info.read
    - files_metadata.read
    - files_content.read
- Under "Settings", consider setting "Access token expiration" to `No expiry` if you plan on using the API regularly
- If happy with settings, generate an API token with the `generate` button
- Note: we do not need `App Key` or `App Secret`
- Copy the API token string

3. Store API token as secret

```
TOKEN=yourtokenhere
mkdir -p ~/tokens
mkdir -p ~/storage/dropbox
echo $TOKEN > ~/tokens/.dropbox.token.secret
```

4. If necessary, install dropbox for python

```
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
./dropbox_fetcher.py -s mydropbox/subfolder -d ~/temp/dbx-download

# specify path to token secret
./dropbox_fetcher.py -t ~/mytokens/.dropbox.token.secret
```
