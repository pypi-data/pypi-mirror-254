import numpy as np
import pandas as pd
from list_all_files_recursively import get_folder_file_complete_path
from collections import defaultdict
from arrayhascher import get_hash_column
import os

try:
    O_BINARY = os.O_BINARY
except:
    O_BINARY = 0
READ_FLAGS = os.O_RDONLY | O_BINARY
WRITE_FLAGS = os.O_WRONLY | os.O_CREAT | os.O_TRUNC | O_BINARY

try:
    O_BINARY = os.O_BINARY
except:
    O_BINARY = 0
READ_FLAGS = os.O_RDONLY | O_BINARY
WRITE_FLAGS = os.O_WRONLY | os.O_CREAT | os.O_TRUNC | O_BINARY


def read_bytes_from_file(file, d, buffer=1024):
    try:
        fin = os.open(file.path, READ_FLAGS)
        stat = os.fstat(fin)
        statdict = dict(
            tuple(
                [(x, getattr(stat, x)) for x in dir(stat) if str(x).startswith("st_")]
            )
        )
        statdict["aa_file"] = file.file
        statdict["zz_filepath"] = file.path
        statdict["zz_folder"] = file.folder
        statdict["zz_exception"] = ""

        hashdata = get_hash_column(
            (
                np.fromiter(iter(lambda: os.read(fin, buffer), b""), dtype="S1")
                .view(np.uint8)
                .ravel()
                .reshape((1, -1))
            ),
            fail_convert_to_string=True,
            whole_result=False,
        )
        d[hashdata[0]].append(statdict)
    except Exception as fe:
        d[0].append(
            {
                "st_atime": -1,
                "st_atime_ns": -1,
                "st_ctime": -1,
                "st_ctime_ns": -1,
                "st_dev": -1,
                "st_file_attributes": -1,
                "st_gid": -1,
                "st_ino": -1,
                "st_mode": -1,
                "st_mtime": -1,
                "st_mtime_ns": -1,
                "st_nlink": -1,
                "st_reparse_tag": -1,
                "st_size": -1,
                "st_uid": -1,
                "aa_file": file.file,
                "zz_filepath": file.path,
                "zz_folder": file.folder,
                "zz_exception": str(fe),
            }
        )

    finally:
        try:
            os.close(fin)

        except Exception as fe:
            print(fe)


