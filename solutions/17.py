# -----------------------------
# Author: Tuan Nguyen
# Date: 20190531
#!solutions/17.py
# -----------------------------
"""
Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

```
dir
    subdir1
    subdir2
        file.ext
```

The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

```
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
```

The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. 
subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. 
For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", 
and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, 
return the length of the longest absolute path to a file in the abstracted file system. 
If there is no file in the system, return 0.
"""


def longestDirectoryPath(string):
# input: a string representing directories
# output: longest directory path to file and its length
	paths = []
	directories = string.split("\n")	# e.g string="dir\n\tsubdir1\n\t\tfile.ext" -> directories=["dir", "\tsubdir1", "\t\tfile.ext"]
	files = [d for d in directories if "." in d]	# above example -> files=["\t\tfile.ext"]
	for f in files:
		subLevel = f.count("\t")	# locate file in which subsection
		fIndex = directories.index(f)	# index of file in list directories[]
		j = fIndex - 1					# previous index of file in list directories[]
		path = f.replace("\t", "")		# init str path of file name
		while j >= 0:	# loop in list directories[]
			if directories[j].count("\t") == subLevel - 1:	# if file is in that folder
				path = directories[j].replace("\t", "") + "/" + path 	# add folder to path
				subLevel -= 1	# decrease subsection level -> 0 := root folder
			j -= 1
		paths.append(path)	# add 1 possible path
	# return
	if paths:
		return max(paths), len(max(paths))
	return "", 0


def longestDirectoryPath_test(string):
	print(string)
	print(longestDirectoryPath(string))


if __name__ == '__main__':
	longestDirectoryPath_test("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")	# return ('dir/subdir2/file.ext', 20)
	longestDirectoryPath_test("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")	
	# return ('dir/subdir2/subsubdir2/file2.ext', 32)
