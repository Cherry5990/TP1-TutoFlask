#>>>import random, string, os
#>>>"".join([random.choice(string.printable) for _ in os.urandom(24) ] )

import os

SECRET_KEY = "2lzUl{$*D6#`8uXqlU."
ABOUT = "Bienvenue sur la page à propos de Flask !"
CONTACT = "Voici mon contact : pommedeterre@exemple.fr"

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'monApp.db')