def hash_files_in_folder(foldertoscan, maxsubfolders=-1):
    r"""
    Hashes files in the specified folder and its subfolders.

    Parameters:
        foldertoscan: str, the path of the folder to scan.
        maxsubfolders: int, optional, the maximum number of subfolders to scan. Default is -1 (No limit).

    Returns:
        pandas DataFrame: A DataFrame containing the file hashes and related information (columns=
        ['aa_file', 'aa_filehash', 'aa_first_date', 'aa_group', 'aa_last_date',
        'st_atime', 'st_atime_ns', 'st_ctime', 'st_ctime_ns', 'st_dev',
        'st_file_attributes', 'st_gid', 'st_ino', 'st_mode', 'st_mtime',
        'st_mtime_ns', 'st_nlink', 'st_reparse_tag', 'st_size', 'st_uid',
        'zz_exception', 'zz_filepath', 'zz_folder'],)


    Example:

        from filehashs2df import hash_files_in_folder
        df = hash_files_in_folder(
            foldertoscan=r"C:\ProgramData\BlueStacks_nxt", maxsubfolders=-1
        )
        print(df.to_string())
        # ...
        # 25                           radio_selected_disaled.png   626056694397970692   1.703810e+09        50  1.703810e+09  1.706831e+09  1706830788706027600  1.703810e+09  1703810493924268200  3067733448                  32       0   1970324841331629    33206  1.642674e+09  1642673891363929100         1               0         579       0                                                    C:\ProgramData\BlueStacks_nxt\Client\Assets\radio_selected_disaled.png                            C:\ProgramData\BlueStacks_nxt\Client\Assets
        # 26                             radio_selected_hover.png   626056694397970692   1.703810e+09        50  1.703810e+09  1.706831e+09  1706830788706027600  1.703810e+09  1703810493925014800  3067733448                  32       0   1970324841331630    33206  1.642674e+09  1642673891363929100         1               0         577       0                                                      C:\ProgramData\BlueStacks_nxt\Client\Assets\radio_selected_hover.png                            C:\ProgramData\BlueStacks_nxt\Client\Assets
        # 27                                 radio_unselected.png   626056694397970692   1.703810e+09        50  1.703810e+09  1.706831e+09  1706830788706027600  1.703810e+09  1703810493925014800  3067733448                  32       0   1970324841331631    33206  1.642674e+09  1642673891363929100         1               0         480       0                                                          C:\ProgramData\BlueStacks_nxt\Client\Assets\radio_unselected.png                            C:\ProgramData\BlueStacks_nxt\Client\Assets
        # 28                           radio_unselected_click.png   626056694397970692   1.703810e+09        50  1.703810e+09  1.706831e+09  1706830788706027600  1.703810e+09  1703810493925761600  3067733448                  32       0   1970324841331632    33206  1.642674e+09  1642673891364929600         1               0         480       0                                                    C:\ProgramData\BlueStacks_nxt\Client\Assets\radio_unselected_click.png                            C:\ProgramData\BlueStacks_nxt\Client\Assets
        # 29                         radio_unselected_disaled.png   626056694397970692   1.703810e+09        50  1.703810e+09  1.706831e+09  1706830788706027600  1.703810e+09  1703810493925761600  3067733448                  32       0   1970324841331633    33206  1.642674e+09  1642673891364929600         1               0         476       0                                                  C:\ProgramData\BlueStacks_nxt\Client\Assets\radio_unselected_disaled.png                            C:\ProgramData\BlueStacks_nxt\Client\Assets
        # 30                           radio_unselected_hover.png   626056694397970692   1.703810e+09        50  1.703810e+09  1.706831e+09  1706830788706774000  1.703810e+09  1703810493925761600  3067733448                  32       0   1970324841331634    33206  1.642674e+09  1642673891364929600         1               0         480       0                                                    C:\ProgramData\BlueStacks_nxt\Client\Assets\radio_unselected_hover.png                            C:\ProgramData\BlueStacks_nxt\Client\Assets
        # 31                                      ErrorCircle.png -6348580002679852874   1.703810e+09        21  1.703810e+09  1.706831e+09  1706830788702294200  1.703810e+09  1703810493909334500  3067733448                  32       0   1970324841331607    33206  1.701756e+09  1701756155001836700         1               0        3157       0                                                               C:\ProgramData\BlueStacks_nxt\Client\Assets\ErrorCircle.png                            C:\ProgramData\BlueStacks_nxt\Client\Assets
        # 32                                        ErrorIcon.png  7103858608122155380   1.703810e+09        82  1.703810e+09  1.706831e+09  1706830788702294200  1.703810e+09  1703810493909334500  3067733448                  32       0   1970324841331608    33206  1.701756e+09  1701756155001836700         1               0        1824       0                                                                 C:\ProgramData\BlueStacks_nxt\Client\Assets\ErrorIcon.png                            C:\ProgramData\BlueStacks_nxt\Client\Assets
        # 33                                   loadingCircles.gif  8501003400277898774   1.703810e+09        92  1.703810e+09  1.706831e+09  1706830788703040800  1.703810e+09  1703810493910828100  3067733448                  32       0   1970324841331612    33206  1.642674e+09  1642673891359927900         1               0      163942       0                                                            C:\ProgramData\BlueStacks_nxt\Client\Assets\loadingCircles.gif                            C:\ProgramData\BlueStacks_nxt\Client\Assets
        # 34                                     message_info.png  -884033196740917800   1.703810e+09        44  1.703810e+09  1.706831e+09  1706830788703787600  1.703810e+09  1703810493918295200  3067733448                  32       0   1970324841331615    33206  1.642674e+09  1642673891360927100         1               0        5699       0                                                              C:\ProgramData\BlueStacks_nxt\Client\Assets\message_info.png                            C:\ProgramData\BlueStacks_nxt\Client\Assets
        # 35                                Moba_cursor_right.png -2580839602864221807   1.703810e+09        39  1.703810e+09  1.706831e+09  1706830788704534200  1.703810e+09  1703810493920535000  3067733448                  32       0   1970324841331623    33206  1.701756e+09  1701756154542820800         1               0        2380       0                                                         C:\ProgramData\BlueStacks_nxt\Client\Assets\Moba_cursor_right.png                            C:\ProgramData\BlueStacks_nxt\Client\Assets
        # ....
    """
    buffer_size = 1024
    d = defaultdict(list)
    allfis = get_folder_file_complete_path(foldertoscan, maxsubfolders=maxsubfolders)
    if not allfis:
        return pd.DataFrame()
    for file in allfis:
        read_bytes_from_file(file, d, buffer=buffer_size)
    df = pd.DataFrame(d.items()).explode(1).reset_index(drop=True)
    df = pd.concat([df[0], df[1].apply(pd.Series)], axis=1).rename(
        columns={0: "aa_filehash"}
    )
    df["aa_group"] = df.groupby(["aa_filehash"]).ngroup()
    grouped = df.groupby(["aa_filehash"]).st_ctime.max()
    groupedd = grouped.to_dict()
    df["aa_last_date"] = df["aa_filehash"].apply(lambda x: groupedd.get(x))
    grouped = df.groupby(["aa_filehash"]).st_ctime.min()
    groupedd = grouped.to_dict()
    df["aa_first_date"] = df["aa_filehash"].apply(lambda x: groupedd.get(x))
    return df.filter(sorted(df.columns))
