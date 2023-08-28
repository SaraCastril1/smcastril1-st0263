from concurrent import futures

import os
import grpc
import file_pb2
import file_pb2_grpc
#CONSUMER

HOST = '[::]:50051'


def serve():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        file_pb2_grpc.add_FileServicer_to_server(File(), server)
        server.add_insecure_port(HOST)
        print("Service find/list is running... ")
        server.start()
        server.wait_for_termination()

#Link el microservicio con una clase de python
class File(file_pb2_grpc.FileServicer):
        
        def Find_file(self, request, context):
                if os.path.exists(request):
                        response = file_pb2.file_response(file=True)
                        return response
                else:
                       response = file_pb2.file_response(file=False)
                       return response

               
      
        # def Find_file(self, request, context):
        #        print(request.file)
        #        response = file_pb2.file_response(file='1')
        #        return response
      
    #   def List_file(self, request, context):
    #         print(request.date)
    #         #print(request.source)
    #         response = monedas_pb2.Moneda_response(data=request.open)
    #         return response
   
#    def AddProduct(self, request, context):
#       print("Request is received: " + str(request))
#       return Service_pb2.TransactionResponse(status_code=1)


if __name__ == "__main__":
    serve()
