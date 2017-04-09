#!usr/bin/env python

from URLShortener import app
from config import SERVER_ADDR, PORT

if __name__ == '__main__':
    app.run(debug=True, host=SERVER_ADDR, port=PORT)
