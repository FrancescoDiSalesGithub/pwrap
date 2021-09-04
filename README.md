# pwrap
command line utility for testing php local file inclusion 

## How to use

launch pwrap by following these rules:

` python3 pwrap.py [URL] [File inclusion entry point] [wrapper] `

where:

* URL = the url location you want to test your LFI
* File Inclusion entry point = the parameter that is vulnerable to LFI
* wrapper = the possible wrapper that pwrap uses

The possible wrappers that pwrap uses are:

* file 
* filter
* data
* zip
* expect
* input

### Example usage

` python3 pwrap.py http://somesite.com/ page file `


