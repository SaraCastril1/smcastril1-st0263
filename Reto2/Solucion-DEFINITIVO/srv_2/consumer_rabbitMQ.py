# https://medium.com/better-programming/introduction-to-message-queue-with-rabbitmq-python-639e397cb668
# consumer.py
# Consume RabbitMQ queue

import pika
import os
import fnmatch

        
def Find_file(request):
    matching_files = []
    file_path = os.path.join(request)
    if os.path.exists(file_path):
        print("True: ", file_path)
    else:
        #return file_pb2.file_response(file= 0, coincidence = 'File not found')
        matching_files = fnmatch.filter(os.listdir("."), os.path.basename(file_path))
        if matching_files:
            print("True: ", matching_files)
        else:
            print("False: File not found -> Not coincidences ")
              

# def List_file(self, request, context):
#     try:
#         files = os.listdir(request.file)
#         print("List: ", request.file)
#         return file_pb2.list_response(file = files)
#     except OSError as e:
#         return f"Error listing files in '{request.file}': {e}"
#         #return []

def main():

    connection = pika.BlockingConnection(pika.ConnectionParameters('54.85.196.208', 5672, '/', pika.PlainCredentials("user", "password")))
    channel = connection.channel()

    def callback(ch, method, properties, body):
        segmento = body.decode('utf-8').split('/')
        if segmento[0] == "list":
            print("list")
        elif segmento[0] == "find":
            print("find: ", segmento[1])
            Find_file(segmento[1])
        else:
            print("Status: 400")
        
    channel.basic_consume(queue="my_app", on_message_callback=callback, auto_ack=True)
    channel.start_consuming()



if __name__ == "__main__":
    main()