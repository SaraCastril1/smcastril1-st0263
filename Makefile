.PHONY = pb2
SHELL := /bin/bash

pb2:
	pip3 install grpcio grpcio-tools
	python3 -m grpc_tools.protoc -I ./protobufs --python_out=./srv_1 --pyi_out=./srv_1 --grpc_python_out=./srv_1 ./protobufs/monedas.proto

	cp -R srv_1/monedas_pb2.py API_Gateway
	cp -R srv_1/monedas_pb2_grpc.py API_Gateway
	cp -R srv_1/monedas_pb2.pyi API_Gateway