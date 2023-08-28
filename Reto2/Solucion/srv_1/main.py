import grpc 
import os
import monedas_pb2
import monedas_pb2_grpc
#PRODUCER

from repositories.File_repository import File_repository

HOST = '[srv_persistor]:50051'

def serve():
	#Codigo estra -------------------------------------------------
	file_repository = File_repository('/tmp/data/BTCUSD_M5.csv')
	readed_data = file_repository.get_data()
	#source = os.environ['HOST']
	#--------------------------------------------------------------
	for row in readed_data:
		#Aqui se debe levantar la conexion
		with grpc.insecure_channel('srv_persistor:50051') as channel:
			stub = monedas_pb2_grpc.MonedasStub(channel)
			#request = monedas_pb2.EmptyMessage()
			#response = stub.PingMonedas(request)
			#print("Recived: ", response.ack)
			request = monedas_pb2.Moneda_request(date = row[0], open = row[1], high = row[2], low = row[3], close = row[4])
			response = stub.SendMoneda(request)
			print("Recived: ", response.data)
			


if __name__ == "__main__":
	serve()
