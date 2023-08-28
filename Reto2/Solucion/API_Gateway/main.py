import grpc
from concurrent import futures
import monedas_pb2
import monedas_pb2_grpc

#Genera un virtual env local para tener las dependencias instaladas -> Crealo dentro de srv_persistor

def main():
    #Numero de workers por defecto = 10
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10)) 

    #Después de generar los ficheros pb2, los usaremos.
    # 1. Importalos
    # 2. Escuchar peticiones del
    monedas_pb2_grpc.add_MonedasServicer_to_server(monedas_pb2_grpc.Monedas(), server)

    # 3. Arrancar el servidor -> Cualquier IP en el puerto 50051
    server.add_insecure_port('[::]:50051')
    print("Service persistor is running... ")
    server.start()
    server.wait_for_termination()
    




if __name__ == "__main__":
    main()