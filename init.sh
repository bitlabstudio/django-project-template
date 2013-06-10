#!/bin/bash
# The variable values here are just examples. Replace them all with real values
# of your own app.

# Your full name, will appear in AUTHORS, LICENSE and setup.py
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
        sed -i "" "s#VAR_PROJECT_NAME#${VAR_PROJECT_NAME}#g" $f
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

# And finally create our local_settings.py
cp $VAR_PROJECT_NAME/$VAR_PROJECT_NAME/settings/local_settings.py.sample $VAR_PROJECT_NAME/$VAR_PROJECT_NAME/settings/local_settings.py 
