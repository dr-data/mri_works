##########################################################################
# mriWorks - Copyright (C) IRMAGE/INSERM, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# https://cecill.info/licences/Licence_CeCILL_V2-en.html
# for details.
##########################################################################

'''
Created on 11 jan. 2018
@author: omonti

'''

import subprocess
import sys

from PyQt5.QtWidgets import QWidget, QTabWidget, QApplication, QVBoxLayout, \
    QMenuBar, QAction, qApp, QLineEdit, QMainWindow

from Config import Config
from About import AboutSoft
from NodeEditor.python.PipeLine_Irmage import NodeEdit
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon


class Project_Irmage(QMainWindow):
    def __init__(self):

        # Main Window ###########################################
        super(Project_Irmage, self).__init__()

        # initial setting #######################################
        config = Config()
        self.currentRep = config.getPathData()

        # Create Menus #########################################
        mfile = self.menuBar().addMenu('File')
        mhelp = self.menuBar().addMenu('Help')

        exitAct = QAction(QIcon('sources_images/exit.png'), 'Exit', self)
        exitAct.triggered.connect(qApp.quit)
        mfile.addAction(exitAct)

        about = QAction(QIcon(), 'About mriWorks', self)
        about.triggered.connect(self.showAbout)
        mhelp.addAction(about)

        # Create Tabs ##########################################
        t = createTabs()
        self.setCentralWidget(t)

        # Window Main ##########################################
        self.setWindowTitle("mriWorks "+config.getVersion())
        self.showMaximized()
        self.statusBar().showMessage('Ready')

    def showAbout(self):
        AboutSoft()


class createTabs(QWidget):
    def __init__(self):
        super(createTabs, self).__init__()

        self.config = Config()
        self.currentRep = self.config.getPathData()

        self.tabs = QTabWidget()
        self.tabs.setAutoFillBackground(False)
        self.tabs.setStyleSheet('QTabBar{font-size:14pt;font-family:Times;text-align: center;color:blue;}')
        self.tabs.setMovable(True)

        self.textInfo = QLineEdit(self)
        self.textInfo.resize(500, 40)
        # self.textInfo.setEnabled(False)
        self.textInfo.setText('Welcome to Irmage')

        self.tabs.addTab(NodeEdit(self.textInfo), "PipeLine Manager")
        self.tabs.setCurrentIndex(1)

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.addWidget(self.tabs)
        self.verticalLayout.addWidget(self.textInfo)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    imageViewer = Project_Irmage()
    imageViewer.show()
    app.setWindowIcon(QIcon('mri_works.png'))
    sys.exit(app.exec_())
