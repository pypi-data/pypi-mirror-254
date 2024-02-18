#!/usr/bin/env python3
from pathlib import Path

# get samples_qmd list
samples_list = snakemake.input.list_sample_qmd
samples_list_for_txt = []
for sample in samples_list:
    file = Path(sample).name
    parent = Path(sample).parent.name
    sample_txt = f'        - {parent}/{file}\n'
    samples_list_for_txt.append(sample_txt)
sample_txt_list = "".join(samples_list_for_txt).rstrip("\n")


quarto_conf_in = Path(snakemake.input.quarto)
with open(quarto_conf_in, "r") as input_conf:
    conf_txt = input_conf.read()

output_dir = snakemake.params.out_dir
conf_txt = conf_txt.replace("OUTPUT_DIR", output_dir)
conf_txt = conf_txt.replace("        SAMPLE", sample_txt_list)

quarto_conf_out = Path(snakemake.output.quarto_conf)
with open(quarto_conf_out, "w") as out_conf:
    out_conf.write(conf_txt)

