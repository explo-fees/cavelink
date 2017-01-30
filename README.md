# README #
[![Build Status](https://travis-ci.org/SebastienPittet/lcavelink.svg?branch=master)](https://travis-ci.org/SebastienPittet/lcavelink)

### About Cave-Link ###
Cave-link is a radio device able to transmit data from a cave. You can add some measurement sensors.
The data is consolidated on creator's server (database) and displayed through a webpage where the data is dump to, as [this example shows](http://www.cavelink.com/cl/da.php?s=106&g=1&w=0&l=10 title="example").

If you own a Cave-link, you should ask Felix Ziegler to get your specific URL, for the sensors you have.

If you know nothing about Cave-link system, the official [website](http://www.cavelink.com title="CaveLink website") is the good place to start ! Or maybe, you can also start with [Wikipedia](https://de.wikipedia.org/wiki/Cave-Link title="Wikipedia CaveLink").

### What is this repository for? ###

This python library gather the data by parsing the webpage. You will then be able to display the data on your dashboard or store it to your own database.
I also provide code samples to better explain this -[see directory 'samples'](https://github.com/SebastienPittet/cavelink/tree/master/samples)-.

### How do I get set up? ###
Written for python v.2.7.

To ensure a proper setup, I recommend the use of virtualenv (but optionnal).

    sudo apt-get update && sudo apt-get install git python-pip --yes
    git clone git@github.com:SebastienPittet/lcavelink.git
    cd lcavelink
    virtualenv venv
    source venv/bin/activate
    sudo pip install -r requirements.txt

You should now be able to test the library with:
    python lcavelink.py

### Contribution guidelines ###

Feel free to submit issue or better, some pull requests !

### Who do I talk to? ###

[sebastien at pittet dot org](https://sebastien.pittet.org)
