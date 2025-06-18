import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QTimer, QRectF


radius = 20
x = 400
y = 300
vx = 0
vy = 0
gravity = 0.5
elasticity = 0.8

def update_position():
    global x, y, vx, vy

    vy += gravity

    x += vx
    y += vy

    if y + radius > window.height():
        y = window.height() - radius
        vy = -vy * elasticity

    if y - radius < 0:
        y = radius
        vy = -vy * elasticity

    if x - radius < 0:
        x = radius

    window.update()

def paint_event(event):
    painter = QPainter(window)
    painter.setBrush(QColor(255, 180, 100))
    painter.setPen(QColor(50, 50, 50))
    painter.drawEllipse(QRectF(x - radius, y - radius, radius * 2, radius * 2))

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Kick the Ball!")
window.setGeometry(100, 100, 800, 800)

window.paintEvent = paint_event

timer = QTimer()
timer.timeout.connect(update_position)
timer.start(16)

window.show()
sys.exit(app.exec_())
