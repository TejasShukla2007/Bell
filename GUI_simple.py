import PySimpleGUI as qt
qt.theme('DarkTeal9')
layout = [
    [qt.Text('Speaking deaf-mute',size=(30,0))],
    [qt.Text('Communicate better.',size=(40,0)),qt.InputText(key='Response')],
    [qt.Button('Submit')]
]
window = qt.Window('Home',layout)
while True:
    event,value = window.read()
    print(value['Response'])
    print(event)
    if event=='Submit' or event==qt.WIN_CLOSED:
        break
window.close()