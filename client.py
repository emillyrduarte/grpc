import grpc
import proto.cartao_sus_pb2_grpc as pb2_grpc
import proto.cartao_sus_pb2 as pb2


class UnaryClient(object):

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051 

        # instanciando um canal
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # enviando o stub para o client e o server
        self.stub = pb2_grpc.UnaryStub(self.channel) 

    def get_url(self, cartao_sus, especialidade):

        message = pb2.Message(
            cartao_sus = cartao_sus, especialidade = especialidade)

        return self.stub.GetServerResponse(message) #enviando requisição ao servidor


if __name__ == '__main__':
    cartaoSus = input('Digite o número do cartão do sus: ')
    especialidadE = input('Para clínico geral digite 1, para pediatra digite 2: ')

    client = UnaryClient()
    result = client.get_url(cartao_sus=cartaoSus, especialidade=especialidadE)
    print(f'\n{result}')