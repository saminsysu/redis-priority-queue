#!/usr/bin/env python3

class RpqLua:
    connection = None # Redis Instance
    queue = None # Loaded queue
    script = None # Script source

    def __init__(self, redisConnection, luaPath):
        '''Sets Redis connection, load LUA from path'''
        self.setRedisConnection(redisConnection);
        self.loadSource(luaPath);

    def file_get_contents(self, filename):
        '''Get a file content'''
        with open(filename) as f:
            return f.read()

    def setRedisConnection(self, connection):
        '''Set a Redis connection'''
        self.connection = connection;

    def loadSource(self, path):
        '''Load LUA script source code from a file'''
        self.source = self.file_get_contents(path);

    def register(self):
        '''Load the script into Redis'''
        self.queue = self.connection.register_script(self.source)
        return self.queue;

#     def getQueue:
#         '''Return loaded queue'''
#         return self.queue;