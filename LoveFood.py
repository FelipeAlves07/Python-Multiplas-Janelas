import PySimpleGUI as sg


# Criando os layouts das janelas
def janela_de_login():
    sg.theme('LightGrey4')
    layout = [
        [sg.Text('Insira seu nome')],
        [sg.Input()],
        [sg.Button('Avançar')]
    ]
    return sg.Window('Login', layout=layout, finalize= True)


def janela_de_pedido():
    sg.theme('LightGrey4')
    layout = [
        [sg.Text('Escolha seu pedido')],
        [sg.Checkbox('X-tudo', key='sanduiche1'), sg.Checkbox('X-tudo especial', key='sanduiche2')],
        [sg.Button('Voltar'), sg.Button('Finalizar Pedido!')]
    ]
    return sg.Window('Monte o pedido', layout=layout, finalize= True)
# Criando as janelas 
janela1, janela2 = janela_de_login(), None
# Criando um loop de leitura de eventos
while True:
    window,event,values = sg.read_all_windows()
    # Quando janela for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    # Quando queremos ir pra prox. janela
    if window == janela1 and event == 'Avançar':
        janela2 = janela_de_pedido()
        janela1.hide()
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and event == 'Finalizar Pedido!':
        if values['sanduiche1'] == True and values['sanduiche2'] == True:
            sg.Popup('Pedido de X-tudo e X-tudo especial realizado com sucesso. Por favor aguarde! Levará em média 15 a 20 minutinhos. Thank you ♥')
        elif values ['sanduiche1'] == True:
            sg.Popup('Pedido de X-tudo realizado com sucesso. Por favor aguarde! Levará em média 15 a 20 minutinhos. Thank you ♥')
        elif values['sanduiche2'] == True:
            sg.Popup('Pedido de X-tudo especial realizado com sucesso. Por favor aguarde! Levará em média 15 a 20 minutinhos. Thank you ♥')
    if window == janela2 and event == sg.WIN_CLOSED:
        break
