import os
import shutil
from string import ascii_uppercase

from var_print import varp
import win32api
from clipboard import paste
from colorful_terminal import *
from .rounding import round_relative_to_decimal
from .percentage import get_percentage_as_fitted_string


def delete_empty_directories(
    directory: str, full_tree: bool = False, reverb: bool = False
):
    """Delete empty directories

    Args:
        directory (str): mother directory to search in
        full_tree (bool, optional): if True all subdirectories will be effected. Defaults to False.
        reverb (bool, optional): print which paths were removed. Defaults to False.

    Returns:
        list[str]: removed directory paths
    """
    removed = []
    if full_tree:
        for root, dirs, files in os.walk(directory, topdown=False):
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)
                    if reverb:
                        colored_print(f"Deleted empty directory: {Fore.YELLOW}{dir_path}")
                    removed.append(dir_path)
    else:
        for f in os.listdir(directory):
            fp = os.path.join(directory, f)
            if os.path.isdir(fp):
                if os.listdir(fp) == []:
                    os.rmdir(dir_path)
                    if reverb:
                        colored_print(f"Deleted empty directory: {Fore.YELLOW}{dir_path}")
                    removed.append(dir_path)
    return removed


def get_disc_informations(print_out: bool = True):
    """Get the information about your discs.

    Args:
        print_out (bool, optional): If True the string will be printed. Defaults to True.

    Returns:
        str: string with the information
    """
    first = True
    out = ""
    for c in ascii_uppercase:
        try:
            (
                name,
                seriennummer,
                maxfilenamelenght,
                sysflags,
                filesystemname,
            ) = win32api.GetVolumeInformation(f"{c}:\\")
            # total, used, free = shutil.disk_usage("/")
            total, used, free = shutil.disk_usage(f"{c}:\\")
            total, used, free = (
                round(total / 10**9, 2),
                round(used / 10**9, 2),
                round(free / 10**9, 2),
            )
            if not first:
                out += "\n"
            out += f"Hard disk information for {c}:\n"
            out += f"\t\tName:                " + name + "\n"
            out += f"\t\Serial number:        " + seriennummer + "\n"
            out += f"\t\tmax filename lenght: " + maxfilenamelenght + "\n"
            out += f"\t\tsys flags:           " + sysflags + "\n"
            out += f"\t\tfilesystem name:     " + filesystemname + "\n"
            out += f"\tMemory:\n"
            out += f"\t\tTotal:" + total, "GB\n"
            out += f"\t\tUsed: " + used, "GB\n"
            out += f"\t\tFree: " + free, "GB\n"
            first = False
        except:
            pass
    if print_out:
        print(out)
    return out


def move_and_integrate_directory(
    dirpath: str,
    targetpath: str,
):
    """Move the content of the directory (dirpath) to the target path. Removes the dirpath if empty.

    Args:
        dirpath (str): source
        targetpath (str): target / destination

    Returns
        list[str]: paths that couldn't be moved
    """
    folderpath = os.path.normpath(dirpath)
    fails = []

    def try_move(fp: str):
        rel_path = os.path.relpath(fp, folderpath)
        structure = rel_path.split("\\")
        try:
            if not os.path.isdir(fp):
                npdp = os.path.join(targetpath, *structure[: len(structure) - 1])
                if not os.path.isdir(npdp):
                    os.makedirs(npdp)
            # nfp = os.path.join(targetpath, *structure)
            shutil.move(fp, targetpath)
        except:
            if os.path.isdir(fp):
                for n in os.listdir(fp):
                    try_move(os.path.join(fp, n))
            else:
                fails.append(fp)

    for f in os.listdir(folderpath):
        fp = os.path.join(folderpath, f)
        try_move(fp)
    try:
        os.rmdir(folderpath)
    except:
        pass
    return fails


def get_directory_size(
    dirpath,
    unit: str = "GB",
):
    """unit can be B / MB / GB"""
    if unit == "B":
        u = 1
    elif unit == "MB":
        u = 10**6
    elif unit == "GB":
        u = 10**9
    else:
        raise ValueError("unit not recognized")
    return (
        sum([os.path.getsize(os.path.join(dirpath, f)) for f in os.listdir(dirpath)])
        / u
    )


def get_all_subdir_sizes(
    dirpath: str,
    unit: str = "GB",
    round_to: int = 2,
    sort_for_size: bool = False,
    print_it: bool = False,
    percentages: bool = True,
    with_sum: bool = True,
):
    """Get a dictionary of the sizes of all the contents of the given directory.

    Args:
        dirpath (str): Directory to get the sizes of
        unit (str, optional): Size unit. Defaults to "GB".
        round_to (int, optional): Round size to. Defaults to 2.
        sort_for_size (bool, optional): Sort the dictionary for size (ascending). Defaults to False.
        print_it (bool, optional): Immediately print the dictionary using varp form var_print. Defaults to False.
        percentages (bool, optional): Adds the percentage to the size string. Defaults to True.
        with_sum (bool, optional): Adds the sum to the dictionary. Defaults to True.

    Raises:
        ValueError: if unit is not B / MB or GB or a number representing the size like 10**9 for GB

    Returns:
        dict[str, str]: Dictionary with the file names (keys) and the size as a string with the unit (possibly with the percentage)
    """
    if unit == "B":
        u = 1
    elif unit == "MB":
        u = 10**6
    elif unit == "GB":
        u = 10**9
    elif type(unit) == int or type(unit) == float:
        u = unit
    else:
        raise ValueError("unit not recognized")
    mp = dirpath
    summe = 0
    max_nachkomma = 0
    subdir_to_size = {}
    max_size = sum([os.path.getsize(os.path.join(mp, f)) for f in os.listdir(mp)]) / u
    pres = len(str(max_size).split(".")[0])
    for d in os.listdir(mp):
        dp = os.path.join(mp, d)
        size = os.path.getsize(dp) / u
        pras = len(str(size).split(".")[0])
        extr = pres - pras
        add_space = extr * " "
        summe += size
        size = round_relative_to_decimal(size, round_to).strip(".")
        value = f"{add_space}{size} {unit}"
        subdir_to_size[d] = value
        nachkomma = len(value.split(".")[-1])
        if nachkomma > max_nachkomma:
            max_nachkomma = nachkomma
    if sort_for_size:
        subdir_to_size = {
            k: v for (k, v) in sorted(subdir_to_size.items(), key=lambda item: item[1])
        }

    size = round_relative_to_decimal(summe, round_to).strip(".")
    if with_sum:
        subdir_to_size["<Summe>"] = f"{size} {unit}"

    if percentages:
        subdir_to_size_perc = {}
        for sd, size in subdir_to_size.items():
            if sd != "<Summe>":
                perc = get_percentage_as_fitted_string(
                    float(size.strip(" " + unit)), summe, 2
                )
                nachkomma = len(size.split(".")[-1])
                if nachkomma == len(size):
                    nachkomma = len(unit)
                spc = max_nachkomma - nachkomma + 4
                subdir_to_size_perc[sd] = size + " " * spc + perc
                # if sd == "Elo":
                #     varp(sd, value)
            else:
                subdir_to_size_perc[sd] = size
    if print_it:
        try:
            varp(subdir_to_size_perc)
        except:
            varp(subdir_to_size)
    return subdir_to_size


def copied_paths_to_list():
    "path copied in Windows to a list"
    urls = paste().replace("\r", "").split("\n")
    urls = [u[1:-1] for u in urls]
    return urls
