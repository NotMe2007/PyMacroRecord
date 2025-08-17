from os import path, system
from sys import platform

from utils.get_file import resource_path

try:
    from win10toast import ToastNotifier
except ImportError:
    # Not on Windows or package not available
    ToastNotifier = None


def show_notification_minim(main_app):
    if platform == "win32":
        if ToastNotifier is None:
            return
        toast = ToastNotifier()
        try:
            toast.show_toast(
                title="PyMacroRecord",
                msg=main_app.text_content["options_menu"]["settings_menu"]["minimization_toast"],
                duration=3,
                icon_path=resource_path(path.join("assets", "logo.ico"))
            )
        except Exception:
            # Toast display failed; continue without crashing
            return

    elif "linux" in platform.lower():
        system(f"""notify-send -u normal "PyMacroRecord" "{main_app.text_content["options_menu"]["settings_menu"]["minimization_toast"]}" """)
    elif "darwin" in platform.lower():
        system(f"""osascript -e 'display notification "{main_app.text_content["options_menu"]["settings_menu"]["minimization_toast"]}" with title "PyMacroRecord"'""")
