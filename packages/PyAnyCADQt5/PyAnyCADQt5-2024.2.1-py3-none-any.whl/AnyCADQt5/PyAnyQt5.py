from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QTimer, QAbstractEventDispatcher

from AnyCAD import PyAnyCAD as AnyCAD
from AnyCAD.PyAnyView import IRenderControl

class QtRenderControl(QWidget, IRenderControl):
    '''
    Qt三维控件
    '''
    def __init__(self, par):
        super().__init__(par)

        sz = self.size()
        self.viewer = AnyCAD.RenderingEngine.CreateView(int(self.winId()), sz.width(), sz.height())
        self.viewer.InstallEventHandlers()
        QAbstractEventDispatcher.instance().awake.connect(self.Redraw)
        self.timer = QTimer(self)
        self.timer.setInterval(33)
        self.timer.timeout.connect(self._RenderOneFrame)     
    
    def Redraw(self):
        '''
        绘制
        '''
        self.timer.stop()
        hit = self._RenderOneFrame()
        if hit == AnyCAD.EnumRedrawResult_Idle:
            return
        elif hit == AnyCAD.EnumRedrawResult_Animation or hit == AnyCAD.EnumRedrawResult_Partial:
            self.timer.start()
        else:
            return

    def _RenderOneFrame(self):
        '''
        内部方法
        '''
        tick = self.viewer.GetTimeTicks()
        self.viewer.OnTime(tick)
        return self.viewer.Redraw(tick)

    def resizeEvent(self, evt):
        sz = self.size()
        self.viewer.OnResized(int(sz.width()), int(sz.height()))        
    def paintEngine(self):
        return None
    def paintEvent(self, event):
        self.viewer.RequestUpdate(AnyCAD.EnumUpdateFlags_Dynamic)