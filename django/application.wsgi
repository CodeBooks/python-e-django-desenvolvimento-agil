#!/usr/bin/env python

import os
import sys
import site

from os.path import abspath, join, dirname

# Nome do nosso projeto
project_name = "gerenciador"

# Diretorio raiz do ambiente virtualenv
root_dir = abspath(join(dirname(__file__), '..'))

# Ajusta o sys.path para encontrar os
# modulos das bibliotecas Python e da
# nossa aplicacao.
python_version = sys.version_info[:2] 
site_dir = 'lib/python%s.%s/site-packages' % python_version 
site.addsitedir(join(root_dir, site_dir))
sys.path.append(root_dir)
sys.path.append(join(root_dir, project_name))
  
# Configura e executa a aplicacao.
os.environ['DJANGO_SETTINGS_MODULE'] = project_name + '.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
