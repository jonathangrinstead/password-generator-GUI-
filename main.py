import PySimpleGUI as sg
import string
import secrets
import pyperclip

sg.theme('BlueMono')

def password_generator(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

# All the stuff in the window.
layout = [[ sg.Push(),sg.Text('Generate a Password',font=("Calibri", 16)), sg.Push()],
            [ sg.Push(), sg.Button('Generate', key='Generate', font=("Calibri")), sg.Push()],
            [sg.Push(),sg.Text('', font=("Calibri", 16), key='-OUTPUT-'),sg.Push()], 
            [sg.Push(),sg.Button('Copy to Clipboard', key='Copy',font=("Calibri")),sg.Push()]]

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
        sg.popup('Password copied to clipboard!', title='Success',font=('Calibri'), auto_close=True, auto_close_duration=3, button_justification='center')

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

window.close()
