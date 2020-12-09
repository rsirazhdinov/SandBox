"""
appserver.py
- creates an application instance and runs the dev server
"""

if __name__ == '__main__':
  from sandbox.application import create_app
  app = create_app()
  app.run(debug=True, host="0.0.0.0", port=8000)
  # app.run(debug=True, host="127.0.0.1", port=8001)