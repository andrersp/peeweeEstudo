# -*- coding: utf-8 -*-

import peewee


from Conexao import Conexao, CategoriaProduto


class CrudCatProduto(object):
    def __init__(self, id="", categoria_produto=""):
        self.id = id
        self.categoria_produto = categoria_produto

        # Criando tabela Categoria Produtos
        try:
            CategoriaProduto.create_table()
        except:
            print(Conexao().erro)

        # Recebendo ultimo Id inserido
    def lastIdCatProduto(self):

        try:

            # Query
            ultimo = CategoriaProduto.select().order_by(
                CategoriaProduto.id.desc()).get()
            self.id = ultimo.id + 1

            # Fechando Conexao
            Conexao().dbhandler.close()

        except:

            self.id = 1

        return self.id

    # Cadastrando categoria produto

    def inseriCatProduto(self):

        try:
            # Query
            row = CategoriaProduto.insert(
                id=self.id,
                categoria_produto=self.categoria_produto
            ).on_conflict_replace()

            # Executando a query
            row.execute()

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

    # Listando todas as categorias

    def listaCatProdutos(self):

        try:
            # Query
            busca = CategoriaProduto.select()

            # Fechando a Conexao
            Conexao().dbhandler.close()

            # Convertendo variaveis em lista
            self.id = []
            self.categoria_produto = []

            # Adicionando dados em suas listas

            for row in busca:
                self.id.append(row.id)
                self.categoria_produto.append(row.categoria_produto)

            # Fechando Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)

            pass
