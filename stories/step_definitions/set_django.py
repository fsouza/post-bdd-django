from django.core.management import setup_environ
import os
import sys

abs_path = os.path.dirname(os.path.abspath(__file__))
abs_path = abs_path.replace('stories/step_definitions', '')
sys.path.append(abs_path)

import settings

setup_environ(settings)

