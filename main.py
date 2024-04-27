import PySimpleGUI as sg

reply = ''

# All the stuff inside your window.
layout = [  [sg.Text("What's your name?")],
            [sg.InputText()],
            [sg.Text(reply, key='reply')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Desktop.GPT', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    name = values[0]

    reply = 'Hello {name} !'

    if event == 'Ok':
        window['reply'].update(reply)

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    print('Hello', values[0], '!')

window.close()
