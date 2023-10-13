from pathlib import Path

targetDir = Path("")

directories = {"IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", ".heif", ".psd"],
               "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg",
                          ".mpeg", ".3gp"],
               "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", "ogg",
                         "oga", ".raw", ".vox", ".wav", ".wma"],
               "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar",
                            ".xar", ".zip"],
               "APPS\\EXE": [".exe"],
               "APPS\\APK": [".apk"],
               "DOCUMENTS": [".oxps", ".pages", ".fdf", ".ods", ".odt", ".pwi", ".xsn",
                             ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd"],
               "DOCUMENTS\\PLAINTEXT": [".txt", ".in", ".out"],
               "DOCUMENTS\\PDF": [".pdf"],
               "DOCUMENTS\\WORD": [".docx", ".doc"],
               "DOCUMENTS\\EXCEL": [".xls", ".xlsx"],
               "DOCUMENTS\\POWERPOINT": [".ppt", "pptx"],
               "DOCUMENTS\\EBOOKS": [".epub", ".mobi"],
               "DEV\\PYTHON": [".py"],
               "DEV\\XML": [".xml"],
               "DEV\\SHELL": [".sh"],
               "DEV\\HTML": [".html5", ".html", ".htm", ".xhtml"]
               }

fileList = [x for x in targetDir.rglob('*')
            if x.is_file()
            and not x.is_relative_to(targetDir.joinpath('OrganizerPie'))]
dirList = sorted([(len(x.parts), x) for x in targetDir.rglob('*')
                  if x.is_dir()
                  and not x.is_relative_to(targetDir.joinpath('OrganizerPie'))], reverse=True)

for f in fileList:
    distdirPath = targetDir.joinpath('OrganizerPie', "OTHERS")
    for x, y in directories.items():
        if f.suffix in y:
            distdirPath = targetDir.joinpath('OrganizerPie', x)
    distdirPath.mkdir(parents=True, exist_ok=True)
    distFilePath = distdirPath.joinpath(f.name)
    renaming_counter = 1
    while distFilePath.exists():
        distFilePath = distFilePath.with_stem(f'{f.stem}({renaming_counter})')
        renaming_counter += 1
    f.replace(distFilePath)
for d in dirList:
    try:
        d[1].rmdir()
    except OSError:
        continue
