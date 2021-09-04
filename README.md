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
