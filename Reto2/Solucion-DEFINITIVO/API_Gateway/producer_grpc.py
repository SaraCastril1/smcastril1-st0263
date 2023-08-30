import grpc 
import os
import file_pb2
import file_pb2_grpc
#PRODUCER


HOST = '[3.222.15.155]:50051'

def serve():
	#Codigo estra -------------------------------------------------
	
	#source = os.environ['HOST']
	#--------------------------------------------------------------
	
    #Aqui se debe levantar la conexion
    with grpc.insecure_channel("3.209.30.241:50051") as channel:
        stub = file_pb2_grpc.FileStub(channel)
        #request = monedas_pb2.EmptyMessage()
        #response = stub.PingMonedas(request)
        #print("Recived: ", response.ack)
        request = file_pb2.file_request(file = "REST.py")
        response = stub.Find_file(request)
        print(response.file)
			


if __name__ == "__main__":
	serve()
