# -*- coding: utf-8 -*-
from peewee import MySQLDatabase
from peewee import IntegerField
from peewee import ForeignKeyField
from peewee import DecimalField
from peewee import BigBitField
from peewee import CharField
from peewee import PrimaryKeyField
from peewee import DatabaseError
from peewee import Model
from playhouse.mysql_ext import MySQLConnectorDatabase


""" 
Classe responsável pela conexao com o DB.
Caso não exista o DB será criado
 """


class Conexao(object):
    def __init__(self, dbhandler="", erro=""):
        user = 'andre'
        senha = 'rsp'
        host = '127.0.0.1'
        dbname = 'infotec'
        self.erro = erro

        self.dbhandler = dbhandler
        try:
            self.dbhandler = MySQLConnectorDatabase(
                dbname, user=user, password=senha, host=host
            )
            self.dbhandler.connect()
        except DatabaseError:
            import mysql.connector
            try:
                conn = mysql.connector.connect(
                    user=user, password=senha, host=host)
                cursor = conn.cursor()
                cursor.execute('SET sql_notes = 0 ;')
                cursor.execute("create database IF NOT EXISTS %s" % dbname)
            except mysql.connector.Error as err:
                print(err)


# Classe campo personalizado longblob
class LongBlobCampo(BigBitField):
    field_type = 'LONGBLOB'


# Base model
class BaseModel(Model):
    class Meta:
        conecta = Conexao()
        database = conecta.dbhandler


# Tabela Categoria de produtos
class CategoriaProduto(BaseModel):
    id = PrimaryKeyField(null=False)
    categoria_produto = CharField(max_length=100)

    class Meta:
        db_table = 'categoria_produto'


# Tabela Marca Produtos
class MarcaProduto(BaseModel):
    id = PrimaryKeyField(null=False)
    marca_produto = CharField(max_length=50)

    class Meta:
        db_table = 'marca_produto'


# Tabela Produtos
class Produto(BaseModel):
    id = PrimaryKeyField(null=False)
    produto = CharField(max_length=80)
    imagem = LongBlobCampo()
    categoria = ForeignKeyField(CategoriaProduto, column_name='categoria')
    marca = ForeignKeyField(MarcaProduto, column_name='marca')
    estoque_minimo = IntegerField(default=0)
    estoque_maximo = IntegerField(default=0)
    qtde = IntegerField(default=0)
    valor_compra = DecimalField(9, 2)
    valor_unitario = DecimalField(9, 2)
    valor_atacado = DecimalField(9, 2)
    qtde_atacado = IntegerField(default=5)
    obs = CharField(max_length=80)

    class Meta:
        db_table = 'produto'


# Tabela Clientes
class Cliente(BaseModel):
    id = PrimaryKeyField(null=False)
    nome = CharField(max_length=50)
    sobrenome = CharField(max_length=50)
    cpf = CharField(max_length=15)
    rg = CharField(max_length=15)
    celular = CharField(max_length=15)
    telefone = CharField(max_length=15)
    email = CharField(max_length=50)
    obs = CharField(max_length=50)
    cep = CharField(max_length=12)
    endereco = CharField(max_length=50)
    numero = CharField(max_length=5)
    bairro = CharField(max_length=40)
    cidade = CharField(max_length=40)
    estado = CharField(max_length=2)

    class Meta:
        db_table = 'cliente'


#  Tabela Fornecedor

class Fornecedor(BaseModel):
    id = PrimaryKeyField(null=False)
    nome_fantasia = CharField(max_length=80)
    razao_social = CharField(max_length=(80))
    cnpj = CharField(max_length=20)
    insc_estadual = CharField(max_length=20)
    telefone = CharField(max_length=20)
    email = CharField(max_length=80)
    site = CharField(max_length=80)
    obs = CharField(max_length=100)
    cep = CharField(max_length=12)
    endereco = CharField(max_length=50)
    numero = CharField(max_length=5)
    bairro = CharField(max_length=40)
    cidade = CharField(max_length=40)
    estado = CharField(max_length=2)

    class Meta:
        db_table = 'fornecedor'
