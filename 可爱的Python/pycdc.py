#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import exit
import cmd


pycdcintro = '''
PyCDC0.5 使用说明:
  dir 目录名    # 指定保存和搜索目录,默认是 "cdc"
  walk 文件名   # 指定光盘信息文件名,使用 "*.cdc"
  find 关键词   # 指定搜索关键词
  ?             # 查询
  EOF           # 退出系统,也可以使用 Crtl+D(Unix)|Ctrl+Z(Dos/Windows)
'''

class PyCDC(cmd.Cmd):
	def __init__(self):
		cmd.Cmd.__init__(self)
		self.prompt="(PyCDC)> "
		self.intro = pycdcintro


	def help_help(self):
		print("您可以调用help命令查看帮助信息，格式为\nhelp <topic>")

	def help_EOF(self):
		print("退出程序")
	def do_EOF(self, line):
		exit()

	def help_walk(self):
		print "扫描光盘内容"
	def do_walk(self, filename):
		if filename == "":filename = raw_input("输入 cdc 文件名:: ")
		print "扫描光盘内容保存到:'%s'" % filename

	def help_dir(self):
		print "指定保存/搜索目录"
	def do_dir(self, pathname):
		if pathname == "": pathname = raw_input("输入指定保存/搜索目录: ")

	def help_find(self):
		print "搜索关键词"
	def do_find(self, keyword):
		if keyword == "": keyword = raw_input("输入搜索关键字: ")
		print "搜索关键词:'%s'" % keyword


if __name__ == '__main__':
	cdc = PyCDC()
	cdc.cmdloop()

	#from cdctools import ListFileSystemTree
	#print(sys.argv)
	#import sys
	#ListFileSystemTree('/media');
