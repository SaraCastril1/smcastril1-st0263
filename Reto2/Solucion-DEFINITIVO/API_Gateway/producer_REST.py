from flask import Flask
import grpc
import file_pb2
import file_pb2_grpc

app = Flask(__name__)

PRODUCER_HOST = '3.209.30.241'
PRODUCER_PORT = 50051

def find_file(pattern):
    with grpc.insecure_channel(f"{PRODUCER_HOST}:{PRODUCER_PORT}") as channel:
        stub = file_pb2_grpc.FileStub(channel)
        response = stub.Find_file(file_pb2.file_request(file=pattern))
        return response

def list_files(directory):
    with grpc.insecure_channel(f"{PRODUCER_HOST}:{PRODUCER_PORT}") as channel:
        stub = file_pb2_grpc.FileStub(channel)
        response = stub.List_file(file_pb2.file_request(file=directory))
        return response

@app.route('/find/<pattern>', methods=['GET'])
def find_route(pattern):
    response = find_file(pattern)
    return f"Find result: {response.file}, {response.coincidence}"

@app.route('/list/<directory>', methods=['GET'])
def list_route(directory):
    response = list_files(directory)
    return f"List result: {response.file}"

if __name__ == '__main__':
    app.run(debug=True)

