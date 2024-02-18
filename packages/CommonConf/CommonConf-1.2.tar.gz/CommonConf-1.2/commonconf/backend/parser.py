# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from configparser import RawConfigParser, NoOptionError


class ConfigParserBackend(object):
    def __init__(self, path, section):
        self.config = config = RawConfigParser()
        self.config.read(path)
        self.section = section

    def get(self, key):
        try:
            return self.config.get(self.section, key)
        except NoOptionError as ex:
            raise AttributeError(
                "Key {} not in section {}".format(key, self.section))
