import PySimpleGUI as sg
import string
import secrets
import pyperclip

sg.theme('BluePurple')

def password_generator(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

# All the stuff in the window.
layout = [[ sg.Push(),sg.Text('Generate a Password'), sg.Push()],
            [ sg.Push(), sg.Button('Generate', key='Generate'), sg.Push()],
            [sg.Push(),sg.Push(),sg.Text('', size=(30, 1), key='-OUTPUT-'),sg.Push()], 
            [sg.Push(),sg.Button('Copy to Clipboard', key='Copy'),sg.Push()]]

# Create the Window
window = sg.Window('Password Generator', layout,size=(300,150 ))

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if event == 'Generate':
        # Call the password generator function and update the output Text Element
        new_password = password_generator()
        window['-OUTPUT-'].update(new_password)

    elif event == 'Copy':
        # Copy the currently displayed password to the clipboard
        current_password = window['-OUTPUT-'].get()
        pyperclip.copy(current_password)
        sg.popup('Password copied to clipboard!')

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

window.close()
