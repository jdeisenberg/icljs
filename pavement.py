import paver
from paver.easy import *
import paver.setuputils
paver.setuputils.install_distutils_tasks()
import os, sys

from sphinxcontrib import paverutils

sys.path.append(os.getcwd())

updateProgressTables = True
try:
    from runestone.server.chapternames import populateChapterInfob
except ImportError:
    updateProgressTables = False

home_dir = os.getcwd()
master_url = 'http://127.0.0.1:8000'
master_app = 'runestone'
serving_dir = "./build/cljsbook"
dest = "../../static"


options(
    sphinx = Bunch(docroot=".",),

    build = Bunch(
        builddir="./build/cljsbook",
        sourcedir="_sources",
        outdir="./build/cljsbook",
        confdir=".",
        project_name = "cljsbook",
        template_args={'course_id': 'cljsbook',
                       'login_required':'false',
                       'appname':master_app,
                       'loglevel': 0,
                       'course_url':master_url,
                       'use_services': 'true',
                       'python3': 'true',
                       'dburl': '',
                       'basecourse': 'cljsbook'
                        }
    )
)

from runestone import build  # build is called implicitly by the paver driver.

