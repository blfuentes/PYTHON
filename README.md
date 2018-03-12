# Python
Python Test projects
Update all pip packges: pip list --outdated --format=freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}
