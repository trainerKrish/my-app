# Overview

This repository houses the materials and code examples used for our comprehensive DevOps training. Our CI/CD pipeline is set up using GitHub Actions, automating tasks like testing, building, and deploying our applications to AWS ECS.

## Stages:

### TESTING

- git clone ( login )
- install python3 (optional) - 3.10 (current version)
- pip3 install -r requirements.txt
- flake8 --ignore E226
- pytest

### BUILD

- git clone ( login )
- install docker (optional) - 24.0.6 (current version)
- docker build -t tag-name .
- docker tag ECR-repo-name
- setup AWS credentials in ~/.aws/ (or) run aws configure (not possible)
- aws ecr login
- docker push ECR-repo-name > tag

### DEPLOY

- git clone ( login )
- generate task definition file
- cli command to update the ECS cluster

## Static Testing Codes (Flake8)

F - pyflake (logical errors)
E W - (pycodestyle(PEP8))
C - McCabe (complexity)
