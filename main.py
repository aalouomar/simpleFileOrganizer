from pathlib import Path


def trier(path: str, ):
    target_dir = Path(path)

    directories = {
        "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg", ".heif", ".psd", ".tif",
                   ".TIF", ".JPG", ".ico"],
        "VIDEOS": [".avi", ".flv", ".FLV", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg",
                   ".mpeg", ".3gp"],
        "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", ".ogg",
                  ".oga", ".raw", ".vox", ".wav", ".wma", ".wpl", ".amr"],
        "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar",
                     ".xar", ".zip"],
        "DOCUMENTS": [".oxps", ".pages", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".TXT"
                                                                                                  ".docm", ".dox",
                      ".rvg", ".rtf", ".rtfd", ".wpd", ".txt", ".in", ".out", ".pdf",
                      ".docx", ".doc", ".xls", ".xlsx", ".ppt", ".pptx", ".epub", ".mobi", ".PDF", ".XLS",
                      ".XLSX", ".xlsm", ".xlsb", ".pps", ".PPS", ".PPT", ".DOC", ".DOCX", ".csv", ".xla"]
    }

    file_list = [x for x in target_dir.rglob('*')
                 if x.is_file()
                 and not x.is_relative_to(target_dir.joinpath('FOP_'))]

    for f in file_list:
        distdir_path = target_dir.joinpath('FOP_OTHERS')
        for x, y in directories.items():
            if f.suffix in y:
                distdir_path = target_dir.joinpath('FOP_' + x)
        distdir_path.mkdir(parents=True, exist_ok=True)
        distfile_path = distdir_path.joinpath(f.name)
        renaming_counter = 1
        while distfile_path.exists():
            distfile_path = distfile_path.with_stem(f'{f.stem}({renaming_counter})')
            renaming_counter += 1
        f.replace(distfile_path)

    dir_list = sorted([(len(x.parts), x) for x in target_dir.rglob('*')
                       if x.is_dir() and not x.is_relative_to(target_dir.joinpath('OrganizerPie'))],
                      reverse=True)
    for d in dir_list:
        try:
            d[1].rmdir()
        except OSError:
            continue
    return "opération completed!!"
