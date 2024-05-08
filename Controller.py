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
