#!/bin/bash
# The variable values here are just examples. Replace them all with real values
# of your own app.

# Your django project name. Would be good if it is the same as your server
# name. Will be part of folder names, so only use letters and underscore.
VAR_PROJECT_NAME='myproject'

# ============================================================================

VAR_PROJECT_ROOT=`pwd`

# We remove the .git repository because this should be the beginning of our new
# project's repository.
rm -rf .git

# We remove the README.rst because it described how to use this template and
# not how to use our new project.
rm README.rst

# In all relevant files, we replace some text so that it fits to our new
# project.
CMD=(find . -type f \( ! -iname '*.pyc' ! -iname 'init.sh' \) -print0)
"${CMD[@]}" | xargs -0 perl -pi -e "s#VAR_PROJECT_NAME#${VAR_PROJECT_NAME}#g"

# Now we rename the generic folder name into the correct project folder name
mv project_name/project_name project_name/$VAR_PROJECT_NAME
mv project_name $VAR_PROJECT_NAME

# And we remove this very script because we should only run it once anyways.
rm init.sh

# Now this project is clean and we can start our new repository
git init
git add .
git commit -am "Initial commit"

# We also need to add the Twitter Bootstrap submodule
git submodule add git://github.com/twbs/bootstrap.git $VAR_PROJECT_NAME/submodules/bootstrap
git submodule add git://github.com/jschr/bootstrap-modal/ $VAR_PROJECT_NAME/submodules/bootstrap-modal
git submodule add git://github.com/tarruda/bootstrap-datetimepicker $VAR_PROJECT_NAME/submodules/bootstrap-datetimepicker
git submodule init
git submodule update

# Now that the submodule exists, we can copy some symlinks
cd $VAR_PROJECT_ROOT/$VAR_PROJECT_NAME/$VAR_PROJECT_NAME/static/css/libs/bootstrap
ln -s ../../../../../submodules/bootstrap/less/* .
cd $VAR_PROJECT_ROOT/$VAR_PROJECT_NAME/$VAR_PROJECT_NAME/static/css/libs/
ln -s ../../../../submodules/bootstrap-modal/css/bootstrap-modal.css .
ln -s ../../../../submodules/bootstrap-datetimepicker/build/css/bootstrap-datetimepicker.min.css .
cd $VAR_PROJECT_ROOT/$VAR_PROJECT_NAME/$VAR_PROJECT_NAME/static/js/libs/
ln -s ../../../../submodules/bootstrap-modal/js/* .
ln -s ../../../../submodules/bootstrap-datetimepicker/build/js/bootstrap-datetimepicker.min.js .
cd $VAR_PROJECT_ROOT
git add .
git commit -am "Added submodules"

# Creating .pgpass in the $HOME folder
# This allows you to run `psql -U <username>` without entering a password
# Make sure to replace the db credentials in that file
cp scripts/.pgpass $HOME
chmod 600 $HOME/.pgpass

# Creating the mylogs/cron folder
mkdir -p $HOME/mylogs/cron

# Copying local_settings.py so that we can do a first deployment
cd $VAR_PROJECT_ROOT/$VAR_PROJECT_NAME/$VAR_PROJECT_NAME/settings/
cp local_settings.py.sample local_settings.py

# Symlinking the server scripts 
mkdir -p $HOME/bin && cd $HOME/bin
ln -s $HOME/src/$VAR_PROJECT_NAME/scripts/*.sh .
rm script-settings.sh
cp $HOME/src/$VAR_PROJECT_NAME/scripts/script-settings.sh .

# Copying redirect scripts for https and www
DIR=$HOME'/webapps/'$VAR_PROJECT_NAME'_www'
cd $DIR
rm index.html
cp $HOME/src/$VAR_PROJECT_NAME/scripts/.htaccess_www .htaccess

DIR=$HOME'/webapps/'$VAR_PROJECT_NAME'_no_ssl'
cd $DIR
rm index.html
cp $HOME/src/$VAR_PROJECT_NAME/scripts/.htaccess_no_ssl .htaccess

DIR=$HOME'/webapps/'$VAR_PROJECT_NAME'_static'
cd $DIR
rm index.html
