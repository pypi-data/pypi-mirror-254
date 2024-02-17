import subprocess
import os

def prior_install():
    path = os.path.dirname(scPECA.__file__)
    subprocess.run(['wget', '-O', './Prior/Opn_median_mm9.bed',
                    'https://github.com/SUwonglab/PECA/raw/master/Prior/Opn_median_mm9.bed'])