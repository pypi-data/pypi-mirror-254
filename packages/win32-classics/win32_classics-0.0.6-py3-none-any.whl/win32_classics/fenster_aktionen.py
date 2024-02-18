import ctypes
import ctypes.wintypes
import os

from screeninfo import get_monitors
import win32api
import win32com.client
import win32con
import win32process
from win32con import (
    HWND_BOTTOM,
    HWND_NOTOPMOST,
    HWND_TOP,
    HWND_TOPMOST,
    SW_MAXIMIZE,
    SW_MINIMIZE,
    SW_SHOWNORMAL,
    SWP_ASYNCWINDOWPOS,
)
from win32gui import (
    EnumWindows,
    GetForegroundWindow,
    GetWindowRect,
    GetWindowText,
    SetForegroundWindow,
    SetWindowPos,
    ShowWindow,
    FindWindow,
)
from colorful_terminal import *
from exception_details import *


def get_monitor_infos():
    mons = get_monitors()
    mons = sorted(mons, key=lambda item: item.x)
    return mons


def set_window_position(
    WindowHandle, x: int = None, y: int = None, w: int = None, h: int = None
):
    flag = SWP_ASYNCWINDOWPOS
    flag_dexciption = "If the calling thread and the thread that owns the window are attached to different input queues, the system posts the request to the thread that owns the window. This prevents the calling thread from blocking its execution while other threads process the request. "
    # insert_after = HWND_TOPMOST
    # insert_after = HWND_TOP
    # insert_after = HWND_BOTTOM
    insert_after = HWND_NOTOPMOST
    hWnd = WindowHandle

    if any([n == None for n in [x, y, w, h]]):
        x_, y_, w_, h_ = GetWindowRect(hWnd)
        if x == None:
            x = x_
        if y == None:
            y = y_
        if w == None:
            w = w_
        if h == None:
            h = h_

    try:
        SetWindowPos(hWnd, insert_after, x, y, w, h, flag)
        return 0
    except Exception as exc:
        title = GetWindowText(hWnd)
        return get_exception_details_str(exc)
        # colored_print(Fore.RED + f"Fehler für '{title}':")
        # print_exception_details(exc)


def maximize_current_window():
    hwnd = GetForegroundWindow()
    ShowWindow(hwnd, SW_MAXIMIZE)


def minimize_current_window():
    hwnd = GetForegroundWindow()
    ShowWindow(hwnd, SW_MINIMIZE)


def get_window_rect(hwnd):
    try:
        f = ctypes.windll.dwmapi.DwmGetWindowAttribute
    except WindowsError:
        f = None
    if f:
        rect = ctypes.wintypes.RECT()
        DWMWA_EXTENDED_FRAME_BOUNDS = 9
        f(
            ctypes.wintypes.HWND(hwnd),
            ctypes.wintypes.DWORD(DWMWA_EXTENDED_FRAME_BOUNDS),
            ctypes.byref(rect),
            ctypes.sizeof(rect),
        )
        return rect.left, rect.top, rect.right, rect.bottom


def get_all_WindowHandles(no_nonames: bool = True) -> list:
    windowhandles = []

    def callback(hwnd, extra):
        if no_nonames:
            if GetWindowText(hwnd).strip() != "":
                windowhandles.append(hwnd)
        else:
            windowhandles.append(hwnd)

    EnumWindows(callback, None)
    return windowhandles


def get_all_WindowHandles_plus(
    no_nonames: bool = True, no_invisible_windows: bool = True
) -> list[dict]:
    """Every dictionary contains hwnd, name, rect and path"""
    windowhandles = []

    def myfilter(hwnd):
        if no_nonames:
            if GetWindowText(hwnd).strip() == "":
                return False
        if no_invisible_windows:
            if GetWindowRect(hwnd) == (0, 0, 0, 0):
                return False
            elif GetWindowText(hwnd) == "NVOGLDC invisible":
                return False
        return True

    def callback(hwnd, extra):
        if myfilter(hwnd):
            windowhandles.append(hwnd)

    EnumWindows(callback, None)

    windows = []
    for h in windowhandles:
        try:
            n, r = GetWindowText(h), get_window_rect(h)
            try:
                p = get_exe_path_from_window_handle(h)
            except:
                p = "<UNKNOWN>"
            windows.append({"hwnd": h, "name": n, "rect": r, "path": p})
        except:
            pass

    return windows


