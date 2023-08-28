from concurrent import futures

import grpc
import monedas_pb2
import monedas_pb2_grpc
#CONSUMER

HOST = '[::]:50051'


def serve():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        monedas_pb2_grpc.add_MonedasServicer_to_server(Monedas(), server)
        server.add_insecure_port(HOST)
        print("Service persistor is running... ")
        server.start()
        server.wait_for_termination()

#Link el microservicio con una clase de python
class Monedas(monedas_pb2_grpc.MonedasServicer):
      
      def PingMonedas(self, request, context):
            #creamos un objeto respuesta
            response = monedas_pb2.PingMonedasResponse(ack='1')
            return response
      
      def SendMoneda(self, request, context):
            print(request.date)
            #print(request.source)
            response = monedas_pb2.Moneda_response(data=request.open)
            return response
   
#    def AddProduct(self, request, context):
#       print("Request is received: " + str(request))
#       return Service_pb2.TransactionResponse(status_code=1)


if __name__ == "__main__":
    serve()