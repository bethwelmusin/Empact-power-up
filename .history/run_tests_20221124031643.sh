#!/bin/bash

source env/bin/activate

cd /var/lib/jenkins/workspace/Empact_api/app

python3 manage.py test

