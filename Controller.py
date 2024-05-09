from Models import *
from DataAssetsObjects import *
from datetime import datetime


class ControllerCategoria:
    def cadastrarCategoria(self, novaCategoria):
        existeCategoria = False
        lerCategoria = DaoCategoria.ler()

        for categoria in lerCategoria:
            if categoria.categoria == novaCategoria:
                existeCategoria = True

        if not existeCategoria:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria cadastrada com sucesso!')

        else:
            print('Impossível cadastrar! Essa categoria já existe.')

    def removerCategoria(self, categoriaRemover):
        listaCategoria = DaoCategoria.ler()
        filtrarCategoria = list(filter(lambda lerCategoria: lerCategoria.categoria == categoriaRemover, listaCategoria))

        if len(filtrarCategoria) <= 0:
            print('Impossível remover! Essa categoria não existe.')

        else:
            # remover categoria da memória ram
            for i in range(len(listaCategoria)):
                if listaCategoria[i].categoria == categoriaRemover:
                    del listaCategoria[i]
                    break

            print('Categoria removida com sucesso!')

            # abrir o arquivo .txt e reescrever o que tem na variável lerCategoria
            with open('categorias.txt', 'w') as arquivo:
                for categoria in listaCategoria:
                    arquivo.writelines(categoria.categoria)
                    arquivo.writelines('\n')

    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        listaCategoria = DaoCategoria.ler()
        filtrarCategoria = list(filter(lambda lerCategoria: lerCategoria.categoria == categoriaAlterar, listaCategoria))

        # verifica se a categoria existe
        if len(filtrarCategoria) > 0:
            filtrarCategoriaExiste = list(filter(lambda lerCategoria: lerCategoria.categoria == categoriaAlterada, listaCategoria))

            # verifica se o novo nome que desejo alterar já existe e altera se não existir
            if len(filtrarCategoriaExiste) == 0:
                alterarCategoria = list(map(lambda lerCategoria: Categoria(categoriaAlterada)
                                            if(lerCategoria.categoria == categoriaAlterar)
                                            else(lerCategoria), listaCategoria))
                
                print('Categoria alterada com sucesso!')

            else:
                print('Essa categoria já existe!')

        else:
            print('A categoria que deseja alterar não existe.')

        with open('categorias.txt', 'w') as arquivo:
            for categoria in alterarCategoria:
                arquivo.writelines(categoria.categoria)
                arquivo.writelines('\n')

    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()

        if len(categorias) == 0:
            print('Sem categorias registradas')
            return 0
        
        for categoria in categorias:
            print(f'Categoria: {categoria.categoria}')


class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        listaEstoque = DaoEstoque.ler()
        listaCategoria = DaoCategoria.ler()

        filtrarCategoria = list(filter(lambda listaCategoria: listaCategoria.categoria == categoria, listaCategoria))
        filtrarProdutoEstoque = list(filter(lambda listaEstoque: listaEstoque.produto.nome == nome, listaEstoque))

        if len(filtrarCategoria) > 0:
            if len(filtrarProdutoEstoque) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)

                print('Produto cadastrado com sucesso!')

            else:
                print('Impossível cadastrar! Esse produto já existe em estoque.')

        else:
            print('Impossível cadastrar! Categoria inexistente.')

    def removerProduto(self, nome):
        listaEstoque = DaoEstoque.ler()
        filtrarEstoque = list(filter(lambda listaEstoque: listaEstoque.produto.nome == nome, listaEstoque))

        if len(filtrarEstoque) > 0:
            for i in range(len(listaEstoque)):
                listaEstoque[i].produto.nome == nome
                del listaEstoque[i]
                break

            print('Produto removido com sucesso!')

        else:
            print('Impossível remover! O produto não existe no estoque.')

        with open('estoque.txt', 'w') as arquivo:
            for produto in listaEstoque:
                arquivo.writelines(produto.produto.nome + '|' + produto.produto.preco + '|'
                                   + produto.produto.categoria + '|' + str(produto.quantidade))
                arquivo.writelines('\n')

    def alterarProduto(self, nomeProduto, novoNome, novoPreco, novaCategoria, novaQuantidade):
        listaEstoque = DaoEstoque.ler()
        listaCategoria = DaoCategoria.ler()
        filtrarCategoria = list(filter(lambda listaCategoria: listaCategoria.categoria == novaCategoria, listaCategoria))

        if len(filtrarCategoria) > 0:
            filtrarProdutoEstoque = list(filter(lambda listaEstoque: listaEstoque.produto.nome == nomeProduto, listaEstoque))

            if len(filtrarProdutoEstoque) > 0:
                filtrarNomeProdutoExiste = list(filter(lambda listaEstoque: listaEstoque.produto.nome == novoNome, listaEstoque))

                if len(filtrarNomeProdutoExiste) == 0:
                    alterarProduto = list(map(lambda produto:
                                              Estoque(Produtos(novoNome, novoPreco, novaCategoria), novaQuantidade)
                                              if(produto.produto.nome == nomeProduto)
                                              else(produto), listaEstoque))

                    print('Produto alterado com sucesso!')

                else:
                    print('Impossível alterar o nome! Esse produto já existe.')

            else:
                print('Impossível alterar! O Produto não existe no estoque.')

            with open('estoque.txt', 'w') as arquivo:
                for produto in alterarProduto:
                    arquivo.writelines(produto.produto.nome + '|' + produto.produto.preco + '|'
                                       + produto.produto.categoria + '|' + str(produto.quantidade))
                    arquivo.writelines('\n')

        else:
            print('Impossível alterar! A Categoria não existe')

    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()

        if len(estoque) == 0:
            print('Estoque vazio!')

        else:
            print('==========Produto==========')
            for produto in estoque:
                print(f'Nome: {produto.produto.nome}\n'
                      f'Preço: {produto.produto.preco}\n'
                      f'Categoria: {produto.produto.categoria}\n'
                      f'Quantidade: {produto.quantidade}'
                    )
                print('-----------------')


