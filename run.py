from app import create_app
from app.config import dev_config

if __name__ == '__main__':
    app = create_app(dev_config)
    app.run(host='0.0.0.0', port=5001)
