from pathlib import Path

DOCS = "https://culebront-pipeline.readthedocs.io/en/latest/"
GIT_URL = "https://forge.ird.fr/diade/culebront_pipeline"

SINGULARITY_URL_FILES = [('oras://registry.forge.ird.fr/diade/culebront_pipeline/apptainer/apptainer.culebront_tools.sif:0.0.1',
                          f'INSTALL_PATH/containers/apptainer.culebront_tools.sif')
                         ]

DATATEST_URL_FILES = ("https://itrop.ird.fr/culebront_utilities/Data-Xoo-sub.zip", "Data-Xoo-sub.zip")


AVAIL_ASSEMBLY = ("CANU", "FLYE", "MINIASM", "RAVEN", "SMARTDENOVO", "SHASTA")
AVAIL_CORRECTION = ("MEDAKA", "PILON")
AVAIL_POLISHING = ("RACON")
AVAIL_QUALITY = ("BUSCO", "QUAST", "BLOBTOOLS", "ASSEMBLYTICS", "FLAGSTATS", "MERQURY")

ALLOW_FASTQ_EXT = (".fastq", ".fq", ".fq.gz", ".fastq.gz")

