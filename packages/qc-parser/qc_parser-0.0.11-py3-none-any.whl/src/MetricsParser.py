import sys
from src.metrics_to_extract import metrics, SAMTOOLS_STATS, BAMSTATS, RNASEQQC, PICARD_COLLECT_ALIGNMENT_SUMMARY_METRICS, PICARD_COLLECT_INSERT_SIZE_METRICS, PICARD_COLLECT_WGS_METRICS, FASTQC
from src.QMGeneric import QMValue
from typing import List
import json


class Parser:

    def __init__(self, tool: str, metrics_file: str):

        self.tool = tool
        self.path = metrics_file

    def parse(self):

        if self.tool == SAMTOOLS_STATS:
            return self.parse_samtools_stats()
        elif self.tool == PICARD_COLLECT_ALIGNMENT_SUMMARY_METRICS:
            return self.parse_picard_CollectAlignmentSummaryMetrics()
        elif self.tool == PICARD_COLLECT_INSERT_SIZE_METRICS:
            return self.parse_picard_CollectInsertSizeMetrics()
        elif self.tool == PICARD_COLLECT_WGS_METRICS:
            return self.parse_picard_CollectWgsMetrics()
        elif self.tool == RNASEQQC:
            return self.parse_rnaseqqc()
        elif self.tool == BAMSTATS:
            return self.parse_bamstats()
        elif self.tool == FASTQC:
            return self.parse_fastqc()
        else:
            sys.exit(
                f"{self.tool} is not supported. Please add a parser to Parser.py")

    def parse_samtools_stats(self) -> List[QMValue]:
        qm_values = []
        # Parse file and save values
        with open(self.path) as fi:
            for line in fi:
                if line.startswith('SN'):
                    line = line.rstrip().split('\t')
                    field, value = line[1].replace(':', ''), line[2]
                    if field in metrics[SAMTOOLS_STATS]:
                        m = metrics[SAMTOOLS_STATS][field]
                        value_cast = self.safe_cast(value, m["type"])
                        if value_cast == None:
                            continue
                        qmv = QMValue(
                            m["key"], value_cast, tooltip=m["tooltip"], derived_from=m["derived_from"])
                        qm_values.append(qmv)
        return qm_values

    def parse_bamstats(self) -> List[QMValue]:
        qm_values = []
        # Parse file and save values
        fi = open(self.path)
        bamstats_res = json.load(fi)
        for key in bamstats_res.keys():
            if key in metrics[BAMSTATS]:
                m = metrics[BAMSTATS][key]
                value = bamstats_res[key]
                value_cast = self.safe_cast(value, m["type"])
                if value_cast == None:
                    continue
                qmv = QMValue(
                    m["key"], value_cast, tooltip=m["tooltip"], derived_from=m["derived_from"])
                qm_values.append(qmv)
        fi.close()
        return qm_values

    def parse_fastqc(self) -> List[QMValue]:
        qm_values = []
        # Parse file and save values
        with open(self.path) as fi:
            for line in fi:
                value, field, _ = line.rstrip().split('\t')
                if field in metrics[FASTQC]:
                    m = metrics[FASTQC][field]
                    value_cast = self.safe_cast(value, m["type"])
                    qmv = QMValue(
                        m["key"], value_cast, tooltip=m["tooltip"], derived_from=m["derived_from"])
                    qm_values.append(qmv)
        return qm_values

    def parse_rnaseqqc(self) -> List[QMValue]:
        # TODO
        return

    def parse_picard_CollectAlignmentSummaryMetrics(self) -> List[QMValue]:
        qm_values = []
        header, pair, unpair = [], [], []
        with open(self.path) as fi:
            for line in fi:
                if line.startswith('CATEGORY'):
                    header = line.rstrip().split('\t')
                elif line.startswith('PAIR'):
                    pair = line.rstrip().split('\t')
                elif line.startswith('UNPAIRED'):
                    unpair = line.rstrip().split('\t')

        # Check for both PAIR and UNPAIRED -> ERROR
        if pair and unpair:
            sys.exit(
                f"Paired-end BAM file contains unpaired reads")
        elif unpair:
            pair = unpair

        for i, field in enumerate(header):
            if field in metrics[PICARD_COLLECT_ALIGNMENT_SUMMARY_METRICS]:
                m = metrics[PICARD_COLLECT_ALIGNMENT_SUMMARY_METRICS][field]
                value_cast = self.safe_cast(pair[i], m["type"])
                if value_cast == None:
                    continue
                qmv = QMValue(
                    m["key"], value_cast, tooltip=m["tooltip"], derived_from=m["derived_from"])
                qm_values.append(qmv)
        return qm_values

    def parse_picard_CollectInsertSizeMetrics(self) -> List[QMValue]:
        qm_values = []
        header, pairs, is_block = [], [], False
        with open(self.path) as fi:
            for line in fi:
                line = line.rstrip()
                if line:
                    if line.startswith('## HISTOGRAM'):
                        break
                    elif line.startswith('MEDIAN_INSERT_SIZE'):
                        is_block = True
                        header = line.split('\t')
                    elif is_block:
                        line = line.split('\t')
                        pairs.append(line)

        for pair in pairs:
            orientation = pair[8]
            for i, field in enumerate(header):
                if field in metrics[PICARD_COLLECT_INSERT_SIZE_METRICS]:
                    m = metrics[PICARD_COLLECT_INSERT_SIZE_METRICS][field]
                    value_cast = self.safe_cast(pair[i], m["type"])
                    if value_cast == None:
                        continue
                    qmv = QMValue(
                        m["key"]+f' ({orientation}) [Picard]', value_cast, tooltip=m["tooltip"], derived_from=m["derived_from"])
                    qm_values.append(qmv)
        return qm_values

    def parse_picard_CollectWgsMetrics(self) -> List[QMValue]:
        qm_values = []
        header, stats, is_block = [], [], False
        with open(self.path) as fi:
            for line in fi:
                line = line.rstrip()
                if line:
                    if line.startswith('## HISTOGRAM'):
                        break
                    elif line.startswith('GENOME_TERRITORY'):
                        is_block = True
                        header = line.split('\t')
                    elif is_block:
                        stats = line.split('\t')

        for i, field in enumerate(header):
            if field in metrics[PICARD_COLLECT_WGS_METRICS]:
                m = metrics[PICARD_COLLECT_WGS_METRICS][field]
                value_cast = self.safe_cast(stats[i], m["type"])
                if value_cast == None:
                    continue
                qmv = QMValue(
                    m["key"], value_cast, tooltip=m["tooltip"], derived_from=m["derived_from"])
                qm_values.append(qmv)
        return qm_values

    def safe_cast(self, value, to_type, default=None):
        try:
            return to_type(value)
        except (ValueError, TypeError):
            raise ValueError(f"Value {value} is not of type {to_type}")
