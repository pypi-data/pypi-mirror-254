import hashlib
import hmac
from viggocore.common import exception


class TransactionHash():

    SECRET_KEY = '54B9D213-B30C-4E3B-A759-AEEB554513BB'

    def __init__(self, id=None, cnpj=None, account_id=None, url=None,
                 total_amount=None, psp_id=None, tax_id=None):
        self.id = id
        self.cnpj = cnpj
        self.account_id = account_id
        self.url = url
        self.total_amount = total_amount
        self.psp_id = psp_id
        self.tax_id = tax_id

    def gerar_hash(self, msg):
        b_message = bytes(msg, 'utf-8')
        b_key = bytes(self.SECRET_KEY, 'utf-8')

        h = hmac.new(b_key, b_message, hashlib.sha256)

        return {'Transaction-Hash': h.hexdigest()}

    def get_hash_id(self):
        if None in [self.id]:
            raise exception.PreconditionFailed(
                'É necessário preencher o id.')

        return self.gerar_hash(self.id)

    def get_hash_id_cnpj(self):
        if None in [self.id, self.cnpj]:
            raise exception.PreconditionFailed(
                'É necessário preencher o id e o cnpj.')

        return self.gerar_hash(f'{self.id}{self.cnpj}')

    def get_hash_account_id(self):
        if None in [self.account_id]:
            raise exception.PreconditionFailed(
                'É necessário preencher o account_id.')

        return self.gerar_hash(self.account_id)

    def get_hash_url(self):
        if None in [self.url]:
            raise exception.PreconditionFailed(
                'É necessário preencher url.')

        return self.gerar_hash(self.url)

    def get_hash_four_fields(self):
        if None in [self.total_amount, self.account_id, self.psp_id,
                    self.tax_id]:
            raise exception.PreconditionFailed(
                'É necessário preencher os campos: total_amount, ' +
                'account_id, psp_id e tax_id.')
        msg = (f'{self.total_amount}{self.account_id}{self.psp_id}' +
               f'{self.tax_id}')
        return self.gerar_hash(msg)
