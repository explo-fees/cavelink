README
======

|Build Status|

About Cave-Link
~~~~~~~~~~~~~~~

Cave-link is a radio device able to transmit data from a cave. You can
add some measurement sensors. The data is consolidated on creator’s
server (database) and displayed through a webpage where the data is dump
to, as `this example shows`_.

If you own a Cavelink, you should ask Felix Ziegler to get your
specific URL, for the sensors you have.

If you know nothing about Cavelink system, the official `website`_ is
the good place to start. Or maybe, you can also begin with `Wikipedia`_.

What is this repository for?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This python module gather the data by parsing the webpage. You will
then be able to display the data on your dashboard or store it to your
own database. I also provide code samples to better explain this -`see
directory ‘samples’`_-.

How do I get set up?
~~~~~~~~~~~~~~~~~~~~

To ensure a proper setup, I recommend the use of virtualenv (but
optionnal).

..

   sudo apt-get update && sudo apt-get install git python-pip --yes
   mkdir your-project
   cd your-project
   virtualenv venv
   source venv/bin/activate
   sudo pip install cavelink


Then you can use the module that way:

.. code:: python

   from cavelink import cavelink
   webpage="http://www.cavelink.com/cl/da.php?s=142&g=10&w=1&l=10"
   nb_rows = 5
   cvlnk = cavelink.Sensor(webpage, nb_rows)
   motiers = cvlnk.getJSON(datefmt='human')  # or datefmt='epoch'
   print(motiers)

You will get a the measurements and the sensor details formatted in JSON.

::

   {
      "measures": {
         "22.12.2018 16:00": 6.3,
         "22.12.2018 16:30": 5.67,
         "22.12.2018 17:00": 6.0,
         "22.12.2018 17:30": 5.45,
         "22.12.2018 18:00": 5.87
      },
      "sensor": {
         "group": "10",
         "number": "1",
         "station": "142",
         "unit": "C"
      }
   }


You can also fetch additionnal information, also available from the page.
Please note that the following data is provided in JSON object as well.
This is:

>>> print(cvlnk.station)
>>> print(cvlnk.group)
>>> print(cvlnk.number)
>>> print(cvlnk.unit)

To parse the measures, you can use this sample:

.. code:: python

   import json
   
   # convert the json-formatted string to a python dictionnay
   motiers_json = json.loads(motiers)

   # parse measures
   for timestamp in motiers_json['measures']:
      print('%s -> %s %s' % (timestamp,
                           motiers_json['measures'][timestamp],
                           motiers_json['sensor']['unit']))


Contribution guidelines
~~~~~~~~~~~~~~~~~~~~~~~

Feel free to submit issue or better, some pull requests !

Contributors
~~~~~~~~~~~~

* Sébastien Pittet (main contributor)
* Loïc, Bruno and other friends at exoscale.com


Who do I talk to?
~~~~~~~~~~~~~~~~~

`sebastien at pittet dot org`_

.. _this example shows: http://www.cavelink.com/cl/da.php?s=106&g=1&w=0&l=10
.. _website: http://www.cavelink.com
.. _Wikipedia: https://de.wikipedia.org/wiki/Cave-Link
.. _see directory ‘samples’: https://github.com/SebastienPittet/cavelink/tree/master/samples
.. _sebastien at pittet dot org: https://sebastien.pittet.org

.. |Build Status| image:: https://travis-ci.org/SebastienPittet/cavelink.svg?branch=master
   :target: https://travis-ci.org/SebastienPittet/cavelink