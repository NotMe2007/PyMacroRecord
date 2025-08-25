from json import load, dumps
from tkinter import NORMAL, DISABLED
from tkinter import filedialog, messagebox

from utils import UserSettings
from utils.warning_pop_up_save import confirm_save


class RecordFileManagement:
    """Manage save and load record from main app"""

    def __init__(self, main_app, menu_bar):
        self.main_app = main_app
        self.menu_bar = menu_bar
        self.config_text = self.menu_bar.text_config

    def save_macro_as(self, event=None):
        if not self.main_app.macro_recorded or self.main_app.macro.playback:
            return
        self.main_app.prevent_record = True
        macroSaved = filedialog.asksaveasfile(
            filetypes=[("PyMacroRecord Files", "*.pmr"), ("Json Files", "*.json")],
            defaultextension=".pmr",
        )
        if macroSaved is not None:
            self.main_app.current_file = macroSaved.name
            self.save_macro()
            self.main_app.macro_saved = True
        self.main_app.prevent_record = False

    def save_macro(self, event=None):
        if not self.main_app.macro_recorded or self.main_app.macro.playback:
            return
        if self.main_app.current_file is not None:
            with open(self.main_app.current_file, "w", encoding="utf-8") as current_file:
                compactJson = UserSettings(self.main_app).settings_dict["Saving"]["Compact_json"]
                userSettings = self.main_app.settings.settings_dict
                macroSettings = {"settings": {
                    "Playback": userSettings["Playback"],
                    "Minimization": userSettings["Minimization"],
                    "After_Playback": userSettings["After_Playback"]
                }}
                macroData = {
                    **macroSettings,
                    **self.main_app.macro.macro_events
                }
                # Support a versioned wrapper format for future extensibility.
                # If the target filename ends with .pmr2 use the wrapper; otherwise keep legacy behavior.
                use_wrapper = False
                if self.main_app.current_file.lower().endswith('.pmr2'):
                    use_wrapper = True

                payload = macroData
                if use_wrapper:
                    wrapper = {"format": "pmr", "version": 2, "payload": payload}
                    if compactJson:
                        json_macroEvents = dumps(wrapper, separators=(',', ':'))
                    else:
                        json_macroEvents = dumps(wrapper, indent=4)
                else:
                    if compactJson:
                        json_macroEvents = dumps(payload, separators=(',', ':'))
                    else:
                        json_macroEvents = dumps(payload, indent=4)
                current_file.write(json_macroEvents)
        else:
            self.save_macro_as()

    def load_macro(self, event=None):
        if self.main_app.macro.playback:
            return
        self.main_app.prevent_record = True
        if not self.main_app.macro_saved and self.main_app.macro_recorded:
            wantToSave = confirm_save(self.main_app)
            if wantToSave:
                self.save_macro()
            elif wantToSave is None:
                self.main_app.prevent_record = False
                return
        macroFile = filedialog.askopenfile(
            filetypes=[("PyMacroRecord Files", "*.pmr"), ("Json Files", "*.json")],
            defaultextension=".pmr",
        )
        if macroFile is not None:
            self.main_app.playBtn.configure(
                state=NORMAL, command=self.main_app.macro.start_playback
            )
            self.menu_bar.file_menu.entryconfig(
                self.config_text["file_menu"]["save_text"], state=NORMAL, command=self.save_macro
            )
            self.menu_bar.file_menu.entryconfig(
                self.config_text["file_menu"]["save_as_text"], state=NORMAL, command=self.save_macro_as
            )
            self.menu_bar.file_menu.entryconfig(
                self.config_text["file_menu"]["new_text"], state=NORMAL, command=self.new_macro
            )
            macroFile.close()
            with open(macroFile.name, "r", encoding="utf-8") as macroContent:
                # Detect versioned wrapper format. If wrapped, extract payload.
                try:
                    loaded = load(macroContent)
                except Exception:
                    loaded = None
            if loaded is None:
                return
            # If wrapped format v2: {"format":"pmr","version":2,"payload":{...}}
            if isinstance(loaded, dict) and loaded.get("format") == "pmr" and "payload" in loaded:
                record_obj = loaded["payload"]
            else:
                # Legacy unwrapped format (direct dict of settings+events)
                record_obj = loaded

            self.main_app.macro.import_record(record_obj)
            self.main_app.macro_recorded = True
            self.main_app.macro_saved = True
            self.main_app.current_file = macroFile.name
            if "settings" in self.main_app.macro.macro_events:
                if not self.main_app.settings.settings_dict["Loading"]["Always_import_macro_settings"]:
                    if messagebox.askyesno("PyMacroRecord", self.config_text["global"]["load_macro_settings"]):
                        macro_settings = self.main_app.macro.macro_events["settings"]
                        self.main_app.settings.settings_dict["Playback"] = macro_settings["Playback"]
                        self.main_app.settings.settings_dict["Minimization"] = macro_settings["Minimization"]
                        self.main_app.settings.settings_dict["After_Playback"] = macro_settings["After_Playback"]
        self.main_app.prevent_record = False


    def new_macro(self, event=None):
        if not self.main_app.macro_recorded or self.main_app.macro.playback:
            return
        if not self.main_app.macro_saved and self.main_app.macro_recorded:
            wantToSave = confirm_save(self.main_app)
            if wantToSave:
                self.save_macro()
            elif wantToSave is None:
                return
        self.main_app.playBtn.configure(state=NORMAL)
        self.menu_bar.file_menu.entryconfig(self.config_text["file_menu"]["save_text"], state=DISABLED)
        self.menu_bar.file_menu.entryconfig(self.config_text["file_menu"]["save_as_text"], state=DISABLED)
        self.menu_bar.file_menu.entryconfig(self.config_text["file_menu"]["new_text"], state=DISABLED)
        self.main_app.playBtn.configure(state=DISABLED)
        self.main_app.current_file = None
        self.main_app.macro_saved = False
        self.main_app.macro_recorded = False
