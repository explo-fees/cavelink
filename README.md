# README #

Cave-link is a radio device able to transmit data from a cave. You can add some measurement captors.
The data is consolidated on creator's website (database) and displayed on a [webpage where the data is dump to](http://www.cavelink.com/cl/da.php?s=106&g=1&w=0&l=10 title="example").

If you own a Cave-link, you should ask Felix Ziegler to get your specific URL.

If you want to know more about Cave-link system, the [website](http://www.cavelink.com title="CaveLink website") is the good place to start !

### What is this repository for? ###

This python library gather the data by parsing the webpage. You will then be able to store your data in your own database.
I will provide code samples to better explain this.

### How do I get set up? ###

    sudo apt-get update && sudo apt-get install git python-pip --yes
    git clone git@bitbucket.org:sebastienpittet/lcavelink.git
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
