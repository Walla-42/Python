# This program is to showcase the programs that I have developed over the past week. This is a complex program that
# demonstrates strings, functions, and imports/exports
# imports for program
from collections import Counter
import sys


# dictionary for functions
def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n - k + 1):
        Pattern = Text[i:i + k]
        freq[Pattern] = 0
        for i in range(n - k + 1):
            if Text[i:i + k] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    return freq


def Frequent_words(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            pattern = key
            words.append(pattern)
    return words


def count_bases_RNA(seq):
    return Counter(seq)


def count_bases_DNA(nuc):
    return Counter(nuc)


def reverse_sequencing(rna_sequence):
    reverse_sequence = rna_sequence.replace('A', 't').replace('U', 'a').replace(
        'G', 'c').replace('C', 'g').upper()
    return reverse_sequence


def reverse_complement_DNA(dna_sequence):
    reverse_complement = dna_sequence.replace('A', 't').replace(
        'T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
    return reverse_complement


def Transcription(dna_sequence):
    mRNA = dna_sequence.replace('A', 'u').replace('T', 'a').replace('C', 'g').replace(
        'G', 'c').upper()
    return mRNA


def translate(seq):
    table = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
             "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
             "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
             "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
             "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
             "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
             "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
             "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
             "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
             "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
             "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
             "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
             "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
             "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
             "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
             "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", }
    protein = ""
    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]
            protein += table[codon]
    return protein


def open_and_parse_fasta(filepath):
    FASTA_file = open(f"{filepath}", "r")
    FASTA_dict = {}
    FASTA_label = ""
    for line in FASTA_file:
        line = line.rstrip()  # removes spaces and newline chars each line
        if line.startswith(">"):  # catches sequence label
            FASTA_label = line[1:]  # set the label as 1st char and after #set sequence label in dict with empty string
            FASTA_dict[FASTA_label] = ""
        else:  # must be sequence #add sequence to end of dict entry
            FASTA_dict[FASTA_label] += line
    return FASTA_dict  # function to count base occurrence and print results


# start of Program


while True:
    Directory = input('what is your file directory?')

    if Directory[-4:] == ".fna":
        Sequence_data = open_and_parse_fasta(Directory)
        break

    elif Directory[-4:] == ".seq":
        Sequence_data = open_and_parse_fasta(Directory)
        break

    # elif Directory[-4:] == ".dna":
    #     Sequence_data = open_and_parse_fasta(Directory)
    #     break

    elif Directory[-4:] == ".txt":
        print('\033[1;31m' + "file type not supported...")
        print('\033[0m')

    else:
        print('\033[1;31m' + "file type not supported, please use another file.\n Supported file types include: .fna , "
                             ".seq , .dna" + '\033[0m')

print('\033[1;33m' + "Sequence Received..." + '\033[0m')

for FASTA_label in Sequence_data:
    print("This is your reference Sequence Name: \n" + '\033[1;32m' + FASTA_label)
    print('\033[0m')
    Header = FASTA_label
Sequence = str(Sequence_data)

while True:
    Sequence_type = input('Is your sequence DNA, or RNA? ')
    if Sequence_type == "DNA":
        break

    elif Sequence_type == "RNA":
        break

    else:
        print('\033[1;31m' + "Please enter a valid response...")
        print('\033[0m')

