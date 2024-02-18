import wx
from wbBase import App, ApplicationWindow

from wbBase.control.textEditControl import TextEditCtrl

def test_app_instance():
    app = App(test=True)
    assert isinstance(app, App)
    app.Destroy()

def test_ApplicationWindow_instance():
    app = App(test=True)
    assert isinstance(app.TopWindow, ApplicationWindow)
    app.Destroy()

def test_TextEditCtrl():
    app = App(test=True)
    textEditCtrl = TextEditCtrl(app.TopWindow)
    assert isinstance(textEditCtrl, TextEditCtrl)
    app.Destroy()
