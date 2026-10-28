import os
import subprocess
from http.server import BaseHTTPRequestHandler

# Inicia o servidor do Streamlit em segundo plano apontando para o app.py
cmd = "streamlit run app.py --server.port 8501 --server.headless true"
subprocess.Popen(cmd, shell=True)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Aplicacao Streamlit a iniciar...")
        return