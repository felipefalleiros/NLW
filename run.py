# Caminha na estrutura de pastas até o server para importar o app
from src.main.server.server import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)