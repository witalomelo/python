import os;

restaurantes = [{'nome':'Praca', 'categoria':'japonesa','ativo': False},
                {'nome': 'Pizza Suprema', 'categoria': 'Italiana', 'ativo': True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo': False }]

def exibir_nome_do_programa():
    '''Exibe o nome do programa'''
    print('Sabor Express\n')

def exibir_opcoes():
    '''Exibe as opcoes disponiveis no menu principal'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')
    
def cadastrar_novo_restaurante():
    '''Essa funcao é responsavel por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria
    
    Output:
    - Adiciona um novo restaurante a lista de restaurantes
    
    '''
    exibir_subtitulo('Cadastrar novo restaurante\n')
    nome = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome}: ')
    dados_restaurante = {'nome': nome, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'Restaurante {nome} cadastrado com sucesso !')
    
    voltar_ao_menu_principal()
    
def listar_restaurantes():
    '''Lista os restaurantes presentes na lista
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo('Listando restaurantes')
    
    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(22)} | {'Status'}')
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print (f'- {nome.ljust(20)} | {categoria.ljust(20)} | {ativo}')
            
    voltar_ao_menu_principal()

def ativar_restaurante():
    ''' Alterar o estado ativo/ desativado de um restaurante
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operacao
    '''
    exibir_subtitulo('Alterando estado do restaurante')
    nome = input('Digite o nome do restaurante que deseja alterar status: ').strip().lower()
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome == restaurante['nome'].lower():
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] # troca independente de estar ativo ou nao
            mensagem = f'O restaurante {nome.capitalize()} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome.capitalize()} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('Restaurante nao encontrado! ')
        
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Digite uma opção: '))
                
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            ativar_restaurante()           
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    
        '''
        # match
        match opcao_escolhida:  
            case 1:
                print('Adicionar restaurante')
            case 2:
                print('Listar restaurante')
            case 3:
                print('Ativar restaurante')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
        '''
    except ValueError:
        opcao_invalida()
                       
# print(f'Opção escolhida: {opcao_escolhida}')

def finalizar_app():
    exibir_subtitulo('Finalizando programa...')
     
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()
    
def opcao_invalida():
    print('opcao invalida !\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
    
def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()
