=====================
READ ME For Shenmartav
=====================
Hello and welcome to the shenmartav code! here you can learn and enjoy the codes.

This is a first attempt at writing the documentation how to set it all up. Please bear with me, as there will be some rough edges until the system has been installed from scratch on various platforms.

Cheers,
 Sebastian Henschel <sebastiantransparency@gmail.com>


INSTALL
=======

Dependencies
------------

First, issue:

$ sudo apt-get install python-pip python-gdal python-xapian python-dev libpq-dev git-core postgresql-9.1-postgis

(or similar depending on your Linux flavor).

The rest of the dependencies should all be listed in requirements.txt . After installing the distribution-specific packages mentioned above, you can use PIP to install all the rest:

$ sudo pip install -r requirements.txt

If you are installing into a virtualenv, you will need to manually compile xapian, as described here: http://nomad.coop/blog/installing-xapian-in-virtualenv-django/ . The latest version of Xapian known to work is 1.0.18; other versions may work as well but are not guaranteed.

Now you should be good to go to the next stage.

Patches
-------

You will find a few patch files in the directory patches/ which you should apply (but don't have to!):
- django-unicode_slug.diff patches Django to support unicode slugs (partyly from https://code.djangoproject.com/ticket/16501)
  this patch is against Django 1.4 and will fail party against 1.3. but it's a simle patch and you can easily fix this yourself.
- django_date_extensions-fields.diff patches django-date-extensions/django_date_extensions/fields.py to improve unicode support

Settings
--------
Copy settings.py.example to settings.py and adapt it to your needs. Most likely, you will have to change database settings.


Web Server
----------
Make sure the web server runs on UTF8, Apache on Ubuntu 10.04 LTS does not by default. Edit

/etc/apache2/envvars

appropriately, e.g.

export LANG=en_US.utf8


After extracting the code into a directory you should configure the web server to use WSGI.
A directive for Apache could be:

WSGIScriptAlias / /home/tigeorgia/wsgi/shenmartav.wsgi

You are welcome to use the example shenmartav.wsgi shipped in this package, but you probably have to adapt it to your site-specific paths.
Or for testing purposes, you can just use Django's built-in server:

$ ./manage.py runserver



Database
--------
Ideally, you will only have to run

$ ./manage.py syncdb

and

$ ./manage.py migrate


to install everything required by the database.


Import Data
-----------

There are 4 data sets to import, best do it in this order. The scripts are fairly verbose to tell you what is going on.

# import representatives from one CSV file
$ ./manage.py import_representatives ../import/representatives.csv

# import draft laws from one CSV file
$ ./manage.py import_draftlaws ../import/draftlaws.csv

# import voting records from many JSON files, as output by
# https://github.com/tigeorgia/Parliament.ge-VotingRecord-Scraper
$ ./manage.py import_votingrecords ../import/votingrecords/*

# import income declarations from a directory with fixed-named CSV files, as output by
# https://github.com/tigeorgia/Declaration.ge-PDF-Scraper
$ ./manage.py import_incomedeclarations ../import/incomedeclarations/


Then you should call the update commands (in order) to connect all these:

# update voting record results with links to representatives
# (might take a while, >100k records to update)
$ ./manage.py update_votingrecordresults

# update draft laws with links to voting records
$ ./manage.py update_votingrecords

# update representatives' assets from income declarations
$ ./manage.py update_assets

# update representatives' attendance from voting records
$ ./manage.py update_attendance


Search Index
------------

For the site-wide search to function, you need to build a search index once:

$ ./manage.py build_index

The fields being indexed can be found in apps/<app>/search_indexes.py .

Every now and then, maybe on a daily basis per cron, you have to update the search index:

$ ./manage.py update_index


Although currently the search function is not really used. The only search is to be found in representatives and hooks into one custom view.



Deployment
==========

There are a few scripts for deployment, that shouldn't concern you.
On the development server, issue

$ ./deployment/on_dev.sh

which will prepare the code and database for the production server and upload it.
It calls ./deployment/update_version.sh which puts some sort of version number into the footer of the base template.


On the production server, then issue

$ ./deployment/on_prod.sh

which will unpack the code and install the new database.
It calls ./deployment/redo_db.sh to redo the database, calls ./deployment/update_site.py to update the Django Site, collect static files and then restarts the web server.


Export Data / API (2013-12-04: broken)
=================

The API is based on TastyPie, http://tastypieapi.org/, so go there and read up on how to use it if you don't know it already.
The data is available at: http://shenmartav.ge/api/v1/?format=json . You can look at the output of the the API url above and discover for yourself, 'list_endpoint' might be the most interesting bit of data to you.


License
=======

My Parliament is released under the terms of [GNU General Public License (V2)](http://www.gnu.org/licenses/gpl-2.0.html).
