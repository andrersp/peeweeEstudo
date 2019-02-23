# -*- coding: utf-8 -*-

import peewee

from Conexao import Conexao, FormaPagamento


class CrudFormaPagamento(object):
    def __init__(self, id="", formaPagamento="", query=""):
        self.id = id
        self.formaPagamento = formaPagamento
        self.query = query

        # Criando Tabela e dados padrão

        try:
            # Criando tabela
            FormaPagamento.create_table()

            # Inserindo Dado caso não exista
            FormaPagamento.get_or_create(forma_pagamento='À Vista')

        except:

            print(Conexao().erro)

    # Recebendo ultimo Id inserido

    def lastIdFormaPagamento(self):

        try:

            # Query
            ultimo = (FormaPagamento.select().order_by(
                FormaPagamento.id.desc()).get())

            self.id = ultimo.id + 1

            # Fechando a conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist:
            self.id = 1

        return self.id

    # Cadastrando categoria a receber

    def inseriFormaPagamento(self):

        try:

            # Query
            row = FormaPagamento.insert(
                id=self.id,
                categoria_a_receber=self.formaPagamento
            ).on_conflict_replace()

            # Executando a query
            row.execute()

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

    # Listando todas as categorias
    def listaFormaPagamento(self):

        try:

            # Query
            self.query = FormaPagamento.select()

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.DoesNotExist as err:
            print(err)
