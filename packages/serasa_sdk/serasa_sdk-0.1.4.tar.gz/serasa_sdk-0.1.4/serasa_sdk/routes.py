class Digitalizacao:
    def __init__(self, client):
        """Serasa Digitalizacao Wrapper
        :param serasa_sdk.client.Client client: Serasa SDK cliente
        :rtype: serasa_sdk.domains.Digitalizacao
        """

        self.client = client
        self.domain = 'digitalizacao-rest-ful'

    def send(self, cpf: str, contrato: int, files: dict) -> dict:
        path = 'cadastrar-registro-ws-v2'

        data = {'cpfcnpj': cpf, 'contrato': str(contrato), 'arquivos': files}

        return self.client.post(path=f'{self.domain}/{path}', data=data)

    def get(
        self,
        protocol: str = '',
        cpf: str = '',
        initial_date: str = '',
        end_date: str = '',
    ) -> list:
        path = 'consultar-digitalizacao-v2'

        data = {
            'cpfcnpj': cpf,
            'dataCadastroINI': initial_date,
            'dataCadastroFIM': end_date,
            'protocoloBrFlow': protocol,
        }

        return self.client.post(path=f'{self.domain}/{path}', data=data)
