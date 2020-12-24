"""
appserver.py
- creates an application instance and runs the dev server
"""
from OpenSSL import SSL
context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
context.use_privatekey_file('sertificate/bapi-sandbox.mts.ru.key')
context.use_certificate_file('sertificate/bapi-sandbox.mts.ru.cer')

if __name__ == '__main__':
  from sandbox.application import create_app
  app = create_app()
  # context = ('sertificate/bapi-sandbox.mts.ru.cer', 'sertificate/bapi-sandbox.mts.ru.key')
  app.run(debug=True, host="0.0.0.0", port=8000, ssl_context=context)