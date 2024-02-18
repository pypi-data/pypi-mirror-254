from plus.config import Config
from plus.project import Project
from plus.repository import Repository
from plus.requirement_manager import RequirementManager
from plus.rtext import *

import os

def init_project(args):
    type = 'console-app'

    if args.app:
        type = 'app'
    elif args.lib:
        type = 'static-lib'
    elif args.shared_lib:
        type = 'shared-lib'

    if os.path.exists(args.init_name):
        exit(f"Project {rtext(args.init_name, color=color.green, style=style.bold)} already exists")
    
    os.mkdir(args.init_name)
    os.chdir(args.init_name)

    config = Config.create(
        name=args.init_name,
        type=type,
    )
    
    Project.create(config)

def build_project(args):
    if not os.path.exists(args.build_name):
        exit(f"Project {rtext(args.build_name, color=color.green, style=style.bold)} does not exist")
    
    os.chdir(args.build_name)

    config = Config.from_file('plus.toml')
    project = Project('.', config)
    project.compile(debug=True)
    config.save()

def run_project(args):
    if not os.path.exists(args.run_name):
        exit(f"Project {rtext(args.run_name, color=color.green, style=style.bold)} does not exist")
    
    os.chdir(args.run_name)

    config = Config.from_file('plus.toml')
    project = Project('.', config)
    project.run()
    config.save()

def install_project(args):
    config = Config.from_file('plus.toml')

    for req in config.get_requirement_manager():
        req.compile(force=args.force)
        print(f"Installed {rtext(req.name, color=color.green, style=style.bold)} " + rtext("✓", color=color.green, style=style.bold))

def new_project(args):
    config = Config.from_file('plus.toml')
    project = Project('.', config)

    if args.source:
        project.new_source(f"{args.new_name}.cpp", overwrite=args.overwrite)
    elif args.header:
        project.new_header(f"{args.new_name}.hpp", overwrite=args.overwrite, default="#pragma once\n")
    else:
        project.new_header(
            f"{args.new_name}.hpp", 
            overwrite=args.overwrite,
            default="#pragma once\n"
        )
        project.new_source(
            f"{args.new_name}.cpp",
            overwrite=args.overwrite,
            default=f"#include \"{args.new_name}.hpp\"\n"
        )
    
def upgrade_project(args):
    dep = Repository()
    dep.upgrade()

def add_project(args):
    config = Config.from_file('plus.toml')

    config.get_requirement_manager().add(args.add_name)

def clean_project(args):
    if not os.path.exists(args.clean_name):
        exit(f"Project {rtext(args.clean_name, color=color.green, style=style.bold)} does not exist")

    os.chdir(args.clean_name)

    config = Config.from_file('plus.toml')
    project = Project('.', config)

    project.clean(files=args.files, deps=args.deps, subprojects=args.subprojects)