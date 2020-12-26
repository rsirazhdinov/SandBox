"""
appserver.py
- creates an application instance and runs the dev server
"""

from sandbox.application import create_app
app = create_app()
app.config['CORS_HEADERS'] = 'Content-Type'
  # context = ('ssl/bapi-sandbox.mts.ru.cer', 'ssl/bapi-sandbox.mts.ru.key')
if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=8000)