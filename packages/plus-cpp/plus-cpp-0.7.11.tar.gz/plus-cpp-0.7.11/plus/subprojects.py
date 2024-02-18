from plus.rtext import *

import os

class Subprojects:
    def __init__(self, config: "Config", path: str):
        self.subprojects = {}
        self.config = config
        self.path = path

        if 'subprojects' in self.config.dict:
            self.subprojects = config.dict['subprojects']

        self.compiled_subprojects = []
    
    def compile(self, debug=False):
        print(f'Compiling subprojects ...')

        for name in self.subprojects:
            if name in self.compiled_subprojects:
                continue

            subproject = self.config.dict['subprojects'][name]
            self.compile_subproject(name, subproject, debug=True)
            self.compiled_subprojects.append(name)
        
        for compiled in self.compiled_subprojects:
            print(f'Compiled subproject {rtext(compiled, color=color.green, style=style.bold)}')
        
    def compile_subproject(self, name: str, project: dict, debug=False):
        if not 'path' in project:
            project['path'] = name
        
        path = os.path.join(self.path, project['path'])
        
        from plus.project import Project
        from plus.config import Config

        old_dir = os.getcwd()
        os.chdir(path)

        config = Config.from_file(os.path.join(path, 'plus.toml'))
        subprojects = config.get_subprojects(path=path)

        for subproject in subprojects:
            if subproject in self.compiled_subprojects:
                continue

            else:
                dc = subprojects[subproject].copy()
                dc['path'] = os.path.join(project['path'], dc['path'])
                
                self.compile_subproject(subproject, dc, debug=True)
                self.compiled_subprojects.append(subproject)

        subproject = Project(path, config)
        subproject.compile(debug=False, compile_subprojects=False)
        os.chdir(old_dir)

    def clean(self, files=True, deps=True):
        old_dir = os.getcwd()

        from plus.project import Project
        from plus.config import Config

        for subproject in self.subprojects:
            os.chdir(os.path.join(self.path, self.subprojects[subproject]['path']))

            config = Config.from_file('plus.toml')
            project = Project('.', config)
            project.clean(files=files, deps=deps, subprojects=False)

            os.chdir(old_dir)

    def get_compiler_config(self):
        from plus.config import Config

        includes = []
        libs = []
        libdirs = []
        binaries = []
        defines = []

        for name in self.subprojects:
            subproject = self.subprojects[name]
            path = os.path.join(self.path, subproject['path'])
            config = Config.from_file(os.path.join(path, 'plus.toml'))
            compiler = config.dict.get('compiler', { })
            linker = config.dict.get('linker', { })

            if 'linker' in config.dict and 'type' in config.dict['linker']:
                if config.dict['linker']['type'] == 'static-lib':
                    libs += [f'{name}']
                    libdirs += [os.path.join(path, 'lib')]
                    
                    subprojects = config.get_subprojects(path=path)

                    for subproject in subprojects:
                        config = Config.from_file(os.path.join(path, subprojects[subproject]["path"] + '/plus.toml'))

                        if 'linker' in config.dict and 'type' in config.dict['linker']:
                            if config.dict['linker']['type'] == 'static-lib':
                                libs += [f'{subproject}']
                                libdirs += [os.path.join(path, subprojects[subproject]["path"] + '/lib')]
            
            includes += [os.path.join(path, f) for f in compiler.get('includes', [])]
            libs += linker.get('libs', [])
            libdirs += [os.path.join(path, f) for f in linker.get('libdirs', [])]
            binaries += [os.path.join(path, f) for f in compiler.get('binaries', [])]
            defines += compiler.get('defines', [])

        libs.reverse()
        
        return {
            'includes': includes,
            'libs': libs,
            'libdirs': libdirs,
            'binaries': binaries,
            'defines': defines
        }

    def __iter__(self):
        return iter(self.subprojects)

    def __len__(self):
        return len(self.subprojects)

    def __getitem__(self, key):
        return self.subprojects[key]
    
    def __setitem__(self, key, value):
        self.subprojects[key] = value

    def __delitem__(self, key):
        del self.subprojects[key]

    def __contains__(self, item):
        return item in self.subprojects
    
    def __str__(self):
        return str(self.subprojects)