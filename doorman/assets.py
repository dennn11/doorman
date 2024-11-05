# -*- coding: utf-8 -*-
from flask_assets import Bundle, Environment
import os

css = Bundle(
    Bundle('css/bootstrap.less',
           depends=('**/*.less'),
           output='css/bootstrap.css',
           filters='less',
    ),
    'node_modules/bootstrap-vertical-tabs/bootstrap.vertical-tabs.css',
    'node_modules/jQuery-QueryBuilder/dist/css/query-builder.default.css',
    'node_modules/@selectize/selectize/dist/css/selectize.css',
    'css/style.css',
    filters='cssmin',
    output='public/css/common.css',
)

node_modules_path = os.path.join(os.path.dirname(__file__), '..', '..', 'node_modules')

js = Bundle(
    'node_modules/@popperjs/core/dist/umd/popper.min.js',
    'node_modules/jquery/dist/jquery.js',
    'node_modules/jquery-extendext/jquery-extendext.js',
    'node_modules/jQuery-QueryBuilder/dist/js/query-builder.standalone.js',
    'node_modules/interactjs/dist/interact.js',
    'node_modules/bootstrap/dist/js/bootstrap.js',
    'node_modules/@selectize/selectize/dist/js/selectize.js',
    'js/plugins.js',
    filters='jsmin',
    output='static/public/js/common.js',
)

assets = Environment()

assets.register('js_all', js)
assets.register('css_all', css)
