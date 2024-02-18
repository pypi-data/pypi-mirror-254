#!/usr/bin/env python3

import nbformat as nbf
from pathlib import Path
from datetime import datetime

nb = nbf.v4.new_notebook()
nb['cells'] = []

date_time = datetime.now()


jupyter = Path(snakemake.output.qmd_by_sample)
name_jupyter = jupyter.stem
dir_jupyter = jupyter.parent
jupyter = jupyter.resolve().as_posix()

header = """---
format: 
  html:
    code-fold: false
    toc: true
    toc-depth: 4
    toc-expand: 2
jupyter: python3
execute: 
  echo: false
  warning: false
  message: false
  error: false
  cache: false
  output: asis
filters:
   - lightbox
lightbox:
  match: auto
  effect: fade
  loop: false
---
"""

nb['cells'].append(nbf.v4.new_markdown_cell(header))

import_packages = """
import pandas as pd
from pathlib import Path
from itables import init_notebook_mode, show
import itables.options as opt
opt.columnDefs = [{"className": "dt-center", "targets": "_all"}]
opt.style = "table-layout:auto;width:auto;margin:auto;caption-side:bottom;float:left"
opt.showIndex = False
init_notebook_mode(all_interactive=False)
# round to two decimal places in python pandas 
pd.options.display.float_format = '{:.2f}'.format
"""

nb['cells'].append(nbf.v4.new_code_cell(import_packages))

# START REPORT

text = f"""
# {snakemake.params.sample_name}
"""

nb['cells'].append(nbf.v4.new_markdown_cell(text))

# BENCHMARK

title_benchmark = f"""
## Benchmark time

Time used (in seconds) to execute activated tools in this pipeline.  

"""

nb['cells'].append(nbf.v4.new_markdown_cell(title_benchmark))

benchmark_table = f"""

# create a sample DataFrame
df = pd.read_csv('{snakemake.input.bench_list[0]}', index_col=[0,1], header=0)
df.sort_values(by=df.columns[0], axis=0, inplace=True)

# print the DataFrame
S = df.style.format(precision=2)
S.background_gradient(axis=None, cmap="YlOrRd")
opt.showIndex = True
show(S, dom="lfr", paging=False, classes="display cell-border", scrollCollapse=True, scrollX=True)
opt.showIndex = False
"""

nb['cells'].append(nbf.v4.new_code_cell(benchmark_table))

# STAT ASSEMBLY

title_stat = f"""
## Statistics

Useful global statistics to compare assemblies obtained at each step of this pipeline for the whole of samples.
- **Sequence_count**  is the number of contigs. 
- **GC content** is the percentage of GC nucleic bases.
- **Longest** is the longest contig assembled.
- **Shortest** is the shortest contig assembled.
- **Mean** : is the sum of the lenght of contigs divised by the number of contigs.
- **Median** : the median is the value separating the higher half from the lower half of contigs.
- **Total_bps** : Total bases number into contigs.
- **Ln** : n=10,n=20,n=30, n=40,n=50 : minimun number of contigs that produces n % of the bases
- **Nn** : n=10,n=20,n=30, n=40,n=50 : length of the contig for which longer length contigs cover at least n % of the assembly

"""

nb['cells'].append(nbf.v4.new_markdown_cell(title_stat))

stat_table = f"""
# create a sample DataFrame
df = pd.read_csv('{snakemake.input.stats_assembly[0]}', index_col=False, header=0)
df.sort_values(by=df.columns[0], axis=0, inplace=True)

# print the DataFrame
S = df.style.format(precision=2)
S.background_gradient(axis=0, cmap="coolwarm")
show(S, dom="lftr",paging=False, classes="display compact cell-border", scrollCollapse=True, scrollX=True)


"""

nb['cells'].append(nbf.v4.new_code_cell(stat_table))

# BUSCO

if "busco_stats" in snakemake.input.keys():
    title_busco = f"""
## BUSCO

BUSCO sets are collections of orthologous groups with near-universally-distributed single-copy genes in each species
    """

    nb['cells'].append(nbf.v4.new_markdown_cell(title_busco))

    busco_table = f"""
    # create a sample DataFrame
    df = pd.read_csv('{snakemake.input.busco_stats[0]}', index_col=False, header=0)
    df.sort_values(by=df.columns[0], axis=0, inplace=True)

    # print the DataFrame
    S = df.style.format(precision=2)
    S.background_gradient(axis=0, cmap="YlOrRd")
    show(S, dom="lfr", paging=False, classes="display compact cell-border", scrollCollapse=True, scrollX=True)


    """

    nb['cells'].append(nbf.v4.new_code_cell(busco_table))


