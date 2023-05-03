import grpc
import json
import random
from datetime import date
from concurrent import futures
from proto import cartao_sus_pb2_grpc as pb2_grpc
from proto import cartao_sus_pb2 as pb2


class UnaryService(pb2_grpc.UnaryServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):

        # recebe cartao sus e especialidade da request
        cartao_sus = request.cartao_sus 
        especialidade = request.especialidade 
        print(f'{cartao_sus} \n{especialidade}')
        #cria um date object com valores aleatorios 
        result1 = date(2023,random.randint(1,12),random.randint(1,30))
        #convertendo o date object em string
        x = result1.strftime("%d/%m/%Y")
        y = str(random.randint(0,24))
        result2 = f"{y}:00"
        result = {'data': x,'hora':result2, 'received': True}
        #enviando a resposta ao cliente
        return pb2.MessageResponse(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10)) #o servidor suporta ate 10 clientes simultaneos
    pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server) 
    server.add_insecure_port('[::]:50051') #indica a porta do servidor
    server.start() #inicia o servidor 
    server.wait_for_termination()


if __name__ == '__main__':
    serve()