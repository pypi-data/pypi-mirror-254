import flask
import json
import uuid

from viggocore.common import exception, utils, controller
from viggopayfac.subsystem.controle.configuracao_pay_fac.resource \
    import ConfiguracaoPayFacTipo as cpf_tipo


class Controller(controller.CommonController):
    # TODO(JorgeSilva): trocar por ambiente de PRODUCAO antes de subir
    API_PAYFAC = cpf_tipo.HOMOLOGACAO

    def __init__(self, manager, resource_wrap, collection_wrap):
        super(Controller, self).__init__(
            manager, resource_wrap, collection_wrap)

    def montar_response_dict(self, response):
        try:
            response_dict = json.loads(response.text)
        except Exception:
            response_dict = {'error': response.text}

        return response_dict

    def get_conta(self):
        data = flask.request.get_json()
        data['api_payfac'] = self.API_PAYFAC

        try:
            response = self.manager.get_conta(**data)
        except exception.ViggoCoreException as exc:
            return flask.Response(response=exc.message,
                                  status=exc.status)

        response_dict = self.montar_response_dict(response)
        response_final = response_dict.get('data', {})

        return flask.Response(response=utils.to_json(response_final),
                              status=response.status_code,
                              mimetype="application/json")

    def add_chave_pix(self):
        data = flask.request.get_json()
        account_id = data.get('account_id', None)

        alias = {
            "account_id": account_id,
            "externalIdentifier": uuid.uuid4().hex,
            "alias": {
                "type": "EVP"
            }
        }
        alias['api_payfac'] = self.API_PAYFAC

        try:
            response = self.manager.add_chave_pix(**alias)
        except exception.ViggoCoreException as exc:
            return flask.Response(response=exc.message,
                                  status=exc.status)

        response_dict = self.montar_response_dict(response)
        response_final = response_dict.get('data', {})

        return flask.Response(response=utils.to_json(response_final),
                              status=response.status_code,
                              mimetype="application/json")

    def list_chaves_pix(self):
        data = flask.request.get_json()
        data['api_payfac'] = self.API_PAYFAC

        try:
            response = self.manager.list_chaves_pix(**data)
        except exception.ViggoCoreException as exc:
            return flask.Response(response=exc.message,
                                  status=exc.status)

        response_dict = self.montar_response_dict(response)
        response_final = response_dict.get('data', {})

        return flask.Response(response=utils.to_json(response_final),
                              status=response.status_code,
                              mimetype="application/json")

    def get_transacoes(self):
        data = flask.request.get_json()
        data['api_payfac'] = self.API_PAYFAC

        try:
            response = self.manager.get_transacoes(**data)
        except exception.ViggoCoreException as exc:
            return flask.Response(response=exc.message,
                                  status=exc.status)

        response_dict = self.montar_response_dict(response)
        response_final = response_dict.get('data', {})

        return flask.Response(response=utils.to_json(response_final),
                              status=response.status_code,
                              mimetype="application/json")

    def get_extrato(self):
        data = flask.request.get_json()
        data['api_payfac'] = self.API_PAYFAC

        try:
            response = self.manager.get_extrato(**data)
        except exception.ViggoCoreException as exc:
            return flask.Response(response=exc.message,
                                  status=exc.status)

        response_dict = self.montar_response_dict(response)
        response_final = response_dict.get('data', {})

        return flask.Response(response=utils.to_json(response_final),
                              status=response.status_code,
                              mimetype="application/json")

    def get_saldo(self):
        data = flask.request.get_json()
        data['api_payfac'] = self.API_PAYFAC

        try:
            response = self.manager.get_saldo(**data)
        except exception.ViggoCoreException as exc:
            return flask.Response(response=exc.message,
                                  status=exc.status)

        response_dict = self.montar_response_dict(response)
        response_final = response_dict.get('data', {})

        return flask.Response(response=utils.to_json(response_final),
                              status=response.status_code,
                              mimetype="application/json")

    def cashout_via_pix(self):
        data = flask.request.get_json()
        data['api_payfac'] = self.API_PAYFAC

        data['total_amount'] = data.get('totalAmount', None)
        recipient = data.get('withdrawInfo', {}).get('instantPayment', {})\
            .get('recipient', {})
        data['psp_id'] = recipient.get('pspId', None)
        data['tax_id'] = recipient.get('taxIdentifier', {}).get('taxId', None)
        data['externalIdentifier'] = uuid.uuid4().hex

        try:
            response = self.manager.cashout_via_pix(**data)
        except exception.ViggoCoreException as exc:
            return flask.Response(response=exc.message,
                                  status=exc.status)

        response_dict = self.montar_response_dict(response)
        response_final = response_dict.get('data', {})

        return flask.Response(response=utils.to_json(response_final),
                              status=response.status_code,
                              mimetype="application/json")
