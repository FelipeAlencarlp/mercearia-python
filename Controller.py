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
