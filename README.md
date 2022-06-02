# pwrap
command line utility for testing php local file inclusion 

## How to use

run:
`pip3 install -r requirements.txt`

launch pwrap by following these rules:

` python3 pwrap.py [URL] [File inclusion entry point] [wrapper] [yaml filename]`

where:

* URL = the url location you want to test your LFI
* File Inclusion entry point = the parameter that is vulnerable to LFI
* wrapper = the possible wrapper that pwrap uses
* yaml filename = yaml file where there are cookies information

The possible wrappers that pwrap uses are:

* file 
* filter
* data
* zip
* expect
* input



### Example usage

create a file with yaml extension and put the cookie informations:

```
---
"PHPSESSID": "abcderete43w",
"info1": "asdfasdad"
"info2": "sddskhfds"

```
then run the program:
`python3 pwrap.py http://somesite.com/ page file example-file.yaml`

If everything goes well, pwrap will open a browser window with the outcome of the local file inclusion

# Donation

If you want to support me donate monero coins at:
`4B9WQivaHfd3miDfPKEfCianocGpBx9d8FXycz2vmNW3aBDVKHgkBd9Gmapt4RBVEpTwnehujsiUBBehUiLvnEHs7VFstCC`

![immagine](https://user-images.githubusercontent.com/17337009/171695268-3996f8b8-ca26-4771-8e32-0f75f941a70c.png)


or here (0.0043 XMR):

![immagine](https://user-images.githubusercontent.com/17337009/171695566-420c3948-3fe2-4448-9ba1-472c6a4aaee5.png)



