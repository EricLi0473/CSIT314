import PySimpleGUI as sg
from control.UserControl import UserControl
from control.AgentControl import AgentControl
from AdminMenu import AdminMenu
from AgentMenu import AgentMenu

class LoginWindow:

    def __init__(self):
        self.userControl = UserControl()

    def getUserControl(self):
        return self.userControl
    def login(self):
        Layout = [
            [sg.Text('Log In')],
            [sg.Text('UserName'), sg.InputText()],
            [sg.Text('PassWord'), sg.InputText()],
            [sg.Button('Login'), sg.Button('Cancel')]
        ]
        window = sg.Window('login', Layout)
        while True:
            event, values = window.read()
            if event in (None, 'Cancel'):
                break 
            if event == 'Login':
                try:
                    user,userType = self.userControl.checkLogin(values[0], values[1])
                    if userType == 'admin':
                        adminMenu = AdminMenu()
                        adminMenu.Menu()
                    if userType == 'agent':
                        agent = user.getUser()
                        agentControl = AgentControl(agent)
                        agentMenu = AgentMenu(agentControl)
                        agentMenu.Menu()
                    if userType == 'buyer':
                        sg.Popup('This is Buyer window')
                    if userType == 'seller':
                        sg.Popup('This is Seller window')
                    break
                except Exception as e:
                    sg.Popup(e)
        window.close()

loginWindow = LoginWindow()
loginWindow.login()
