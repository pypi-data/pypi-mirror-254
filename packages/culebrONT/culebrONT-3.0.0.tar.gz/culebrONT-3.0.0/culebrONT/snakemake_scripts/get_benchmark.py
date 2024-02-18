#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import argparse
from pathlib import Path
from collections import OrderedDict
from pprint import pprint as pp
version = "0.0.1"
pd.set_option("display.precision", 2)


class AutoVivification(OrderedDict):
    """
    Implementation of perl's autovivification feature.

    Example:

    >>> a = AutoVivification()
    >>> a[1][2][3] = 4
    >>> a[1][3][3] = 5
    >>> a[1][2]['test'] = 6
    >>> print a
    >>> {1: {2: {'test': 6, 3: 4}, 3: {3: 5}}}

    """

    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value


def main():
    from pprint import pp
    stat_time = snakemake.output.stat_time
    output_dir = Path(snakemake.params.out_dir)
    dico_benchmark_time = AutoVivification()

    for bench_file in snakemake.input["assembly_list"]:
        bench_file_path = Path(bench_file)
        assembler = bench_file_path.stem
        df = pd.read_csv(bench_file, sep="\t")
        dico_benchmark_time["STEP-ASSEMBLERS"][f"ASSEMBLERS"][assembler] = f'{df["s"][0]:.2f}'
     
        # check if MINIASM to load MINIASM_MINIPOLISH file
        if assembler in ("MINIASM"):
            df = pd.read_csv(f"{output_dir}/BENCHMARK/ASSEMBLER/MINIASM_MINIPOLISH.txt", sep="\t")
            df2 = pd.read_csv(f"{output_dir}/BENCHMARK/ASSEMBLER/MINIMAP4MINIASM.txt", sep="\t")
            dico_benchmark_time["STEP-ASSEMBLERS"][f"MINIMAP"][assembler] = f'{df2["s"][0]:.2f}'
            dico_benchmark_time["STEP-ASSEMBLERS"][f"MINIPOLISH"][assembler] = f'{df["s"][0]:.2f}'
        
        # check if SMARTDENOVO to load FASTQ2FASTA file
        if assembler in ("SMARTDENOVO", "SHASTA"):
            df = pd.read_csv(f"{output_dir}/BENCHMARK/ASSEMBLER/FASTQ2FASTA.txt", sep="\t")
            dico_benchmark_time["STEP-ASSEMBLERS"][f"FASTQ2FASTA"][assembler] = f'{df["s"][0]:.2f}'

    if "polishers_list" in snakemake.input.keys():
        for bench_file in snakemake.input["polishers_list"]:
            bench_file_path = Path(bench_file)
            assembler, polisher = bench_file_path.stem.split("_")
            df = pd.read_csv(bench_file, sep="\t")
            dico_benchmark_time["STEP-POLISHER"][f"{polisher}"][assembler] = f'{df["s"][0]:.2f}'
    if "correction_list" in snakemake.input.keys():
        for bench_file in snakemake.input["correction_list"]:
            bench_file_path = Path(bench_file)
            assembler = bench_file_path.stem
            corrector = bench_file_path.parent.stem
            df = pd.read_csv(bench_file, sep="\t")
            dico_benchmark_time["STEP-CORRECTION"][f"{corrector}"][assembler] = f'{df["s"][0]:.2f}'
    if "correction_list_pilon" in snakemake.input.keys():
        for bench_file in snakemake.input["correction_list_pilon"]:
            bench_file_path = Path(bench_file)
            assembler, corrector = bench_file_path.stem.split("_")
            df = pd.read_csv(bench_file, sep="\t")
            dico_benchmark_time["STEP-CORRECTION"][f"{corrector}"][assembler] = f'{df["s"][0]:.2f}'
         
    df = pd.DataFrame.from_dict(dico_benchmark_time)
    dataframe_benchmark = df.T.stack().apply(pd.Series)
    with open(f"{stat_time}", "w") as benchmark_file:
        with pd.option_context('display.float_format', '{:0.2f}'.format):
        # print(f"dico_benchmark_time:\n{dataframe_benchmark}\n")
            dataframe_benchmark.to_csv(benchmark_file, index=True)


if __name__ == '__main__':
    main()
