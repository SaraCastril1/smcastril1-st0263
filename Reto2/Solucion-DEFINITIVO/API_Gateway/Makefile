.PHONY = pb2
SHELL := /bin/bash

API_Gateway:
	pip3 install grpcio grpcio-tools
	python3 -m grpc_tools.protoc -I ./protobufs --python_out=./ --pyi_out=./ --grpc_python_out=./ ./protobufs/file.proto
