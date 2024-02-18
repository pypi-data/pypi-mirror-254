from PyQt6 import QtCore, QtGui, QtWidgets
import os
from enum import Enum, auto

from frameless_dialog import frmls_resources

PIXELS_TO_ACT = 7


class TitleMode(Enum):

    CLEAN_TITLE = 0
    ONLY_CLOSE_BTN = auto()
    MENU_OFF = auto()
    MAX_MIN_OFF = auto()
    FULL_SCREEN_MODE = auto()
    MAX_MODE_OFF = auto()
    MIN_MODE_OFF = auto()
    FULL_TITLE = auto()
    NO_TITLE = auto()


class FramelessDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.setup_cust_win_ui()
        self.setWindowIcon(QtGui.QIcon(':ConMedSwoosh.png'))

        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.Window)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_DeleteOnClose, False)
        super().setMouseTracking(True)
        self.setMouseTracking(True)

        self.flag_move_widget: bool = False
        self.flag_allow_resize: bool = False
        self.flag_resize_vert_top: bool = False
        self.flag_resize_horz_left: bool = False
        self.flag_resize_diag_top_left: bool = False
        self.flag_resize_diag_top_right: bool = False
        self.flag_in_resize_zone: bool = False

        self.pbMin.clicked.connect(self.minimizeBtnClicked)
        self.pbMax.clicked.connect(self.maximize_restore_BtnClicked)
        self.pbRestore.clicked.connect(self.maximize_restore_BtnClicked)
        self.pbClose.clicked.connect(self.close)

        self.title_mode: TitleMode = TitleMode.FULL_TITLE
        self.pbRestore.setVisible(False)
        self.old_geometry = self.geometry()

    def setMouseTracking(self, flag: bool):
        def recursive_set(parent):
            for child in parent.findChildren(QtCore.QObject):
                if hasattr(child, 'setMouseTracking'):
                    child.setMouseTracking(flag)
                recursive_set(child)

        QtWidgets.QWidget.setMouseTracking(self, flag)
        recursive_set(self)

    def setWindowTitle(self, a0: str) -> None:
        super().setWindowTitle(a0)
        self.lbl_title.setText(a0)

    def set_central_widget(self, widget: QtWidgets.QWidget, widgetName=None):

        self.cent_widget = widget
        self.cent_widget.destroyed.connect(self.close)

        self.layout_central_widget.addWidget(self.cent_widget)

    def set_titlebar_mode(self, flag: TitleMode):
        self.title_mode = flag
        mode_actions = {
            TitleMode.CLEAN_TITLE: lambda: self.set_titlebar_clean(),
            TitleMode.NO_TITLE: lambda: self.set_titlebar_no_title(),
            TitleMode.ONLY_CLOSE_BTN: lambda: self.set_titlebar_only_close_btn(),
            TitleMode.MENU_OFF: lambda: self.set_titlebar_menu_off(),
            TitleMode.MAX_MIN_OFF: lambda: self.set_titlebar_max_min_off(),
            TitleMode.MAX_MODE_OFF: lambda: self.set_titlebar_max_mode_off(),
            TitleMode.MIN_MODE_OFF: lambda: self.set_titlebar_min_mode_off(),
            TitleMode.FULL_TITLE: lambda: self.set_titlebar_full_title()
        }
        mode_actions.get(flag, lambda: None)()
        self.lbl_title.setVisible(True)

    def set_titlebar_clean(self):
        self.tb_menu.setHidden(True)
        self.pbMin.setHidden(True)
        self.pbMax.setHidden(True)
        self.pbClose.setHidden(True)

    def set_titlebar_no_title(self):
        self.tb_menu.setHidden(True)
        self.pbMin.setHidden(True)
        self.pbMax.setHidden(True)
        self.pbClose.setHidden(True)
        self.title_bar.setHidden(True)

    def set_titlebar_only_close_btn(self):
        self.tb_menu.setHidden(True)
        self.pbMin.setHidden(True)
        self.pbMax.setHidden(True)
        self.pbClose.setHidden(False)

    def set_titlebar_menu_off(self):
        self.tb_menu.setHidden(True)
        self.pbMin.setHidden(False)
        self.pbMax.setHidden(False)
        self.pbClose.setHidden(False)

    def set_titlebar_max_min_off(self):
        self.tb_menu.setHidden(False)
        self.pbMin.setHidden(True)
        self.pbMax.setHidden(True)
        self.pbClose.setHidden(False)

    def set_titlebar_max_mode_off(self):
        self.tb_menu.setHidden(False)
        self.pbMin.setHidden(False)
        self.pbMax.setHidden(True)
        self.pbClose.setHidden(False)

    def set_titlebar_min_mode_off(self):
        self.tb_menu.setHidden(False)
        self.pbMin.setHidden(True)
        self.pbMax.setHidden(False)
        self.pbClose.setHidden(False)

    def set_titlebar_full_title(self):
        self.tb_menu.setHidden(False)
        self.pbMin.setHidden(False)
        self.pbMax.setHidden(False)
        self.pbClose.setHidden(False)

    def set_titlebar_menu(self, menu, icon_path = None):

        self.tb_menu.setMenu(menu)
        if icon_path is not None:
            self.tb_menu.setIcon(QtGui.QIcon(icon_path))


    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        super().closeEvent(a0)

    def setup_cust_win_ui(self):
        self.setObjectName("CustomWindow")

        self.custom_win_layout = QtWidgets.QVBoxLayout(self)
        self.custom_win_layout.setContentsMargins(0, 1, 0, 0)
        self.custom_win_layout.setSpacing(0)
        self.custom_win_layout.setObjectName("custom_win_layout")

        self.frm_win_frame = QtWidgets.QFrame(self)
        self.frm_win_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frm_win_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)

        self.layout_frm_win_frame = QtWidgets.QVBoxLayout(self.frm_win_frame)
        self.layout_frm_win_frame.setContentsMargins(0, 0, 0, 0)
        self.layout_frm_win_frame.setSpacing(0)
        self.layout_frm_win_frame.setObjectName("layout_frm_win_frame")

        self.title_bar = QtWidgets.QWidget(self.frm_win_frame)
        self.title_bar.setMinimumSize(QtCore.QSize(0, 24))
        self.title_bar.setMaximumSize(QtCore.QSize(16777215, 24))
        self.title_bar.setObjectName("titleBar")

        self.layout_titlebar = QtWidgets.QHBoxLayout(self.title_bar)
        self.layout_titlebar.setContentsMargins(5, 0, 1, 0)
        self.layout_titlebar.setSpacing(4)
        self.layout_titlebar.setObjectName("layout_titlebar")
        self.tb_menu = QtWidgets.QToolButton(self.title_bar)
        # self.tbMenu.setIcon(QtGui.QIcon(':ConMedSwoosh.png'))
        self.tb_menu.setIconSize(QtCore.QSize(16, 16))
        self.tb_menu.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup)
        self.tb_menu.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.tb_menu.setObjectName("tbMenu")

        self.layout_titlebar.addWidget(self.tb_menu)
        self.menu_bar = QtWidgets.QMenuBar(self.title_bar)
        self.menu_bar.setMinimumWidth(0)
        sp = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.menu_bar.setSizePolicy(sp)
        self.layout_titlebar.addWidget(self.menu_bar)

        self.lbl_title = QtWidgets.QLabel(self.title_bar)
        self.lbl_title.setMinimumSize(QtCore.QSize(100, 22))
        self.lbl_title.setMaximumSize(QtCore.QSize(16777215, 22))
        self.lbl_title.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_title.setFont(font)

        self.lbl_title.setObjectName("LTitle")

        self.layout_titlebar.addWidget(self.lbl_title)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.layout_titlebar.addItem(spacerItem1)
        self.pbMin = QtWidgets.QPushButton(self.title_bar)
        self.pbMin.setMinimumSize(QtCore.QSize(22, 22))
        self.pbMin.setMaximumSize(QtCore.QSize(22, 22))
        self.pbMin.setIconSize(QtCore.QSize(22, 22))
        self.pbMin.setFlat(True)
        self.pbMin.setObjectName("pbMin")
        self.layout_titlebar.addWidget(self.pbMin)
        self.pbMax = QtWidgets.QPushButton(self.title_bar)
        self.pbMax.setMinimumSize(QtCore.QSize(22, 22))
        self.pbMax.setMaximumSize(QtCore.QSize(22, 22))
        self.pbMax.setIconSize(QtCore.QSize(22, 22))
        self.pbMax.setFlat(True)
        self.pbMax.setObjectName("pbMax")
        self.layout_titlebar.addWidget(self.pbMax)
        self.pbRestore = QtWidgets.QPushButton(self.title_bar)
        self.pbRestore.setMinimumSize(QtCore.QSize(22, 22))
        self.pbRestore.setMaximumSize(QtCore.QSize(22, 22))
        self.pbRestore.setIconSize(QtCore.QSize(22, 22))
        self.pbRestore.setFlat(True)
        self.pbRestore.setObjectName("pbRestore")
        self.layout_titlebar.addWidget(self.pbRestore)
        self.pbClose = QtWidgets.QPushButton(self.title_bar)
        self.pbClose.setMinimumSize(QtCore.QSize(22, 22))
        self.pbClose.setMaximumSize(QtCore.QSize(22, 22))
        self.pbClose.setIconSize(QtCore.QSize(22, 22))
        self.pbClose.setFlat(True)
        self.pbClose.setObjectName("pbClose")
        self.layout_titlebar.addWidget(self.pbClose)
        self.layout_frm_win_frame.addWidget(self.title_bar)

        self.central_widget = QtWidgets.QWidget(self.frm_win_frame)
        self.central_widget.setObjectName("centralWidget")
        self.layout_central_widget = QtWidgets.QVBoxLayout(self.central_widget)
        self.layout_central_widget.setContentsMargins(11, 11, 11, 11)
        self.layout_central_widget.setSpacing(6)
        self.layout_central_widget.setObjectName("centralLayout")
        self.layout_frm_win_frame.addWidget(self.central_widget)

        self.status_bar = QtWidgets.QStatusBar(self.frm_win_frame)
        self.status_bar.setObjectName("statusbar")
        self.layout_frm_win_frame.addWidget(self.status_bar)

        self.custom_win_layout.addWidget(self.frm_win_frame)
        QtCore.QMetaObject.connectSlotsByName(self)

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:

        xMouse = a0.pos().x()
        yMouse = a0.pos().y()
        wWidth = self.geometry().width()
        wHeight = self.geometry().height()
        # print(f'{self.objectName()}: Mouse move event {xMouse},{yMouse}')

        if self.flag_move_widget:
            self.flag_in_resize_zone = False
            self.moveWindow(a0)
        elif self.flag_allow_resize:
            self.resizeWindow(a0)
        elif xMouse >= wWidth - PIXELS_TO_ACT:
            self.flag_in_resize_zone = True


            if yMouse >= wHeight - PIXELS_TO_ACT:
                self.setCursor(QtCore.Qt.CursorShape.SizeFDiagCursor)
                # print(f'{self.objectName()}: In right-bottom')
            elif yMouse <= PIXELS_TO_ACT:
                self.setCursor(QtCore.Qt.CursorShape.SizeBDiagCursor)
                # print(f'{self.objectName()}: In right-top')
            else:
                self.setCursor(QtCore.Qt.CursorShape.SizeHorCursor)
                # print(f'{self.objectName()}: In right')

            self.resizeWindow(a0)
        elif xMouse <= PIXELS_TO_ACT:
            self.flag_in_resize_zone = True

            if yMouse >= wHeight - PIXELS_TO_ACT:
                self.setCursor(QtCore.Qt.CursorShape.SizeBDiagCursor)
            elif yMouse <= PIXELS_TO_ACT:
                self.setCursor(QtCore.Qt.CursorShape.SizeFDiagCursor)
            else:
                self.setCursor(QtCore.Qt.CursorShape.SizeHorCursor)
            self.resizeWindow(a0)

        elif yMouse >= wHeight - PIXELS_TO_ACT:
            self.flag_in_resize_zone = True
            self.setCursor(QtCore.Qt.CursorShape.SizeVerCursor)
            self.resizeWindow(a0)

        elif yMouse <= PIXELS_TO_ACT:
            self.flag_in_resize_zone = True
            self.setCursor(QtCore.Qt.CursorShape.SizeVerCursor)
            self.resizeWindow(a0)

        else:
            self.flag_in_resize_zone = False
            self.setCursor(QtCore.Qt.CursorShape.ArrowCursor)

        a0.accept()

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:

        if a0.button() == QtCore.Qt.MouseButton.LeftButton:
            xPos = a0.pos().x()
            yPos = a0.pos().y()

            if self.flag_in_resize_zone:
                self.flag_allow_resize = True

                if yPos <= PIXELS_TO_ACT:
                    if xPos <= PIXELS_TO_ACT:
                        self.flag_resize_diag_top_left = True
                    elif xPos >= self.geometry().width() - PIXELS_TO_ACT:
                        self.flag_resize_diag_top_right = True
                    else:
                        self.flag_resize_vert_top = True
                elif xPos <= PIXELS_TO_ACT:
                    self.flag_resize_horz_left = True
            elif xPos >= PIXELS_TO_ACT and xPos < self.title_bar.geometry().width() and yPos >= PIXELS_TO_ACT and \
                    yPos < self.title_bar.geometry().height():
                self.flag_move_widget = True
                self.mDragPosition = (a0.globalPosition() - QtCore.QPointF(self.frameGeometry().topLeft())).toPoint()

        a0.accept()

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:

        self.flag_move_widget = False
        self.flag_allow_resize = False
        self.flag_resize_vert_top = False
        self.flag_resize_horz_left = False
        self.flag_resize_diag_top_left = False
        self.flag_resize_diag_top_right = False

        a0.accept()

    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:

        tbMenuGeo = self.tb_menu.geometry()
        titleBarGeo = self.title_bar.geometry()
        xPos = a0.pos().x()
        yPos = a0.pos().y()

        if xPos < tbMenuGeo.right() and yPos < tbMenuGeo.bottom() and xPos >= tbMenuGeo.x() and yPos >= tbMenuGeo.y() and self.tb_menu.isVisible():
            self.close()
        elif self.title_mode != TitleMode.FullScreenMode and xPos < titleBarGeo.width() and yPos < titleBarGeo.height():
            self.maximize_restore_BtnClicked()

        a0.accept()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:

        opt = QtWidgets.QStyleOption()
        opt.initFrom(self)
        p = QtGui.QPainter(self)
        self.style().drawPrimitive(QtWidgets.QStyle.PrimitiveElement.PE_Widget, opt, p, self)

    def moveWindow(self, e: QtGui.QMouseEvent):

        if e.buttons() & QtCore.Qt.MouseButton.LeftButton:
            self.move((e.globalPosition() - QtCore.QPointF(self.mDragPosition)).toPoint())
            e.accept()

    def resizeWindow(self, e: QtGui.QMouseEvent):

        if self.flag_allow_resize:
            cursorShape = self.cursor().shape()

            if cursorShape == QtCore.Qt.CursorShape.SizeVerCursor:
                self.resizeWhenVerCursor(e.pos())
            elif cursorShape == QtCore.Qt.CursorShape.SizeHorCursor:
                self.resizeWhenHorCursor(e.pos())
            elif cursorShape == QtCore.Qt.CursorShape.SizeBDiagCursor:
                self.resizeWhenBDiagCursor(e.pos())
            elif cursorShape == QtCore.Qt.CursorShape.SizeFDiagCursor:
                self.resizeWhenFDiagCursor(e.pos())
            else:
                pass
            e.accept()

    def resizeWhenVerCursor(self, p: QtCore.QPoint):

        yMouse = p.y()
        wWidth = self.geometry().width()
        wHeight = self.geometry().height()

        if self.flag_resize_vert_top:
            newY = self.geometry().y() + yMouse
            newHeight = wHeight - yMouse

            if newHeight > self.minimumSizeHint().height():
                self.resize(wWidth, newHeight)
                self.move(self.geometry().x(), newY)

        else:
            self.resize(wWidth, yMouse + 1)

    def resizeWhenHorCursor(self, p: QtCore.QPoint):

        xMouse = p.x()
        wWidth = self.geometry().width()
        wHeight = self.geometry().height()

        if self.flag_resize_horz_left:
            newX = self.geometry().x() + xMouse
            newWidth = wWidth - xMouse

            if newWidth > self.minimumSizeHint().width():
                self.resize(newWidth, wHeight)
                self.move(newX, self.geometry().y())

        else:
            self.resize(xMouse, wHeight)

    def resizeWhenBDiagCursor(self, p: QtCore.QPoint):

        xMouse = p.x()
        yMouse = p.y()
        wWidth = self.geometry().width()
        wHeight = self.geometry().height()

        if self.flag_resize_diag_top_right:
            newX = self.geometry().x()
            newWidth = xMouse
            newY = self.geometry().y() + yMouse
            newHeight = wHeight - yMouse

        else:
            newX = self.geometry().x() + xMouse
            newWidth = wWidth -  xMouse
            newY = self.geometry().y()
            newHeight = yMouse

        if newWidth >= self.minimumSizeHint().width() and newHeight >= self.minimumSizeHint().height():
            self.resize(newWidth, newHeight)
            self.move(newX, newY)
        elif newWidth >= self.minimumSizeHint().width():
            self.resize(newWidth, wHeight)
            self.move(newX, self.geometry().y())
        elif newHeight >= self.minimumSizeHint().height():
            self.resize(wWidth, newHeight)
            self.move(self.geometry().x(), newY)

    def resizeWhenFDiagCursor(self, p: QtCore.QPoint):

        xMouse = p.x()
        yMouse = p.y()
        wWidth = self.geometry().width()
        wHeight = self.geometry().height()
        geoX = self.geometry().x()
        geoY = self.geometry().y()

        if self.flag_resize_diag_top_left:
            newX = geoX + xMouse
            newWidth = wWidth - xMouse
            newY = geoY + yMouse
            newHeight = wHeight - yMouse

            if newWidth >= self.minimumSizeHint().width() and newHeight >= self.minimumSizeHint().height():
                self.resize(newWidth, newHeight)
                self.move(newX, newY)
            elif newWidth >= self.minimumSizeHint().width():
                self.resize(newWidth, wHeight)
                self.move(newX, geoY)
            elif newHeight >= self.minimumSizeHint().height():
                self.resize(wWidth, newHeight)
                self.move(geoX, newY)
        else:
            self.resize(xMouse + 1, yMouse + 1)


    def maximize_restore_BtnClicked(self):

        if self.isFullScreen() or self.isMaximized():

            self.setWindowState(self.windowState() & ~QtCore.Qt.WindowState.WindowMaximized)
            self.setGeometry(self.old_geometry)
            self.pbRestore.setVisible(False)
            self.pbMax.setVisible(True)
        else:
            self.old_geometry = self.geometry()
            self.setWindowState(self.windowState() | QtCore.Qt.WindowState.WindowMaximized)
            self.pbRestore.setVisible(True)
            self.pbMax.setVisible(False)

    def minimizeBtnClicked(self):

        if self.isMinimized():
            self.setWindowState(self.windowState() & ~QtCore.Qt.WindowState.WindowMinimized)
        else:
            self.setWindowState(self.windowState() | QtCore.Qt.WindowState.WindowMinimized)

    def set_tbMenu_icon(self, file_path: str):

        try:
            self.tb_menu.setIcon(QtGui.QIcon(file_path))
        except FileNotFoundError:
            # Handle the exception if the file does not exist
            pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    file = QtCore.QFile(":/dark/stylesheet.qss")
    file.open(QtCore.QFile.OpenModeFlag.ReadOnly | QtCore.QFile.OpenModeFlag.Text)
    stream = QtCore.QTextStream(file)
    app.setStyleSheet(stream.readAll())

    # print(qt_material.list_themes())
    win = FramelessDialog()
    win.setWindowTitle('Test')
    win.show()
    sys.exit(app.exec())