class ControllerVenda:
    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        listaEstoque = DaoEstoque.ler()
        temp = []
        existeEmEstoque = False
        temQuantidade = False

        for produto in listaEstoque:
            if existeEmEstoque == False:
                if produto.produto.nome == nomeProduto:
                    existeEmEstoque = True

                    if produto.quantidade >= quantidadeVendida:
                        temQuantidade = True
                        produto.quantidade = int(produto.quantidade) - int(quantidadeVendida)

                        vendido = Venda(Produtos(produto.produto.nome, produto.produto.preco, produto.produto.categoria),
                                        vendedor, comprador, quantidadeVendida)

                        valorCompra = int(quantidadeVendida) * int(produto.produto.preco)

                        DaoVenda.salvar(vendido)

            # guardar os valores dentro da variável temporária para não perder nenhuma informação
            temp.append(Estoque(Produtos(produto.produto.nome, produto.produto.preco, produto.produto.categoria), produto.quantidade))

        arquivo = open('estoque.txt', 'w')
        arquivo.write('')

        for i in temp:
            with open('estoque.txt', 'a') as arquivo:
                arquivo.writelines(i.produto.nome + '|' + i.produto.preco + '|'
                                    + i.produto.categoria + '|' + str(i.quantidade))
                arquivo.writelines('\n')

        if existeEmEstoque == False:
            print('Impossível prosseguir! O produto não existe em estoque.')
            return None
        
        elif not temQuantidade:
            print('A quantidade de venda não contém no estoque.')
            return None
        
        else:
            print('Venda realizada com sucesso!')
            return valorCompra

    def relatorioProdutos(self):
        listaVendas = DaoVenda.ler()
        listaProdutos = []

        for venda in listaVendas:
            nome = venda.produtosVendido.nome
            quantidade = venda.quantidadeVendido
            tamanho = list(filter(lambda produto: produto['produto'] == nome, listaProdutos))

            if len(tamanho) > 0:
                listaProdutos = list(map(lambda produto: {'produto' : nome,'quantidade' : int(produto['quantidade']) + int(quantidade)} if(produto['produto'] == nome) else(produto), listaProdutos))

            else:
                listaProdutos.append({'produto' : nome, 'quantidade' : int(quantidade)})

        ordenado = sorted(listaProdutos, key=lambda k: k['quantidade'], reverse=True)
        a = 1

        print('Esses são os produtos mais vendidos')
        for i in ordenado:
            print(f'==========Produto [{a}]==========')
            print(f"Produto: {i['produto']}\n"
                  f"Quantidade: {i['quantidade']}\n")
            a += 1

    def mostrarVendas(self, dataInicial, dataFinal):
        listaVendas = DaoVenda.ler()
        dataInicioFormatada = datetime.strptime(dataInicial, '%d/%m/%Y')
        dataFinalFormatada = datetime.strptime(dataFinal, '%d/%m/%Y')

        vendasSelecionadas = list(filter(lambda venda: datetime.strptime(venda.data, '%d/%m/%Y') >= dataInicioFormatada
                                         and datetime.strptime(venda.data, '%d/%m/%Y') <= dataFinalFormatada, listaVendas))

        contador = 1
        totalVendido = 0

        for venda in vendasSelecionadas:
            print(f'==========Venda [{contador}]==========')
            print(f'Nome: {venda.produtosVendido.nome}\n'
                  f'Preço: {venda.produtosVendido.preco}\n'
                  f'Categoria: {venda.produtosVendido.categoria}\n'
                  f'Quantidade: {venda.quantidadeVendido}\n'
                  f'Cliente: {venda.comprador}\n'
                  f'Vendedor: {venda.vendedor}\n'
                  f'Data: {venda.data}\n')
            
            totalVendido += int(venda.produtosVendido.preco) * int(venda.quantidadeVendido)
            contador += 1

        print(f'Total vendido: {totalVendido}')


