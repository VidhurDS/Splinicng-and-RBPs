hek_file = "HEK293T_spliced_exons.txt"
with open(hek_file, "r") as ins:
    hek = ins.readlines()    # ins.readlines()[1:] if header
ins.close()


mcf_file = "MCF7_spliced_exons.txt"
with open(mcf_file, "r") as ins2:
    mcf = ins2.readlines()  # ins2.readlines()[1:] if header
ins2.close()

hek_outfile = open("HEK293T_MALAT1_KO.bed", 'w')
mcf_outfile = open("MCF7_MALAT1_KO.bed", 'w')

# input: GeneID	geneSymbol	gene_biotype	chr	strand	event	exonStart_0base	exonEnd	Trend
# output: chr chrstart chrend strand cell_line,line_num

hek_bed = []
i = 0
for line in hek[1:]:
    i += 1
    line = line.strip()
    elements = line.split("\t")
    t_str = elements[3]+"\t"+elements[6]+"\t"+elements[7]+"\t"+elements[4]+"\thek_line_"+str(i)+"\n"
    # t_str_d = elements[3]+"\t"+elements[6]+"\t"+elements[7]+"\t"+elements[4]+"\n"
    # hek_bed.append(t_str_d)
    hek_bed.append(t_str)
    hek_outfile.write(t_str)

print(len(hek_bed))
print(len(set(hek_bed)))

# create two bed files for each cell line, one with buffer one without

mcf_bed = []
i = 0
for line in mcf[1:]:
    i += 1
    line = line.strip()
    elements = line.split("\t")
    t_str = elements[3]+"\t"+elements[6]+"\t"+elements[7]+"\t"+elements[4]+"\thek_line_"+str(i)+"\n"
    # t_str_d = elements[3]+"\t"+elements[6]+"\t"+elements[7]+"\t"+elements[4]+"\n"
    # mcf_bed.append(t_str_d)
    mcf_bed.append(t_str)
    mcf_outfile.write(t_str)

print(len(mcf_bed))
print(len(set(mcf_bed)))

# create bed files with 500bp extension


def exon_extender(in_list,out_filehandle):
    # print(in_list[0])
    for line in in_list:
        elements = line.split("\t")
        out_str = elements[0] + "\t" + str(int(elements[1])-500) + "\t" + str(int(elements[2])+500) + "\t" + elements[3] + "\t" + elements[4]
        out_filehandle.write(out_str)
    out_filehandle.close()


hek_500_outfile = open("HEK293T_500_MALAT1_KO.bed", 'w')
exon_extender(hek_bed,hek_500_outfile)

mcf_500_outfile = open("MCF7_500_MALAT1_KO.bed", 'w')
exon_extender(mcf_bed,mcf_500_outfile)

# find number of uniq locations across both cell lines


