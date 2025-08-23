install python 3.13

#create venv
python -m venv <name>

#activate venv
./<name>/script/activate
or
source c:/<path>
#make sure venv activate as cmd shows <(name)> (open new terminal)

#install all requirements
navigate to <swapnil_automation> folder in repo
pip install -r requirement.txt

#execute API pytest
navigate to <swapnil_automation/api_automation_pytest> folder in repo
python -m pytest --html=log.html tests/test_api_endpoints.py
OR
pytest --html=log.html tests/assert_aad/test_assert_add.py 
