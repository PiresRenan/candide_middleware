import json

from models import Nota


class Core:
    def __init__(self):
        data_emitente = {"CNPJ": ["62434436001703"], "xNome": ["CANDIDE INDUSTRIA E COMERCIO LIMITADA"],
                         "xFant": ["CANDIDE INDUSTRIA"],
                         "enderEmit": [{"xLgr": ["RUA TEODORO SAMPAIO"], "nro": ["399"], "xCpl": ["CONJ 57"],
                                        "xBairro": ["PINHEIROS"],
                                        "cMun": ["3550308"], "xMun": ["SAO PAULO"], "UF": ["SP"], "CEP": ["05405000"],
                                        "cPais": ["1058"],
                                        "xPais": ["BRASIL"], "fone": ["1133270277"]}],
                         "IE": ["119760925119"], "CRT": ["3"]}
        self.emitente = {"emit": [data_emitente]}

    def parse_json(self, data: Nota = None) -> dict:
        converted_to_dict = dict(data)
        formatted_data = {}
        portal_nfe = json.dumps(converted_to_dict.get('NFe').get('$'))
        infNFe = converted_to_dict.get('NFe').get('infNFe')
        print("Dados gerais: {}\n".format(infNFe))
        destinatario = infNFe[0].get('dest')
        print("Dados destinatario: {}\n".format(destinatario))
        detalhes = infNFe[0].get('det')
        print("Dados detalhamento: {}\n".format(detalhes))
        total = infNFe[0].get('total')
        print("Dados total: {}\n".format(total))
        transportadora = infNFe[0].get('transp')
        print("Dados transportadora: {}\n".format(transportadora))
        pagamento = infNFe[0].get('pag')
        print("Dados pagamento: {}\n".format(pagamento))
        infComp = infNFe[0].get('infAdic')
        print("Dados da informação complementar: {}\n".format(infComp))
        return formatted_data
