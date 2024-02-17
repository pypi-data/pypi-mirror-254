import subprocess
import os

def prior_install(path):
    subprocess.run(['mkdir','{}/Prior'.format(path)])
    subprocess.run(['wget','-O','{}/Prior/Opn_median_mm9.bed'.format(path),'https://github.com/SUwonglab/PECA/raw/master/Prior/Opn_median_mm9.bed'])
    subprocess.run(['wget','-O','{}/Prior/Opn_median_mm10.bed'.format(path),'https://github.com/SUwonglab/PECA/raw/master/Prior/Opn_median_mm10.bed'])
    subprocess.run(['wget','-O','{}/Prior/Opn_median_hg19.bed'.format(path),'https://github.com/SUwonglab/PECA/raw/master/Prior/Opn_median_hg19.bed'])
    subprocess.run(['wget','-O','{}/Prior/Opn_median_hg38.bed'.format(path),'https://github.com/SUwonglab/PECA/raw/master/Prior/Opn_median_hg38.bed'])
    subprocess.run(['wget','-O','{}/Prior/RE_gene_corr_mm9.bed'.format(path),'https://github.com/SUwonglab/PECA/raw/master/Prior/RE_gene_corr_mm9.bed'])
    subprocess.run(['wget','-O','{}/Prior/RE_gene_corr_mm10.bed'.format(path),'https://github.com/SUwonglab/PECA/raw/master/Prior/RE_gene_corr_mm10.bed'])
    subprocess.run(['wget','-O','{}/Prior/RE_gene_corr_hg19.bed'.format(path),'https://github.com/SUwonglab/PECA/raw/master/Prior/RE_gene_corr_hg19.bed'])
    subprocess.run(['wget','-O','{}/Prior/RE_gene_corr_hg38.bed'.format(path),'https://github.com/SUwonglab/PECA/raw/master/Prior/RE_gene_corr_hg38.bed'])
    subprocess.run(['wget','-O','{}/Prior/TFTG_corr_mouse.mat'.format(path),'https://github.com/SUwonglab/PECA/raw/master/Prior/TFTG_corr_mouse.mat'])
    subprocess.run(['wget','-O','{}/Prior/TFTG_corr_human.mat'.format(path),'https://github.com/SUwonglab/PECA/raw/master/Prior/TFTG_corr_human.mat'])
    