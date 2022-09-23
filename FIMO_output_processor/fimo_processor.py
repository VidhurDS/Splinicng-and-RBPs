
def fimo_out_parser(file_name, sample_tag):
    hek_file = file_name
    with open(hek_file, "r") as ins:
        hek = ins.readlines()    # ins.readlines()[1:] if header
    ins.close()

    hek_outfile = open(sample_tag + "_RBP_frequency.tsv", 'w')
    freq_dict = {}

    for line in hek[1:]:
        line = line.strip()
        elements = line.split("\t")
        if len(elements) > 7 and float(elements[7]) <= 0.05:
            gene_name = elements[0].split(".")[0]
            if "_readdb" in gene_name:
                gene_name = gene_name.replace('_readdb', '')
            if gene_name in freq_dict:
                freq_dict[gene_name] += 1
            else:
                freq_dict[gene_name] = 1

    hek_outfile.write("RBP\tNumber_of_significant_predictions\n")

    sorted_freq_dict = sorted(freq_dict.items(), key=lambda kv: kv[1], reverse=True)

    for k in sorted_freq_dict:
        print(k)
        hek_outfile.write(k[0] + "\t" + str(k[1]) + "\n")

    hek_outfile.close()


fimo_out_parser("MCF7_MALAT1_KO_fimo_out.tsv", "MCF7_MALAT1_KO")
fimo_out_parser("MCF7_500_MALAT1_KO_fimo_out.tsv", "MCF7_500_MALAT1_KO")
fimo_out_parser("HEK293T_MALAT1_KO_fimo_out.tsv", "HEK293T_MALAT1_KO")
fimo_out_parser("HEK293T_500_MALAT1_KO_fimo_out.tsv", "HEK293T_500_MALAT1_KO")

