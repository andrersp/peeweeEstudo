# -*- coding: utf-8 -*-

import peewee


from Conexao import Conexao, MarcaProduto


class CrudMarcaProduto(object):
    def __init__(self, id="", marca_produto=""):
        self.id = id
        self.marca_produto = marca_produto

        # Criando tabela Categoria Produtos
        try:
            MarcaProduto.create_table()
        except:
            print(Conexao().erro)

    # Recebendo ultimo Id inserido

    def lastIdMarcaProduto(self):
        try:

            ultimo = MarcaProduto.select().order_by(
                MarcaProduto.id.desc()).get()
            self.id = ultimo.id + 1

            # Fechando Conexao
            Conexao().dbhandler.close()

        except:

            self.id = 1

        return self.id

    # Cadastrando Marca produto

    def inseriMarcaProduto(self):

        try:
            # Query
            row = MarcaProduto.insert(
                id=self.id,
                marca_produto=self.marca_produto
            ).on_conflict_replace()

            # Executando a query
            row.execute()

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

        pass

    # Listando todas as Marcas

    def listaMarcaProdutos(self):

        try:
            # Query
            busca = MarcaProduto.select()

            # Fechando a Conexao
            Conexao().dbhandler.close()

            # Convertendo variaveis em lista
            self.id = []
            self.marca_produto = []

            # Adicionando dados em suas listas

            for row in busca:
                self.id.append(row.id)
                self.marca_produto.append(row.marca_produto)

            # Fechando Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)

        pass
