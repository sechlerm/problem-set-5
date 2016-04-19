#! usr/bin/env python


import pybedtools

from collections import defaultdict, Counter

filename = '/Users/marybethsechler/Desktop/GAW/data-sets/bed/lamina.bed'
genes=pybedtools.BedTool(filename)


#what chromosome has the region with the largest start position
#in ipython, for each line- type record. and hit TAB to see all the data identifiers-thats where we got record.chrom from


large_start = 0
for record in genes:
     
    if record.start > large_start:
        large_start = record.start
        chrom = record.chrom

print 'answer 1.1-', chrom 


# what is the region with the largets end position on chrY?

largest_end = 0
for record in genes:
    if record.chrom == "chrY":
        if record.end > largest_end:
            largest_end = record.end
            chrom = record.chrom
            start = record.start
print 'answer 1.2-', chrom, ':', start, '-', largest_end 
    




#problem 2- parse a FQ file. if you open file and go over line by line. line1 = name, 2 = sequence 3= empty line and 4 = quality scores. use the modulo % to keep track of which line/ record you are on,

filename = '/Users/marybethsechler/Desktop/GAW/data-sets/fastq/SP1.fq'


import ipdb

def sum_quals(qual):
    qualsum= 0
    for char in qual:
        qualsum += ord(char)
    return qualsum

def complement(seq):
    comps = []
    for char in seq:
        if char == 'A':
            comps.append('T')
        elif char == 'G': 
            comps.append('C')
        elif char == 'C':
            comps.append('G')
        elif char == 'T':
            comps.append('A')
    return comps

def parse_fastq(filename):
    line_num = 0    
    for line in open(filename):
        line_type = line_num % 4

        if line_type == 0:
            name = line.strip()
        elif line_type == 1:
            seq = line.strip()
            compstring = complement(seq)
        #        print compstring
            revcomp = ''.join(reversed(compstring))
#            print revcomp
        elif line_type == 3:
            quals = line.strip()
            qual_sum = sum_quals(quals)
            
       
            yield name, seq, revcomp, quals, qual_sum
        
        line_num += 1
        
  




num_records = 0
Ccounts = 0
for name, seq, revcomp, quals, qual_sum in parse_fastq(filename):

    if num_records <= 9:
        counts=Counter(seq)
        if counts['C'] > Ccounts:
            Ccounts = counts['C']
            recname = name
    num_records += 1
print 'answer 2.1-', recname, 'number of Cs=', Ccounts


big_qualsum = 0
for name, seq, revcomp, quals, qual_sum in parse_fastq(filename):
    if qual_sum > big_qualsum:
        big_qualsum = qual_sum
        bigname = name
        bigseq = seq
        bigquals = quals

print 'answer 2.2-', big_qualsum

num_records = 0
for name, seq, revcomp, quals, qual_sum in parse_fastq(filename):
    if num_records <= 9:
        print 'answer 2.3-', num_records + 1, revcomp
    num_records += 1

'''

#another useful counter- from collections import Counter, if seq = CACTGCATGCATGC then Counter(seq) will output the number of each character. to get the number out counts = Counter(seq), then call counts['C'] and it will output the number

#ord('a'), ordinal value ord returns integer value of a one character string. build a function that takes on input a string of characters, evaluates the ordinal value of each character and then 


#reverse compliment
'''