while True:
    # noinspection PyUnboundLocalVariable
    DNA = Sequence_data.get(Header)
    if Sequence_type == "DNA":
        Work_type = input('Would you like a base count, kmer analysis, transcription, or reverse compliment strand?\n'
                          ' Or would you like to try a new sequence? else type END. \n')

        if (Work_type == "base count" or Work_type == "Base Count"
                or Work_type == "base Count" or Work_type == "Base count"):
            print("This is the count for each base in your sequence:\n " + '\033[1;32m' + str(Counter(DNA)) + '\033[0m')

        elif Work_type == "Kmer Analysis" or Work_type == "kmer Analysis" or Work_type == "kmer analysis":
            k = input('How many bases should be in your pattern? ')
            print('\033[1;33m' + "One moment....processing request" + '\033[0m')
            print("These are the most frequent repeats: " + '\033[1;32m' + str(Frequent_words(DNA, int(k))) + '\033[0m')

        elif Work_type == "transcription" or Work_type == "Transcription":
            RNA = Transcription(DNA)
            line_length = 70
            lines = [RNA[i:i + line_length] + '\n' for i in range(0, len(RNA), line_length)]
            RNA_Complete = ''.join(lines)

            while True:
                Ans = input("Would you like to save this sequence?")

                if Ans == "Yes" or Ans == "yes" or Ans == "YES":
                    File_name = input("what should I name the RNA Sequence file?") + ".fna"
                    File_Path = input("Where would you like to export your document?")

                    with open(File_Path + '/' + File_name, 'a') as RNA_File:
                        RNA_File.write(">" + Header + " RNA Sequence\n" + RNA_Complete + "\n")
                        print('\033[1;43m' + "RNA Sequence has been saved in the specified directory." + '\033[0m')
                    break

                elif Ans == "no" or Ans == "NO" or Ans == "No":
                    print(RNA_Complete)
                    print('\033[1;43m' + "Sequence not saved...")
                    print('\033[0m')
                    break

                else:
                    print('\033[1;31m' + "Please enter a valid response...")
                    print('\033[0m')

        elif (Work_type == "Reverse Compliment Strand" or Work_type == "reverse compliment strand"
              or Work_type == "Reverse compliment Strand" or Work_type == "Reverse Compliment strand"
              or Work_type == "reverse Compliment Strand"):
            RCS = reverse_complement_DNA(DNA)
            Length_line = 70
            Line_DNA = [RCS[i:i + Length_line] + '\n' for i in range(0, len(RCS), Length_line)]
            Reverse_strand = ''.join(Line_DNA)

            while True:
                Answer = input("Would you like to save this sequence to a file? ")
                if Answer == "No" or Answer == "NO" or Answer == "no":
                    print(Reverse_strand)
                    print('\033[1;43m' + "Sequence not saved..." + '\033[0m')
                    break

                elif Answer == "yes" or Answer == "Yes" or Answer == "YES":
                    File_name = input("what should I name the DNA Sequence file? ") + ".fna"
                    File_Path = input("Where would you like to export your document?")
                    with open(File_Path + '/' + File_name, "a") as Reverse_Compliment:
                        Reverse_Compliment.write(">" + Header + "Reverse Compliment Strand: \n" + Reverse_strand + "\n")
                        print('\033[1;43m' + "RNA Sequence has been saved in the specified directory." + '\033[0m')
                    break

                else:
                    print('\033[1;31m' + "Please enter a valid response..." + '\033[0m')

        elif (Work_type == "end" or Work_type == "END" or Work_type == "End" or Work_type == "new Sequence"
              or Work_type == "New Sequence" or Work_type == "new sequence" or Work_type == "New sequence"):
            break

        else:
            print('\033[1;31m' + "Please enter a valid response..." + '\033[0m')
    else:
        break

while True:
    Seq_RNA = Sequence_data.get(Header)
    if Sequence_type == "RNA":
        Work_type = input('Would you like a base count, translation, or the DNA Sequence? ')

        if (Work_type == 'Base Count' or Work_type == 'Base count' or Work_type == 'base count'
                or Work_type == 'base Count'):
            print("This is the count for each base in your sequence:\n " + str(count_bases_RNA(Seq_RNA)))

        elif Work_type == 'Translation' or Work_type == 'translation':
            print("Translated RNA:\n " + translate(Sequence))

        elif Work_type == 'DNA Sequence' or Work_type == 'dna Sequence' or Work_type == 'DNA sequence':
            REVDNA = reverse_sequencing(Seq_RNA)
            Length_line = 70
            Line_DNA = [REVDNA[i:i + Length_line] + '\n' for i in range(0, len(REVDNA), Length_line)]
            DNA_Complete = ''.join(Line_DNA)
            File_name = input("what should I name the DNA Sequence file? (include file type indicator)") + ".fna"
            File_Path = input("Where would you like to export your document? (set a file path)")
            with open(File_Path + '/' + File_name, 'a') as DNA_File:

                DNA_File.write(">" + Header + " RNA Sequence\n" + DNA_Complete + "\n")
                print("DNA Sequence has been saved in the specified directory.")

        elif Work_type == 'Stop' or Work_type == 'end' or Work_type == 'End' or Work_type == 'stop':
            break

        else:
            print('\033[1;31m' + "Please enter a valid response...")
            print('\033[0m')

    else:
        sys.exit()
