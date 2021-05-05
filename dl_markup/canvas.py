from PyQt5 import QtGui, QtCore, QtWidgets
from .cylinder_item import CylinderItem


class Canvas(QtWidgets.QGraphicsView):
    def __init__(self, scene, undo_redo):
        super().__init__(scene)
        self.undo_redo = undo_redo
        self.color = QtGui.QColor(0, 255, 0)
        self.brush_size = 20
        self.last_x, self.last_y = None, None

    def mouseMoveEvent(self, e):
        if self.last_x is None: # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            return # Ignore the first time.

        cylinder = CylinderItem(
            QtCore.QPointF(self.last_x, self.last_y),
            QtCore.QPointF(e.x(), e.y()),
            self.brush_size,
            pen=QtGui.QPen(self.color),
            brush=QtGui.QBrush(self.color)
        )
        self.undo_redo.insert_in_undo_redo_add(cylinder)
        
        # Update the origin for next time.
        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None