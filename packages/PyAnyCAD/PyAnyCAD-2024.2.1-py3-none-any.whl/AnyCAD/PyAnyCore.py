
import os
import sys

import PyAnyCAD as AnyCAD

class GlobalInstance():
    '''
    应用入口实例，全局设置
    '''
    def Initialize():
        '''
        初始化。静态方法
        '''        
        print("Welcome to use AnyCAD Rapid Py!")
        
    def Destroy():
        '''
        释放资源。静态方法
        '''
        AnyCAD.Application.Instance().Destroy()
        
    def RegisterSDK(email, uuid, sn):
        AnyCAD.RenderingEngine.RegiserPythonSdk(email, uuid, sn)

    def SetDpiScaling(scaling:float):
        '''
        设置屏幕缩放系数。静态方法
        '''
        AnyCAD.RenderingEngine.SetDpiScaling(scaling)

def __AnyCAD_Main():
    _runtimePath = os.path.abspath(os.path.join(os.path.dirname(__file__), "."))
    if AnyCAD.Application.Instance().Initialize(AnyCAD.Path(_runtimePath), False) == False:
        print("Failied to initialize AnyCAD Rapid Py!")
        
__AnyCAD_Main()