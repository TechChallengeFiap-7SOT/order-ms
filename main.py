from src.api.apiHandler import ApiHandler, app
from flask_cors import CORS


if __name__ == '__main__':
    # Inicia a thread do worker
    CORS(app)
    app.run(debug=True, host='0.0.0.0', port=5000)