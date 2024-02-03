#!/usr/bin/env bash -xo pipefail 

brew install pyenv pyenv-virtualenv  # to manage virtual environments
brew install hdf5 parallel  # for specific alphaMELTSEnsemble dependencies

if ! grep -q alphamelts <<< $(pyenv virtualenvs) ; then
    pyenv install 3.11  # install python3.11 as your base interpreter
    pyenv virtualenv 3.11 alphamelts  # create a virtual "alphamelts" environment based on 3.11
fi

cd $(dirname $0)
pyenv local alphamelts  # always select alphamelts interpreter when in this directory

pip install --upgrade pip setuptools  # upgrade the base tooling within alphamelts environment
pip install -r requirements.txt  # install dependencies of alphaMELTSEnsemble