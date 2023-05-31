from __init__ import create_app
from flask import jsonify
from modules.intentions.controllers import intentions_module

app = create_app()

app.register_blueprint(intentions_module)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)

app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
