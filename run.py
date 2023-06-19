from app import app
from config import Config

# Test 2
if __name__ == '__main__':
    app.config.from_object(Config)
    app.run()