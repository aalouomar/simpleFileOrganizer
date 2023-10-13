import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from tkinter.filedialog import askdirectory


class OrganizerPie(ttkb.Frame):
    def __init__(self, master):
        super().__init__(master, padding=5)
        self.pack(fill=BOTH, expand=YES)

        self.filename = ttkb.StringVar()
        self.op_options = {"Delete empty folders": ttkb.BooleanVar(value=False),
                           "Save ancient folder hierarchy": ttkb.BooleanVar(value=False),
                           "Use files extensions as named folders": ttkb.BooleanVar(value=False),
                           "Select file types to be moved": ttkb.BooleanVar(value=False)
                           }
        self.fileselection = {
            "Documents": {'id': ttkb.BooleanVar(value=True),
                          'pdf': ttkb.BooleanVar(value=False),
                          'word': ttkb.BooleanVar(value=False),
                          'excel': ttkb.BooleanVar(value=False),
                          'ppt': ttkb.BooleanVar(value=False),
                          'epub': ttkb.BooleanVar(value=False),
                          'txt': ttkb.BooleanVar(value=False)
                          },
            "Images": {'id': ttkb.BooleanVar(value=True),
                       'jpg': ttkb.BooleanVar(value=False),
                       'gif': ttkb.BooleanVar(value=False),
                       'png': ttkb.BooleanVar(value=False),
                       'svg': ttkb.BooleanVar(value=False),
                       'bmp': ttkb.BooleanVar(value=False)},
            "Video": {'id': ttkb.BooleanVar(value=True),
                      'mp4': ttkb.BooleanVar(value=False),
                      'avi': ttkb.BooleanVar(value=False),
                      'mkv': ttkb.BooleanVar(value=False),
                      'mpeg': ttkb.BooleanVar(value=False),
                      'webm': ttkb.BooleanVar(value=False)},
            "Audio": {'id': ttkb.BooleanVar(value=True),
                      'mp3': ttkb.BooleanVar(value=False),
                      'flac': ttkb.BooleanVar(value=False),
                      'ogg': ttkb.BooleanVar(value=False),
                      'wav': ttkb.BooleanVar(value=False)},
            "Archive": {'id': ttkb.BooleanVar(value=True),
                        'zip': ttkb.BooleanVar(value=False),
                        'rar': ttkb.BooleanVar(value=False),
                        '7z': ttkb.BooleanVar(value=False),
                        'gz': ttkb.BooleanVar(value=False),
                        'iso': ttkb.BooleanVar(value=False)}
        }

        self.directory_browser_block()
        self.options_block()
        self.footer_block()

    def directory_browser_block(self):
        """Create and add the directory browser widget elements"""
        browser_container = ttkb.Labelframe(self, text="Select target folder")
        browser_container.pack(side=TOP, fill=X, padx=5, pady=5)

        file_entry = ttkb.Entry(browser_container, textvariable=self.filename)
        file_entry.pack(side=LEFT, fill=X, expand=YES, padx=5, pady=5)

        browse_btn = ttkb.Button(browser_container, text="Browse", command=self.open_file)
        browse_btn.pack(side=RIGHT, fill=X, padx=5, pady=5)

    def options_block(self):
        """Create and add options widgets elements"""
        options_container = ttkb.Labelframe(self, text="Options")
        options_container.pack(side=TOP, fill=X, padx=5, pady=5)

        for name, var in self.op_options.items():
            op_checkbox = ttkb.Checkbutton(options_container, text=name, variable=var,
                                           command=self.on_toggle)
            op_checkbox.pack(side=TOP, fill=X, padx=5, pady=5)

        selection_container = ttkb.Frame(options_container)
        selection_container.pack(side=TOP, fill=X, padx=(20, 0))
        for key, value in self.fileselection.items():
            categories_container = ttkb.Frame(selection_container)
            categories_container.pack(side=LEFT, fill=Y)

            op_checkbox = ttkb.Checkbutton(categories_container, text=key, width=11,
                                           variable=value["id"],
                                           state='disabled',
                                           command=self.on_toggle)
            op_checkbox.pack(side=TOP, fill=X, padx=5, pady=5)

            for x, y in value.items():
                if x != 'id':
                    op_checkbox = ttkb.Checkbutton(categories_container, text=x, variable=y,
                                                   state='disabled')
                    op_checkbox.pack(side=TOP, fill=X, padx=(10, 0), pady=5)

    def footer_block(self):
        """Create and add "proceed" and "cancel" bouttons"""
        footer_container = ttkb.Frame(self)
        footer_container.pack(side=TOP, fill=X, padx=5, pady=5)

        proceed_btn = ttkb.Button(footer_container, text="Proceed", command=self.on_proceed)
        proceed_btn.pack(side=RIGHT, fill=X, padx=5, pady=5)
        cancel_btn = ttkb.Button(footer_container, text="Cancel", command=self.quit)
        cancel_btn.pack(side=RIGHT, fill=X, padx=5, pady=5)

    def open_file(self):
        path = askdirectory()
        if not path:
            return
        self.filename.set(path)

    def on_cancel(self):
        pass

    def on_proceed(self):
        pass
        # for x in self.winfo_children()[1].winfo_children():
        #     if x.winfo_class() == 'TCheckbutton':
        #         if str(x.configure('state')[4]) != 'disabled':
        #             if self.getvar(x.configure('variable')[4]) == '1':
        #                 print(str(x.configure('text')[4]))

    def on_toggle(self):
        catframe = self.winfo_children()[1].winfo_children()[-1].winfo_children()

        if self.op_options["Select file types to be moved"].get():
            for frame in catframe:
                catcb = frame.winfo_children()[0]
                itemscb = frame.winfo_children()[1:]
                catcb['state'] = 'normal'
                vvar = self.fileselection[str(catcb.configure('text')[4])]
                if vvar["id"].get():
                    for itemcb in itemscb:
                        itemcb['state'] = 'disabled'
                else:
                    for itemcb in itemscb:
                        itemcb['state'] = 'normal'
        else:
            for frame in catframe:
                for cb in frame.winfo_children():
                    cb['state'] = 'disabled'





if __name__ == '__main__':
    app = ttkb.Window("Orignize Pie", "darkly")
    OrganizerPie(app)
    app.mainloop()