## BLOBTOOLS
if "blob_files" in snakemake.input.keys():
    blobresult = """
## Blobtools
    
    """
    assembler_found = []
    for blob_file in snakemake.input.blob_files:
        assembler = Path(f"{blob_file}").stem.split("_")[1]
        quality_step = '_'.join(Path(f"{blob_file}").stem.split("_")[2:])
        path = Path(f"{blob_file}").parent
        read_cov = path.joinpath("read_cov.png").as_posix()
        blob = path.joinpath("blob.png").as_posix()
        newblob = dir_jupyter.joinpath(f'blob_{assembler}_{quality_step}.png')
        newreadcov = dir_jupyter.joinpath(f'read_cov_{assembler}_{quality_step}.png')
        if not newblob.exists():
            newblob.symlink_to(blob)
        if not newreadcov.exists():
            newreadcov.symlink_to(read_cov)
        if assembler not in assembler_found:
            blobresult = f"{blobresult}\n### {assembler} \n\n"
            assembler_found.append(assembler)
        blobresult = f"{blobresult}\n\n\n#### {quality_step}\n\n"
        blobresult = f"""{blobresult}
![thumbnail]({newblob.name}){{width='48%' group='{newblob.name}'}}
![thumbnail]({newreadcov.name}){{width='48%' group='{newreadcov.name}'}}\n\n"""


    nb['cells'].append(nbf.v4.new_markdown_cell(blobresult))

## ASSEMBLYTICS
if "assemblytics_files" in snakemake.input.keys():
    assemblyticsresults = """
## Assemblytics
    
blablabla assemblytics blabla rules ...pouet 
    """
    zip_list = zip(snakemake.input.assemblytics_dotplot, snakemake.input.assemblytics_Nchart, snakemake.input.assemblytics_log_all_sizes)
    assembler_found = []
    for dotplot, nchart, log_size in zip_list:
        assembler = Path(f"{dotplot}").stem.split("__")[1]
        quality_step = '_'.join(Path(f"{dotplot}").stem.split("__")[2:])
        quality_step = quality_step.split(".")[0]
        
        newdotplot = dir_jupyter.joinpath(Path(f"{dotplot}").name)
        if not newdotplot.exists():
            newdotplot.symlink_to(dotplot)
        newNchart = dir_jupyter.joinpath(Path(f"{nchart}").name)
        if not newNchart.exists():
            newNchart.symlink_to(nchart)
        newLogsize = dir_jupyter.joinpath(Path(f"{log_size}").name)
        if not newLogsize.exists():
            newLogsize.symlink_to(log_size)
        
        if assembler not in assembler_found:
            assemblyticsresults = f"{assemblyticsresults}\n### {assembler} \n\n"
            assembler_found.append(assembler)
        assemblyticsresults = f"{assemblyticsresults}\n\n\n#### {quality_step}\n\n"
        assemblyticsresults = f"""
{assemblyticsresults}\n
![thumbnail]({newdotplot.name}){{width='48%' group='{newdotplot.name}'}}
![thumbnail]({newNchart.name}){{width='48%' group='{newdotplot.name}'}}
![thumbnail]({newLogsize.name}){{width='48%' group='{newdotplot.name}'}}
![thumbnail]({newreadcov.name}){{width='48%' group='{newdotplot.name}'}}\n\n"""

    nb['cells'].append(nbf.v4.new_markdown_cell(assemblyticsresults))

# FLAGSTATS

if "flagstats_stats" in snakemake.input.keys():
    title_flagstat = f"""
## Flagstats

SAMTOOLS FLAGSTATS was used to calculate remapping between illumina reads and each last assembler.
    """

    nb['cells'].append(nbf.v4.new_markdown_cell(title_flagstat))

    flagstat_table = f"""
    # create a sample DataFrame
    df = pd.read_csv('{snakemake.input.flagstats_stats[0]}', index_col=False, header=0)
    df.sort_values(by=df.columns[0], axis=0, inplace=True)

    # print the DataFrame
    S = df.style.format(precision=2)
    show(S, dom="lfr", paging=False, classes="display compact cell-border", scrollCollapse=True, scrollX=True)

    """

    nb['cells'].append(nbf.v4.new_code_cell(flagstat_table))


# MERQURY

if "merqury_files" in snakemake.input.keys():
    title_merqury = f"""
## MERQURY

MERQURY : Overall k-mer evaluation is performed using the k-mer multiplicity of illumina WGS reads
    """

    nb['cells'].append(nbf.v4.new_markdown_cell(title_merqury))

    merqury_table = f"""
    # create a sample DataFrame
    df = pd.read_csv('{snakemake.input.merqury_files[0]}', index_col=False, sep="\t", header=None, names=['Assembly','mapped_kmer', 'all_kmers', 'QV', 'error_rate'])
    df.sort_values(by=df.columns[0], axis=0, inplace=True)

    # print the DataFrame
    S = df.style.format(precision=2)
    show(S, dom="r", paging=False, classes="display compact cell-border", scrollCollapse=True, scrollX=True)


    """

    nb['cells'].append(nbf.v4.new_code_cell(merqury_table))

if "quast_file" in snakemake.input.keys():
    title_quast = f"""
## QUAST

QUAST is a good starting point to help evaluate the quality of assemblies. It provides many helpful contiguity statistics.
    """

    nb['cells'].append(nbf.v4.new_markdown_cell(title_quast))

    quast_path_file = Path(snakemake.input.quast_file[0])
    new_quast_file = dir_jupyter.joinpath(quast_path_file.name)
    if not new_quast_file.exists():
        new_quast_file.symlink_to(quast_path_file)
    quast_link = f'''
{quast_path_file}
{new_quast_file}

[Open QUAST report on new window ...]({new_quast_file.name}){{target="_blank"}}
    '''

    nb['cells'].append(nbf.v4.new_markdown_cell(quast_link))

## write to file

with open(jupyter, 'w') as f:
    nbf.write(nb, f)