def get_all_WindowHandles_Names_Rects(
    no_nonames: bool = True, no_invisible_windows: bool = True
):
    windows = []

    def myfilter(hwnd):
        if no_nonames:
            if GetWindowText(hwnd).strip() == "":
                return False
        if no_invisible_windows:
            if GetWindowRect(hwnd) == (0, 0, 0, 0):
                return False
            elif GetWindowText(hwnd) == "NVOGLDC invisible":
                return False
        return True

    def callback(hwnd, extra):
        if myfilter(hwnd):
            windows.append((hwnd, GetWindowText(hwnd), GetWindowRect(hwnd)))

    EnumWindows(callback, None)
    return windows


def get_WindowHandle_plus_from_ExePath(
    path: str,
    contains: bool = False,
    pre_filter_invisible_windows: bool = True,
    acknowledge_case: bool = True,
) -> list[dict]:
    """Every dictionary contains hwnd, name, rect and path"""
    windows = get_all_WindowHandles_plus(True, pre_filter_invisible_windows)
    result = []
    for dic in windows:
        if contains:
            if acknowledge_case:
                if path in dic["path"]:
                    result.append(dic)
            else:
                if path.lower() in dic["path"].lower():
                    result.append(dic)
        else:
            if acknowledge_case:
                if path == dic["path"]:
                    result.append(dic)
            else:
                if path.lower() == dic["path"].lower():
                    result.append(dic)
    return result


def get_WindowHandle_plus_from_ExeName(
    name: str,
    contains: bool = False,
    pre_filter_invisible_windows: bool = True,
    acknowledge_case: bool = True,
) -> list[dict]:
    """Every dictionary contains hwnd, name, rect and path"""
    windows = get_all_WindowHandles_plus(True, pre_filter_invisible_windows)
    result = []
    for dic in windows:
        try:
            file = os.path.basename(dic["path"])
            if contains:
                if acknowledge_case:
                    if name in file:
                        result.append(dic)
                else:
                    if name.lower() in file.lower():
                        result.append(dic)
            else:
                if acknowledge_case:
                    if name == file:
                        result.append(dic)
                else:
                    if name.lower() == file.lower():
                        result.append(dic)
        except:
            pass
    return result


def get_WindowHandle_plus_from_Title(
    title: str,
    contains: bool = False,
    pre_filter_invisible_windows: bool = True,
    acknowledge_case: bool = True,
):
    """Every dictionary contains hwnd, name, rect and path"""
    windows = get_all_WindowHandles_plus(True, pre_filter_invisible_windows)
    result = []
    for dic in windows:
        if contains:
            if acknowledge_case:
                if title in dic["name"]:
                    result.append(dic)
            else:
                if title.lower() in dic["name"].lower():
                    result.append(dic)
        else:
            if acknowledge_case:
                if title == dic["name"]:
                    result.append(dic)
            else:
                if title.lower() == dic["name"].lower():
                    result.append(dic)
    return result


def get_WindowHandle_from_ExePath(
    path,
    contains: bool = False,
    pre_filter_invisible_windows: bool = True,
    acknowledge_case: bool = True,
) -> list[dict]:
    result = get_WindowHandle_plus_from_ExePath(
        path, contains, pre_filter_invisible_windows, acknowledge_case
    )
    if result == None or result == []:
        return None
    try:
        return result[0]["hwnd"]
    except:
        return result["hwnd"]


def get_WindowHandle_from_ExeName(
    name,
    contains: bool = False,
    pre_filter_invisible_windows: bool = True,
    acknowledge_case: bool = True,
) -> list[dict]:
    result = get_WindowHandle_plus_from_ExeName(
        name, contains, pre_filter_invisible_windows, acknowledge_case
    )
    if result == None:
        return None
    print(type(result))
    try:
        return result[0]["hwnd"]
    except:
        return result["hwnd"]


def get_WindowHandle_from_Title(
    title,
    contains: bool = False,
    pre_filter_invisible_windows: bool = True,
    acknowledge_case: bool = True,
# ) -> int | list[dict]:
):
    result = get_WindowHandle_plus_from_Title(
        title, contains, pre_filter_invisible_windows, acknowledge_case
    )
    if result == []:
        return None
    try:
        return result[0]["hwnd"]
    except:
        return result["hwnd"]


