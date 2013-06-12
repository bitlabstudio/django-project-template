#!/bin/bash
# The variable values here are just examples. Replace them all with real values
# of your own app.

# Your django project name. Would be good if it is the same as your server
# name. Will be part of folder names, so only use letters and underscore. 
VAR_PROJECT_NAME='myproject'

# ============================================================================

# We remove the .git repository because this should be the beginning of our new
# project's repository.
rm -rf .git

# We remove the README.rst because it described how to use this template and
# not how to use our new project.
rm README.rst

# In all relevant files, we replace some text so that it fits to our new
# project.
for f in $(find . -type f | egrep "\.(py|txt|html|sample)$")
    do
        sed -i "s#VAR_PROJECT_NAME#${VAR_PROJECT_NAME}#g" $f
    done

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
git submodule add git://github.com/twitter/bootstrap.git $VAR_PROJECT_NAME/submodules/bootstrap
git submodule init
git submodule update

# Now that the submodule exists, we can copy some symlinks
cd $VAR_PROJECT_NAME/$VAR_PROJECT_NAME/static/css/libs/bootstrap
ln -s ../../../../../submodules/bootstrap/less/* .
cd ../../../../../../
git add .
git commit -am "Added bootstrap submodule"

# We will symlink the server scripts 
mkdir -p $HOME/bin && cd $HOME/bin
ln -s $HOME/src/$VAR_PROJECT_NAME/scripts/*.sh .
rm script-settings.sh
cp $HOME/src/$VAR_PROJECT_NAME/scripts/script-settings.sh .
cp $HOME/srv/$VAR_PROJECT_NAME/scripts/.pgpass $HOME
chmod 600 $HOME/.pgpass
