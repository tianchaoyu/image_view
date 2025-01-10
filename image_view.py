# -*- coding: utf-8 -*-
# @File    : image_view.py
# 功能：
# @Time    : 2025/1/8 上午9:31
# @Author  : lhy

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog,QDialog,QColorDialog,QTextEdit,QApplication, QMainWindow
from PIL import Image, ImageOps,ImageDraw,ImageFont
from PyQt5.QtGui import QPixmap, QImage,QColor
import sys

class Ui_image_view(QMainWindow):

    def __init__(self):
        super().__init__()
        self.iamge_path = None
        self.gray_flag = False
        self.base_pil_image = None
        self.pil_image = None
        self.watermark_color = (255, 0, 0)
        self.watermark_location = None
        self.watermark =  None
        self.watermark_size = None

        self.setupUi()

    def setupUi(self):
        self.setObjectName("image_view")
        self.resize(1026, 563)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1001, 521))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_open = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_open.setObjectName("pushButton_open")
        self.verticalLayout.addWidget(self.pushButton_open)
        self.label_size = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_size.setObjectName("label_size")
        self.verticalLayout.addWidget(self.label_size)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_width = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_width.setObjectName("label_width")
        self.horizontalLayout_2.addWidget(self.label_width)
        self.lineEdit_width = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_width.setObjectName("lineEdit_width")
        self.lineEdit_width.setText('640')
        self.horizontalLayout_2.addWidget(self.lineEdit_width)

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label__height = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label__height.setObjectName("label__height")
        self.horizontalLayout_3.addWidget(self.label__height)
        self.lineEdit_height = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_height.setObjectName("lineEdit_height")
        self.lineEdit_height.setText('480')
        self.horizontalLayout_3.addWidget(self.lineEdit_height)

        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.pushButton_gray = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_gray.setObjectName("pushButton_gray")
        self.verticalLayout.addWidget(self.pushButton_gray)

        self.label_add = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_add.setObjectName("label_add")
        self.verticalLayout.addWidget(self.label_add)
        # self.horizontalLayout_4.addWidget(self.label_add)
        self.lineEdit_add = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_add.setObjectName("lineEdit_add")
        font = QtGui.QFont("Microsoft YaHei", 9)
        self.lineEdit_add.setFont(font)
        self.verticalLayout.addWidget(self.lineEdit_add)
        # 水印位置修改
        self.label_location = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_location.setObjectName("label_location")
        self.verticalLayout.addWidget(self.label_location)
        self.lineEdit_location = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_location.setObjectName("lineEdit_location")
        self.lineEdit_location.setText("10,10")
        self.verticalLayout.addWidget(self.lineEdit_location)
        self.pushButton_color = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_color.setObjectName("pushButton_color")
        self.verticalLayout.addWidget(self.pushButton_color)
        # 水印字体大小
        self.label_font = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_font.setObjectName("label_font")
        self.verticalLayout.addWidget(self.label_font)
        self.QSlider_font = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.QSlider_font.setOrientation(QtCore.Qt.Horizontal)
        self.QSlider_font.setMinimum(0)  # 设置最小值
        self.QSlider_font.setMaximum(100)  # 设置最大值
        self.QSlider_font.setValue(50)  # 设置默认值为50
        self.QSlider_font.setObjectName("mark_size")
        self.verticalLayout.addWidget(self.QSlider_font)


        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_save = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_save.setObjectName("pushButton_save")
        self.verticalLayout.addWidget(self.pushButton_save)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.label_image = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_image.setObjectName("label_image")
        self.label_image.setStyleSheet("border: 1px solid gray;")
        self.horizontalLayout.addWidget(self.label_image)
        self.horizontalLayout.setStretch(1, 2)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.signal_slots_connection()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("image_view", "图片定制"))
        self.pushButton_open.setText(_translate("image_view", "open image"))
        self.label_size.setText(_translate("image_view", "图像大小设置"))
        self.label_width.setText(_translate("image_view", "width"))
        self.label__height.setText(_translate("image_view", "height"))
        self.pushButton_gray.setText(_translate("image_view", "灰度处理"))
        self.label_add.setText(_translate("image_view", "添加水印"))
        self.pushButton_save.setText(_translate("image_view", "保存"))
        self.label_location.setText(_translate("image_view", "水印位置设置"))
        self.pushButton_color.setText(_translate("image_view", "水印颜色设置"))

    def signal_slots_connection(self):
        def get_image_file():
            fileName, _ = QFileDialog.getOpenFileName(None, "Open Image", "",  "image Files (*.jpg *.png *.JPEG *.gif)")

            if fileName:
                self.gray_flag = False
                self.base_pil_image = Image.open(fileName)
                self.display_image(self.base_pil_image)


        self.pushButton_open.clicked.connect(lambda: get_image_file())
        self.lineEdit_add.textChanged.connect(self.on_lineEdit_add_textChanged)
        self.lineEdit_location.textChanged.connect(self.on_lineEdit_add_textChanged)

        self.pushButton_gray.clicked.connect(self.gray_image)
        self.pushButton_save.clicked.connect(self.save_image_file)
        self.pushButton_color.clicked.connect(self.choose_color)
        self.QSlider_font.valueChanged.connect(self.on_lineEdit_add_textChanged)  # 反馈视频帧数


    def choose_color(self):
        "颜色选择"
        color = QColorDialog.getColor()
        self.watermark_color=(color.red(), color.green(), color.blue())
        self.on_lineEdit_add_textChanged()

    # def onSliderValueChanged(self,value):
    #     self.watermark_size = value

    def pil_to_qt(self, pil_image):
        if pil_image.mode == "RGB":
            format = QImage.Format_RGB888
        elif pil_image.mode == "RGBA":
            format = QImage.Format_RGBA8888
        elif pil_image.mode == "L":
            format = QImage.Format_Grayscale8
        else:
            raise ValueError(f"Unsupported image mode: {pil_image.mode}")

        qt_image = QImage(pil_image.tobytes("raw", pil_image.mode), pil_image.width, pil_image.height, format)
        return qt_image

    def display_image(self,pil_image):
        if hasattr(self, 'pil_image'):
            qt_image = self.pil_to_qt(pil_image)
            pixmap = QPixmap.fromImage(qt_image)
            self.label_image.setPixmap(pixmap)

    def gray_image(self):
        self.gray_flag = True
        self.pil_image = self.base_pil_image.convert('L')
        qt_image = self.pil_to_qt(self.pil_image)
        pixmap = QPixmap.fromImage(qt_image)
        self.label_image.setPixmap(pixmap)

    def on_lineEdit_add_textChanged(self):
        if self.pil_image or self.base_pil_image:
            text = self.lineEdit_add.text()
            location = self.lineEdit_location.text()
            font_size = self.QSlider_font.value()
            try:
                if text and location and font_size:
                    self.watermark = text
                    self.watermark_location = location
                    self.watermark_size = font_size

                    x, y = map(int, location.split(","))
                    color = self.watermark_color
                    if self.pil_image:
                        image = self.pil_image.copy()
                    else:
                        image = self.base_pil_image.copy()
                    draw = ImageDraw.Draw(image)
                    font = ImageFont.truetype("simhei.ttf",  self.watermark_size) #ImageFont.load_default()  # 你可以选择其他字体
                    draw.text((x,y), text, font=font, fill=color)  # 白色文字

                    qt_image = self.pil_to_qt(image)

                    pixmap = QPixmap.fromImage(qt_image)
                    scaled_pixmap = pixmap.scaled(self.label_image.size(), Qt.KeepAspectRatio,
                                                    Qt.SmoothTransformation)

                    self.label_image.setPixmap(scaled_pixmap)
                    self.label_image.update()
                    print(f"添加水印成功: {text}")
            except Exception as e:
                print(f"添加水印出错: {e}")

    def save_image_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "Images (*.png *.xpm *.jpg *.bmp);;All Files (*)")
        if file_path:
            try:
                width = self.lineEdit_width.text()
                height = self.lineEdit_height.text()
                if self.gray_flag:
                    self.pil_image = self.base_pil_image.convert('L')
                # 添加水印
                text = self.lineEdit_add.text()
                save_image = None
                if self.watermark and self.watermark_location and self.watermark_size:
                    x, y = map(int, self.watermark_location.split(","))
                    color = self.watermark_color
                    if self.pil_image:
                        image = self.pil_image.copy()
                    else:
                        image = self.base_pil_image.copy()
                    draw = ImageDraw.Draw(image)
                    font = ImageFont.truetype("msyh.ttc", self.watermark_size)  # ImageFont.load_default()  # 你可以选择其他字体
                    draw.text((x, y), text, font=font, fill=color)  # 白色文字

                    save_image = image
                if save_image is None:
                    if self.pil_image:
                        save_image = self.pil_image
                    else:
                        save_image = self.base_pil_image
                save_image = save_image.resize((int(width), int(height)))

                save_image.save(file_path)

                print(f"图片已保存到 {file_path}")
            except Exception as e:
                print(f"保存图片时出错: {e}")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = Ui_image_view()
    editor.show()
    sys.exit(app.exec_())




