# -*- coding: utf-8 -*-

import peewee

from Conexao import Conexao, Fornecedor


class CrudFornecedor(object):

    def __init__(self, id="", nomeFantasia="", razaoSocial="", cnpj="",
                 inscEstadual="", telefone="", email="", site="", obs="",
                 cep="", endereco="", numero="", bairro="", cidade="",
                 estado=""):

        self.id = id
        self.nomeFantasia = nomeFantasia
        self.razaoSocial = razaoSocial
        self.cnpj = cnpj
        self.inscEstadual = inscEstadual
        self.telefone = telefone
        self.email = email
        self.site = site
        self.obs = obs
        self.cep = cep
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado

        # Criando Tabela:
        try:
            Fornecedor.create_table()
        except:
            print(Conexao().erro)

     # Recebendo última id inserido

    def lastIdFornecedor(self):
        try:

            # Query
            ultimo = Fornecedor.select().order_by(Fornecedor.id.desc()).get()

            self.id = ultimo.id + 1

            pass

        except peewee.DoesNotExist:

            self.id = 1

            pass

        return self.id

    # Cadastro de Fornecedor

    def inseriFornecedor(self):

        try:

            # Query
            row = Fornecedor.insert(
                id=self.id,
                nome_fantasia=self.nomeFantasia,
                razao_social=self.razaoSocial,
                cnpj=self.cnpj,
                insc_estadual=self.inscEstadual,
                telefone=self.telefone,
                email=self.email,
                site=self.site,
                obs=self.obs,
                cep=self.cep,
                endereco=self.endereco,
                numero=self.numero,
                bairro=self.bairro,
                cidade=self.cidade,
                estado=self.estado
            ).on_conflict_replace()

            # Executando a query
            row.execute()

            # Fechando a Conexao
            Conexao().dbhandler.close()

        except peewee.InternalError as err:
            print(err)

    # Selecionar Fornecedor por Id

    def SelectFornecedorId(self):

        try:

        except peewee.DoesNotExist as err:
            print(err)


Inseri = CrudFornecedor()
Inseri.id = Inseri.lastIdFornecedor()
Inseri.nomeFantasia = "Azul e Rosa Personalizados"
Inseri.inseriFornecedor()
