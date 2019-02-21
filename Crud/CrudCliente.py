# -*- coding: utf-8 -*-

import peewee


from Conexao import Conexao, Cliente


class CrudCliente(object):

    def __init__(self, id="", nome="", sobrenome="", cpf="", rg="",
                 celular="", telefone="", email="", obs="", cep="",
                 endereco="", numero="", bairro="", cidade="", estado="",
                 dataEmissao="", dataEntrega="", Total="",
                 idPedido=""):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.rg = rg
        self.celular = celular
        self.telefone = telefone
        self.email = email
        self.obs = obs
        self.cep = cep
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado

        # Criando tabela Clientes
        try:

            Cliente.create_table()
            pass
        except:
            print(Conexao().erro)
            pass

    # Recebendo última id inserido
    def lastIdCliente(self):
        try:

            # Query

            ultimo = Cliente.select().order_by(Cliente.id.desc()).get()

            self.id = ultimo.id + 1

            pass

        except:

            self.id = 1

        return self.id

    #  Cadastro Cliente
    def inseriCliente(self):

        try:

            # Query
            row = Cliente.insert(

                id=self.id,
                nome=self.nome,
                sobrenome=self.sobrenome,
                cpf=self.cpf,
                rg=self.rg,
                celular=self.celular,
                telefone=self.telefone,
                email=self.email,
                obs=self.obs,
                cep=self.cep,
                endereco=self.endereco,
                numero=self.numero,
                bairro=self.bairro,
                cidade=self.cidade,
                estado=self.estado
            ).on_conflict_replace()

            # Execurando a Query
            row.execute()

            # Fechando a Conexao
            Conexao().dbhandler.close()

            pass

        except peewee.InternalError as err:

            print(err)

            pass

    # Buscando cliente por ID
    def selectClienteId(self):
        try:
            # Query
            busca = Cliente.get_by_id(self.id)

            # Fechando a conexao
            Conexao().dbhandler.close()

            # Salvando resultado da Query
            self.id = busca.id
            self.nome = busca.nome
            self.sobrenome = busca.sobrenome
            self.cpf = busca.cpf
            self.rg = busca.rg
            self.celular = busca.celular
            self.telefone = busca.telefone
            self.email = busca.email
            self.obs = busca.obs
            self.cep = busca.cep
            self.endereco = busca.endereco
            self.numero = busca.numero
            self.bairro = busca.bairro
            self.cidade = busca.cidade
            self.estado = busca.estado

            pass

        except peewee.DoesNotExist as err:

            print(err)

        pass

    # Buscando Cliente por nome
    def listaCliente(self):
        try:

            # Query
            busca = Cliente.select().where(
                Cliente.nome.contains('{}'
                                      .format(self.nome)))

            # fechando a conexao
            Conexao().dbhandler.close()

            # Convertendo variaveis em lista
            self.id = []
            self.nome = []
            self.sobrenome = []
            self.cpf = []
            self.rg = []
            self.celular = []
            self.telefone = []
            self.email = []
            self.obs = []
            self.cep = []
            self.endereco = []
            self.numero = []
            self.bairro = []
            self.cidade = []
            self.estado = []
            self.resultado = []

            # Adicionando dados em suas listas
            for row in busca:
                self.id.append(row.id)
                self.nome.append(row.nome)
                self.sobrenome.append(row.sobrenome)
                self.cpf.append(row.cpf)
                self.rg.append(row.rg)
                self.celular.append(row.celular)
                self.telefone.append(row.telefone)
                self.email.append(row.email)
                self.obs.append(row.obs)
                self.cep.append(row.cep)
                self.endereco.append(row.endereco)
                self.numero.append(row.numero)
                self.bairro.append(row.bairro)
                self.cidade.append(row.cidade)
                self.estado.append(row.estado)

            pass

        except peewee.DoesNotExist as err:

            print(err)

            pass

    # Lista AutoComplete Cliente

    def autoCompleteCliente(self):

        try:

            # Query
            busca = (Cliente.select(Cliente.id, Cliente.nome)
                     .where(Cliente.nome.contains(self.nome)))

            # Convertendo variaveis em lista
            self.id = []
            self.nome = []

            # Adicionando dados em suas listas
            for row in busca:
                self.id.append(row.id)
                self.nome.append(row.nome)

            pass

        except peewee.DoesNotExist as err:

            print(err)

            pass
