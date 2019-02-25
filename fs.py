import io
import os


class FSException(Exception):
    pass


class OpenFile:
    def __init__(self, fil):
        self.fil = fil
        self.stream = io.StringIO(fil.contents)

    def read(self):
        return self.fil.contents

    def write(self, data):
        self.fil.contents += data

    def readline(self):
        return self.stream.readline()


class File:
    def __init__(self):
        self.contents = ''

    def open(self):
        return OpenFile(self)


class Directory:
    def __init__(self):
        self.contents = {}

    def get_node(self, path):
        if len(path) == 0 or path[0] == '':
            return self
        next_part = path[0]
        if next_part not in self.contents:
            return None
        child = self.contents[next_part]
        if len(path) == 1:
            return child
        else:
            return child.get_node(path[1:])


class Filesystem:
    def __init__(self):
        self.root = Directory()

    def parse_path(self, path):
        if not path[0] == '/':
            raise FSException("Need an absolute path...")
        if path[-1] == '/':
            path = path[:-1]
        return path[1:].split('/')

    def list_dir(self, path):
        path = self.parse_path(path)
        dir = self.root.get_node(path)
        if not dir:
            raise FSException("Path not found: " + path)
        return dir.contents

    def make_dir(self, path):
        path = self.parse_path(path)
        node = self.root
        while len(path) > 0:
            part = path.pop(0)
            if part not in node.contents:
                old_node = node
                node = Directory()
                old_node.contents[part] = node
            elif type(node.contents[part]) == Directory:
                node = node.contents[part]
            else:
                raise FSException("Can't create directory: " + part)

    def make_file(self, path):
        dirpath = self.parse_path(path)
        filnam = dirpath.pop()
        dir = self.root.get_node(dirpath)
        if not dir:
            raise FSException("Directory not found: " + dirpath)
        fil = File()
        dir.contents[filnam] = fil

    def open(self, path):
        path = self.parse_path(path)
        node = self.root.get_node(path)
        if type(node) != File:
            raise FSException("Cant open: " + "/".join(path))
        return node.open()