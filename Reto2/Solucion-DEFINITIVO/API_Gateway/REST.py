from flask import Flask, jsonify
import grpc 
import file_pb2
import file_pb2_grpc

app = Flask(__name__)

@app.route('/find/<pattern>', methods=['GET'])
def find_file(stub, pattern):
    response = stub.Find_file(file_pb2.file_request(file=pattern))
    print(response.file)
    print("Coincidences:", response.coincidence)

@app.route('/list', methods=['GET'])
def list_files(stub, directory):
    response = stub.List_file(file_pb2.file_request(file=directory))
    print("Files in directory:", response.file)


def serve():

    #Aqui se debe levantar la conexion
    with grpc.insecure_channel("3.209.30.241:50051") as channel:
        stub = file_pb2_grpc.FileStub(channel)

        


if __name__ == '__main__':
    app.run(debug=True)
    serve()
