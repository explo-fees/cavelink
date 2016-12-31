# README #

Cave-link is a radio device able to transmit data from a cave. You can add some measurements captor.
The data is consolidated on creator's website (database) and displayed on a webpage.

Ask Felix to get your specific URL.

If you want to know more about Cave-link system, the [website](http://www.cavelink.com title="CaveLink website") is the good place to start !

### What is this repository for? ###

This python library allows you to gather the data by parsing the webpage. You will the be able to store your data in your own database.
I will provide code samples to better explain this.

### How do I get set up? ###

`sudo apt-get update && sudo apt-get install git python-pip --yes`
`git clone git@bitbucket.org:sebastienpittet/lcavelink.git`
`cd lcavelink`
`virtualenv venv`
`source venv/bin/activate`
`sudo pip install -r requirements.txt`

You should now be able to test the library with:
`python lcavelink.py`

### Contribution guidelines ###

* Feel free to submit issue or better, some pull requests !

### Who do I talk to? ###

sebastien at pittet dot org
Société Suisse de Spéléologie
