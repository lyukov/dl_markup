from PyQt5.QtWidgets import QListView
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QMainWindow

from .model import Model


class View(QMainWindow):
    """
    Application view
    """
    def __init__(self, model):
        super().__init__()
        self.setWindowTitle("DL Markup")

        mainLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        centralWidget.setLayout(mainLayout)

        mainLayout.addWidget(model.inputDirectory)
        mainLayout.addWidget(model.outputDirectory)

        layout = QHBoxLayout()
        mainLayout.addLayout(layout)

        self.fileList = QListView()
        self.fileList.setModel(model.listModel)
        layout.addWidget(self.fileList)

        layout.addWidget(QGraphicsView(model.scene))

        self._createToolbar(model)

    def _createToolbar(self, model):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Select input directory', model.selectInputDirectory)
        tools.addAction('Select output directory', model.selectOutputDirectory)
        tools.addAction('Open', model.open)
        tools.addAction('Save', model.save)
