from flask import Flask
from config.config import DEBUG, PORT
from flask_cors import CORS
# from routers.login_router import login_routes
# from routers.user_router import user_routes
from routers.home_router import home
from routers.web_auth import web_auth

app = Flask(__name__)

#habilitando cors
CORS(app)


#routes
app.register_blueprint(home)
# app.register_blueprint(login_routes)
# app.register_blueprint(user_routes)
# app.register_blueprint(web_auth)



if __name__ == "__main__":
    app.run(debug=DEBUG, port=PORT)