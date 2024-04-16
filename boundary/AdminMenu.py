import PySimpleGUI as sg
from control.AdminControl import AdminControl

class AdminMenu:

    def __init__(self):
        self.adminControl = AdminControl()

    def getAdminCountrol(self):
        return self.adminControl
    def Menu(self):
        header = ['Username','Password','Email','UserType','UserStatus']
        tableValues = self.getAdminCountrol().viewAllUser()
        Layout = [
            [sg.Text('Welcome to Admin Menu')],
            [sg.InputText(key='searchText',size=(20)),sg.Button('Search'),sg.Button('Create'),sg.Button('Update'),sg.Button('Freeze'),sg.Button('Show all')],
            [sg.Table(values=tableValues,headings=header,key='table')],
            [sg.Button('Logout')]
        ]
        window = sg.Window('Admin',Layout)
        while True:
            event, values = window.read()
            if event in (None,'Logout'):
                break 
            if event == 'Search':
                try:
                    tableValues = self.getAdminCountrol().seachAUser(values['searchText'])
                    print(tableValues[0][1])
                    window['table'].update(values=tableValues)
                except Exception as e:
                    sg.Popup(e)
            if event == 'Show all':
                tableValues = self.getAdminCountrol().viewAllUser()
                window['table'].update(values=tableValues)
            if event == 'Freeze':
                username = values['searchText']
                try:
                    self.getAdminCountrol().freezeUser(username)
                    tableValues = self.adminControl.seachAUser(values['searchText'])
                    window['table'].update(values=tableValues)
                    sg.Popup('Freeze success!')
                except Exception as e:
                    sg.Popup(e)
            if event == 'Create':
                username = self.create()
                if username != '':
                    tableValues = self.adminControl.seachAUser(username)
                    window['table'].update(values=tableValues)
            if event == 'Update':
                try:
                    username = values['searchText']
                    username = self.update(username)
                    if username != '':
                        tableValues = self.adminControl.seachAUser(username)
                        window['table'].update(values=tableValues)
                except Exception as e:
                    sg.Popup(e)
        window.close()

    def create(self):
        username = ''
        Layout = [
            [sg.Text('Username',size=8),sg.InputText()],
            [sg.Text('Password',size=8), sg.InputText()],
            [sg.Text('Email',size=8), sg.InputText()],
            [sg.Text('UserType',size=8), sg.Combo(['admin','agent','buyer','seller'])],
            [sg.Button('Create'),sg.Button('Cancel')]
        ]
        window = sg.Window('Create', Layout)
        while True:
            event,value = window.read()
            if event in ('Cancel',None):
                break
            if event == 'Create':
                try:
                    self.getAdminCountrol().createUser(value[0],value[1],value[2],value[3])
                    username = value[0]
                    sg.Popup('Create success!')
                    break
                except Exception as e:
                    sg.Popup(e)
        window.close()
        return username


    def update(self,oldUsername):
        username = ''
        user = self.adminControl.seachAUser(oldUsername)
        Layout = [
            [sg.Text('Username', size=8), sg.InputText(user[0][0])],
            [sg.Text('Password', size=8), sg.InputText(user[0][1])],
            [sg.Text('Email', size=8), sg.InputText(user[0][2])],
            [sg.Text('UserType', size=8), sg.Combo(['admin', 'agent', 'buyer', 'seller'],default_value=user[0][3])],
            [sg.Button('Update'), sg.Button('Cancel')]
        ]
        window = sg.Window('Update', Layout)
        while True:
            event, value = window.read()
            if event in ('Cancel', None):
                break
            if event == 'Update':
                try:
                    self.getAdminCountrol().updateUser(oldUsername,value[0], value[1], value[2], value[3],user[0][4])
                    username = value[0]
                    sg.Popup('Update success!')
                except Exception as e:
                    sg.Popup(e)
                break
        window.close()
        return username

