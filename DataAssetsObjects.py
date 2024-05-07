from Models import *


class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('categorias.txt', 'a') as arquivo:
            arquivo.writelines(categoria)
            arquivo.writelines('\n')

    @classmethod
    def ler(cls):
        with open('categorias.txt', 'r') as arquivo:
            cls.categoria = arquivo.readlines()

        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

        listaCategoria = []

        for categoria in cls.categoria:
            listaCategoria.append(Categoria(categoria))

        return listaCategoria


class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('vendas.txt', 'a') as arquivo:
            arquivo.writelines(venda.produtosVendido.nome + '|' 
                               + venda.produtosVendido.preco + '|' 
                               + venda.produtosVendido.categoria + '|'
                               + venda.vendedor + '|'
                               + venda.comprador + '|'
                               + str(venda.quantidadeVendido) + '|'
                               + venda.data)
            
            arquivo.writelines('\n')

    @classmethod
    def ler(cls):
        with open('vendas.txt', 'r') as arquivo:
            cls.venda = arquivo.readlines()

        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))

        listaVenda = []

        for venda in cls.venda:
            listaVenda.append(Venda(Produtos(venda[0], venda[1], venda[2],
                                             venda[3], venda[4], venda[5])))

        return listaVenda
    

class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open('estoque.txt', 'a') as arquivo:
            arquivo.writelines(produto.nome + '|' + produto.preco + '|'
                               + produto.categoria + '|' + str(quantidade))
            arquivo.writelines('\n')

    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arquivo:
            cls.estoque = arquivo.readlines()

        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))

        listaEstoque = []

        if len(cls.estoque) > 0:
            for estoque in cls.estoque:
                listaEstoque.append(Estoque(Produtos(estoque[0], estoque[1], estoque[2], estoque[3])))
            
        return listaEstoque
    

class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedores.txt', 'a') as arquivo:
            arquivo.writelines(fornecedor.nome + '|' + fornecedor.cnpj + '|'
                               + fornecedor.telefone + '|' + fornecedor.categoria)
            arquivo.writelines('\n')

    @classmethod
    def ler(cls):
        with open('fornecedores.txt', 'r') as arquivo:
            cls.fornecedores = arquivo.readlines()

        cls.fornecedores = list(map(lambda x: x.replace('\n', ''), cls.fornecedores))
        cls.fornecedores = list(map(lambda x: x.split('|'), cls.fornecedores))

        listaFornecedores = []

        for fornecedor in cls.fornecedores:
            listaFornecedores.append(Fornecedor(fornecedor[0], fornecedor[1],
                                                fornecedor[2], fornecedor[3]))

        return listaFornecedores
    

class DaoPessoa:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('clientes.txt', 'a') as arquivo:
            arquivo.writelines(pessoa.nome + '|' + pessoa.telefone + '|'
                               + pessoa.cpf + '|' + pessoa.email + '|' + pessoa.endereco)
            arquivo.writelines('\n')

    @classmethod
    def ler(cls):
        with open('clientes.txt', 'r') as arquivo:
            cls.clientes = arquivo.readlines()

        cls.clientes = list(map(lambda x: x.replace('\n', ''), cls.clientes))
        cls.clientes = list(map(lambda x: x.split('|'), cls.clientes))

        listaClientes = []

        for cliente in cls.clientes:
            listaClientes.append(Pessoa(cliente[0], cliente[1], cliente[2],
                                        cliente[3], cliente[4]))
            
        return listaClientes
    

class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionarios.txt', 'a') as arquivo:
            arquivo.writelines(funcionario.clt + '|' + funcionario.nome + '|'
                               + funcionario.telefone + '|' + funcionario.cpf + '|'
                               + funcionario.email + '|' + funcionario.endereco)
            arquivo.writelines('\n')

    @classmethod
    def ler(cls):
        with open('funcionarios.rxt', 'r') as arquivo:
            cls.funcionarios = arquivo.readlines()

        cls.funcionarios = list(map(lambda x: x.replace('\n', ''), cls.funcionarios))
        cls.funcionarios = list(map(lambda x: x.split('|'), cls.funcionarios))

        listaFuncionarios = []

        for funcionario in cls.funcionarios:
            listaFuncionarios.append(Funcionario(funcionario[0], funcionario[1], funcionario[2],
                                                 funcionario[3], funcionario[4], funcionario[5]))
            
        return listaFuncionarios
