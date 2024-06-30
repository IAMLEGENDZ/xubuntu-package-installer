#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
from setuptools import setup, find_packages


def create_mo_files():
    podir = "po"
    mo = []
    for po in os.listdir(podir):
        if po.endswith(".po"):
            os.makedirs("{}/{}/LC_MESSAGES".format(podir, po.split(".po")[0]), exist_ok=True)
            mo_file = "{}/{}/LC_MESSAGES/{}".format(podir, po.split(".po")[0], "xubuntu-package-installer.mo")
            msgfmt_cmd = 'msgfmt {} -o {}'.format(podir + "/" + po, mo_file)
            subprocess.call(msgfmt_cmd, shell=True)
            mo.append(("/usr/share/locale/" + po.split(".po")[0] + "/LC_MESSAGES",
                       ["po/" + po.split(".po")[0] + "/LC_MESSAGES/xubuntu-package-installer.mo"]))
    return mo


changelog = "debian/changelog"
version = "0.1.0"
if os.path.exists(changelog):
    head = open(changelog).readline()
    try:
        version = head.split("(")[1].split(")")[0]
    except:
        print("debian/changelog format is wrong for get version")
    f = open("src/__version__", "w")
    f.write(version)
    f.close()

data_files = [
    ("/usr/share/applications", ["ar.org.xubuntu.package-installer.desktop"]),
    ("/usr/share/xubuntu/xubuntu-package-installer/ui", ["ui/MainWindow.glade"]),
    ("/usr/share/xubuntu/xubuntu-package-installer/src",
     ["src/Actions.py", "src/Main.py", "src/MainWindow.py", "src/__version__"]),
    ("/usr/bin", ["xubuntu-package-installer"]),
    ("/usr/share/polkit-1/actions", ["ar.org.xubuntu.pkexec.xubuntu-package-installer.policy"]),
    ("/usr/share/icons/hicolor/scalable/apps/", ["images/xubuntu-package-installer.svg"])
] + create_mo_files()

setup(
    name="Xubuntu Package Installer",
    version=version,
    packages=find_packages(),
    scripts=["xubuntu-package-installer"],
    install_requires=["PyGObject"],
    data_files=data_files,
    author="Mohamed Benkouider",
    author_email="mbkasr@gmail.com",
    description="Xubuntu Deb Package Installer.",
    license="GPLv3",
    keywords="deb package installer",
    url="https://github.com/newmbk0/xubuntu-package-installer",
)
