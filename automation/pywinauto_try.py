from pywinauto import Desktop
from pywinauto.application import Application

app = Application().start("notepad.exe")
app.UntitledNotepad.menu_select("帮助(&H)->关于记事本")
about = app.window(title='关于“记事本”')
about.close()

app.UntitledNotepad.print_control_identifiers()
app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces=True)
desktop = Desktop(backend='uia')
print(desktop.windows())
