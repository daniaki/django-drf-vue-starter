# django-drf-vue-starter
A ready-to-go template for building a Django API-driven backend with a Vue 
front-end.

# Requirements
- npm
- django
- djangorestframework
- django-filter>=2.0.0
- djangorestframework-filters
- django-webpack-loader
- drf-yasg
- factory-boy
- mock
- coverage

For staging/production
- mod_wsgi

# Setup
You will need to create a `secrets.json` file in the `settings` module. This 
file should contains items which should remain secret, such as your
application's `SECRET_KEY`, external API keys and database settings 
(username, password, etc).

If you wish you may change the `app` folder name and `PROJECT_NAME` and the 
setting in `settings/base.py`, however make sure to also change references to 
this name in `app/wsgi.py` and `manage.py`.

Finally, the folder `frontend` contains the frontend source code and development
configuration files. A project structure has already been setup for your ready 
to go. Before starting the server, make sure to build the javascript bundle
using `npm build` or `npm run watch`.

# Notes
A UI/CSS framework has not been included so you will need to pick your favourite
flavour and manage the installation yourself. This process should be relatively
straight forward though. 

The webpack bundle is not minified for debug purposes. You will need to configure
webpack to create production/minified bundles (See TODO) 

# TODO
 -Webpack configurations and optimisations for staging and production have not
  yet been created.