# https://medium.com/better-programming/introduction-to-message-queue-with-rabbitmq-python-639e397cb668
# consumer.py
# Consume RabbitMQ queue

import pika
import os

        
# def Find_file(self, request, context):
#     file_path = os.path.join(request.file)
#     print("Find: ",file_path)
#     if os.path.exists(file_path):
#         return file_pb2.file_response(file= 1, coincidence = [file_path])
#     else:
#         #return file_pb2.file_response(file= 0, coincidence = 'File not found')
#         matching_files = fnmatch.filter(os.listdir("."), os.path.basename(file_path))
#     if matching_files:
#         return file_pb2.file_response(file=1, coincidence = matching_files)
#     else:
#         return file_pb2.file_response(file= 0, coincidence = ["File not found -> No coincidences"])
                

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
        print(f'{body} is received')
        
    channel.basic_consume(queue="my_app", on_message_callback=callback, auto_ack=True)
    channel.start_consuming()



if __name__ == "__main__":
    main()