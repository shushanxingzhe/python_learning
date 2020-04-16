import uiautomation

taskbar = uiautomation.PaneControl(searchDepth=1, Name='任务栏')
trayNotify = taskbar.PaneControl(searchDepth=1, ClassName='TrayNotifyWnd')

sysPager = trayNotify.PaneControl(searchDepth=1, ClassName='SysPager')

toolbar = sysPager.ToolBarControl(searchDepth=1, ClassName='ToolbarWindow32')
children = toolbar.GetChildren()
for item in children:
    uiautomation.LogControl(item, 1, True)

youdao_icon = toolbar.ButtonControl(searchDepth=1, RegexName='网易有道词典.*')
youdao_icon.Click()

youdao = uiautomation.PaneControl(searchDepth=1, RegexName='网易有道词典.*')
youdao_input = youdao.EditControl(searchDepth=1, ClassName='Edit')
youdao_input.SendKeys('guten tag')
youdao_input.SendKeys('{enter}')
