from pandas.io.parsers import read_csv
import wbgapi as wb
import pandas as pd

print(wb.source.info())

wbdata = wb.data.DataFrame(['EG.ELC.ACCS.ZS', "FX.OWN.TOTL.ZS", "SE.PRM.ENRR", "NY.GNP.PCAP.PP.CD", "NY.GDP.MKTP.KD.ZG", "NY.GDP.PCAP.CD", "NY.ADJ.NNAT.GN.ZS", "SH.MED.PHYS.ZS", "SP.DYN.CBRT.IN"],  labels = True)

wbdata.to_csv("wb_output.csv")

