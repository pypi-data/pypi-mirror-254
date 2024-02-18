from pySAXS.guisaxs.qt import plugin
from pySAXS.guisaxs.qt import dlgXeuss3Surveyor
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import os

#from pySAXS.guisaxs.qt import startpyFAICalib

classlist=['pluginSurveyorXeuss3']#,'pluginFAI',]







    
class pluginSurveyorXeuss3(plugin.pySAXSplugin):
    menu="Data Treatment"
    subMenu="Tools"
    subMenuText="Xeuss3 Surveyor"
    icon="numero-3.png"
    toolbar=True
        
    def execute(self):
        #display the FAI dialog box
        parameterfile=None#self.parent.pref.get("parameterfile",'pyFAI')
        #print "XEUSS"
        self.dlg=dlgXeuss3Surveyor.XeussSurveyorDialog(self.parent,parameterfile)
        self.dlg.show()
        