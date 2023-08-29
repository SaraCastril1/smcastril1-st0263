from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/find/<file_name>', methods=['GET'])
def file(file_name):
    mensaje = {'file name': file_name}
    """
    aqui se llama los metodos para encontrar de grpc
    """
    return jsonify(mensaje)

@app.route('/list', methods=['GET'])
def obtener_saludo():
    mensaje = {'mensaje': '¡Hola! Bienvenido a mi API en Flask'}
    return jsonify(mensaje)

if __name__ == '__main__':
    app.run(debug=True)
