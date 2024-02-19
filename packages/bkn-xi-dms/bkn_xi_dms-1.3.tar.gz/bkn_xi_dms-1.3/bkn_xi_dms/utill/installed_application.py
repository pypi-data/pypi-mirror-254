import winreg


def is_excel_installed():
    reg_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\excel.exe"
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path) as key:
            value, _ = winreg.QueryValueEx(key, None)
            return True
    except:
        return False
