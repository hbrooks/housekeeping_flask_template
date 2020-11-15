## HouseKeeping (Flask) Template Repository
This repository allows one to quickly create a Flask service.  The service can be run locally in a Docker container and then easily deployed to AWS Lambda.

### How to Run the Service Locally
1.  `./scripts/start.sh`

### Submodules as Dependencies
-  To show submodules: `git config --file=.gitmodules -l` (from https://tech.serhatteker.com/post/2019-01/changing-git-submodules-urlbranch-to/)
-  To update which version of a submodule this repo expects:
   -  `cd` to submodule
   -  With changes in the submodule, `git add`, `git commit`, and `git push` like normal.
   -  `cd` back to the root of this repository, one level above the submodule
   -  `git add housekeeping_flask/`
   -  `git commit -m 'update housekeeping_flask version;'`
   -  `git push`


### How to Deploy
**Note**: `./scipts/deploy` should work after the first deployment and if the containers are running.  If not, follow the below steps.
From the root of the Git repo.
1.  `git status`: Make sure you're on master!
2.  Stop containers.
3.  Start containers.
4.  `docker exec -it public_api bash`
5.  `cd /usr/src/public_api`
6.  `python3 -m venv venv`
7.  `source ./venv/bin/activate`
8.  `pip install zappa`
9.  `pip install -r requirements.txt`
10. `zappa package -s zappa_settings.yaml -o out.zip`
11. `exit` to get out of the container.  `cd my_api/`:
12. `zappa deploy -z out.zip -s zappa_settings.json `
    1.  NOTE: The first time you deploy using `zappa deploy` with `-z out.zip` it'll fail because the IAM Execution role doesn't exist.  This is a bug with zappa.  To fix, first do `zappa deploy` without `-z out.zip`.  Zappa will create the execution role, though the command will fail.  The command output will have a line like:  ```  
    Creating documentguardian-public-api-dev-ZappaLambdaExecutionRole IAM Role..
    Creating zappa-permissions policy on documentguardian-public-api-dev-ZappaLambdaExecutionRole IAM Role.
    ```
    After that, `zappa deploy -z out.zip -s zappa_settings.json ` should pass.