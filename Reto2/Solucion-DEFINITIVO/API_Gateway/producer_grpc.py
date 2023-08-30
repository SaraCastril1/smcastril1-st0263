import grpc 
import os
import file_pb2
import file_pb2_grpc

import sys
#PRODUCER


HOST = '[3.222.15.155]:50051'


def find_file(stub, pattern):
    response = stub.Find_file(file_pb2.file_request(file=pattern))
    print(response.file)
    print("Coincidences:", response.coincidence)

    
def list_files(stub, directory):
    response = stub.List_file(file_pb2.file_request(file=directory))
    print("Files in directory:", response.file)


def serve():

    #Aqui se debe levantar la conexion
    with grpc.insecure_channel("3.209.30.241:50051") as channel:
        stub = file_pb2_grpc.FileStub(channel)

        if len(sys.argv) < 3:
            print("Valid input: python3 producer_grpc.py find/list <file/directory> ")
            return (1)

        #command = sys.argv[1]
        #argument = sys.argv[2]

        if sys.argv[1] == 'find':
            find_file(stub, sys.argv[2])
        elif sys.argv[1] == 'list':
            list_files(stub, sys.argv[2])
        else:
            print("Invalid command. Use 'find' or 'list'.")
            return(1)

        # request = file_pb2.file_request(file = "*.txt")
        # response = stub.Find_file(request)
        # print(response.file)
        # print(response.coincidence)

        # request_list = file_pb2.file_request(file = "./")
        # response_list = stub.List_file(request_list)
        # print(response_list.file)
			


if __name__ == "__main__":
	serve()
