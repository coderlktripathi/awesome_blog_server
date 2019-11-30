import os
from app import get_app

if __name__ == '__main__':
    host = '0.0.0.0'
    app = get_app()
    port = int(os.environ.get('PORT', '5000'))
    app.run(host=host, port=port, debug=True, use_reloader=True)
