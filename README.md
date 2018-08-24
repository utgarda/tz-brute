# Tz-Brute
Tezos password bruteforcer built on top of Arthur Breitman's fundraiser tools for validation.  
  
## How to use:  
##### Mac OS
###### Just run ```run-osx.sh``` or follow the steps below:

Firstly you'll need to install Python 3 if you don't have it already.  
pyenv is a great way to manage multiple python installations, if you want to use pyenv open up a Terminal and run:  
```bash
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
pyenv install 3.6.5
pyenv global 3.6.5
```  
If you don't want to use pyenv you can download Python 3 here:  
https://www.python.org/downloads/  
  
Next step is installing pip:
```bash
sudo easy_install pip
```  
  
Now we have pip we need to download and unzip this file:  
https://github.com/NODESPLIT/tz-brute/archive/master.zip  
You can then type "cd " into terminal (without brackets and with the space at the end) then drag and drop the newly unzipped folder into the terminal window and run the resulting command.  
  
We now need to install dependencies:
```bash
pip install -r requirements.txt
```

From here we can run Tz-Brute like so:
```bash
python main.py
```
  
##### Linux
###### probably works the same way
##### Windows
###### try it yourself
###
###
## Parameters:
##### Pattern:
Try to remember what you could put in that password, express it in the form like 
```
secr(3|e)t(key)?[0-9]{2}
```
Check https://github.com/asciimoo/exrex to see your options.

##### Public key (e.g. tz1ABCDeF...):
This is the address you were given as your Tezos address upon contribution.

##### Email address:
This is the email address you used when you contributed. This is CASE SENSITIVE.

##### Mnemonic (e.g. apples cat radio...):
This is the mnemonic you received upon contribution, it will be within the PDF you downloaded. It's a long string of words all in lowercase separated by spaces.

## Reset:
Without resetting the script will start from where it last left off.  
You can reset your anchor.json by running:
```bash
python main.py reset
```
This will backup your anchor.json with a timestamp, remember to delete these when you're done as they will have your contribution details in them.

###
###
###
###
___
###
###
###

built by Jon - admin of the [unofficial Tezos Telegram](https://t.me/tezosplatform)
  
web: [e.rroneo.us](http://e.rroneo.us/)  
email: [jon@e.rroneo.us](mailto:jon@e.rroneo.us)  
telegram: [@erroneous](https://t.me/erroneous)  

updated with pattern usage by E.T.
