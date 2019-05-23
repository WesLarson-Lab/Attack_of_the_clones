#Last Edit: 7/5/2018, Matthew Bootsma
#Built to work with Stacks 2.0b
#####MAKE SURE TO CHANGE THE INPUT FILE TO MATCH OUTPUT NAMES
#####MAKE SURE TO CHANGE NAMES OF OUTPUT FILES DEPENDING ON THE DATA SET (e.g. CF vs NO_CF) 
#####   lines: 15, 84, 139
# script parse vcf file get alleles per individual
import os

os.getcwd()
os.chdir("E:/raw_data_files/cisco/192_inds_snp_dev_5_3_17/stacks/U/Stacks_7-7-18")
# open vcf file read all lines into an array, close file
raw_vcf_file = open("CF/populations_batch1/r25/populations.snps.vcf", "r")
raw_vcf_array = raw_vcf_file.readlines()
raw_vcf_file.close()

# open file you are going to write new GENOTYPE CALL results to
out_file = open("CF_b1_r25_parsed_genotype_calls.txt", "w")
r = 1
# for each line in vcf file
for i in raw_vcf_array:
    # this is trying to recognize the header line
    if i.startswith("#CHROM"):

        # hard code column names you want
            out_file.write(
            "Chrom" + "\t" + "ID" + "\t" + "REF1" + "\t" + "REF2" + "\t" + "Num Samples W/ Data" + "\t" + "Allele Frequency" + "\t" + "delete_col" + "\t")
            header_line = i.rstrip().split("\t")
            # grabbing individual names
            z = 0
            for j in header_line:
                z = z + 1                
                if z > 9 and z < len(header_line)+1:
                    out_file.write(j + "\t")                 
                #else: out_file.write(j)

            out_file.write("\n")
            # at this point we should have header line

    # use the if not # to go to the data
    elif "#" not in i:
        # splits each thing into their respective cells by tabs
        split_ind_line = i.rstrip().split("\t")
        split_info_line = split_ind_line[7].split(";")
        # outputs locus name, you're going to need to output stuff from other columns too
        out_file.write(split_ind_line[0] + "\t" + split_ind_line[1] + "\t" + split_ind_line[3] + "\t" + split_ind_line[4] + "\t")
        out_file.write(split_info_line[0] + "\t" + split_info_line[1] + "\t")
        # iterates through individuals
        z = 0
        for j in split_ind_line:
            #print j
            z = z + 1
            #print z
            if z > 8:
                # split the genotype cell
                gen_data = j.split(":")
                #print gen_data[0]
                # call zygosity based
                # "0" = homo1
                # "1" = Het
                # "2"= homo2
                # "9" = no data
                zygosity = gen_data[0]
                if zygosity == "0/0":
                    genotype_to_print = "0"
                elif zygosity == "0/1":
                    genotype_to_print = "1"
                elif zygosity == "1/1":
                    genotype_to_print = "2"
                else:
                    genotype_to_print = "9"

                # print out the genotype
                out_file.write(genotype_to_print + "\t")


        out_file.write("\n")


out_file.close()  # script parse vcf file get alleles per individual
####
####
# open file you are going to write new READ COUNT results to
out_file = open("CF_b1_r25_parsed_read_depth.txt", "w")
r = 1
# for each line in vcf file
for i in raw_vcf_array:
    # this is trying to recognize the header line
    if i.startswith("#CHROM"):

        # hard code column names you want
            out_file.write(
            "Chrom" + "\t" + "ID" + "\t" + "REF1" + "\t" + "REF2" + "\t" + "Num Samples W/ Data" + "\t" + "Allele Frequency" + "\t"+ "delete_col" + "\t")
            header_line = i.rstrip().split("\t")
            # grabbing individual names
            z = 0
            for j in header_line:
                z = z + 1                
                if z > 9 and z < len(header_line)+1:
                    out_file.write(j + "\t")                 
                #else: out_file.write(j)

            out_file.write("\n")
            # at this point we should have header line

    # use the if not # to go to the data
    elif "#" not in i:
        # splits each thing into their respective cells by tabs
        split_ind_line = i.rstrip().split("\t")
        split_info_line = split_ind_line[7].split(";")
        # outputs locus name, you're going to need to output stuff from other columns too
        out_file.write(split_ind_line[0] + "\t" + split_ind_line[1] + "\t" + split_ind_line[3] + "\t" + split_ind_line[4] + "\t")
        out_file.write(split_info_line[0] + "\t" + split_info_line[1] + "\t")
        # iterates through individuals
        z = 0
        for j in split_ind_line:
            #print j
            z = z + 1
            gen_data = j.split(":")
            #print z
            if z > 8:
                # split the genotype cell
                if len(gen_data) == 1:
                    #print(gen_data[0])
                    read_number_to_write = "0"
                else:
                    read_number_to_write = gen_data[1]
                    #print(gen_data[1])
                # print out the genotype
                out_file.write(read_number_to_write + "\t")


        out_file.write("\n")


out_file.close()  # script parse vcf file get alleles per individual

# open file you are going to write new READ COUNT results to
out_file = open("CF_b1_r25_parsed_reads_per_allele.txt", "w")
r = 1
# for each line in vcf file
for i in raw_vcf_array:
    # this is trying to recognize the header line
    if i.startswith("#CHROM"):

        # hard code column names you want
            out_file.write(
            "Chrom" + "\t" + "ID" + "\t" + "REF1" + "\t" + "REF2" + "\t" + "Num Samples W/ Data" + "\t" + "Allele Frequency" + "\t"+ "delete_col" + "\t")
            header_line = i.rstrip().split("\t")
            # grabbing individual names
            z = 0
            for j in header_line:
                z = z + 1                
                if z > 9 and z < len(header_line)+1:
                    out_file.write(j + "\t")                 
                #else: out_file.write(j)

            out_file.write("\n")
            # at this point we should have header line

    # use the if not # to go to the data
    elif "#" not in i:
        # splits each thing into their respective cells by tabs
        split_ind_line = i.rstrip().split("\t")
        split_info_line = split_ind_line[7].split(";")
        # outputs locus name, you're going to need to output stuff from other columns too
        out_file.write(split_ind_line[0] + "\t" + split_ind_line[1] + "\t" + split_ind_line[3] + "\t" + split_ind_line[4] + "\t")
        out_file.write(split_info_line[0] + "\t" + split_info_line[1] + "\t")
        # iterates through individuals
        z = 0
        for j in split_ind_line:
            #print j
            z = z + 1
            gen_data = j.split(":")
            #print z
            if z > 8:
                # split the genotype cell
                if len(gen_data) == 1:
                    #print(gen_data[0])
                    read_number_to_write = "0,0"
                else:
                    read_number_to_write = gen_data[2]
                    #print(gen_data[1])
                # print out the genotype
                out_file.write(read_number_to_write + "\t")


        out_file.write("\n")


out_file.close()  # script parse vcf file get alleles per individual