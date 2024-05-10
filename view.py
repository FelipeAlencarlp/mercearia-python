import Controller
import os.path


def criarArquivos(*args):
    for caminho in args:
        if not os.path.exists(caminho):
            with open(caminho, 'w') as arquivo:
                arquivo.write('')

criarArquivos('categorias.txt', 'clientes.txt', 'estoque.txt',
             'fornecedores.txt', 'funcionarios.txt', 'vendas.txt')


if __name__ == "__main__":
    while True:
        escolha = int(input("Digite 1 para acessar ( Categorias )\n"
                            "Digite 2 para acessar ( Estoque )\n"
                            "Digite 3 para acessar ( Fornecedores )\n"
                            "Digite 4 para acessar ( Clientes )\n"
                            "Digite 5 para acessar ( Funcionários )\n"
                            "Digite 6 para acessar ( Vendas )\n"
                            "Digite 7 para ver os produtos mais vendidos\n"
                            "Digite 8 para sair do programa\n"))

        if escolha == 1:
            categoria = Controller.ControllerCategoria()

            while True:
                decisao = int(input("Digite 1 para cadastrar uma categoria\n"
                                    "Digite 2 para remover uma categoria\n"
                                    "Digite 3 para alterar uma categoria\n"
                                    "Digite 4 para mostrar todas as categorias\n"
                                    "Digite 5 para voltar ao menu principal\n"))

                if decisao == 1:
                    cadastrarCategoria = input("Digite a categoria que deseja cadastrar\n")
                    categoria.cadastrarCategoria(cadastrarCategoria)

                elif decisao == 2:
                    removerCategoria = input("Digite a categoria que deseja remover\n")
                    categoria.removerCategoria(removerCategoria)

                elif decisao == 3:
                    alterarCategoria = input("Digite a categoria que deseja alterar\n")
                    novaCategoria = input("Digite o novo nome para a categoria\n")
                    categoria.alterarCategoria(alterarCategoria, novaCategoria)

                elif decisao == 4:
                    categoria.mostrarCategoria()
                else:
                    break

        elif escolha == 2:
            estoque = Controller.ControllerEstoque()

            while True:
                decisao = int(input("Digite 1 para cadastrar um produto\n"
                                    "Digite 2 para remover um produto\n"
                                    "Digite 3 para alterar um produto\n"
                                    "Digite 4 para mostrar os produtos em estoque\n"
                                    "Digite 5 para voltar ao menu principal\n"))

                if decisao == 1:
                    nome = input("Digite o nome do produto\n")
                    preco = input("Digite o preço do produto\n")
                    categoria = input("Digite a categoria do Produto\n")
                    quantidade = input("Digite a quantidade do produto\n")

                    estoque.cadastrarProduto(nome, preco, categoria, quantidade)

                elif decisao == 2:
                    nome = input("Digite o nome do produto que deseja remover\n")
                    estoque.removerProduto(nome)

                elif decisao == 3:
                    nome = input("Digite o nome do produto\n")
                    novoNome = input("Digite o novo nome do produto\n")
                    novoPreco = input("Digite o novo valor do produto\n")
                    novaCategoria = input("Digite a nova categoria do produto\n")
                    novaQuantidade= input("Digite a nova quantidade do produto\n")

                    estoque.alterarProduto(nome, novoNome, novoPreco, novaCategoria, novaQuantidade)

                elif decisao == 4:
                    estoque.mostrarEstoque()

                else:
                    break

        elif escolha == 3:
            fornecedor = Controller.ControllerFornecedor()

            while True:
                decisao = int(input("Digite 1 para cadastrar um fornecedor\n"
                                    "Digite 2 para remover um fornecedor\n"
                                    "Digite 3 para alterar um fornecedor\n"
                                    "Digite 4 para mostrar todos os fornecedores\n"
                                    "Digite 5 para voltar ao menu principal\n"))

                if decisao == 1:
                    nome = input("Digite o nome do fornecedor\n")
                    cnpj = input("Digite o CNPJ do fornecedor\n")
                    telefone = input("Digite o telefone do fornecedor\n")
                    categoria = input("Digite a categoria que o fornecedor fornece\n")

                    fornecedor.cadastrarFornecedor(nome, cnpj, telefone, categoria)

                elif decisao == 2:
                    nome = input("Digite o nome do fornecedor que deseja remover\n")
                    fornecedor.removerFornecedor(nome)

                elif decisao == 3:
                    nome = input("Digite o nome do fornecedor\n")
                    novoNome = input("Dgite o novo nome do fornecedor")
                    novoCnpj = input("Digite o novo CNPJ do fornecedor\n")
                    novoTelefone = input("Digite o novo telefone do fornecedor")
                    novaCategoria = input("DIgite a nova categoria que o fornecedor fornece\n")

                    fornecedor.alterarProduto(nome, novoNome, novoCnpj, novoTelefone, novaCategoria)

                elif decisao == 4:
                    fornecedor.mostrarFornecedores()

                else:
                    break

        elif escolha == 4:
            cliente = Controller.ControllerCliente()

            while True:
                decisao = int(input("Digite 1 para cadastrar um cliente\n"
                                    "Digite 2 para remover um cliente\n"
                                    "Digite 3 para alterar um cliente\n"
                                    "Digite 4 para mostrar todos os clientes\n"
                                    "Digite 5 para voltar ao menu principal\n"))

                if decisao == 1:
                    nome = input("Digite o nome do cliente\n")
                    telefone = input("Digite o telefone do cliente\n")
                    cpf = input("Digite o CPF do cliente\n")
                    email = input("Digite o e-mail do cliente\n")
                    endereco = input("Digite o endereço do cliente\n")

                    cliente.cadastrarCliente(nome, telefone, cpf, email, endereco)

                elif decisao == 2:
                    nome = input("Digite o nome do cliente que deseja remover\n")
                    cliente.removerCliente(nome)

                elif decisao == 3:
                    nome = input("Digite o nome do cliente\n")
                    novoNome = input("Dgite o novo nome do cliente")
                    novoTelefone = input("Digite o novo telefone do cliente")
                    novoCpf = input("Digite o novo CNPJ do cliente\n")
                    novoEmail = input("Digite o novo e-mail do cliente\n")
                    novoEndereco = input("Digite o novo endereço do cliente\n")

                    cliente.alterarCliente(nome, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)

                elif decisao == 4:
                    cliente.mostrarClientes()

                else:
                    break

        elif escolha == 5:
            funcionario = Controller.ControllerFuncionario()

            while True:
                decisao = int(input("Digite 1 para cadastrar um funcionario\n"
                                    "Digite 2 para remover um funcionario\n"
                                    "Digite 3 para alterar um funcionario\n"
                                    "Digite 4 para mostrar todos os funcionarios\n"
                                    "Digite 5 para voltar ao menu principal\n"))

                if decisao == 1:
                    clt = input("Digite a CLT do funcionario\n")
                    nome = input("Digite o nome do funcionario\n")
                    telefone = input("Digite o telefone do funcionario\n")
                    cpf = input("Digite o CPF do funcionario\n")
                    email = input("Digite o e-mail do funcionario\n")
                    endereco = input("Digite o endereço do funcionario\n")

                    funcionario.cadastrarFuncionario(clt, nome, telefone, cpf, email, endereco)

                elif decisao == 2:
                    nome = input("Digite o nome do funcionario que deseja remover\n")
                    funcionario.removerFuncionario(nome)

                elif decisao == 3:
                    nome = input("Digite o nome do funcionario\n")
                    novaClt = input("Digite a nova CLT do fundionário\n")
                    novoNome = input("Dgite o novo nome do funcionario\n")
                    novoTelefone = input("Digite o novo telefone do funcionario")
                    novoCpf = input("Digite o novo CNPJ do funcionario\n")
                    novoEmail = input("Digite o novo e-mail do funcionario\n")
                    novoEndereco = input("Digite o novo endereço do funcionario\n")

                    funcionario.alterarFuncionario(nome, novaClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)

                elif decisao == 4:
                    funcionario.mostrarFuncionarios()

                else:
                    break

        elif escolha == 6:
            venda = Controller.ControllerVenda()

            while True:
                decisao = int(input("Digite 1 para cadastrar uma venda\n"
                                    "Digite 2 para mostrar todas as vendas\n"
                                    "Digite 3 para voltar ao menu principal\n"))

                if decisao == 1:
                    nomeProduto = input("Digite o nome do produto\n")
                    vendedor = input("Digite o nome do vendedor\n")
                    comprador = input("Digite o nome do cliente que comprou\n")
                    quantidade = input("Digite a quantidade que foi vendido\n")

                    venda.cadastrarVenda(nomeProduto, vendedor, comprador, quantidade)

                elif decisao == 2:
                    dataInicial = input("Digite a data inicial que deseja buscar\n")
                    dataFinal = input("Digite a data final que deseja buscar\n")

                    venda.mostrarVendas(dataInicial, dataFinal)

                else:
                    break

        elif escolha == 7:
            maisVendido = Controller.ControllerVenda()
            maisVendido.relatorioProdutos()

        else:
            break