class ControllerFornecedor:
    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        listaFornecedor = DaoFornecedor.ler()
        listaCnpj = list(filter(lambda lista: lista.cnpj == cnpj, listaFornecedor))
        listaTelefone = list(filter(lambda lista: lista.telefone == telefone, listaFornecedor))

        if len(listaCnpj) > 0:
            print('Esse CNPJ já existe.')

        elif len(listaTelefone) > 0:
            print('Esse telefone já existe.')

        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone ) >= 10:
                DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
                print('Fornecedor cadastrado com sucesso!')

            else:
                print('Digite um CNPJ ou telefone válido.')

    def removerFornecedor(self, nome):
        listaFornecedores = DaoFornecedor.ler()
        fornecedores = list(filter(lambda fornecedor: fornecedor.nome == nome, listaFornecedores))

        if len(fornecedores) > 0:
            for i in range(len(fornecedores)):
                if listaFornecedores[i].nome == nome:
                    del listaFornecedores[i]
                    break

        else:
            print('O fornecedor que deseja remover não existe.')
            return None

        with open('fornecedores.txt', 'w') as arquivo:
            for fornecedor in listaFornecedores:
                arquivo.writelines(fornecedor.nome + '|' + fornecedor.cnpj + '|'
                                   + fornecedor.telefone + '|' + fornecedor.categoria)
                arquivo.writelines('\n')

            print('Fornecedor removido com sucesso!')

    def alterarFornecedor(self, nomeAlterar, novoNome, novoCnpj, novoTelefone, novaCategoria):
        listaFornecedores = DaoFornecedor.ler()

        existeFornecedor = list(filter(lambda fornecedor: fornecedor.nome == nomeAlterar, listaFornecedores))

        if len(existeFornecedor) > 0:
            fornecedorCnpj = list(filter(lambda fornecedor: fornecedor.cnpj == novoCnpj, listaFornecedores))

            if len(fornecedorCnpj) == 0:
                fornecedorAlterado = list(map(lambda fornecedor: Fornecedor(novoNome, novoCnpj, novoTelefone, novaCategoria)
                                              if(fornecedor.nome == nomeAlterar) else(fornecedor), listaFornecedores))
                
            else:
                print('O CNPJ informado já existe.')

        else:
            print('O fornecedor que deseja alterar não foi encontrado.')

        with open('fornecedores.txt', 'w') as arquivo:
            for fornecedor in fornecedorAlterado:
                arquivo.writelines(fornecedor.nome + '|' + fornecedor.cnpj + '|'
                                   + fornecedor.telefone + '|' + fornecedor.categoria)
                arquivo.writelines('\n')

            print('Fornecedor alterado com sucesso!')

    def mostrarFornecedores(self):
        fornecedores = DaoFornecedor.ler()

        if len(fornecedores) == 0:
            print('Lista de fornecedores vazia!')
            return None
        
        print('==========Fornecedores==========')
        for fornecedor in fornecedores:
            print(f'Categoria fornecida: {fornecedor.categoria}\n'
                  f'Nome: {fornecedor.nome}\n'
                  f'Telefone: {fornecedor.telefone}\n'
                  f'CNPJ: {fornecedor.cnpj}')
            print('----------------------')
