from flask import Flask, request, jsonify
import grpc
import file_pb2
import file_pb2_grpc

HOST = "[3.222.15.155]:50051"

app = Flask(__name__)

def find_file(pattern):
    with grpc.insecure_channel(HOST) as channel:
        stub = file_pb2_grpc.FileStub(channel)
        response = stub.Find_file(file_pb2.file_request(file=pattern))
        return response

def list_files(directory):
    with grpc.insecure_channel(HOST) as channel:
        stub = file_pb2_grpc.FileStub(channel)
        response = stub.List_file(file_pb2.file_request(file=directory))
        return response

@app.route('/find', methods=['GET'])
def find_handler():
    pattern = request.args.get('pattern')
    response = find_file(pattern)
    return jsonify({
        "file": response.file,
        "coincidence": response.coincidence
    })

@app.route('/list', methods=['GET'])
def list_handler():
    directory = request.args.get('directory')
    response = list_files(directory)
    return jsonify({
        "files": response.file
    })

if __name__ == '__main__':
    app.run(debug=True)

