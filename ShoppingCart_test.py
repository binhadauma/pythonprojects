from unittest import TestCase, main
from should_dsl import should, should_not
from ShoppingCart import CarrinhoCompra

class CarrinhoCompraTest(TestCase):

#teste 'pesquisar_produtos'

    def setUp(self):
        self.carrinho = CarrinhoCompra('pesquisar_produtos')

    def test_pesquisar_produtos(self):
        self.carrinho.pesquisar_produtos('novo_acesso') | should | equal_to('pesquisando')
        self.carrinho.pesquisar_produtos('pesquisando') | should_not | equal_to('carrinho_ativo')

#teste 'selecionar_produtos'

    def setUp(self):
        self.carrinho = CarrinhoCompra('selecionar_produtos')

    def test_selecionar_produtos(self):
        self.carrinho.selecionar_produtos('pesquisando') | should | equal_to('carrinho_ativo')
        self.carrinho.selecionar_produtos('carrinho_ativo') | should_not | equal_to('pesquisando')

#teste 'remover_produtos'

    def setUp(self):
        self.carrinho = CarrinhoCompra('remover_produtos')

    def test_remover_produtos(self):
        self.carrinho.remover_produtos('carrinho_ativo') | should | equal_to('pesquisando')
        self.carrinho.remover_produtos('carrinho_ativo') | should_not | equal_to('pagamento_confirmado')

#teste 'selecionar_forma_pagamento'

    def setUp(self):
        self.carrinho = CarrinhoCompra('selecionar_forma_pagamento')

    def test_selecionar_forma_pagamento(self):
        self.carrinho.selecionar_forma_pagamento('carrinho_ativo') | should | equal_to('pagamento_confirmado')
        self.carrinho.selecionar_forma_pagamento('pagamento_confirmado') | should_not | equal_to('compra_finalizada')

#teste 'confirmar_dados_entrega'

    def setUp(self):
        self.carrinho = CarrinhoCompra('confirmar_dados_entrega')

    def test_confirmar_dados_entrega(self):
        self.carrinho.confirmar_dados_entrega('pagamento_confirmado') | should | equal_to('compra_finalizada')
        self.carrinho.confirmar_dados_entrega('novo_acesso') | should_not | equal_to('pesquisando')

if __name__ == '__main__':
    main()