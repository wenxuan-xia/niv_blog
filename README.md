# niv_blog - half finished - (new version is coming soon)

## Ideal Core Structure (roughly, to be modified)
### Construct basic blog administrating core: 
**User**: use default

**Blog**: blog, blog-tag(to do),

**Comment**: comments system(to do)


## Installation and Requirements
Strongly suggest using virtual-environment.
```
$ pip install --upgrade virtualenv
$ mkdir ~/.virtualenvs
$ virtualenv -p python ./.virtualenv
```
activate virtual-environment
```
$ source ./.virtualenv/bin/active
```

use `pip -r requirements/requirements.txt` to install all the requirements.
## migrate core blog app
```
$ python manager.py makemigrations blog
$ python manager.py migrate
```
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
highlight.js

## Thanks
lzjun567/django_blog
