# ======================== Gene Set Enrichment Analysis ==========================
# Go and KEGG
Gene list: ./gene_list.txt
Gene set: MSigDB_Hallmark_2020, KEGG_2021_Human

# Prerank
rnk file:. /temp.rnk
Gene sets: KEGG_2016,. /temp.rnk

# GSEA
data: ./P53_resampling_data.txt
Gene set: ./h.all.v7.0.symbols.gmt
class: ./P53.cls

# ssGSEA
data: ./Leukemia_hgu95av2.trim2.txt
Gene set: ./h.all.v7.0.symbols.gmt

# GSVA
data: ./Leukemia_hgu95av2.trim2.txt
Gene set: ./h.all.v7.0.symbols.gmt

# ================================= Plotting ===================================== 
# dotplot
Input File: ./KEGG_2021_Human.Human.enrichr.reports.txt
column: Adjusted P-value
x: Gene_set
title: KEGG
Output File: kegg_test.png

# barplot
Input File: ./KEGG_2021_Human.Human.enrichr.reports.txt
column: Adjusted P-value
group: Gene_set
title: KEGG
Output File: kegg_test_2.png

# heatmap
Input File: ./gsea_heatmap_matrix.csv
Report File: ./gseapy.phenotype.gsea.report.csv