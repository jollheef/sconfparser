#!/usr/bin/env python3
## This file is part of the sconfparser application, released under
## GNU General Public License, Version 3.0
## See file COPYING for details.
##
## Author: Klementyev Mikhail <jollheef@riseup.net>
#

class SConfParser(object):
    
    def __init__(self, config_filepath=None):
        if config_filepath:
            self.read(config_filepath)

    def read(self, config_filepath=None):
        if config_filepath:
            self.config_filepath=config_filepath
        with open(self.config_filepath, 'r') as config_file:
            for line in config_file:
                line = line.partition('#')[0]
                line = line.rstrip()
                if line != "\n" and line != "":
                    try:
                        lval, rval = line.split('=')
                    except ValueError:
                        raise SConfParserError("Non valid config file")
                    assign = "self." + lval.strip() \
                             + " = '" + rval.strip() + "'"
                    exec(assign)

    def write(self, config_filepath=None):
        if config_filepath:
            self.config_filepath=config_filepath
        with open(self.config_filepath, 'w') as config_file:
            for var in self.variables():
                config_file.write(var + " = "
                                  + eval("self." + var) + "\n")

    def variables(self):
        variables = self.__dict__.copy()
        try:
            del variables['config_filepath']
        except KeyError:
            pass
        return variables

    def __iter__(self):
        return self.variables().__iter__()

    def __getitem__(self, key):
        return eval("self." + key)

    def __setitem__(self, key, value):
        return exec("self." + key + " = " + value.__repr__())

    def __repr__(self):
        return self.variables().__repr__()

class SConfParserError(Exception):
    pass
