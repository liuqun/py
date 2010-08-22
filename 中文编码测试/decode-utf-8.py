#!/usr/bin/env python
# -*- coding: utf-8 -*-

utf_8_str = "这是测试文字"
unicode_str = utf_8_str.decode("utf-8")
if utf_8_str == unicode_str.encode("utf-8"):
	print("UTF-8 ok")