def find_window(name: str):
    """Getting the window handle by calling win32gui.FindWindow(name, None)"""
    hwnd = FindWindow(name, None)
    return hwnd


def set_window_topmost_in_windows(WindowHandle=None, x=None, y=None, w=None, h=None):
    if WindowHandle == None:
        hWnd = GetForegroundWindow()
    else:
        hWnd = WindowHandle
    if any([n == None for n in [x, y, w, h]]):
        x0, y0, w0, h0 = get_window_rect(hWnd)
        # from icecream import ic

        # ic(x0, y0, w0, h0)
        if x == None:
            x = x0
        if y == None:
            y = y0
        if w == None:
            w = w0
        if h == None:
            h = h0
    flag = SWP_ASYNCWINDOWPOS
    flag_dexciption = "If the calling thread and the thread that owns the window are attached to different input queues, the system posts the request to the thread that owns the window. This prevents the calling thread from blocking its execution while other threads process the request. "
    insert_after = HWND_TOPMOST
    # insert_after = HWND_TOP
    # insert_after = HWND_BOTTOM
    # insert_after = HWND_NOTOPMOST

    SetWindowPos(hWnd, insert_after, x, y, w, h, flag)


def set_window_top_in_windows(WindowHandle=None, x=None, y=None, w=None, h=None):
    if WindowHandle == None:
        hWnd = GetForegroundWindow()
    else:
        hWnd = WindowHandle
    if any([n == None for n in [x, y, w, h]]):
        x0, y0, w0, h0 = get_window_rect(hWnd)
        if x == None:
            x = x0
        if y == None:
            y = y0
        if w == None:
            w = w0
        if h == None:
            h = h0
    flag = SWP_ASYNCWINDOWPOS
    flag_dexciption = "If the calling thread and the thread that owns the window are attached to different input queues, the system posts the request to the thread that owns the window. This prevents the calling thread from blocking its execution while other threads process the request. "
    # insert_after = HWND_TOPMOST
    insert_after = HWND_TOP
    # insert_after = HWND_BOTTOM
    # insert_after = HWND_NOTOPMOST

    SetWindowPos(hWnd, insert_after, x, y, w, h, flag)


def set_window_bottom_in_windows(WindowHandle=None, x=None, y=None, w=None, h=None):
    if WindowHandle == None:
        hWnd = GetForegroundWindow()
    else:
        hWnd = WindowHandle
    if any([n == None for n in [x, y, w, h]]):
        x0, y0, w0, h0 = get_window_rect(hWnd)
        if x == None:
            x = x0
        if y == None:
            y = y0
        if w == None:
            w = w0
        if h == None:
            h = h0
    flag = SWP_ASYNCWINDOWPOS
    flag_dexciption = "If the calling thread and the thread that owns the window are attached to different input queues, the system posts the request to the thread that owns the window. This prevents the calling thread from blocking its execution while other threads process the request. "
    # insert_after = HWND_TOPMOST
    # insert_after = HWND_TOP
    insert_after = HWND_BOTTOM
    # insert_after = HWND_NOTOPMOST

    SetWindowPos(hWnd, insert_after, x, y, w, h, flag)


def set_window_nottopmost_in_windows(WindowHandle=None, x=None, y=None, w=None, h=None):
    if WindowHandle == None:
        hWnd = GetForegroundWindow()
    else:
        hWnd = WindowHandle
    if any([n == None for n in [x, y, w, h]]):
        x0, y0, w0, h0 = get_window_rect(hWnd)
        if x == None:
            x = x0
        if y == None:
            y = y0
        if w == None:
            w = w0
        if h == None:
            h = h0
    flag = SWP_ASYNCWINDOWPOS
    flag_dexciption = "If the calling thread and the thread that owns the window are attached to different input queues, the system posts the request to the thread that owns the window. This prevents the calling thread from blocking its execution while other threads process the request. "
    # insert_after = HWND_TOPMOST
    # insert_after = HWND_TOP
    # insert_after = HWND_BOTTOM
    insert_after = HWND_NOTOPMOST

    SetWindowPos(hWnd, insert_after, x, y, w, h, flag)


