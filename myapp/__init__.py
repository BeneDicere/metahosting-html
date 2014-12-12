from flask import Flask
from flask_bootstrap import Bootstrap
from flask.ext.login import LoginManager
from facade import Facade
from autho import get_authorizer
from stores.dict_store import Store

app = Flask(__name__)
app.secret_key = '03aa1'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC+1'
app.config.from_envvar('META-HTTP', silent=True)

Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

authorizer = get_authorizer()
type_store = Store()
instance_store = Store()
facade = Facade(authorization=authorizer,
                type_store=type_store,
                instance_store=instance_store)

import myapp.views
