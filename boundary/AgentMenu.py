import PySimpleGUI as sg
from His.AgentControl import AgentControl

class AgentMenu:

    def __init__(self,agentControl = AgentControl()):
        self.agentControl = agentControl
    def getAgentCountrol(self):
        return self.agentControl
    def Menu(self):
        header = ['Title','Description','BedNum','BathNum','Size','Price','Status','Views','Shortlisted','Seller']
        tableValues =self.getAgentCountrol().viewAllProperty()
        Layout = [
            [sg.Text('Welcome to Agent Menu')],
            [sg.InputText(key='searchText',size=(20)),sg.Button('Search'),sg.Button('Create'),sg.Button('Remove'),sg.Button('Update'),sg.Button('Show all')],
            [sg.Table(values=tableValues,headings=header,key='table')],
            [sg.Button('Logout')]
        ]
        window = sg.Window('Agent',Layout)
        while True:
            event, values = window.read()
            if event in (None,'Logout'):
                break
            if event == 'Search':
                try:
                    tableValues = self.getAgentCountrol().searchProperty(values['searchText'])
                    print(tableValues[0][1])
                    window['table'].update(values=tableValues)
                except Exception as e:
                    sg.Popup(e)
            if event == 'Show all':
                tableValues = self.getAgentCountrol().viewAllProperty()
                window['table'].update(values=tableValues)
            if event == 'Remove':
                title = values['searchText']
                try:
                    self.getAgentCountrol().removeProperty(title)
                    tableValues = self.getAgentCountrol().viewAllProperty()
                    window['table'].update(values=tableValues)
                    sg.Popup('Remove success!')
                except Exception as e:
                    sg.Popup(e)
            if event == 'Create':
                title = self.create()
                tableValues = self.getAgentCountrol().searchProperty(title)
                window['table'].update(values=tableValues)
            if event == 'Update':
                title = values['searchText']
                self.update(title)
                tableValues = self.getAgentCountrol().searchProperty(title)
                window['table'].update(values=tableValues)
        window.close()

    def create(self):
        title = ''
        Layout = [
            [sg.Text('Title',size=8),sg.InputText()],
            [sg.Text('Description',size=8), sg.InputText()],
            [sg.Text('BedNum',size=8), sg.InputText()],
            [sg.Text('BathNum',size=8), sg.InputText()],
            [sg.Text('Size', size=8), sg.InputText()],
            [sg.Text('Price', size=8), sg.InputText()],
            [sg.Text('Seller', size=8), sg.InputText()],
            [sg.Button('Create'),sg.Button('Cancel')]
        ]
        window = sg.Window('Create', Layout)
        while True:
            event,value = window.read()
            if event in ('Cancel',None):
                break
            if event == 'Create':
                try:
                    self.getAgentCountrol().createProperty(value[0],value[1],int(value[2]),int(value[3]),int(value[4]),float(value[5]),value[6])
                    title = value[0]
                    sg.Popup('Create success!')
                    break
                except Exception as e:
                    sg.Popup('seller not exist')
        window.close()
        return title

    def update(self,title):
        property = self.getAgentCountrol().searchProperty(title)
        Layout = [
            [sg.Text('Title', size=8), sg.InputText(property[0][0])],
            [sg.Text('Description', size=8), sg.InputText(property[0][1])],
            [sg.Text('BedNum', size=8), sg.InputText(property[0][2])],
            [sg.Text('BathNum', size=8), sg.InputText(property[0][3])],
            [sg.Text('Size', size=8), sg.InputText(property[0][4])],
            [sg.Text('Price', size=8), sg.InputText(property[0][5])],
            [sg.Text('States', size=8), sg.Combo(['available','sold'] ,default_value=property[0][6])],
            [sg.Text('Seller', size=8), sg.InputText(property[0][9])],
            [sg.Button('Update'), sg.Button('Cancel')]
        ]
        window = sg.Window('Update', Layout)
        while True:
            event, value = window.read()
            if event in ('Cancel', None):
                break
            if event == 'Update':
                self.getAgentCountrol().updatePropertry(value[0],title,value[1], int(value[2]), int(value[3]), int(value[4]),
                                                       float(value[5]), value[6],value[7])
                title = value[0]
                sg.Popup('Update success!')
                break
        window.close()
        return title
