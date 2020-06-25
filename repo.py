import sys
import os
import subprocess
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('hidden.txt',scope)

gc = gspread.authorize(credentials)
wks = gc.open('SublimeDocs').sheet1
sheetdata = wks.get_all_records()
ARsheetdata = wks.get_all_values()
class program:

        def PopLocalFile(self, Filename):
                for data in sheetdata:
                        if data['Document Name'] == Filename:
                                open(Filename,'w').write(data['Document data'])
                                #print(data['Document data'])

        def AutoUpload(self, Filename):
                self.Filename = Filename
                saved = open(Filename,'r').read()

                while True:
                        if saved != open(Filename,'r').read():
                                new = open(Filename,'r').read()
                                i = 1
                                for data in ARsheetdata:
                                        if data[0] == Filename:
                                                updateTime = time.strftime('%d/%m/%Y')
                                                #wks.update_cell(row, column, 'new data')
                                                wks.update_cell(i, 2, new)
                                                wks.update_cell(i, 3, updateTime)
                                                print('Everything has been backed up!')
                                                saved = new
                                                i = 1

                                        i=(i+1)

        def OpenSubtext(self, Filename):
                self.Filename = Filename
                print('Opening '+ Filename +' with sublime text')
                subprocess.call([""xdg-open"", Filename])

        def __init__(self, Filename):
                self.Filename = Filename
                self.PopLocalFile(Filename)
                self.OpenSubtext(Filename)
                self.AutoUpload(Filename)

def spellcheck():
        for data in sheetdata:
                print(data['Document Name'])

        UserInput = input('What file would you like to open? ')

        if UserInput == 'exit':
                return

        for data in sheetdata:
                if UserInput == data['Document Name']:
                        UserInput = program(UserInput)
'''
 this is the spellcheck and im having trouble with it.
                elif error == true:
                        print(""Sorry, I couldn't find that file, did you type it correctly?"")        
                        spellcheck()

'''


spellcheck()