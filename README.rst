Django Project Template
=======================

This repository aims to kickstart a fully fledged Django project within
seconds.

This script has been created to accompany a 3.5 hour tutorial which was
presented at PyCon Singapore 2013. You can find slides with step by step
instructions here: https://speakerdeck.com/mbrochh/hosting-complex-web-applications-on-webfaction-servers

* The project will be ready for test driven develpment
* It has an extensive fabfile for automated deployments and continuous testing
* It is structured and configured to be hosted on Webfaction servers
* It uses a rapid prototyping view which allows your designers to start working
  on the new project immediately, even though no urls, models or views have
  been implemented, yet

Usage
=====

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

TODO: Describe how to prepare the first deployment
