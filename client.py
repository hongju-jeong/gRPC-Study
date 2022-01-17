import grpc

import hello_grpc_pb2  #메세지
import hello_grpc_pb2_grpc # 서비스

# gRPC 통신 채널 생성
channel = grpc.insecure_channel('localhost:50051')

#protoc가 생성한 _pb2_grpc의 stub 함수와 채널을 사용하고 실행해서 stub를 생성함
#클라이언트에서 호출
stub = hello_grpc_pb2_grpc.MyServiceStub(channel)

# protoc가 생성한 _pb2 파일의 메세지 타입에 맞춰, 원격 함수에 전달할 메세지 생성
request = hello_grpc_pb2.MyNumber(value=4)


# 원격 함수를 stub을 사용하여 호출
response = stub.MyFunction(request)

print("gRPC result:", response.value)





