from viggocore.common.subsystem import router


class Router(router.Router):

    def __init__(self, collection, routes=[]):
        super().__init__(collection, routes)
        self.collection_url = '/pay_facs'
        self.resource_url = '/pay_facs/<id>'

    @property
    def routes(self):
        return [
            {
                'action': 'Pega os dados do domain_account cadastrados ' +
                'na Matera',
                'method': 'POST',
                'url': self.collection_url + '/get_conta',
                'callback': 'get_conta',
                'bypass': True
            },
            {
                'action': 'Adiciona uma chave pix aleatória',
                'method': 'POST',
                'url': self.collection_url + '/add_chave_pix',
                'callback': 'add_chave_pix',
                'bypass': True
            },
            {
                'action': 'Lista as chaves pix ligadas a uma conta',
                'method': 'POST',
                'url': self.collection_url + '/list_chaves_pix',
                'callback': 'list_chaves_pix',
                'bypass': True
            },
            {
                'action': 'Lista transacoes de uma conta',
                'method': 'POST',
                'url': self.collection_url + '/get_transacoes',
                'callback': 'get_transacoes',
                'bypass': True
            },
            {
                'action': 'Lista o extrato de uma conta',
                'method': 'POST',
                'url': self.collection_url + '/get_extrato',
                'callback': 'get_extrato',
                'bypass': True
            },
            {
                'action': 'Pega o saldo de uma conta',
                'method': 'POST',
                'url': self.collection_url + '/get_saldo',
                'callback': 'get_saldo',
                'bypass': True
            },
            {
                'action': 'Realiza a retirada do dinheiro via pix',
                'method': 'POST',
                'url': self.collection_url + '/cashout_via_pix',
                'callback': 'cashout_via_pix',
                'bypass': True
            }
        ]
