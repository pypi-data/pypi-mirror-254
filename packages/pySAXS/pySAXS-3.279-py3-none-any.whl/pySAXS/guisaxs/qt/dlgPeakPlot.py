from PyQt5 import QtGui, QtCore, uic,QtWidgets


import pySAXS.LS.SAXSparametersXML as SAXSparameters
import sys

import pySAXS
from pySAXS.tools import isNumeric
from pySAXS.tools import filetools
from pySAXS.guisaxs.dataset import *
import math
import numpy
import os

class dlgPeakPlot(QtWidgets.QDialog):
    def __init__(self,parent,datasetname=""):#, referencedata=None,backgrounddata=None,datasetlist=None):
        QtWidgets.QDialog.__init__(self)
        self.ui = uic.loadUi(pySAXS.UI_PATH+"dlgPeaks.ui", self)#
        self.datasetname=datasetname
        #self.workingdirectory=self.parent.getWorkingDirectory()
        self.parent=parent
        self.data_dict=self.parent.data_dict
        self.printout=parent.printTXT
        self.icon = QtGui.QIcon(pySAXS.ICON_PATH + 'location-pin.png')
        self.setWindowIcon(self.icon)
        label=None
        label = self.parent.getCurrentSelectedItem()
        if label is not None:

            i = self.data_dict[label].i
            q = self.data_dict[label].q

        self.posA=0.1
        self.ui.buttonBox.clicked.connect(self.click)
        self.ui.edtPosA.textChanged.connect(self.posAchanged)
        self.ui.edtPosA.setText(str(self.posA))
        self.ui.edtPosNM.textChanged.connect(self.posNMchanged)
        self.ui.show()

    def click(self,obj=None):
        name=obj.text()
        #print(str(name))
        if "eset" in name:
            self.parent.plotframe.replot()
            #self.close()
        elif "pply" in name:
            try:
                self.apply()
            except:
                pass
        elif "lose" in name:
            self.close()

    def posAchanged(self):
        posA=float(self.ui.edtPosA.text())
        self.ui.lblPosNM.setText("%8.5f nm"%((2*math.pi/posA)*0.1))
        self.posA=posA
    def posNMchanged(self):
        posNM=float(self.ui.edtPosNM.text())
        self.ui.lblPosA.setText("%6.5f A-1"%((2*math.pi/posNM)*0.1))
        self.posA=(2*math.pi/posNM)*0.1

    def apply(self):
        #plot lines on the graph
        posA = self.posA#float(self.ui.edtPosA.text())
        n=int(self.ui.spinNumber.value())+1
        posAs=numpy.arange(n)*posA
        xmin,ymin,xmax,ymax=self.parent.plotframe.getXYminMax()
        #self.ylim_min, self.ylim_max
        #print(self.parent.plotframe.ylim_min,self.parent.plotframe.ylim_max)
        #self.parent.plotframe.annotate( posA, (self.parent.plotframe.ylim_max-self.parent.plotframe.ylim_min)/2,str(posA))
        self.parent.plotframe.axes.vlines(posAs, 0, 0.9, transform = self.parent.plotframe.axes.get_xaxis_transform(),  linestyles='--',lw=1)
        #self.parent.plotframe.axes.vlines(posAs,ymin,ymax,colors='black',linestyles='--')
        self.parent.plotframe.draw('a')