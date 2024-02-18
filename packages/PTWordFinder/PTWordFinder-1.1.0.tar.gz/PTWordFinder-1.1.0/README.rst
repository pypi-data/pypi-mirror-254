PTWordFinder
============

|Build| |Tests Status| |Coverage Status| |Flake8 Status|

“What specific words would you like to read?” Counting words in “Pan
Tadeusz” poem

Python version
--------------

tested with Python >= 3.10.6

Why
---

It was started as a project to exercise python language. The code helped
to find specific words in a selected file. It became command line tool
that help find any word within any file. The files can be selected by
command line

how to use
----------

you can installl this cmd tool from pip:

::

       pip install PTWordFinder

Usage: 
::

       ptwordf calculate-words WORDS_INPUT_FILE SEARCHED_FILE

where:

WORDS_INPUT_FILE - is path to input file (.txt) that contain searched
words

SEARCHED_FILE - is path to file that program search for a specific word

Try ‘ptwordf –help’ for help

examples:

::

       ptwordf calculate-words words-list.txt test-file.txt

::

       ptwordf calculate-words srcfolder/words-list.csv newfolder/test-file.csv

Features
--------

-  ☒ lines counter
-  ☒ a specific word counter
-  ☒ tracking the script execution time
-  ☒ support csv files

.. |Build| image:: https://github.com/DarekRepos/PanTadeuszWordFinder/actions/workflows/python-package.yml/badge.svg
   :target: https://github.com/DarekRepos/PanTadeuszWordFinder/actions/workflows/python-package.yml
.. |Tests Status| image:: https://raw.githubusercontent.com/DarekRepos/PanTadeuszWordFinder/c57987abc05d76a6f8a1e5898e68821a673ebd95/reports/coverage/coverage-unit-badge.svg
   :target: https://github.com/DarekRepos/PanTadeuszWordFinder/blob/master/reports/coverage/coverage-unit-badge.svg
.. |Coverage Status| image:: https://raw.githubusercontent.com/DarekRepos/PanTadeuszWordFinder/7d5956304ffb4278a142bf0452de57059ee315bb/reports/coverage/coverage-badge.svg
   :target: https://github.com/DarekRepos/PanTadeuszWordFinder/blob/master/reports/coverage/coverage-unit-badge.svg
.. |Flake8 Status| image:: https://raw.githubusercontent.com/DarekRepos/PanTadeuszWordFinder/c57987abc05d76a6f8a1e5898e68821a673ebd95/reports/flake8/flake8-badge.svg
   :target: https://github.com/DarekRepos/PanTadeuszWordFinder/blob/master/reports/flake8/flake8-badge.svg
