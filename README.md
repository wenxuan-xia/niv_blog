# niv_blog - prepare to work
>I start naming everything use prefix niv-. I want to build a new light django blog engine.

## Ideal Core Structure (roughly, to be modified)
### Construct basic blog administrating core: 
**User**: user, user-group, auth-permissions,

**Blog**: blog, blog-tag, blog-auth

**Comment**: comment

Everything above should be able to administrated at ~/admin

## Installation and Requirements
Please use virtual-environment.
```
$ pip install --upgrade virtualenv
$ mkdir ~/.virtualenvs
$ virtualenv -p python ./.virtualenv
```
activate virtual-environment
```
$ source ./.virtualenv/bin/active
```

use 'pip -r requirements/requirements.txt' to install all the requirements.

## Run it on your server
```
$ python manager.py runserver 0.0.0.0:port
```
or directly run
```
$ python manager.py runserver
```

## Current Front-end
Bootstrap - CleanBlog


## Thanks
//TO DO