def set_foreground_window(WindowHandle):
    win32com.client.Dispatch("WScript.Shell").SendKeys(
        "%"
    )  # sends left alt key to make windows accept switch of window focus
    SetForegroundWindow(WindowHandle)


def get_exe_path_from_window_handle(hwnd):
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    hndl = win32api.OpenProcess(
        win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, 0, pid
    )
    path: str = win32process.GetModuleFileNameEx(hndl, 0)
    return path


def set_Filme_and_TV_small_window_to_top_right_corner(hwnd=None):
    if hwnd == None:
        hwnd = get_WindowHandle_from_Title("Filme & TV")
    if (
        get_exe_path_from_window_handle(hwnd)
        == "C:\\Windows\\System32\\ApplicationFrameHost.exe"
    ):
        set_window_position(hwnd, 2051, 10, 600, 290)


def set_window_top_left(hwnd, monitor: int = 0):
    monitors = get_monitor_infos()
    m = monitors[monitor]
    midx = m.x + m.width / 2
    set_window_position(hwnd, m.x, -2, round(m.width / 2) + 2, round(m.height / 2) - 33)


def set_window_bottom_left(hwnd, monitor: int = 0):
    monitors = get_monitor_infos()
    m = monitors[monitor]
    midx = m.x + m.width / 2
    midy = m.y + m.height / 2
    set_window_position(
        hwnd, m.x, round(midy) - 38, round(m.width / 2) + 2, round(m.height / 2) - 33
    )


def set_window_top_right(hwnd, monitor: int = 0):
    monitors = get_monitor_infos()
    m = monitors[monitor]
    midx = m.x + m.width / 2
    set_window_position(
        hwnd, round(midx), -2, round(m.width / 2) + 2, round(m.height / 2) - 33
    )


def set_window_bottom_right(hwnd, monitor: int = 0):
    monitors = get_monitor_infos()
    m = monitors[monitor]
    midx = m.x + m.width / 2
    midy = m.y + m.height / 2
    set_window_position(
        hwnd,
        round(midx),
        round(midy) - 38,
        round(m.width / 2) + 2,
        round(m.height / 2) - 33,
    )


def set_window_mid_by_divider(hwnd, divider: float = 8, monitor: int = 0):
    factor = divider
    monitors = get_monitor_infos()
    m = monitors[monitor]
    x = round(m.x + m.width / factor)
    y = round(m.y + m.height / factor)
    w = round(m.width - m.width / factor * 2)
    h = round(m.height - m.height / factor * 2)
    set_window_position(hwnd, x, y, w, h)


def set_window_mid_small(hwnd, monitor: int = 0):
    factor = 4
    monitors = get_monitor_infos()
    m = monitors[monitor]
    x = round(m.x + m.width / factor)
    y = round(m.y + m.height / factor)
    w = round(m.width - m.width / factor * 2)
    h = round(m.height - m.height / factor * 2)
    set_window_position(hwnd, x, y, w, h)


def set_window_mid_medium(hwnd, monitor: int = 0):
    factor = 6
    monitors = get_monitor_infos()
    m = monitors[monitor]
    x = round(m.x + m.width / factor)
    y = round(m.y + m.height / factor)
    w = round(m.width - m.width / factor * 2)
    h = round(m.height - m.height / factor * 2)
    set_window_position(hwnd, x, y, w, h)


def set_window_mid_large(hwnd, monitor: int = 0):
    factor = 10
    monitors = get_monitor_infos()
    m = monitors[monitor]
    x = round(m.x + m.width / factor)
    y = round(m.y + m.height / factor)
    w = round(m.width - m.width / factor * 2)
    h = round(m.height - m.height / factor * 2)
    set_window_position(hwnd, x, y, w, h)


def minimize_window(hwnd):
    ShowWindow(hwnd, SW_MINIMIZE)


def maximize_window(hwnd):
    ShowWindow(hwnd, SW_MAXIMIZE)


def show_window_normally(hwnd):
    ShowWindow(hwnd, SW_SHOWNORMAL)


if __name__ == "__main__":
    from var_print import varp

    for WindowHandleDictionary in get_all_WindowHandles_plus():
        varp(WindowHandleDictionary)
        print()

    varp(get_monitor_infos())
