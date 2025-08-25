import tkinter as tk

from windows.popup import Popup


class About(Popup):
    def __init__(self, parent, main_app, version, updated):
        super().__init__(main_app.text_content["help_menu"]["about_settings"]["title"], 300, 150, parent)
        tk.Label(self, text=f"{main_app.text_content['help_menu']['about_settings']['publisher_text']}: LOUDO").pack(
            side=tk.TOP, pady=3)
        tk.Label(self,
                 text=f"{main_app.text_content['help_menu']['about_settings']['version_text']}: {version} ({updated})").pack(
            side=tk.TOP, pady=3)
        tk.Label(self,
                 text=f"{main_app.text_content['help_menu']['about_settings']['license_text']}: General Public License v3.0").pack(
            side=tk.TOP, pady=3)
        buttonArea = tk.Frame(self)
        tk.Button(buttonArea, text="Close", command=self.destroy).pack(side=tk.LEFT, padx=10)
        buttonArea.pack(side=tk.BOTTOM, pady=10)
        main_app.prevent_record = True
        self.wait_window()
        main_app.prevent_record = False

