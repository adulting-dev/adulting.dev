# adulting.dev
Repo for the 2019 [adulting.dev](https://www.adulting.dev/) website.

This site builds via Flask and Flask Frozen. The content lives in [Contentful](https://www.contentful.com/) and the site itself is hosted and deployed via netlify.

![Screenshot of Website](static/img/meta-preview.png)


Getting started
=====

### Requirements

For this project you'll need accounts for the following services:

- [Contentful](https://www.contentful.com)
- [Google maps](https://developers.google.com/maps/documentation/javascript/get-api-key#add_key).
- [Netlify](https://www.netlify.com/)

### Setup

* Fork and clone this repository

#### The Contentful part (optional)

This repo currently uses an existing Contentful space. If you'd like to replace this space with your own, so you can modify the content, you're welcome to do so.

* Create a new space using the [Contentful CLI](https://github.com/contentful/contentful-cli)

```console
$ contentful space create --name "adulting.dev"
? Do you want to confirm the space creation? Yes
Your user account is a member of multiple organizations. Please select the organization you would like to add your Space to.
? Please select an organization: Shy's DevRel Playground (orgid)
✨  Successfully created space adulting.dev (your space id here)
```
* Set the newly created space as default space for all further CLI operations. You'll be presented with a list of all available spaces – choose the one you just created.
```console
$ contentful space use
? Please select a space: adulting.dev (your space id here)
Now using the 'master' Environment of Space adulting.dev (your space id here) when the `--environment-id` option is missing.
```

* Import the provided content model (`./import/export.json`) into the newly created space.
```console
$ contentful space import --content-file import/export.json

┌──────────────────────────────────────────────────┐
│ The following entities are going to be imported: │
├─────────────────────────────────┬────────────────┤
│ Content Types                   │ 11              │
├─────────────────────────────────┼────────────────┤
│ Editor Interfaces               │ 11              │
├─────────────────────────────────┼────────────────┤
│ Locales                         │ 1              │
├─────────────────────────────────┼────────────────┤
│ Webhooks                        │ 1              │
├─────────────────────────────────┼────────────────┤
│ Entries                         │ 11              │
├─────────────────────────────────┼────────────────┤
│ Assets                          │ 18              │
└─────────────────────────────────┴────────────────┘
 ✔ Validating content-file
 ✔ Initialize client (1s)
 ✔ Checking if destination space already has any content and retrieving it (1s)
 ✔ Apply transformations to source data (1s)
 ✔ Push content to destination space
   ✔ Connecting to space (1s)
   ✔ Importing Locales (1s)
   ✔ Importing Content Types (4s)
   ✔ Publishing Content Types (2s)
   ✔ Importing Editor Interfaces (1s)
   ✔ Importing Assets (4s)
   ✔ Publishing Assets (0s)
   ✔ Archiving Assets (1s)
   ✔ Importing Content Entries (4s)
   ✔ Publishing Content Entries (1s)
   ✔ Archiving Entries (0s)
   ✔ Creating Web Hooks (0s)
Finished importing all data
┌───────────────────────┐
│ Imported entities     │
├───────────────────┬───┤
│ Locales           │ 1 │
├───────────────────┼───┤
│ Content Types     │ 11 │
├───────────────────┼───┤
│ Editor Interfaces │ 11 │
├───────────────────┼───┤
│ Assets            │ 18 │
├───────────────────┼───┤
│ Published Assets  │ 18 │
├───────────────────┼───┤
│ Archived Assets   │ 0 │
├───────────────────┼───┤
│ Entries           │ 11 │
├───────────────────┼───┤
│ Published Entries │ 11 │
├───────────────────┼───┤
│ Archived Entries  │ 0 │
├───────────────────┼───┤
│ Webhooks          │ 1 │
└───────────────────┴───┘
The import took a few seconds (13s)
No errors or warnings occurred
The import was successful.
```

* Update the space id and access token in [.env](.env) to use the api keys from your newly created space.

#### The flask part

To run this site you'll need to install all of the depenedencies. I'd encourage using virtualenv.

```console
$ virtualenv env
Using base prefix '/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7'
New python executable in /Users/shy/Documents/adulting.dev/env/bin/python3.7
Also creating executable in /Users/shy/Documents/adulting.dev/env/bin/python
Installing setuptools, pip, wheel...
done.
 $ source env/bin/activate
 $ pip install -r requirements.txt
Collecting certifi==2019.6.16
  Using cached certifi-2019.6.16-py2.py3-none-any.whl (157 kB)
Collecting chardet==3.0.4
  Using cached chardet-3.0.4-py2.py3-none-any.whl (133 kB)
Collecting Click==7.0
  Using cached Click-7.0-py2.py3-none-any.whl (81 kB)
Processing /Users/shy/Library/Caches/pip/wheels/0d/bb/fc/0021e718aaccf43ddf7d60806d0cdda49033ee990890cc4c17/contentful-1.12.2-cp37-none-any.whl
Collecting Flask==1.1.1
  Using cached Flask-1.1.1-py2.py3-none-any.whl (94 kB)
Processing /Users/shy/Library/Caches/pip/wheels/f5/2e/98/f87d64297cb0b2d1c5401510612b15861edfc3095c33143fe0/Flask_Markdown-0.3-cp37-none-any.whl
Collecting Frozen-Flask==0.15
  Using cached Frozen_Flask-0.15-py2.py3-none-any.whl (20 kB)
Collecting idna==2.8
  Using cached idna-2.8-py2.py3-none-any.whl (58 kB)
Collecting itsdangerous==1.1.0
  Using cached itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Collecting Jinja2==2.10.1
  Using cached Jinja2-2.10.1-py2.py3-none-any.whl (124 kB)
Collecting Markdown==3.1.1
  Using cached Markdown-3.1.1-py2.py3-none-any.whl (87 kB)
Collecting MarkupSafe==1.1.1
  Using cached MarkupSafe-1.1.1-cp37-cp37m-macosx_10_6_intel.whl (18 kB)
Collecting python-dateutil==2.8.0
  Using cached python_dateutil-2.8.0-py2.py3-none-any.whl (226 kB)
Collecting python-dotenv==0.10.3
  Using cached python_dotenv-0.10.3-py2.py3-none-any.whl (16 kB)
Collecting requests==2.22.0
  Using cached requests-2.22.0-py2.py3-none-any.whl (57 kB)
Processing /Users/shy/Library/Caches/pip/wheels/61/8d/73/a4a250a408b20e90c40d4139095d2e14ff54057944b47760f8/rich_text_renderer-0.2.3-cp37-none-any.whl
Collecting six==1.12.0
  Using cached six-1.12.0-py2.py3-none-any.whl (10 kB)
Collecting urllib3==1.25.3
  Using cached urllib3-1.25.3-py2.py3-none-any.whl (150 kB)
Collecting Werkzeug==0.15.5
  Using cached Werkzeug-0.15.5-py2.py3-none-any.whl (328 kB)
Requirement already satisfied: setuptools>=36 in ./env/lib/python3.7/site-packages (from Markdown==3.1.1->-r requirements.txt (line 11)) (49.1.0)
Installing collected packages: certifi, chardet, Click, idna, urllib3, requests, six, python-dateutil, contentful, Werkzeug, MarkupSafe, Jinja2, itsdangerous, Flask, Markdown, Flask-Markdown, Frozen-Flask, python-dotenv, rich-text-renderer
Successfully installed Click-7.0 Flask-1.1.1 Flask-Markdown-0.3 Frozen-Flask-0.15 Jinja2-2.10.1 Markdown-3.1.1 MarkupSafe-1.1.1 Werkzeug-0.15.5 certifi-2019.6.16 chardet-3.0.4 contentful-1.12.2 idna-2.8 itsdangerous-1.1.0 python-dateutil-2.8.0 python-dotenv-0.10.3 requests-2.22.0 rich-text-renderer-0.2.3 six-1.12.0 urllib3-1.25.3
```

To run the site locally you can call app.py.

```console
$ python app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 337-543-391
127.0.0.1 - - [04/Jul/2020 13:34:08] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [04/Jul/2020 13:34:08] "GET /static/css/main.css HTTP/1.1" 200 -
127.0.0.1 - - [04/Jul/2020 13:34:08] "GET /static/js/main.js HTTP/1.1" 200 -
127.0.0.1 - - [04/Jul/2020 13:34:08] "GET /static/img/rocket@2x.png HTTP/1.1" 200 -
127.0.0.1 - - [04/Jul/2020 13:34:08] "GET /static/img/favicon.png HTTP/1.1" 200 -
```

Running app.py directly is great for when you make changes, because the site will be live so you won't need to wait for things to rebuild to see updates. To checkout how flask frozen builds the site you can use:

```console
$ python freeze.py
$ cd build
$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

You can now navigate to port 8000 and see a statically hosted version of the site. Because it's a static site it's pretty darn fast.

#### The Netlify part (optional)

Head over to Netlify and create a new project using your created repo. You'll need to add all of your env vars in the build settings. Additionally you'll need to see the build settings to `python freeze.py` as your build command and `build` as your publish directory. For your build image, I'd encourage you to use `Ubuntu Trusty 14.04`. At the time of my creating this project, that was the image that I had the most success for python support.

You can also head over to Contentful to setup a webhook that'll cause Netlify to trigger a rebuild anytime you publish new content.

License
=======

Copyright (c) 2020 Adulting.Dev. Code released under the MIT license. See [LICENSE](LICENSE) for further details.


