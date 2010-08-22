#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
def ListFileSystemTree(dir):
	tree = ""
	for root, dirs, files in os.walk(dir):
		tree += ("%s;%s;%s\n" % (root, dirs, files))
	print(tree)
