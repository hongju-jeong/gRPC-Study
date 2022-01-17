import grpc
import concurrent from futures # 비동기

import hello_grpc_pb2 # message class
import hello_grpc_pb2_grpc # client & server class

import hello_grpc # original remotely called functions

# protoc가 생성한 Servicer 클래스를 base class로 해서 원격 호출될 함수들을 멤버로 갖는 서버 클래스 생성
class MyServiceServicer(hello_grpc_pb2_grpc.MyServiceServicer):

    def MyFunction(self, request, context):

        response = hello_grpc_pb2.MyNumber()
        

