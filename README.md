# Python
Python Test projects

Update all pip packages: 

https://stackoverflow.com/a/5839291/452038 

import pip

from subprocess import call

packages = [dist.project_name for dist in pip.get_installed_distributions()]

call("pip install --upgrade " + ' '.join(packages), shell=True)


pip3 list --outdated --format=legacy | ForEach { pip3 install -U $_.split(" ")[0] }


pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U


Installing xgboost rpi3
https://github.com/dmlc/xgboost/issues/2012
