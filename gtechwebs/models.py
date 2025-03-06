from django.db import models

# Create your models here.
class TbCliente(models.Model):
    id_cliente = models.AutoField(db_column='id_cliente', primary_key=True)  # Field name made lowercase.
    nome = models.TextField(db_column='nome')  # Field name made lowercase.
    telefone = models.TextField(db_column='telefone')  # Field name made lowercase.
    data_cadastro = models.DateField(db_column='data_cadastro', auto_now_add=True)  # Field name made lowercase.

    class Meta:        
        db_table = 'tb_cliente'
        unique_together = (('nome', 'telefone'),)


class TbFornecedor(models.Model):
    id_fornecedor = models.AutoField(db_column='id_fornecedor', primary_key=True)  # Field name made lowercase.
    nome_empresa = models.TextField(db_column='nome_empresa')  # Field name made lowercase.
    tipo_empresa = models.TextField(db_column='tipo_empresa', blank=True, null=True)  # Field name made lowercase.
    data_cadastro = models.DateField(db_column='data_cadastro', auto_now_add=True)  # Field name made lowercase.

    class Meta:        
        db_table = 'tb_fornecedor'
        unique_together = (('nome_empresa', 'tipo_empresa'),)

    def __str__(self):
        return self.nome_empresa

class TbTipoProduto(models.Model):
    cod = models.AutoField(db_column='cod', primary_key=True)  # Field name made lowercase.
    descricao = models.TextField(db_column='descricao', unique=True, blank=True, null=True)  # Field name made lowercase.
    margem = models.FloatField(db_column='margem', blank=True, null=True)  # Field name made lowercase.

    class Meta:        
        db_table = 'tb_tipo_produto'

    def __str__(self):
        return self.descricao


class TbProduto(models.Model):
    id_produto = models.AutoField(db_column='id_produto', primary_key=True)  # Field name made lowercase.
    nome = models.TextField(db_column='nome')  # Field name made lowercase.
    preco_custo = models.FloatField(db_column='preco_custo')  # Field name made lowercase.
    tipo_produto = models.ForeignKey(TbTipoProduto, models.DO_NOTHING, db_column='cod')  # Field name made lowercase.
    fabricante = models.TextField(db_column='fabricante', blank=True, null=True)  # Field name made lowercase.
    marca = models.TextField(db_column='marca', blank=True, null=True)  # Field name made lowercase.
    cor = models.TextField(db_column='cor', blank=True, null=True)  # Field name made lowercase.
    id_fornecedor = models.ForeignKey(TbFornecedor, models.DO_NOTHING, db_column='id_fornecedor')  # Field name made lowercase.
    data_cadastro = models.DateField(db_column='data_cadastro', auto_now_add=True)  # Field name made lowercase.
    estoque = models.IntegerField(db_column='estoque')  # Field name made lowercase.
    imagem = models.CharField(db_column='imagem', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:        
        db_table = 'tb_produto'
        unique_together = (('nome', 'id_fornecedor'),)



class TbVenda(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    data = models.DateField(db_column='data')  # Field name made lowercase.
    id_cliente = models.ForeignKey(TbCliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)  # Field name made lowercase.
    id_produto = models.ForeignKey(TbProduto, models.DO_NOTHING, db_column='Id_produto', blank=True, null=True)  # Field name made lowercase.
    quantidade = models.IntegerField(db_column='quantidade', blank=True, null=True)  # Field name made lowercase.
    preco_venda = models.FloatField(db_column='preco_venda')  # Field name made lowercase.
    lucro = models.FloatField(db_column='lucro', blank=True, null=True)  # Field name made lowercase.

    class Meta:        
        db_table = 'tb_venda'


