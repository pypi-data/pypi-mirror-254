from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QAbstractTableModel,Qt


#from PyQt4.Qt import QString
from fileinput import filename
from pyFAI import azimuthalIntegrator
from pySAXS.guisaxs import dataset
from pySAXS.guisaxs.qt import preferences
from pySAXS.guisaxs.qt import QtMatplotlib
from pySAXS.guisaxs.qt import dlgAbsoluteI
#from pySAXS.guisaxs.qt import dlgAutomaticFit
import matplotlib.colors as colors
from pySAXS.tools import FAIsaxs
from pySAXS.tools import filetools
import os
import shutil
import sys
from scipy import ndimage
if sys.version_info.major>=3:
    import configparser
else:
    import ConfigParser as configparser
from pySAXS.guisaxs.qt.dlgAbsoluteI import dlgAbsolute
import pySAXS.LS.SAXSparametersXML as SAXSparameters

from matplotlib.patches import Circle
from PyQt5 import QtTest
from pySAXS.guisaxs import pySaxsColors
import pandas as pd
import pandas
from scipy import interpolate



AUTOMATIC_FIT=False


def my_excepthook(type, value, tback):
    # log the exception here
    #print value
    #print tback
    # then call the default handler
    sys.__excepthook__(type, value, tback)

sys.excepthook = my_excepthook

#from reportlab.graphics.widgets.table import TableWidget
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.patches as patches
from matplotlib.lines import Line2D
#from spyderlib.widgets.externalshell import namespacebrowser
from time import *
import fabio
import numpy
import os
import os.path
import pyFAI
import sys
import threading
import glob
import fnmatch

import pySAXS
from  pySAXS.LS import SAXSparametersXML
from pySAXS.guisaxs.qt import dlgQtFAITest



ICON_PATH=pySAXS.__path__[0]+os.sep+'guisaxs'+os.sep+'images'+os.sep

HEADER=['file','name','exposure','Distance','config','Trans. Flux','Integrated Flux','thickness','Type','x','z']
HEADER_WIDTH=[150,100,70,70,150,100,100,70,100,100,20,20]
FROM_EDF=['Comment','count_time','pilroi0','pilai1','x','z']
FROM_RPT=['filename',"exposure","transmitted flux","incident flux",'samplex','samplez']
FROM_DAT=[None,'Comment','ExposureTime','SampleDistance',None,'TransmittedFlux','SumForIntensity1','Thickness',None,'x','z']
#IMAGE_PARAMS={"edf":FROM_EDF,"tiff":FROM_RPT}
DAT_TYPE=['*.dat']
XCfile="c:\DATA\\2023_05_17_OT\Week_end_WAXS_SAXS"+os.sep+"XeussConfigs.csv"

FOR_ABSOLUTE=['D','TransmittedFlux','thickness','time','wavelength','pixel_size']
EDFHEADER_TO_ABSOLUTE=['SampleDistance','TransmittedFlux','Thickness','ExposureTime','Wavelength','PSize_1']



class XeussSurveyorDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, parameterfile=None, outputdir=None):
        QtWidgets.QWidget.__init__(self, parent)
        #self.ui = dlgSurveyorui.Ui_surveyorDialog()
        self.ui = uic.loadUi(pySAXS.UI_PATH+"dlgXeuss3Surveyor.ui", self)#
        #print experimentName
        self.setWindowTitle('Continuous Xeuss 3 analysis tool for pySAXS (Experimental)')
        if parent is not None:
            # print "icon"
            self.setWindowIcon(parent.windowIcon())

        self.parent = parent
        self.plotapp= None
        self.printout = None
        self.whereZ=False
        self.workingdirectory = None
        self.oldListOfFiles=None
        self.fai=None
        self.mad=None
        self.img=None

        #self.faiMemory=None
        self.faiConfig=None
        self.lastDatas=None
        self.df_xeussConfig=None

        self.colors=pySaxsColors.pySaxsColors()

        self.pixmapExcl = QtGui.QPixmap(ICON_PATH+'exclamation.png')
        self.pixmapValid = QtGui.QPixmap(ICON_PATH+'tick.png')
        #print(self.ui.windowIcon)
        self.icon = QtGui.QIcon(pySAXS.ICON_PATH + 'numero-3.png')
        self.setWindowIcon(self.icon)
        self.AUTOMATIC_FIT=False
        self.PROCESSED = {}  # keep on memory the processed data
        self.plt=self.ui.matplotlibwidget.figure
        self.pltEDF = self.ui.matplotlibwidgetEDF.figure
        #self.canvas = FigureCanvas(Figure(figsize=(5, 3)))  # FigureCanvas(self.plt)
        #self.ui.matplotlibwidget=self.canvas
        #self.plt=self.canvas.figure#plt.figure()
        self.plt.patch.set_facecolor('White')
        self.axes = self.plt.gca()
        self.pltEDF.patch.set_facecolor('White')
        self.axesEDF = self.pltEDF.gca()
        #self.axes = self.plt.add_subplot(111)#subplots()

        self.clbar=None#(imgplot)
        self.ui.tabWidget.setCurrentIndex(0)
        #self.plt.tight_layout()
        #self.plt.subplots_adjust(0.2, 0.2, 0.8, 0.8)  # left,bottom,right,top
        self.plt.subplots_adjust(0.20, 0.10, 0.90, 0.90)  # left,bottom,right,top
        self.pltEDF.subplots_adjust(0.20, 0.10, 0.90, 0.90)  # left,bottom,right,top
        #self.plt.subplots(constrained_layout=True)

        #self.ui.setupUi(self)
        #self.ui.paramFileButton.clicked.connect(self.OnClickparamFileButton)
        self.ui.changeDirButton.clicked.connect(self.OnClickchangeDirButton)
        self.ui.btnCopyFiles.clicked.connect(self.OnClickCopyFiles)
        #QtCore.QObject.connect(self.ui.STARTButton, QtCore.SIGNAL("clicked()"), self.OnClickSTARTButton)
        #QtCore.QObject.connect(self.ui.STOPButton, QtCore.SIGNAL("clicked()"), self.OnClickSTOPButton)
        #self.ui.plotChkBox.clicked.connect(self.OnClickPlotCheckBox)
        self.ui.btnExtUpdate.setIcon(QtGui.QIcon(ICON_PATH + 'refresh.png'))
        self.ui.btnExtUpdate.clicked.connect(self.updateListInit)
        self.ui.btnExtUpdate.setIcon(QtGui.QIcon(ICON_PATH+'refresh.png'))
        #print(ICON_PATH+'refresh.png')
        self.ui.tableWidget.cellClicked[int, int].connect(self.cellClicked)
        self.ui.tableWidget.cellDoubleClicked[int, int].connect(self.cellDoubleClicked)
        self.ui.btnSelectXeussConfFile.clicked.connect(self.OnClickChangeXeussConfigFile)
        self.ui.btnLoadMask.clicked.connect(self.OnClickChangeMaskFile)
        #self.ui.btnDisplaySelected.clicked.connect(self.btnDisplayClicked)
        self.ui.btnZApply.clicked.connect(self.btnZApplyClicked)
        #self.ui.btnReset.clicked.connect(self.btnZResetClicked)
        #self.ui.btnDisplayAV.clicked.connect(self.btnDisplayAVClicked)
        self.ui.btnProcessSelection.clicked.connect(self.btnProcessSelectionClicked)
        self.ui.btnProcessALL.clicked.connect(self.btnProcessALLClicked)
        self.ui.chkDisplayCircles.clicked.connect(self.displayImage)
        self.ui.edit_Q.textChanged.connect(self.displayImage)
        self.ui.chkDisplayQmin.clicked.connect(self.displayImage)
        self.ui.tabWidget.currentChanged.connect(self.btnDisplayClicked)

        #self.ui.paramViewButton.clicked.connect(self.OnClickparamViewButton)
        #self.ui.btnCenterOfMass.clicked.connect(self.OnClickCenterOfMassButton)
        self.ui.btnExportList.clicked.connect(self.OnClickExportList)
        self.ui.navi_toolbarEDF = NavigationToolbar(self.ui.matplotlibwidgetEDF, self)
        self.ui.verticalLayoutEDF.insertWidget(0, self.ui.navi_toolbarEDF)#verticalLayout_2
        #remove the Pan tool
        l=self.ui.navi_toolbarEDF.actions()
        for i in l:
            #print i.text()
            if i.text()=='Pan':
                panAction=i
            if i.text()=='Customize':
                customizeAction=i
            if i.text()=='Subplots':
                subplotAction=i

        #self.ui.navi_toolbar.removeAction(panAction)
        self.ui.navi_toolbarEDF.removeAction(customizeAction)
        self.ui.navi_toolbarEDF.removeAction(subplotAction)
        #--Autoscale
        self.AutoscaleAction= QtWidgets.QAction('Autoscale', self)
        #self.AutoscaleAction.triggered.connect(self.OnAutoscale)
        #self.ui.navi_toolbarEDF.addAction(self.AutoscaleAction)
        #-- fix scale
        self.FixScaleAction= QtWidgets.QAction(QtGui.QIcon(ICON_PATH+'magnet.png'),'Fix Scale', self)
        #self.FixScaleAction.setCheckable(True)
        self.FixScaleAction.setChecked(False)
        self.FixScaleAction.triggered.connect(self.OnButtonFixScale)
        #self.ui.navi_toolbarEDF.addAction(self.FixScaleAction)

        self.ui.navi_toolbar = NavigationToolbar(self.ui.matplotlibwidget, self)
        self.ui.verticalLayoutIQ.insertWidget(0, self.ui.navi_toolbar)  # verticalLayout_2

        self.SelectedFile=None
        #self.ui.labelSelectedFIle.setText("")
        #self.ui.btnDisplaySelected.setEnabled(False)
        #self.ui.btnDisplayAV.setEnabled(False)
        self.ui.radioButton_log.setChecked(True)
        self.ui.radioButton_lin.toggled.connect(lambda:self.btnStateLinLog(self.radioButton_lin))
        self.ui.radioButton_log.toggled.connect(lambda:self.btnStateLinLog(self.radioButton_log))
        self.DISPLAY_LOG=True
        self.EXPORT_LIST=[]

        #self.ui.chkDisplayBeam.clicked.connect(self.OnClickDisplayBeam)
        #self.ui.chkDisplayCircles.clicked.connect(self.btnDisplayClicked)
        #self.ui.btnGetBeamXY.clicked.connect(self.OnClickGetBeamXY)
        #self.ui.btnBeamApply.clicked.connect(self.OnClickButtonBeam)
        #self.ui.btnTransferParams.clicked.connect(self.OnClickButtonTransferParams)
        #self.ui.edit_Q.textChanged.connect(self.btnDisplayClicked)
        #self.ui.edit_dd.textChanged.connect(self.btnDisplayClicked)
        #self.ui.chkDisplayMaskFile.clicked.connect(self.btnDisplayClicked)
        #self.ui.btnResetGeom.clicked.connect(self.btnResetGeometry)
        
        #------------ to uncomment for automatic fit
        #self.ui.btnPAF.setEnabled(True)
        #self.ui.btnPAF.clicked.connect(self.btnEnableAutomaticFit)
        
        if self.AUTOMATIC_FIT:
            self.ui.btnAutomaticFit.setEnabled(True)
            self.automaticFitApp = dlgAutomaticFit.dlgAutomaticFit(parent)
            #self.automaticFitApp.show()
            self.ui.btnAutomaticFit.clicked.connect(self.btnDisplayAutomaticFitClicked)
            #self.ui.btnPAF.setEnabled(True)
            #self.ui.btnPAF.clicked.connect(self.btnProcessALLClicked)
        #--- absolute intensities
        self.ui.btnCheckSolvent.clicked.connect(self.btnCheckSolventClicked)
        if self.parent is None:
            self.ui.chkSubSolvent.setEnabled(False)
            self.ui.btnCheckSolvent.setEnabled(False)
        else:
            if self.parent.referencedata is not None:
                self.ui.solventEdit.setText(str(self.parent.referencedata))



        self.parameterfile=parameterfile

        '''
        try:
            if self.parameterfile is not None and self.parameterfile!="":
                self.ui.paramTxt.setText(str(parameterfile))
        except:
            pass
        '''


         #-- get preferences
        self.pref=preferences.prefs()

        if parent is not None:
            self.printout = parent.printTXT
            self.workingdirectory = parent.workingdirectory
            self.pref=self.parent.pref
            #print("import pref")
            #print(self.pref)
            #print(self.pref.getName())
            try:
                if self.pref.fileExist():
                    self.pref.read()
                    #print( "ref file exist")
                    dr=self.pref.get('defaultdirectory',section="guisaxs qt")
                    #print "dr :",dr
                    if dr is not None:
                        self.workingdirectory=dr
                        #print 'set wd',dr
                        self.ui.DirTxt.setText(str(self.workingdirectory))
                    '''
                    pf=self.pref.get('parameterfile',section="pyFAI")

                    if pf is not None:
                        self.parameterfile=pf
                        self.ui.paramTxt.setText(str(self.parameterfile))
                        try:
                            self.OnClickButtonTransferParams()
                        except:
                            print("problem when trying to read parameters")
                    '''
                    #ext=self.pref.get('fileextension',section="pyFAI")
                    #if ext is not None:
                    #    self.ui.extensionTxt.setText(ext)


                else:
                    self.pref.save()
            except:
                print("couldnt reach working directory ")
                #return


        else :
            self.workingdirectory = "Y:/2017/2017-08-24-OT" #for debugging
            self.ui.DirTxt.setText(self.workingdirectory)   #for debugging

        #--------- read Xeuss Conf

        cf = self.pref.get('configurationFile', section="XEUSS3")
        if cf is not None:
            self.XCfile = cf
            self.ui.edtXeussConfFile.setText(str(self.XCfile))
        else:
            self.XCfile=XCfile
        #print(self.XCfile)
        self.readXeussConfig()

        cf = self.pref.get('maskFilename', section="XEUSS3")
        #print('maskfilename='+cf)
        if cf is not None:
            self.maskFilename = cf
            self.ui.edtMaskFileName.setText(str(self.maskFilename))
        else:
            self.maskFilename=""
        # print(self.XCfile)
        if self.maskFilename!="":
            try:
                self.readMaskEDF()
            except:
                self.mad=None
        #print(self.workingdirectory)
        self.imageToolWindow = None
        self.updateListInit()
        self.fp = str(self.ui.DirTxt.text())
        txt=""
        for i in DAT_TYPE:
            txt+=i+" "
        self.ui.extensionTxt.setText(txt)
        '''self.qfsw = QtCore.QFileSystemWatcher()
        self.fp = str(self.ui.DirTxt.text())
        if self.fp!='':
            self.qfsw.addPath(self.fp)
            QtCore.QObject.connect(self.qfsw,QtCore.SIGNAL("directoryChanged(QString)"),self.onFileSystemChanged)
            #self.qfsw.directoryChanged.connect(self.updateListInit)
        '''
        self._fileSysWatcher    = QtCore.QFileSystemWatcher()
        if self.fp!='':
            if os.path.isdir(self.fp):
                self._fileSysWatcher.addPath(self.fp)
                self._fileSysWatcher.directoryChanged.connect(self.slotDirChanged)



    def readXeussConfig(self):
        '''
        read the xeuss3 config file
        '''
        #print('read xeuss config')
        try:
            self.df_xeussConfig=pd.read_csv(self.XCfile,sep=";")
        except:
            print("cannot read xeuss conf file "+str(self.XCfile))
            return
        self.model=pandasModel(self.df_xeussConfig)
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.show()

    def getConfig(self,header):
        #
        #try to obtain the config name from the header
        #
        # we need the S2 , sampleDistance , source informations
        #header is a dictionnary
        #source is on wavelength
        #try:
        #print(self.df_xeussConfig)
        #print(header)
        try:
            #source=float(header["Wavelength"]  )          #S2 is on s2hl + s2hr
            source = round(float(header['Wavelength']), 15)  # round with 4 digits
        except:
            #print('error Source type not found')
            return None, None
        #print('source ='+str(source))
        try:
            S2=float(header['s2hl'])+float(header['s2hr'])
            #sample distance
            S2D=round(float(header['SampleDistance']),4) #round with 4 digits
             #print("source %s, S2 = %6.4f, distance %6.4f"%(source,S2,S2D))
        except :
            #print('error slit or sample distance type not found')
            return None, None
        #get the information from panda table
        #conf=self.df_xeussConfig[self.df_xeussConfig['S2']==0.25]# & (pd.to_numeric(df_config['SampleDistance'])==S2D)].iloc[0,0]
        try:

            conf=self.df_xeussConfig[(pd.to_numeric(self.df_xeussConfig['S2'])==S2) & (pd.to_numeric(self.df_xeussConfig['SampleDistance'])==S2D) \
                &(pd.to_numeric(self.df_xeussConfig['Wavelength']) == source)].iloc[0,0]

        except:
            print('conf not found  : distance = %s S2 = %s source = %s' % (str(S2D), str(S2),str(source)))
            conf=None
            return None,None
        #conf.iloc[0,0]
        #print(conf)
        #except :
        #    conf="?"
        if conf is not None:
            try:
                conf_dict=self.df_xeussConfig[self.df_xeussConfig['configName'] == conf].to_dict(orient='records')[0]
            except:
                conf_dict=None
        else:
            #print('conf not found  : distance = %s S2 = %s source = %s' % (str(S2D), str(S2), str(source)))
            return None,None

        return conf,conf_dict

    #@QtCore.pyqtSlot("QString")
    def slotDirChanged(self, path):
        #print(path, " changed !")
        #print(self._fileSysWatcher.directories())
        self.updateListInit()


    def OnClickparamFileButton(self):
        '''
        Allow to select a parameter file
        '''
        fd = QtWidgets.QFileDialog(self)
        #old=self.ui.paramTxt.text()
        filename = fd.getOpenFileName(directory=self.workingdirectory)[0]
        #self.workingdirectory = filename
        # print filename
        if filename=='':
            return
        self.ui.paramTxt.setText(filename)
        # self.ui.editor_window.setText(plik)
        self.OnClickButtonTransferParams()
        self.radialPrepare()

    def OnClickCopyFiles(self):
        '''
        User clicked to copy files on another directory
        '''
        #1- ask for directory
        fd = QtWidgets.QFileDialog(self)
        destinationDir = fd.getExistingDirectory(self, "Open Directory", \
                                      directory=self.workingdirectory)#,options=QFileDialog.ShowDirsOnly| QFileDialog.DontResolveSymlinks)
        print(destinationDir)
        #2- get the selected files
        #3- copy the files
        for item in self.ui.tableWidget.selectedIndexes():

            row=item.row()
            name=str(self.ui.tableWidget.item(row,0).text())
            #self.SelectedFile=name
            #processName=""
            #print(name)
            #fullname=self.workingdirectory+os.sep+name
            #print(name)
            # try to copy
            src_path=self.workingdirectory+os.sep+name
            dst_path=destinationDir+os.sep+name
            try:
                shutil.copy(src_path, dst_path)
                print(src_path + " ->" + dst_path+" succeeded !")
                src_path_edf=src_path[:-3]+"edf"
                dst_path_edf=dst_path[:-3]+"edf"
                if os.path.exists(src_path_edf):
                    shutil.copy(src_path_edf, dst_path_edf)
                    print(src_path_edf + " ->" + dst_path_edf + " succeeded !")

            except :
                print('failed to copy the files')
                print(src_path+" ->"+dst_path)


    def OnClickChangeXeussConfigFile(self):
        '''
        Allow to select a parameter file
        '''
        fd = QtWidgets.QFileDialog(self)
        # old=self.ui.paramTxt.text()
        filename = fd.getOpenFileName(directory=self.workingdirectory)[0]
        # self.workingdirectory = filename
        # print filename
        if filename == '':
            return
        self.XCfile=filename
        self.ui.edtXeussConfFile.setText(filename)
        #save in prefs
        try:
            self.pref.set('configurationFile', self.XCfile,section="XEUSS3")
            self.pref.save()
        except:
            pass

    def OnClickChangeMaskFile(self):
        '''
        Allow to select a parameter file
        '''
        fd = QtWidgets.QFileDialog(self)
        # old=self.ui.paramTxt.text()
        filename = fd.getOpenFileName(directory=self.workingdirectory)[0]
        # self.workingdirectory = filename
        # print filename
        if filename == '':
            return
        self.maskFilename = filename
        self.ui.edtMaskFileName.setText(filename)
        # save in prefs
        try:
            self.pref.set('maskFilename', self.maskFilename, section="XEUSS3")
            self.pref.save()
        except:
            pass

    def OnClickchangeDirButton(self):
        '''
        Allow to select a directory
        '''
        #QFileDialog
        #fd = QtWidgets.QFileDialog(self, directory=self.workingdirectory)
        #fd.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        dir=QtWidgets.QFileDialog.getExistingDirectory(directory=self.workingdirectory)
        #if fd.exec_() == 1:
        #print fd.selectedFiles()
        #dir = str(fd.selectedFiles().first())
        #dir = str(fd.selectedFiles()[0])
        #print(dir)
        if dir=='':
            return
        if not(os.path.isdir(dir)):
            return
        # dir=fd.getOpenFileName()
        self.ui.DirTxt.setText(dir)
        self.workingdirectory = dir
        self.updateListInit()

        try:
            self.pref.set('defaultdirectory', self.workingdirectory,section="guisaxs qt")
            self.pref.save()
        except:
            pass
        '''
        l=self.qfsw.directories()
        print "previous watched directories :",list(l)
        self.qfsw.removePaths(l)
        self.qfsw.addPath(dir)
        l=self.qfsw.directories()
        print "Now watched directories :",list(l)
        '''
        #print("la")
        l=self._fileSysWatcher.directories()
        #print("previous watched directories :",list(l))
        if len(l)>0:
            self._fileSysWatcher.removePaths(l)
        self._fileSysWatcher.addPath(dir)
        l=self._fileSysWatcher.directories()
        #print("now watched directories :",list(l))

    def cellClicked(self,row,col):
        self.SelectedFile=str(self.ui.tableWidget.item(row,0).text())
        self.SelectedFiles=[]
        for item in self.ui.tableWidget.selectedIndexes():
            # ll.append()
            row = item.row()
            name = str(self.ui.tableWidget.item(row, 0).text())
            self.SelectedFiles.append(name)

        #self.ui.labelSelectedFIle.setText(self.workingdirectory+os.sep+self.SelectedFile)
        #print self.workingdirectory+os.sep+self.SelectedFile
        #self.ui.btnDisplaySelected.setEnabled(True)
        #self.ui.btnDisplayAV.setEnabled(True)
        self.btnDisplayClicked()

    def cellDoubleClicked(self,row,col):
        self.SelectedFiles=[str(self.ui.tableWidget.item(row,0).text())]
        #self.ui.labelSelectedFIle.setText(self.workingdirectory+os.sep+self.SelectedFile)
        #print self.workingdirectory+os.sep+self.SelectedFile
        #self.ui.btnDisplaySelected.setEnabled(True)
        #self.ui.btnDisplayAV.setEnabled(True)
        self.btnDisplayClicked()

    def btnDisplayClicked(self):
        '''
        display the image
        '''
        ind=self.ui.tabWidget.currentIndex()
        try:
            if ind==0:
                self.displayPLot()
            elif ind==1:
                self.displayImage()
            else:
                self.displayPLot()
                self.displayImage()
        except:
            pass


    def getQIDatas(self,fi):
        '''
        read datas
        '''
        f=open(fi)
        lines=f.readlines()
        n=0
        #print(lines)
        while lines[n][0]=="#":
            #print(lines[n][0])
            n+=1
        #print("header size %i" %n )
        dat = numpy.loadtxt(fi, comments='#', skiprows=n+1, encoding='utf8')
        dat = numpy.transpose(numpy.array(dat))

        q = dat[0]
        i = dat[1]
        s = dat[2]
        #removing nan values
        isnotNan = numpy.where(~numpy.isnan(i))
        q = q[isnotNan]
        i = i[isnotNan]
        s = s[isnotNan]
        #nan_mask = numpy.isnan(i)
        #nan_indices = numpy.where(nan_mask)
        #print(nan_indices)
        #if len(nan_indices)>0:
        #    print("number of nan %i"%len(nan_indices))
        return q,i,s

    def displayPLot(self):
        #print('plotting '+self.SelectedFile)
        self.axes.cla()
        for  selected in self.SelectedFiles:
            if selected is None:
                return
            '''
            try:
                fi=self.workingdirectory+os.sep+selected
                q,i,s=self.getQIDatas(fi)
                #q=self.DATAS[selected]['q']
            except:
                print("pySAXS : unable to open dat file : "+self.workingdirectory+os.sep+selected)
                #QtWidgets.QMessageBox.information(self,"pySAXS", "unable to open imagefile : "+self.workingdirectory+os.sep+self.SelectedFile, buttons=QtWidgets.QMessageBox.Ok, defaultButton=QtWidgets.QMessageBox.NoButton)
                return
            '''
            #print(q)
            name=self.DATAS[selected]['Comment']
            self.axes.plot(self.DATAS[selected]['q'], self.DATAS[selected]['i'], '-', label=name)
        self.axes.loglog()
        self.axes.legend()
        self.axes.grid()
        self.axes.set_xlabel('q (A-1)')
        self.axes.set_ylabel('I (cm-1)')
        plt=self.ui.matplotlibwidget
        plt.draw()



    def displayImage(self):
        '''
        display the image
        '''
        self.axesEDF.cla()

        imagefile=self.SelectedFiles[0]
        if imagefile is None:
            print('no file selected')
            return
        imagefile=imagefile[:-3]+"edf"
        if not os.path.exists(self.workingdirectory+os.sep+imagefile):
            print('edf file not exist in the directory')
            return

        try:
            fi=self.workingdirectory+os.sep+imagefile
            self.img = fabio.open(fi) # Open image file
        except:
            print("pySAXS : unable to open imagefile : "+self.workingdirectory+os.sep+imagefile)
            #QtWidgets.QMessageBox.information(self,"pySAXS", "unable to open imagefile : "+self.workingdirectory+os.sep+self.SelectedFile, buttons=QtWidgets.QMessageBox.Ok, defaultButton=QtWidgets.QMessageBox.NoButton)
            return
        #print('trying to plot '+
        self.ui.lblEDFFile.setText(imagefile)
        D=self.img.data
        """if self.ui.chkDisplayMaskFile.isChecked() and self.mad is not None:
            D = numpy.logical_not(self.mad) * D
        """
        xmax, ymax = numpy.shape(D)
        extent = 0, xmax, 0, ymax
        if self.whereZ:
            zmin=float(self.ui.edtZmin.text())
            zmax=float(self.ui.edtZmax.text())
            D=numpy.where(D<=zmin,zmin,D)
            D=numpy.where(D>zmax,zmax,D)
        else:
            self.ui.edtZmin.setText(str(D.min()))
            self.ui.edtZmax.setText(str(D.max()))
        norm=colors.LogNorm(vmin=D.min(), vmax=D.max())
        if self.DISPLAY_LOG:
            zmin=float(self.ui.edtZmin.text())
            if zmin<=0:
                zmin=0.1
                self.ui.edtZmin.setText("0.1")
            zmax=float(self.ui.edtZmax.text())
            D=numpy.where(D<=zmin,zmin,D)
            D=numpy.where(D>zmax,zmax,D)
            norm=colors.LogNorm(vmin=D.min(), vmax=D.max())
            #--- display the mask
            '''if self.ui.chkDisplayMaskFile.isChecked() and self.mad is not None:
                imgplot=self.axes.imshow(numpy.logical_not(self.mad)*D,cmap="jet",norm=norm)
            else:
                
            '''
            imgplot=self.axesEDF.imshow(D,cmap="jet",norm=norm)

            #print "mode log"#,norm=colors.LogNorm(vmin=D.min(), vmax=D.max()))            # Display as an image  norm=colors.LogNorm(vmin=Z1.min(), vmax=Z1.max()),
        else:
            #--- display the mask
            #if self.ui.chkDisplayMaskFile.isChecked() and self.mad is not None:
            #    imgplot=self.axes.imshow(numpy.logical_not(self.mad)*D,cmap="jet")#,norm=norm)
            #else:
            imgplot=self.axesEDF.imshow(D,cmap="jet")#,norm=norm)

        #imgplot.set_cmap('nipy_spectral')

        #--- display the mask
        '''if self.ui.chkDisplayMaskFile.isChecked():
            #
            #self.imgMask = fabio.open(self.workingdirectory+os.sep+self.SelectedFile)
            if self.mad is not None:
                #print("mask exist in memory")
                aa=self.ui.sliderTransparency.value()/100.0
                #print(aa)
                self.axes.imshow(numpy.logical_not(self.mad)*D,cmap="jet",alpha=aa)#,extent=extent)
        '''

        #--- fix scale
        if self.FixScaleAction.isChecked():
            #axes limits should have been memorized
            self.axesEDF.set_xlim((self.xlim_min,self.xlim_max))
            self.axesEDF.set_ylim((self.ylim_min,self.ylim_max))

        #---- display the beam (or not)

        #if self.ui.chkDisplayBeam.isChecked():
        #draw a cross
        #try:#if text is not float
        BeamX=float(self.img.header['Center_1'])#float(self.ui.edtBeamX.text())
        BeamY=float(self.img.header['Center_2'])#float(self.ui.edtBeamY.text())
        '''xmax,ymax=numpy.shape(D)
        #print xmax, ymax
        #print plt.axes
        #except:
        #print "text is not float"
        #BeamX=0.0
        #BeamY=0.0

        x1, y1 = [BeamX, 0], [BeamX, ymax] #vertical
        x2, y2 = [0,BeamY], [xmax, BeamY]
        #self.axes.plot(x1, y1, x2, y2, marker = 'o')

        # Create a Rectangle patch
        #rect = patches.Rectangle((0, 0),BeamX, BeamY,linewidth=1,edgecolor='r',facecolor='none')
        #rect2 = patches.Rectangle((BeamX, BeamY),xmax, ymax,linewidth=1,edgecolor='r',facecolor='none')
        '''
        crossSize=40
        line1=Line2D([BeamX-crossSize,BeamX+crossSize],[BeamY,BeamY],linewidth=1,color='w')
        line2=Line2D([BeamX,BeamX],[BeamY-crossSize,BeamY+crossSize],linewidth=1,color='w')

        # Add the lines to the Axes
        self.axesEDF.add_line(line1)
        self.axesEDF.add_line(line2)

        # ---- display the circles
        if self.ui.chkDisplayCircles.isChecked():
            # draw circle to Q
            # --- NEW METHOD USING CONTOUR
            # get an array of q
            self.radialPrepare()
            qim = self.fai.array_from_unit(shape=numpy.shape(self.img.data), unit="q_A^-1")
            # using contour
            # wich q max ?
            Q = float(self.ui.edit_Q.text())
            #print(Q)
            posq = numpy.arange(Q, qim.max(), Q)  # array of q
            CS = self.axesEDF.contour(qim, levels=posq, cmap="autumn", linewidths=1, linestyles="dashed")
            self.axesEDF.clabel(CS, inline=True, fontsize=10)  # ,fmt='%1.4f A-1')

        # ---- display the circles
        if self.ui.chkDisplayQmin.isChecked():
            # draw circle to Q
            # --- NEW METHOD USING CONTOUR
            # get an array of q
            self.radialPrepare()
            qim = self.fai.array_from_unit(shape=numpy.shape(self.img.data), unit="q_A^-1")
            # using contour
            # wich q max ?
            #print(self.DATAS.keys())
            if 'qmin_precise' in self.DATAS[imagefile[:-3]+'dat']:
                qmin = float(self.DATAS[imagefile[:-3]+'dat']['qmin_precise'])
                # print(Q)
                posq = [qmin]
                CS = self.axesEDF.contour(qim, levels=posq, cmap="Wistia", linewidths=1)#, linestyles="dashed")
                self.axesEDF.clabel(CS, inline=True, fontsize=10)  # ,fmt='%1.4f A-1')

        # Display the image
        self.pltEDF.subplots_adjust(0.05, 0.05, 0.95, 0.95)  # left,bottom,right,top
        self.ui.matplotlibwidgetEDF.draw_idle()


    def btnDisplayAVClicked(self):
        if self.SelectedFile is None:
            return
        self.radialAverage(self.workingdirectory+os.sep+self.SelectedFile)

    def OnAutoscale(self):
        #print('autoscale')
        sh=self.img.data.shape
        plt=self.ui.matplotlibwidget
        plt.axes.set_ylim((sh[0],0))
        plt.axes.set_xlim((0,sh[1]))
        self.xlim_min,self.xlim_max=plt.axes.get_xlim()
        self.ylim_min,self.ylim_max=plt.axes.get_ylim()
        plt.draw()

    def OnButtonFixScale(self):
        #print("OnButtonFixScale")
        #memorize the current scale"
        plt=self.ui.matplotlibwidget
        self.xlim_min,self.xlim_max=plt.axes.get_xlim()
        self.ylim_min,self.ylim_max=plt.axes.get_ylim()
        #print self.xlim_min,self.xlim_max," - ",self.ylim_min,self.ylim_max


    def btnZApplyClicked(self):
        try:
            self.zmin=float(self.ui.edtZmin.text())
            zmax=float(self.ui.edtZmax.text())
            self.whereZ=True
            self.btnDisplayClicked()
            #print zmin, zmax
        except:
            pass
    def btnZResetClicked(self):
        self.whereZ=False
        self.btnDisplayClicked()

    def btnStateLinLog(self,b):
        #print("toggled")
        if b.text() == "lin":
            if b.isChecked() == True:
                self.DISPLAY_LOG=False
            else:
                self.DISPLAY_LOG=True
                #print "zmin text :",self.ui.edtZmin.text()
                if float(self.ui.edtZmin.text())<=0:
                    self.ui.edtZmin.setText("0.1")

        self.whereZ=True
        self.displayImage()

    def updateListInit(self):
        '''
        Update the initial List WITHOUT treatment
        '''
        #print('generate list')

        #self.ext = str(self.ui.extensionTxt.text())
        #if self.ext == '':
        #      self.ext = '*.*'
        #listoffile=[]
        self.fp = os.path.normpath(str(self.ui.DirTxt.text()))
        #try:
        listoffile,files=self.getList(self.fp)#get a dictionnary
        if listoffile is None:
            msg = QtWidgets.QMessageBox()
            msg.setText("No files in this directory : " + self.fp)
            msg.exec()
            return
        #except:
        if len(listoffile)==0:
            msg = QtWidgets.QMessageBox()
            msg.setText("No files in this directory : " + self.fp)
            msg.exec()
            return
        #    listoffile={}
        #    files=[]

        #    print('erreur %s'%self.fp)
        files=sorted(listoffile,reverse=True) #get a sorted list of the dictionnary
        #print(files)  # an ordered list of files
        #print(listoffile)
        self.ui.tableWidget.setRowCount(0) #clear the table
        self.ui.tableWidget.setRowCount(len(files))
        #headerNames = ["File", "date", "processed", "new"]
        #if self.FROM_EXPERIMENT is not None:
        headerNames=HEADER
        self.EXPORT_LIST=[headerNames]
        self.ui.tableWidget.setColumnCount(len(headerNames))
        self.ui.tableWidget.setHorizontalHeaderLabels(headerNames)
        self.DATAS={}   #key : filename   values : dict of header and datas

        i = 0
        #print self.EXPORT_LIST
        ll=[]
        self.ui.progressBar.setMaximum(len(files))
        for name in files:
            #ll=[name]+listoffile[name]
            self.ui.progressBar.setValue(i)
            # get header from dat
            head = self.getInformationFromDat(name)
            #print(head)
            self.DATAS[name]=head
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(name)))
            #export=[name]
            for col in range(len(HEADER)):
                if i==0:
                    self.ui.tableWidget.setColumnWidth(col, HEADER_WIDTH[col])
                if FROM_DAT[col] is not None:
                    #get info from header
                    try:
                        info=head[FROM_DAT[col]]
                        #print('%s : %s : %i'%(FROM_DAT[col],info,col))
                        self.ui.tableWidget.setItem(i, col, QtWidgets.QTableWidgetItem(str(info)))
                        #export.append(info)
                    except:
                        print('no info found for %s'%FROM_DAT[col])
                        pass
            self.ui.tableWidget.setRowHeight(i, 20)
            if head != {}:
                confName,confDict=self.getConfig(head)

                if confName is not None:
                    self.ui.tableWidget.setItem(i, HEADER.index('config'), QtWidgets.QTableWidgetItem(str(confName)))
                    #export.append(str(confName))
                    #update DATAS
                    if confDict is not None:
                        self.DATAS[name].update(confDict)

                else:
                    #print("no config found for " +str(name))
                    pass
                #------- trying to read datas
            try:
                q,iq,s=self.getQIDatas(self.workingdirectory + os.sep + name)
                self.DATAS[name]['q']=q
                self.DATAS[name]['i'] = iq
                self.DATAS[name]['s'] = s
                self.DATAS[name].update({'q_work': q, 'i_work': i, 's_work': s})
            except:
                print("pySAXS : unable to open dat file : " + self.workingdirectory + os.sep + name)


            i+=1
            #self.EXPORT_LIST.append(export)

        #self.listoffileVerif = glob.glob(os.path.join(self.fp, self.ext))#filetools.listFiles(self.fp,self.ext)
        self.listoffileVerif = listoffile
        self.ui.progressBar.setValue(0)
        #display first
        if len(listoffile)>0:
            self.cellDoubleClicked(0,None)
            if self.ui.chkAutomaticProcess.isChecked:
                #automatic process
                self.btnProcessSelectionClicked()

    def getfiles(self,dirpath):
        a = [s for s in os.listdir(dirpath)
             if os.path.isfile(os.path.join(dirpath, s))]
        a.sort(key=lambda s: os.path.getmtime(os.path.join(dirpath, s)))
        return a

    def getList(self, fp):
        #print "getlist, ",fp
        #print os.path.join(self.fp, self.ext)
        #listoffile = glob.glob(os.path.abspath(self.fp)+os.sep+self.ext)#filetools.listFiles(fp, ext)
        listoffile=[]
        if self.fp=='':
            return [None,None]
        try :
            Files= os.listdir(self.fp)
        except:
            print('cannot reach the directory')
            msg=QtWidgets.QMessageBox()
            msg.setText("Could'nt reach the directory : "+self.fp)
            msg.exec()
            return [None,None]
        for file in Files:
            for ext in DAT_TYPE:
                if fnmatch.fnmatch(file,ext):
                    #print(file)
                    listoffile.append(os.path.abspath(self.fp)+os.sep+file)
        #listoffile.sort(key=lambda s: os.path.getmtime(os.path.join(dirpath, s)))
        #print "end glob : ",listoffile
        files = {}
        ttdict={}
        for name in listoffile:
            '''print(name)

            (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(name)
            print("last modified: %s" % time.ctime(mtime))
            '''
            fich = filetools.getFilename(name)
            try:
                dt = filetools.getModifiedDate(name)
            except:
                dt=None
            newfn = filetools.getFilenameOnly(name)
            try:
                tt=os.path.getmtime(os.path.join(self.fp, name))
            except:
                tt=None
            ttdict[tt]=fich
            ficTiff = newfn
            newfn += '.rgr'
            # print newfn
            if filetools.fileExist(newfn) :
                proc = True
                new = False
            else:
                proc = False
                new = True
            files[fich] = [dt, proc, new,tt]
        #print "end of getlist: ",files
        ttsorted=sorted(ttdict,reverse=True) #get a sorted list of the dictionnary
        #print(ttsorted)
        filessorted=[]
        for i in ttsorted:
            filessorted.append(ttdict[i])
        #print(filessorted)
        return files,filessorted


    def printTXT(self, txt="", par=""):
        '''
        for printing messages
        '''
        if self.printout == None:
            print((str(txt) + str(par)))
        else:
            self.printout(txt, par)

    def readMaskEDF(self):
        """
        read the edf mask
        """
        #print('read mask')
        filename=str(self.ui.edtMaskFileName.text())
        self.mad=fabio.open(filename)

    def radialPrepare(self):
        # print('radial prepare')
        if self.img is None:
            print('error')
            return None, None, None


        head = self.img.header
        dd = float(head['SampleDistance']) * 10  # m->cm
        centerx = float(head['Center_1'])
        centery = float(head['Center_2'])
        tilt = 0
        tiltPlanRotation = 0

        pixelsize = float(head['PSize_1']) * 1e4  # m->micron
        wavelength = float(head['Wavelength'])

        self.faiNewConfig=[dd,centerx,centery,tilt,tiltPlanRotation,pixelsize]
        if self.faiConfig!=self.faiNewConfig:
                #recalculate fai geometry
                #print('recalculate geometry')
                self.fai = FAIsaxs.FAIsaxs()
                self.fai.set_wavelength(wavelength)
                self.fai.setFit2D(dd, centerX=centerx, centerY=centery, tilt=tilt, \
                                  tiltPlanRotation=tiltPlanRotation, \
                                  pixelX=pixelsize, pixelY=pixelsize)
                self.faiConfig=self.faiNewConfig

    def radialPrepareAndAverage(self):
        t0 = time()
        self.radialPrepare()

        ## get the mask
        if self.mad is None:
            self.readMaskEDF()


        #    print "Error plot"
        qdiv = 1000
        qdiv= int(self.ui.edtPyFAINbOfPoints.text())
        qdiv = int(qdiv)
        qtemp, itemp, stemp = self.fai.integrate1d(self.img.data, qdiv, mask=self.mad.data, error_model="poisson",
                                               unit="q_A^-1", )
        q = qtemp
        i = itemp
        s = stemp
        q = qtemp[numpy.nonzero(itemp)]
        i = itemp[numpy.nonzero(itemp)]
        s = stemp[numpy.nonzero(itemp)]
        t1=time()
        #print('radial averaged in %6.4f s'%(t1-t0))
        return q,i,s

    def radialAverage(self, imageFilename,plotRefresh=True):
        if self.fai is None :
            self.radialPrepare()


    def btnProcessALLClicked(self):
        #Process all files in the list
        st=self.ui.chkAutomaticAV.isChecked()
        self.ui.chkAutomaticAV.setChecked(False)
        if self.AUTOMATIC_FIT:
            self.automaticFitApp.clearResult()
        #get the list
        #ll=[]
        n=self.ui.tableWidget.rowCount()
        self.ui.progressBar.setMaximum(n)
        for row in range(0,n):
            #ll.append()
            name=str(self.ui.tableWidget.item(row,0).text())
            name=self.workingdirectory+os.sep+name
            self.radialAverage(name,plotRefresh=False)
            self.ui.progressBar.setValue(row)
            if self.AUTOMATIC_FIT:
                self.btnDisplayAutomaticFitClicked()
                QtTest.QTest.qWait(500)
        #print("LIST : " ,ll)
        #uncheck some box

        #process


        self.radialAverage(name,plotRefresh=True)
        self.ui.progressBar.setValue(0)
        self.ui.chkAutomaticAV.setChecked(st)

    def btnProcessSelectionClicked(self):
         #Process all files in the list
        '''st=self.ui.chkAutomaticAV.isChecked()
        self.ui.chkAutomaticAV.setChecked(False)'''
        param=None
        #get the list
        #ll=[]

        #self.ui.chkCutQRange.isChecked()
        if self.ui.chkMerging.isChecked():
            #try different go to merce process
            self.tryMerge()

            return
        n=self.ui.tableWidget.rowCount()
        self.ui.progressBar.setMaximum(n)


        for item in self.ui.tableWidget.selectedIndexes():

            row=item.row()
            name=str(self.ui.tableWidget.item(row,0).text())
            self.SelectedFile=name
            processName=""
            #print(name)
            fullname=self.workingdirectory+os.sep+name
            q_work = self.DATAS[name]['q']
            i_work = self.DATAS[name]['i']
            s_work = self.DATAS[name]['s']
            self.DATAS[name].update({'q_work': q_work, 'i_work': i_work, 's_work': s_work})

            # from EDF
            if self.ui.radioButton_EDF.isChecked():
                imagefile = name[:-3] + "edf"

                if not os.path.exists(self.workingdirectory + os.sep + imagefile):
                    print('edf file not exist in the directory : ')
                else:
                    try:
                        fi = self.workingdirectory + os.sep + imagefile
                        self.img = fabio.open(fi)  # Open image file
                        # -------- pyFAI
                        #print('radial averaging :' + fi)
                        q_work, i_work, s_work = self.radialPrepareAndAverage()
                        self.DATAS[name].update({'q_work': q_work, 'i_work': i_work, 's_work': s_work})
                        self.DATAS[name].update({'q_edf': q_work, 'i_edf': i_work, 's_edf': s_work})
                    except:
                        print('error when processing file ' + fi)
                    param = SAXSparameters.SAXSparameters()
                    if param is not None:
                        #param.
                        #print(param.parameters)
                        #print(param.get('D'))
                        head = self.img.header
                        #print(head)
                        try:
                            dd = float(head['SampleDistance']) * 100  # m->cm
                            param.set('D',dd)
                        except:
                            print("cannot get the detector distance from edf header")
                        #FOR_ABSOLUTE = ['D', 'TransmittedFlux', 'thickness', 'time', 'wavelength', 'pixel_size']
                        #EDFHEADER_TO_ABSOLUTE = ['SampleDistance', 'TransmittedFlux', 'Thickness', 'ExposureTime','Wavelength', 'PSize_1']
                        #param.calculate_All()
                        #print(head)
                        try:
                            param.set('TransmittedFlux', float(head['TransmittedFlux']))
                        except:
                            print("cannot get the Transmitted Flux from edf header")
                            param.set('TransmittedFlux',1.0)
                        #if float(head['Thickness'])!=0:
                        #    param.set('thickness', float(head['Thickness']))
                        param.set('time', float(head['ExposureTime']))
                        param.set('wavelength', float(head['Wavelength']))
                        param.set('pixel_size', float(head['PSize_1'])*100) #m ->cm




            #do the treatment
            # -------- CUT Q RANGE
            if self.ui.chkCutQRange.isChecked():
                #cut q range
                if 'qmin_precise' in self.DATAS[name]:
                    qmin=float(self.DATAS[name]['qmin_precise'])
                    #print("qmin :"+str(qmin))
                    newq,newi,news=self.clipQmin(q_work,i_work,s_work,qmin)
                    self.DATAS[name].update({'q_clipped':newq,'i_clipped':newi,'s_clipped':news})
                    self.DATAS[name].update({'q_work': newq, 'i_work': newi, 's_work': news})
                    q_work=newq
                    i_work=newi
                    s_work=news
                    processName += "-cut"

            #-------- SUBTRACT SOLVENT if not EDF
            if not self.ui.radioButton_EDF.isChecked() and self.ui.chkSubSolvent.isChecked() and self.parent.referencedata is not None:
                self.subtractSolvent(name,self.parent.referencedata)
                q_work = self.DATAS[name]['q_work']
                i_work = self.DATAS[name]['i_work']
                s_work = self.DATAS[name]['s_work']
                processName += "-sub"
            # create new datas in pySAXS
            myname = self.DATAS[name]['Comment']
            if self.ui.chkKeepFileName.isChecked():
                # keep the filename
                myname=name+"-"+myname
            #if not self.ui.chkMerging.isChecked():
            if not('configName' in self.DATAS[name]):
                myname=name
            else:
                if self.ui.chkConfigName.isChecked():
                    myname=self.DATAS[name]['configName']+"-"+myname

            if self.ui.chkAppendName.isChecked():
                myname+=processName

            #----- Manage the colors
            if myname in self.parent.data_dict:
                #keep the color
                color=self.parent.data_dict[myname].color
            else:
                color = pySaxsColors.pySaxsColors().getColor(len(self.parent.data_dict))  # get a new color

            self.parent.data_dict[myname] = dataset.dataset(myname, q_work, i_work,\
                                                            error=s_work, type='saxs',
                                                            image="Image",color=color)
            if param is not None:
                #subtract solvent here
                if self.ui.chkSubSolvent.isChecked() and self.parent.referencedata is not None:
                    referencedata=self.parent.referencedata
                else:
                    referencedata=None
                try:
                    self.backgd = float(str(self.ui.backgdEdit.text()))
                except:
                    self.backgd = 0.0
                try:
                    self.thickness = float(str(self.ui.thicknessEdit.text()))
                except:
                    self.thickness = 1.0

                newname_scaled = dlgAbsoluteI.OnScalingSAXSApply(self.parent, dataname=myname,
                                                                 parameters=param.parameters,saveRPT=False ,\
                                                                 referencedata=referencedata,\
                                                                 background_by_s=self.backgd, thickness=self.thickness)
                self.parent.data_dict[myname].parameters = param
                self.parent.data_dict[myname].checked = False

            self.PROCESSED[myname]=name #keep on memory the processed data

        self.parent.redrawTheList()
        self.parent.Replot()
        #process last for plot refreshing

        self.ui.progressBar.setValue(0)
        #self.ui.chkAutomaticAV.setChecked(st)

    def tryMerge(self):

        n = self.ui.tableWidget.rowCount()
        self.ui.progressBar.setMaximum(n)
        param=None
        colorMerged=None
        #getting a dataframe with all the files & headers
        fichiers_edf=[]
        for item in self.ui.tableWidget.selectedIndexes():
            row = item.row()
            name = str(self.ui.tableWidget.item(row, 0).text())
            fichiers_edf.append(name)
            #print("will merge %s"%name)
        #print('will process : ')
        #print(fichiers_edf)

        first = True
        for fname in fichiers_edf:

            im = fabio.open(self.workingdirectory + os.sep + fname[:-3]+"edf")
            head = im.header
            new_row = pandas.DataFrame([head])
            new_row['file_name'] = fname
            new_row['DAT_file_name'] = fname[:-3]
            if first:
                df_edf = new_row
                first = False
            else:
                df_edf = pandas.concat([df_edf, new_row], ignore_index=True)
        # df_edf : dataframe with all header
        #self.df_xeussConfig the config
        numeric_columns = ['s2hl', 's2hr', 'SampleDistance', 'Wavelength']
        df_edf[numeric_columns] = df_edf[numeric_columns].apply(pandas.to_numeric, errors='coerce')
        df_edf['S2'] = df_edf['s2hl'] + df_edf['s2hr']
        df_edf['SampleDistance'] = df_edf['SampleDistance'].round(4)
        df_edf['Wavelength'] = df_edf['Wavelength'].round(15)
        # try to join the tables
        merged_df = pandas.merge(df_edf, self.df_xeussConfig, on=['S2', 'SampleDistance', 'Wavelength'], how='left')
        #sort the samples
        samples = merged_df['Comment'].unique()
        print("samples to merge :")
        print(samples)
        #Data_SAMPLE = merged_df[merged_df['Comment'].isin(samples)]
        #Data_SAMPLE_sorted = Data_SAMPLE.sort_values(by='qmin_precise')
        pbValue=0
        self.ui.progressBar.setValue(pbValue)
        for sample_name in samples:
            pbValue +=1
            self.ui.progressBar.setValue(pbValue)
            Data_SAMPLE = merged_df[merged_df['Comment'] == sample_name]
            Data_SAMPLE_sorted = Data_SAMPLE.sort_values(by='qmin_precise')
            #print(Data_SAMPLE_sorted['qmin_precise'])
            colorMerged = pySaxsColors.pySaxsColors().getColor(len(self.parent.data_dict))  # get a new color
            for i in range(len(Data_SAMPLE_sorted)):
                #try if conf is found

                row = Data_SAMPLE_sorted.iloc[i]
                name = row['file_name']
                print('processing  '+str(name))
                print(row['configName'])
                try:
                    test=row['configName']+'-'+name
                except:
                    #no config found
                    print('no config found: failed')
                    break


                #get iq data

                q_work = self.DATAS[name]['q']
                i_work = self.DATAS[name]['i']
                s_work = self.DATAS[name]['s']
                self.DATAS[name].update({'q_work': q_work, 'i_work': i_work, 's_work': s_work})
                datfilename = row['DAT_file_name']
                #q0, i0, e0 = getQIDatas(datfilename)
                t0 = time()
                if self.ui.radioButton_EDF.isChecked():

                    imagefile = name[:-3] + "edf"

                    if not os.path.exists(self.workingdirectory + os.sep + imagefile):
                        print('edf file not exist in the directory : ')
                    else:
                        try:
                            fi = self.workingdirectory + os.sep + imagefile
                            self.img = fabio.open(fi)  # Open image file
                            # -------- pyFAI
                            print('radial averaging :' + fi)
                            q_work, i_work, s_work = self.radialPrepareAndAverage()
                            self.DATAS[name].update({'q_work': q_work, 'i_work': i_work, 's_work': s_work})
                            self.DATAS[name].update({'q_edf': q_work, 'i_edf': i_work, 's_edf': s_work})
                        except:
                            print('error when processing file ' + fi)

                    #
                    param = SAXSparameters.SAXSparameters()
                    if param is not None:
                        # param.
                        # print(param.parameters)
                        # print(param.get('D'))
                        head = self.img.header
                        # print(head)
                        try:
                            dd = float(head['SampleDistance']) * 100  # m->cm
                            param.set('D', dd)
                        except:
                            print("cannot get the detector distance from edf header")
                        # FOR_ABSOLUTE = ['D', 'TransmittedFlux', 'thickness', 'time', 'wavelength', 'pixel_size']
                        # EDFHEADER_TO_ABSOLUTE = ['SampleDistance', 'TransmittedFlux', 'Thickness', 'ExposureTime','Wavelength', 'PSize_1']
                        # param.calculate_All()
                        # print(head)
                        try:
                            param.set('TransmittedFlux', float(head['TransmittedFlux']))
                        except:
                            print("cannot get the Transmitted Flux from edf header")
                            param.set('TransmittedFlux', 1.0)
                        # if float(head['Thickness'])!=0:
                        #    param.set('thickness', float(head['Thickness']))
                        param.set('time', float(head['ExposureTime']))
                        param.set('wavelength', float(head['Wavelength']))
                        param.set('pixel_size', float(head['PSize_1']) * 100)  # m ->cm
                    t1=time()
                    print("edf opened in %6.4fs"%(t1-t0))

                conf = row['configName']
                qmin = float(row['qmin_large'])
                qmax = float(row['qmax_merging'])
                # print('%s : qmin= %s qmax= %s'%(conf,row['qmin_large'],row['qmax_merging']))
                q_work, i_work, s_work = self.clipQmin(q_work, i_work, s_work, qmin)
                '''
                if i < (len(Data_SAMPLE_sorted) - 1):
                    q_work, i_work, s_work = self.clipQmax(q_work, i_work, s_work, qmax)
                self.DATAS[name].update({'q_work': q_work, 'i_work': i_work, 's_work': s_work})
                '''
                # create new datas in pySAXS
                myname = row['Comment']

                if myname in self.parent.data_dict:
                    # keep the color
                    color = self.parent.data_dict[myname].color
                else:
                    if colorMerged is not None:
                        color=colorMerged
                    else:
                        color = pySaxsColors.pySaxsColors().getColor(len(self.parent.data_dict))  # get a new color

                #self.parent.data_dict[myname] = dataset.dataset(myname, q_work, i_work, \
                #                                                error=s_work, type='saxs',
                #                                                image="Image", color=color)

                self.parent.data_dict[myname] = dataset.dataset(myname, q_work, i_work, \
                                                                error=s_work, type='saxs',
                                                                color=color)
                if param is not None:
                    try:
                        self.backgd=float(str(self.ui.backgdEdit.text()))
                    except:
                        self.backgd=0.0
                    try:
                        self.thickness=float(str(self.ui.thicknessEdit.text()))
                    except:
                        self.thickness=1.0
                    newname_scaled = dlgAbsoluteI.OnScalingSAXSApply(self.parent, dataname=myname,
                                                                     parameters=param.parameters,saveRPT=False,\
                                                                     background_by_s=self.backgd,thickness=self.thickness)

                    self.parent.data_dict[myname].parameters = param
                    self.parent.data_dict[myname].checked = False
                    t1 = time()
                    print("scaling in %6.4fs" % (t1 - t0))
                self.PROCESSED[myname] = name  # keep on memory the processed data

                #concatenate
                if param is not None:
                    q1 = self.parent.data_dict[newname_scaled].q
                    i1 = self.parent.data_dict[newname_scaled].i
                    e1 = self.parent.data_dict[newname_scaled].error
                else:
                    q1 = self.parent.data_dict[myname].q
                    i1 = self.parent.data_dict[myname].i
                    e1 = self.parent.data_dict[myname].error
                if i == 0:
                    #firsts datas
                    q_final = q1
                    i_final = i1
                    e_final = e1
                    cut2=qmax
                else:
                    # merging
                    '''
                    q_final = numpy.concatenate((q_final, q1))
                    i_final = numpy.concatenate((i_final, i1))
                    e_final = numpy.concatenate((e_final, e1))
                    '''
                    cut1=qmin
                    #print('cut1 = %6.2f cut2 = %6.2f'%(cut1, cut2))
                    q_final, i_final, e_final = self.merging(q_final, i_final, e_final, q1, i1, e1, cut1, cut2)
                    cut2=qmax
                    #nan_mask = numpy.isnan(i_final)
                    # Print the boolean array
                    #print("Boolean array indicating NaN values:")
                    #print(nan_mask)
                    # Print the indices of NaN values
                    #nan_indices = numpy.where(nan_mask)
                    #print("\nIndices of NaN values:")
                    #print(nan_indices)
            #after all the data from the same sample
            #sort the q
            '''sortedIndexes = numpy.argsort(q_final)
            q_sorted = q_final[sortedIndexes]
            i_sorted = i_final[sortedIndexes]
            e_sorted = e_final[sortedIndexes]
            '''
            t1 = time()
            print("merging in %6.4fs" % (t1 - t0))
            merged_name=self.DATAS[name]['Comment']+"_merged"
            self.parent.data_dict[merged_name] = dataset.dataset(merged_name, q_final, i_final, \
                                                            error=e_final)
            self.parent.data_dict.pop(myname)
            if param is not None:
                if newname_scaled in self.parent.data_dict:
                    self.parent.data_dict.pop(newname_scaled)

            # -------- SUBTRACT SOLVENT
            if self.ui.chkSubSolvent.isChecked():
                solventName = str(self.ui.solventEdit.text())
                self.subtractSolventRaw(merged_name, solventName)

        self.parent.redrawTheList()
        self.parent.Replot()
        # process last for plot refreshing

        self.ui.progressBar.setValue(0)

    def merging(self,q0, i0, e0, q1, i1, e1, cut1, cut2):
        '''
        merging two iq curve
        mean between cut1 & cut2
        '''
        # print("start of merge : from %6.4f"%(q0[0]))
        # cut1=dataArray[j+1][5]
        # print("cut1 %6.4f"%cut1)
        # cut2=dataArray[j][6]
        # print("cut2 %6.4f"%cut2)
        # first datas
        # print("first data")
        # print("end of merge : from %6.4f"%(dataArray[j][1][-1]))
        # 1 part from actual qmin to cut1
        q_final, i_final, e_final = self.clipQmax(q0, i0, e0, cut1)

        # 2 part from next qmin large to actual qmax merging
        # to be merge with next datas
        q2, i2, e2 = self.clipQmin(q0, i0, e0, cut1)
        q2, i2, e2 = self.clipQmax(q2, i2, e2, cut2)

        # 3 part from second qmin large to
        q3, i3, e3 = self.clipQmin(q1, i1, e1, cut1)
        q3, i3, e3 = self.clipQmax(q3, i3, e3, cut2)
        # MEAN
        newf = interpolate.interp1d(q2, i2, kind='linear', bounds_error=False,fill_value='extrapolate')
        newfe = interpolate.interp1d(q2, e2, kind='linear', bounds_error=False,fill_value='extrapolate')
        newi = newf(q3)
        newe = newfe(q3)

        q_final = numpy.concatenate((q_final, q3))
        i_final = numpy.concatenate((i_final, (newi + i3) / 2))
        e_final = numpy.concatenate((e_final, (newe + e3)))

        # 4 part
        q4, i4, e4 = self.clipQmin(q1, i1, e1, cut2)
        q_final = numpy.concatenate((q_final, q4))
        i_final = numpy.concatenate((i_final, i4))
        e_final = numpy.concatenate((e_final, e4))
        return q_final, i_final, e_final

    def clipQmin(self,q,i,error,qmin):
        # clip q min
        if error is not None:
            error = numpy.repeat(error, q >= qmin)
        i = numpy.repeat(i, q >= qmin)
        q = numpy.repeat(q, q >= qmin)
        return q,i,error

    def clipQmax(self, q, i, error, qmax):
        # clip q max
        if error is not None:
            error = numpy.repeat(error, q <= qmax)
        i = numpy.repeat(i, q <= qmax)
        q = numpy.repeat(q, q <= qmax)
        return q, i, error

    def subtractSolventRaw(self,dataName,solventName):

        '''
        '''
        if not(dataName in self.parent.data_dict):
            print('no data %s'%dataName)
            return
        qSample = self.parent.data_dict[dataName].q
        iSample=self.parent.data_dict[dataName].i
        sSample=self.parent.data_dict[dataName].i

        #verify the solvent
        solventExist=False
        if solventName in self.parent.data_dict:
            qSolvent = self.parent.data_dict[solventName].q
            iSolvent = self.parent.data_dict[solventName].i
            sSolvent = self.parent.data_dict[solventName].error
            solventExist = True
        else:
            print("no solvent in datas")
            return

        if solventName==dataName:
            print('solvent = data')
            return

        if len(iSample) != len(iSolvent):
            # trying interpolation
            print("subtraction with interpolation")
            newSolvent = interpolate.interp1d(qSolvent, iSolvent, kind='linear',
                                              bounds_error=0)  # interpolation for i
            iSolvent = newSolvent(qSample)

            if sSolvent is not None:
                newErr = interpolate.interp1d(qSolvent, sSolvent, kind='linear',
                                              bounds_error=0)  # interpolation for i
                sSolvent = newErr(qSample)
            qSolvent = qSample
        '''
        if  'Thickness' in self.DATAS[dataName]:
            thickness=float(self.DATAS[dataName]['Thickness'])
            if thickness==0.0:
                thickness=1.0
        else:
            thickness=1.0
        '''
        thickness=1.0
        iFinal = (iSample - iSolvent) / thickness
        #print("thickness= %6.2f"%thickness)
        #print("-------------------------------------            calculate uncertainties")
        sFinal = (sSample + sSolvent) / thickness
        '''
        self.DATAS[dataName].update({'q_work': qSample, 'i_work': iFinal, 's_work': sFinal})
        self.DATAS[dataName].update({'q_sub': qSample, 'i_sub': iFinal, 's_sub': sFinal})
        self.DATAS[dataName]['solvent_data']=solventName
        '''
        sub_name = dataName + "_subtracted"
        self.parent.data_dict[sub_name] = dataset.dataset(sub_name, qSolvent, iFinal, \
                                                             error=sFinal)
        #self.parent.data_dict.pop(myname)

        self.parent.redrawTheList()
        self.parent.Replot()

        return

    def subtractSolvent(self,dataName,solventName):
        print('solvent subtraction')
        qSample = self.DATAS[dataName]['q_work']
        iSample=self.DATAS[dataName]['i_work']
        sSample=self.DATAS[dataName]['s_work']
        #verify the solvent
        solventExist=False
        if solventName in self.parent.data_dict:
            qSolvent = self.parent.data_dict[solventName].q
            iSolvent = self.parent.data_dict[solventName].i
            sSolvent = self.parent.data_dict[solventName].error
            solventExist = True
        elif solventName in self.PROCESSED:
            solventName=self.PROCESSED[solventName]
            qSolvent=self.DATAS[solventName]['q_work']
            iSolvent = self.DATAS[solventName]['i_work']
            sSolvent = self.DATAS[solventName]['s_work']
            solventExist = True
        print('solvent exist ? :'+str(solventExist))
        if solventName==dataName:
            print('solvent = data')
            return

        if not solventExist:
            print('no solvent data exist')
            return

        if len(iSample) != len(iSolvent):
            # trying interpolation
            print("subtraction with interpolation")
            newSolvent = interpolate.interp1d(qSolvent, iSolvent, kind='linear',
                                              bounds_error=0)  # interpolation for i
            iSolvent = newSolvent(qSample)

            if sSolvent is not None:
                newErr = interpolate.interp1d(qSolvent, sSolvent, kind='linear',
                                              bounds_error=0)  # interpolation for i
                sSolvent = newErr(qSample)
            qSolvent = qSample
        if  'Thickness' in self.DATAS[dataName]:
            thickness=float(self.DATAS[dataName]['Thickness'])
            if thickness==0.0:
                thickness=1.0
        else:
            thickness=1.0

        iFinal = (iSample - iSolvent) / thickness

        #print("thickness= %6.2f"%thickness)
        #print("-------------------------------------            calculate uncertainties")
        sFinal = (sSample + sSolvent) / thickness


        self.DATAS[dataName].update({'q_work': qSample, 'i_work': iFinal, 's_work': sFinal})
        self.DATAS[dataName].update({'q_sub': qSample, 'i_sub': iFinal, 's_sub': sFinal})
        self.DATAS[dataName]['solvent_data']=solventName


        return

    def OnClickPlotCheckBox(self):
        pass
        '''if self.parent is None:
            if self.ui.plotChkBox.isChecked():
                self.plotapp=QtMatplotlib.QtMatplotlib()
                self.plotapp.show()
            else:
                self.plotapp.close()'''

    def OnClickDisplayBeam(self):
        '''
        user clicked on display beam
        '''
        #print "chk"
        #--simply redraw the image
        self.btnDisplayClicked()

    def OnClickparamViewButton(self):
        filename=str(self.ui.paramTxt.text())
        if filename is not None and filename !='':
            self.dlgFAI=dlgQtFAITest.FAIDialogTest(self.parent,filename,None,feedback=self.feedbackFromView)
            self.dlgFAI.show()

    def feedbackFromView(self,filename=None):
        if filename is not None:
            ret=QtWidgets.QMessageBox.question(self, "pySAXS", "Apply parameter file %s ?"%filename,
                                              buttons=QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No,
                                              defaultButton=QtWidgets.QMessageBox.Yes)
            if ret==QtWidgets.QMessageBox.Yes:
                self.ui.paramTxt.setText(filename)
                self.OnClickButtonTransferParams()

    def getInformationFromDat(self,filename):
        '''
        get the information from dat

        '''
        d_header = {'Comment': filename}
        d = self.ui.DirTxt.text()
        filename = self.workingdirectory + os.sep + filename

        try:
            f = open(filename)
            lines = f.readlines()

            for l in lines:
                if l[0] == '#':
                    pos = l[2:].find(" ")
                    if pos > 0:
                        #print(pos+2)
                        h = l[2:pos+2].strip()
                        v = l[pos+2:].strip()
                        if h[0] != '#':
                            d_header[h] = v
        except:
            print('error in reading dat '+filename+ ' header')
        return d_header

    def getInformationFromImage(self,filename):
        '''
        get the information from image
        (header if EDF, or rpt file if TIFF)
        '''
        d=self.ui.DirTxt.text()
        filename=self.workingdirectory+os.sep+filename

        try:
            im=fabio.open(filename)
        except:
            #file not exist
            return []
        l=[]
        #get extension
        EXTE=filetools.getExtension(filename).lower()
        if EXTE=='edf':
            #EDF type file
            for n in FROM_EDF:
                try:
                    l.append(str(im.header[n]))
                except:
                    l.append("?")
        else:
            l=[]
            #print('#no information in edf')
        #OTHER (datas in RPT)
        #try to read the rpt ?
        #l=[]
        #print('try to read rpt')

        rpt=configparser.ConfigParser()
        txt="?"
        filenameRPT=filetools.getFilenameOnly(filename)+'.rpt'
        if not(filetools.fileExist(filenameRPT)):
            #no rpt
            #print("no rpt")
            return l
        test=rpt.read(filenameRPT)
        if len(test)==0:
                print('error when reading file :', filenameRPT)
                return l

        lrpt=[]
        for n in FROM_RPT:
                try:
                    #print(n)
                    lrpt.append(str(rpt.get('acquisition',n)))
                    #print(str(rpt.get('acquisition',n)))
                except:
                    lrpt.append("?")
        if len(l)==0:
            return lrpt
        #try to merge l and lrpt
        for n in range(len(l)):
            if l[n]=='?':
                l[n]=lrpt[n]
        return l

    def OnClickCenterOfMassButton(self):
        '''
        calculate the center of mass
        '''
        #self.axes.set_xlim((self.xlim_min,self.xlim_max))
        #self.axes.set_ylim((self.ylim_min,self.ylim_max))
        plt=self.ui.matplotlibwidget
        xlim_min,xlim_max=plt.axes.get_xlim()
        ylim_max,ylim_min=plt.axes.get_ylim()
        im=self.img.data[int(ylim_min):int(ylim_max),int(xlim_min):int(xlim_max)]
        #print int(self.ylim_min),int(self.ylim_max),int(self.xlim_min),int(self.xlim_max)
        CenterOM=ndimage.measurements.center_of_mass(im)#, labels, index)
        #print CenterOM[0]+ylim_min,CenterOM[1]+xlim_min

        self.ui.chkDisplayBeam.setChecked(True)
        self.ui.edtBeamX.setText("%6.2f"%(CenterOM[1]+xlim_min))
        self.ui.edtBeamY.setText("%6.2f"%(CenterOM[0]+ylim_min))
        self.btnDisplayClicked()


    def OnClickExportList(self):
        '''
        export the list
        '''
        #print "toto"
        fd = QtWidgets.QFileDialog(self)
        filename,ext = fd.getSaveFileName(self,"export list",directory=self.workingdirectory,\
                                      filter="Excel files(*.xlsx);;All files (*.*)")
        #self.workingdirectory = filename
        #print(filename)
        if filename:
            #save
            '''f=open(filename,'w')
            for row in self.EXPORT_LIST:
                tt=""
                for n in row:
                    tt+=str(n)+'\t'
                #print(tt)
                f.write(tt+"\n")
            f.close()'''
            df_export=write_qtable_to_df(self.ui.tableWidget)
            df_export.to_excel(filename)
            #self.ui.tableWidget
            #print filename, " saved"

    def btnDisplayAutomaticFitClicked(self):
        self.automaticFitApp.tryFitThis(self.lastDatas)

    def btnCheckSolventClicked(self):
        if self.parent.referencedata is not None:
                self.ui.solventEdit.setText(str(self.parent.referencedata))
                
    def btnEnableAutomaticFit(self):
        if not self.AUTOMATIC_FIT:
            self.AUTOMATIC_FIT=True
            self.ui.btnAutomaticFit.setEnabled(True)
            self.automaticFitApp = dlgAutomaticFit.dlgAutomaticFit(self.parent)
            #self.automaticFitApp.show()
            self.ui.btnAutomaticFit.clicked.connect(self.btnDisplayAutomaticFitClicked)
            #self.ui.btnPAF.setEnabled(True)
            #self.ui.btnPAF.clicked.connect(self.btnProcessALLClicked)


        

    def closeEvent(self, event):
        '''
        when window is closed
        '''
        l=self._fileSysWatcher.directories()
        #print "previous watched directories :",list(l)
        self._fileSysWatcher.removePaths(l)

        #print "close"
        #save the preferences
        if self.parent is not None:
                #self.parent.pref.set("outputdir",section="pyFAI",value=str(self.ui.outputDirTxt.text()))
                #self.pref.set("parameterfile",section="pyFAI",value=str(self.ui.paramTxt.text()))
                self.pref.set('defaultdirectory',section="guisaxs qt",value=str(self.ui.DirTxt.text()))
                #self.pref.set('fileextension',section="pyFAI",value=str(self.ui.extensionTxt.text()))
                self.pref.save()
        try:
            self.t.stop()

        except:
            pass

def write_qtable_to_df(table):
    col_count = table.columnCount()
    row_count = table.rowCount()
    headers = [str(table.horizontalHeaderItem(i).text()) for i in range(col_count)]

    # df indexing is slow, so use lists
    df_list = []
    for row in range(row_count):
        df_list2 = []
        for col in range(col_count):
            table_item = table.item(row,col)
            df_list2.append('' if table_item is None else str(table_item.text()))
        df_list.append(df_list2)

    df = pd.DataFrame(df_list, columns=headers)

    return df

class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None


if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  myapp = XeussSurveyorDialog()
  myapp.show()
  sys.exit(app.exec_())

