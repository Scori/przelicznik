# coding: utf-8
"""
Created on March 22, 2017
@author: sim1234
"""
import optparse
import sys
from docutils import nodes
from docutils.parsers.rst import directives
from pylint.pyreverse import writer
from pylint.pyreverse.diadefslib import DiadefsHandler
from pylint.pyreverse.inspector import project_from_files, Linker
from pylint.pyreverse.main import OPTIONS
from sphinx.util.compat import Directive
from PIL import Image as IMAGE
from subprocess import call
from hashlib import sha512
import importlib
import os


class MyDotWriter(writer.DotWriter):
    def __init__(self, config, file_name=None):
        super(MyDotWriter, self).__init__(config)
        self.__file_name = file_name

    def close_graph(self):
        if self.file_name is None:
            return super(MyDotWriter, self).close_graph()
        return self.printer.generate(self.__file_name)


class UMLGeneratePyReverseDirective(Directive):
    """UML directive to generate a pyreverse diagram"""
    required_arguments = 1
    optional_arguments = 0
    has_content = False

    def create_image(self, module_name, module_file, target_file, conf={}):
        print(target_file, os.getcwd())
        config = optparse.Values()
        config.module_names = [module_name]
        config.all_ancestors = True
        config.all_associated = True
        config.show_ancestors = 100
        config.show_associated = 100
        for name, data in OPTIONS:
            setattr(config, data.get('dest', name).replace('-', '_'), data.get('default', 0))
        config.output_format = 'png'
        config.project = module_name
        for k, v in conf.items():
            setattr(config, k, v)
        sys.path.insert(0, os.getcwd())
        try:
            project = project_from_files([module_file], project_name=config.project, black_list=config.black_list)
            linker = Linker(project, tag=True)
            handler = DiadefsHandler(config)
            diadefs = handler.get_diadefs(project, linker)
        finally:
            sys.path.pop(0)
        MyDotWriter(config, target_file).write(diadefs)

    def run(self):
        env = self.state.document.settings.env
        target_dir = os.path.abspath(os.path.join(env.doctreedir, '..', 'html', '_images'))
        if not os.path.exists(target_dir):
            os.mkdir(target_dir)
        module_name = self.arguments[0]
        module = importlib.import_module(module_name)
        module_file = module.__path__[0] if hasattr(module, '__path__') else module.__file__
        target_file = os.path.join(target_dir, 'class_diagram_%s.png' % module_name)
        self.create_image(module_name, module_file, target_file)
        uri = directives.uri(target_file)
        i = IMAGE.open(target_file)
        img = nodes.image(uri=uri, width=str(i.size[0]))
        return [img]


def setup(app):
    """Setup directive"""
    app.add_directive('pyreverse', UMLGeneratePyReverseDirective)
