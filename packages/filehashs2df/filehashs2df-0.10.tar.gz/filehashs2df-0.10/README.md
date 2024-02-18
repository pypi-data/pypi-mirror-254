# hashes files in the specified folder and its subfolders

## Tested against Windows / Python 3.11 / Anaconda

## pip install filehashs2df

```
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
```
