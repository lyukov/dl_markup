from PyQt5 import QtGui, QtWidgets


class Scene(QtWidgets.QGraphicsScene):
    """Class that stores drawn primitives."""

    def __init__(self, *argc, **kwargs):
        """Initialize scene."""
        super().__init__(*argc, **kwargs)
        self.__img_item = None
        self.setBackgroundBrush(QtGui.QBrush(
            QtGui.QColor(0, 0, 0)
        ))

    def __set_alpha(self, img: QtGui.QPixmap, alpha: float) -> QtGui.QPixmap:
        """Create new image with another opacity.

        :param img: original image
        :param alpha: opacity value from interval [0, 1]
        """
        output = QtGui.QPixmap(img.size())
        output.fill(QtGui.QColor.fromRgb(0, 0, 0, 0))
        painter = QtGui.QPainter(output)
        painter.setOpacity(alpha)
        painter.drawPixmap(0, 0, img)
        painter.end()
        return output

    def clear(self):
        """Remove all primitives from scene, leaving background image."""
        if self.__img_item is not None:
            self.removeItem(self.__img_item)
        super().clear()
        if self.__img_item is not None:
            self.addItem(self.__img_item)

    @property
    def img(self) -> QtGui.QPixmap:
        """Background image."""
        return self.__img_item.pixmap()

    @img.setter
    def img(self, val: QtGui.QPixmap):
        if self.__img_item is not None:
            self.removeItem(self.__img_item)
        img = self.__set_alpha(val, 0.8)
        self.__img_item = QtWidgets.QGraphicsPixmapItem(img)
        self.__img_item.setZValue(1.0)
        self.addItem(self.__img_item)

    @property
    def segm(self) -> QtGui.QPixmap:
        """Return current segmentation mask."""
        self.removeItem(self.__img_item)

        segm = QtGui.QPixmap(self.width(), self.height())
        segm.fill(QtGui.QColor.fromRgb(0, 0, 0, 0))
        painter = QtGui.QPainter(segm)
        self.render(painter)
        painter.end()

        self.addItem(self.__img_item)
        return segm