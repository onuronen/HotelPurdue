import os
import sys
sys.path.append(os.getcwd())
from src.app.main import make_app

app = make_app()

if __name__ == "__main__":
    app.run()