Django Project Template
=======================

This repository aims to kickstart a fully fledged Django project within
seconds.

This script has been created to accompany a 3.5 hour tutorial which was
presented at PyCon Singapore 2013. You can find slides with step by step
instructions here: https://speakerdeck.com/mbrochh/hosting-complex-web-applications-on-webfaction-servers

* The project will be ready for test driven development
* It has an extensive fabfile for automated deployments and continuous testing
* It is structured and configured to be hosted on Webfaction servers
* It uses a rapid prototyping view which allows your designers to start working
  on the new project immediately, even though no urls, models or views have
  been implemented, yet

Usage
=====

Kickstart the Django project
----------------------------

In order for the ``init.sh`` script to work, you should follow the slides up
until slide 34.

If you have made your control panel settings correctly, if you have initiated
your git repository and deployed your SSH key, you should be able to use this
repository like so::

    # I'm assuming that you chose a good username that can also be used as
    # your project name and git checkout name
    mkdir ~/src && cd ~/src
    git clone git://github.com/bitmazk/django-project-template.git <username>
    cd <username>
    vim init.sh
    # Change the project name to your username
    ./init.sh
    git remote add origin ~/webapps/git/repos/<username>.git
    git push -u origin master
    cd <username>
    mkvirtualenv <username>
    pip install -r requirements.txt

After this task you have a repository sitting at
``~/webapps/git/repos/username.git`` and you have a clone sitting at
``~/src/username/``. You will also have a virtual environment containing
everything you need in order to run your Django project.

First deployment
----------------

First copy your cloned project repo into the folder that has been created
by Webfactions one click installer::

    cp -rf ~/src/<username> ~/webapps/<username>_django/

Then go into that folder and remove some stuff that Webfaction created for us
which we are not going to use::

    cd ~/webapps/<username>_django
    rm -rf myproject
    rm -rf lib/python2.7/*

Now fix the paths in ``httpd.conf``::

    vim apache2/conf/httpd.conf
    # Replace `myproject` with `<username>`
    # Replace the `...lib/python2.7` path which you just deleted with the path
    # to your venv `/home/<username>/Envs/<username>/lib/python2.7/site-packages/`

Finally create your ``local_settings.py``::

    cd ~/webapps/<username>_django/<username>/<username>/settings
    vim local_settings.py

Try ``./manage.py collectstatic`` to see if the static path is set correctly.
Initiate your database with ``./manage.py syncdb --all`` and
``./manage.py migrate --fake``.

You might want to create a .pgpass file, test the server scripts in the ``bin``
folder and add a crontab (example can be found in ``scripts/crontab.txt``).
The scripts in the ``scripts`` folder are useful for:

* creating backups of the database, media files and translation files
* cleaning Django's session table
* sending emails queued by django-mailer
* restarting apache
