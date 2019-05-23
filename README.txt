
###---------Attack of the PCR clones: Rates of clonality have little effect on RAD-seq genotype calls manuscript.-------
Peter T. Euclide, Garrett McKinney, Matthew Bootsma, Charlene Tarsa, Mariah Meek, Wes Larson
# -----------------------------

This folder contains a cleaned up versions of the raw scripts used for data filtering and analysis used in the 
Attack of the PCR clones: Rates of clonality have little effect on RAD-seq genotype calls manuscript.

Parse_populations_stacks-2.py was used to parse VCF files into three seperate files that were then used for all further analysis conducted in R.

Script CF_Log_analysis walks through most of the plots and analysis conducted in Objective 1: Clone summary. nessessary log files used for this script are found in the data folder.

Script 1_locus_selection walks through the process we used to filter all individuals and loci to (see "Locus selection strategy" section of manuscript)

Script 2_genotype_change_analysis walks through some of the figures and analysis presented in Objective 2: Effect of PCR clones on genotype calls.

Scripts for Objective 3: Causes of genotype change are more complex and were conducted in a combination of GTScore and R. Therefore these scripts are avilable upon request only at this time.
for details please contact Peter Euclide peter.euclide@uwsp.edu, or through GitHub https://github.com/peuclide/

Script sumstats_analysis walks through the analysis conducted to compare sumstat outfiles and changes in heterozygosity in Objective 4: Effect of PCR clones on heterozygosity

Files in the run_your_own_data file is a self contained script that takes two VCF files and creates a simple output that showing the proportion of each change type.        