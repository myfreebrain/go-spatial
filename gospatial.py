#!/usr/bin/env python

# This file is intended to be a helper for running gospatial tools from a Python script.
# See gospatial_example.py for an example of how to use it.
import os
import sys
import subprocess
from sys import platform

exe_path = os.path.dirname(os.path.abspath(__file__))
wd = ""

if platform == 'win32':
    ext = '.exe'
else:
    ext = ''

exe_name = "go-spatial{}".format(ext)

def set_gospatial_dir(path):
    global exe_path
    exe_path = path

def set_working_dir(path):
    global wd
    wd = path

def help():
    try:
        os.chdir(exe_path)
        cmd = []
        cmd.append("." + os.path.sep + exe_name)
        cmd.append("-help")
        ps = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True)
        ret = ""
        while True:
            line = ps.stdout.readline()
            if line != '':
                ret += line
            else:
                break

        return ret
    except Exception as e:
        return e

def tool_args(tool_name):
    try:
        os.chdir(exe_path)
        cmd = []
        cmd.append("." + os.path.sep + exe_name)
        cmd.append("-toolargs={}".format(tool_name))
        ps = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True)
        ret = ""
        while True:
            line = ps.stdout.readline()
            if line != '':
                ret += line
            else:
                break

        return ret
    except Exception as e:
        return e

def tool_help(tool_name):
    try:
        os.chdir(exe_path)
        cmd = []
        cmd.append("." + os.path.sep + exe_name)
        cmd.append("-toolhelp={}".format(tool_name))
        ps = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True)
        ret = ""
        while True:
            line = ps.stdout.readline()
            if line != '':
                ret += line
            else:
                break

        return ret
    except Exception as e:
        return e

def list_tools():
    try:
        os.chdir(exe_path)
        cmd = []
        cmd.append("." + os.path.sep + exe_name)
        cmd.append("-listtools")
        ps = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True)
        ret = ""
        while True:
            line = ps.stdout.readline()
            if line != '':
                ret += line
            else:
                break

        return ret
    except Exception as e:
        return e

def default_callback(str):
    print(str)

def run_tool(tool_name, args, callback = default_callback):
    try:
        os.chdir(exe_path)
        cmd = []
        cmd.append("." + os.path.sep + exe_name)
        if len(wd) > 0:
            cmd.append("-cwd=\"{}\"".format(wd))

        cmd.append("-run={}".format(tool_name))
        args_str = ""
        for s in args:
            args_str += s.replace("\"", "") + ";"
        args_str = args_str[:-1]
        cmd.append("-args=\"{}\"".format(args_str))
        # print cmd
        ps = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True)

        # if platform == 'win32':
        #     ext = '.exe'
        # else:
        #     ext = ''
        #
        # exe_name = "go-spatial"
        # cmd = "." + os.path.sep + exe_name #"{0}{1}".format(exe_name, ext)
        # if len(wd) > 0:
        #     cmd += " -cwd {}".format(wd)
        #
        # cmd += ' -run \"{}\"'.format(tool_name)
        # args_str = ""
        # for s in args:
        #     args_str += s.replace("\"", "") + ";"
        # args_str = args_str[:-1]
        # cmd += ' -args \"{}\"'.format(args_str)
        # # print cmd
        # ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True)

        while True:
            line = ps.stdout.readline()
            if line != '':
                callback(line.strip())
            else:
                break

        return 0
    except Exception as e:
        print(e)
        return 1

def version():
    try:
        os.chdir(exe_path)
        cmd = []
        cmd.append("." + os.path.sep + exe_name)
        cmd.append("-version")
        ps = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True)
        ret = ""
        while True:
            line = ps.stdout.readline()
            if line != '':
                ret += line
            else:
                break

        return ret
    except Exception as e:
        return e
