import shutil
from pathlib import Path


def prep_and_copy(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir()
    copy_all(src, dst)


def copy_all(src: Path, dst: Path) -> None:

    # List everything in the source directory
    list_src = []
    for item in src.iterdir():
        list_src.append(item)

    # Iterate
    full_src_path = Path("")
    full_dst_path = Path("")
    for item in list_src:
        full_src_path = item
        full_dst_path = dst / item.name
        if item.is_file():
            shutil.copy(full_src_path, full_dst_path)
        elif item.is_dir():
            full_dst_path.mkdir()
            copy_all(full_src_path, full_dst_path)
        else:
            raise ValueError("ERROR: Inappropriate Value")
