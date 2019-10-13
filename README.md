## Setting up Selenium with python
1. Install python
	
	https://www.python.org/downloads


2. Install pip 				

	run:
	> curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	
	then run: 
	> python get-pip.py
	
	(you may run into permission issues here)


3. Install these dependencies

	run:
	> pip install requests
	> pip install selenium


4. Get Chromedriver (or any other browser driver)

	Chromedriver is basically like a debug version of chrome that can be controlled with the selenium web driver api in python (or any language)

	Just download the executable from https://sites.google.com/a/chromium.org/chromedriver/
	and put it somewhere that you can reference it later.

## rs-sign-in.ahk supplementary files

> user.txt
contains the Gmail username

> password.txt
contains the password for all accounts (assumes the password is the same for all accounts)
