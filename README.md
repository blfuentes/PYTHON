# Python
Python Test projects

Update all pip packges: 

pip list --outdated --format=freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}

pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U


Installing xgboost rpi3
https://github.com/dmlc/xgboost/issues/2012
