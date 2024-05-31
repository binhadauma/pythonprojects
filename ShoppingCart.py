FSM = {
   'pesquisar_produtos': ('novo_acesso', 'pesquisando'),
   'selecionar_produtos': ('pesquisando', 'carrinho_ativo'),
   'remover_produtos': ('carrinho_ativo', 'pesquisando'),
   'selecionar_forma_pagamento': ('carrinho_ativo', 'pagamento_confirmado'),
   'confirmar_dados_entrega': ('pagamento_confirmado', 'compra_finalizada')

}

INVALIDO = "Invalido!"

class CarrinhoCompra(object):

#função 'pesquisar_produtos'

    def __init__(self, estado_corrente):
        self.estado_corrente = estado_corrente

    def pesquisar_produtos(self, estado_corrente) -> str:
        if estado_corrente !=  FSM['pesquisar_produtos'][0]:
            return INVALIDO
        return FSM['pesquisar_produtos'][1]

#função 'selecionar_produtos'

    def __init__(self, estado_ativo):
        self.estado_ativo = estado_ativo

    def selecionar_produtos(self, estado_ativo) -> str:
        if estado_ativo !=  FSM['selecionar_produtos'][0]:
            return INVALIDO
        return FSM['selecionar_produtos'][1]

#função 'remover_produtos'

    def __init__(self, estado_atual):
        self.estado_atual = estado_atual

    def remover_produtos(self, estado_atual) -> str:
        if estado_atual !=  FSM['remover_produtos'][0]:
            return INVALIDO
        return FSM['remover_produtos'][1]

#função 'selecionar_forma_pagamento'

    def __init__(self, estado_on):
        self.estado_on = estado_on

    def selecionar_forma_pagamento(self, estado_on) -> str:
        if estado_on !=  FSM['selecionar_forma_pagamento'][0]:
            return INVALIDO
        return FSM['selecionar_forma_pagamento'][1]

#função 'confirmar_dados_entrega'

    def __init__(self, estado_funcionando):
        self.estado_funcionando = estado_funcionando

    def confirmar_dados_entrega(self, estado_on) -> str:
        if estado_on !=  FSM['confirmar_dados_entrega'][0]:
            return INVALIDO
        return FSM['confirmar_dados_entrega'][1]

# if __name__ == '__main__':
#     pass
