from PyQt5 import QtWidgets

from .undo_redo import UndoRedo
from .scene import Scene
from .view import View
from .model import Model
from .canvas import Canvas


def main():
    app = QtWidgets.QApplication([])
    scene = Scene(0, 0, 512, 512)
    undo_redo = UndoRedo(scene)
    canvas = Canvas(scene, undo_redo)
    model = Model(canvas)
    view = View(model, canvas)
    view.show()
    app.exec_()
