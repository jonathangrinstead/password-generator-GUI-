import PySimpleGUI as sg

sg.theme('BluePurple')

reply = ''

# All the stuff inside your window.
layout = [[ sg.Push(),sg.Text('Generate a Password'), sg.Push()],
            [ sg.Push(), sg.Button('Generate'), sg.Push()] ]

# Create the Window
window = sg.Window('Password Generator', layout,size=(300,150 ))

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    name = values[0]

    print(name)

    if event == 'Ok':
        window['reply'].update(reply)

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

window.close()
