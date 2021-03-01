  if rna_sequence:
        seq=rna_sequence.upper()
        trans=[]
        start_code='AUG'
        remain=len(seq)%3
        start_sit=re.search(start_code, rna_sequence)
        for sit in range(0,(len(seq)-remain),3):
            if sit=='AUG':
                continue:
                for i in range (sit.end(),(len(seq)-remain),3)
                codon=genetic_code[seq[i:i+3]]
                trans,append(coden)
                break:
            

            else:
                return []
