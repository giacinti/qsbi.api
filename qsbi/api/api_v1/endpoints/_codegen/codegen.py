import sys
import os
import logging
from jinja2 import Environment, FileSystemLoader

from module import APIModule
import config  # noqa: F401

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(sys.argv[0])


def render_module(template, m: APIModule) -> None:
    logger.info(f"rendering {m.name} module")
    file_name = f"{m.name}.py"
    with open(file_name, "w") as f:
        output = template.render(module=m.name,
                                 classname=m.classname,
                                 get_by_attrs=m.get_by)
        f.write(output)


def render_list(template, lst: list) -> None:
    if not lst:
        logger.warning("empty list given as argument. Rendering all modules")
    try:
        for m in APIModule.get_modules_list(lst):
            if m:
                render_module(template, m)
    except KeyError as name:
        logger.error(f"module {name} not defined, exiting")
        sys.exit(1)


if __name__ == "__main__":
    tplfile = sys.argv[1]
    tpldir = os.path.join(os.getcwd(), os.path.dirname(tplfile))
    tpl = os.path.basename(tplfile)

    file_loader = FileSystemLoader(tpldir)
    env = Environment(loader=file_loader)
    template = env.get_template(tpl)

    render_list(template, sys.argv[2:])
