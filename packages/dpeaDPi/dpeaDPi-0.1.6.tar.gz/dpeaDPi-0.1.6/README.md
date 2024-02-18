# DPEA_DPi
DPEA Pi Family of Circuit Boards Developed by Stan Reifel 2022

This repo is for all of the DPi files to be added to a python package.


This package is on PyPi under the dpea account 
To maintain, clone the repository, edit files, recreate wheels  
`python3 setup.py sdist bdist_wheel`  
upload the new files to testPyPi first then finally to PyPi with twine.  
`twine upload --skip-existing dist/*`  
**Note:** You will need to have the dpea PyPi API token. When it asks for a username, input `__token__` and the API key as the password.  
Harlow has the token in LastPass  
More information:
https://gist.github.com/arsho/fc651bfadd8a0f42be72156fd21bd8a9 
