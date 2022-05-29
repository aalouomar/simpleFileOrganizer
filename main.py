# import collections
# from pprint import pprint
from pathlib import Path


targetDir = Path(r'D:\Download')
directories = {"HTML": [".html5", ".html", ".htm", ".xhtml"],
               "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", ".heif", ".psd"],
               "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
                          ".qt", ".mpg", ".mpeg", ".3gp"],
               "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                             ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                             ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                             "pptx"],
               "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                            ".dmg", ".rar", ".xar", ".zip"],
               "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
                         ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
               "PLAINTEXT": [".txt", ".in", ".out"],
               "PDF": [".pdf"],
               "PYTHON": [".py"],
               "XML": [".xml"],
               "EXE": [".exe"],
               "SHELL": [".sh"]
               }


fileList = [x for x in targetDir.rglob('*')
            if x.is_file()
            and not x.is_relative_to(targetDir.joinpath('OrganizerPie'))]
dirList = [x for x in targetDir.rglob('*')
           if x.is_dir()
           and not x.is_relative_to(targetDir.joinpath('OrganizerPie'))]
# pprint(collections.Counter(p.suffix for p in fileList))


for f in fileList:
    for x in directories:
        if f.suffix in directories[x]:
            distdirPath = targetDir.joinpath('OrganizerPie', x)
            distdirPath.mkdir(parents=True, exist_ok=True)
            distFilePath = distdirPath.joinpath(f.name)
            if not distFilePath.exists():
                f.replace(distFilePath)
for d in dirList:
    try:
        d.rmdir()
    except OSError:
        continue
