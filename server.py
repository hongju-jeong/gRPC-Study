import grpc
from concurrent import futures # 비동기

import hello_grpc_pb2 # message class
import hello_grpc_pb2_grpc # client & server class

import hello_grpc # original remotely called functions

# protoc가 생성한 Servicer 클래스를 base class로 해서 원격 호출될 함수들을 멤버로 갖는 서버 클래스 생성
class MyServiceServicer(hello_grpc_pb2_grpc.MyServiceServicer):

    def MyFunction(self, request, context):

        response = hello_grpc_pb2.MyNumber()

        response.value = hello_grpc.my_func(request.value)

        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

hello_grpc_pb2_grpc.add_MyServiceServicer_to_server(MyServiceServicer(), server)

print('Starting server, Listening on port 50051')
server.add_insecure_port('[::]:50051')
server.start()

try:
    server.wait_for_termination()
except KeyboardInterrupt:
    server.stop(0)