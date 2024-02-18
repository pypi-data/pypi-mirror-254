from PyQt5 import QtGui, QtCore, QtWidgets

'''import guidata
from  guidata.dataset import datatypes
from guidata.dataset import dataitems
'''
import numpy
from pySAXS.LS import LSusaxs
from pySAXS.guisaxs.dataset import *
from pySAXS.guisaxs.qt import plugin
from pySAXS.LS import invariant
from pySAXS.guisaxs.qt import dlgPeakPlot

classlist = ['pluginPeakPlot']  # need to be specified


class pluginPeakPlot(plugin.pySAXSplugin):
    menu = "Data Treatment"
    subMenu = "Plot "
    subMenuText = "Mark position"
    icon = "location-pin.png"

    # subMenuText="Background and Data correction"

    def execute(self):
        label = self.selectedData

        self.childSaxs = dlgPeakPlot.dlgPeakPlot(self.parent, datasetname=label)
        self.childSaxs.show()



