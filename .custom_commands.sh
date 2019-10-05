#!/bin/bash

function create() {
    cd
    python3 Automator.py $2
    cd /Users/{username}/Documents/$1Projects
    mkdir $2
    cd $2
    touch README.md
    git init
    git remote add origin https://github.com/{git user}/$2.git
    git add .
    git commit -m "first commit"
    git push -u  origin master
    code .
}
