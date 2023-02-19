```
brew install pyenv
eval "$(pyenv init -)"
pyenv install 3.7.9
pyenv global 3.7.9
pip3 install virtualenvwrapper

WORKON_HOME=~/.virtualenvs
export WORKON_HOME=.virtualenvs
export PY3_PATH=$(which python)
virtualenv_executable_path=$(which virtualenvwrapper.sh)
<!-- export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3 -->

export VIRTUALENVWRAPPER_PYTHON=$HOME/.pyenv/shims/python
source $HOME/.pyenv/versions/$($VIRTUALENVWRAPPER_PYTHON -V 2>&1 | grep -Po '(?<=Python )(.+)')/bin/virtualenvwrapper.sh

experimental:

source ~/.pyenv/versions/3.7.9/bin/virtualenvwrapper.sh

mkvirtualenv wsta-python-http
workon wsta-python-http
pip3 install flask

# create requirements.txt
pip3 freeze > requirements.txt
```
