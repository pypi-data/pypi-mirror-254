import subprocess
import os

def prior_install(path):
    subprocess.run(['wget', '-O', '{}/Prior/Opn_median_mm9.bed'.format(path),
                    'https://github.com/SUwonglab/PECA/raw/master/Prior/Opn_median_mm9.bed'])