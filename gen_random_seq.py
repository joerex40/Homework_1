import argparse
import random
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio import SeqIO


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Random sequences (DNA) generator')

    parser.add_argument('-t', '--total_seqs', help='Number of sequences', metavar='Int', type=int, default=10)

    parser.add_argument('-m', '--min_seq_size', help='Minimum sequence(s) size', metavar='Int', type=int, default=100)

    parser.add_argument('-M', '--max_seq_size', help='Maximum sequence(s) size', metavar='Int', type=int, default=1000)

    parser.add_argument('-o', '--output', help='Resulted file name without extension', metavar='FILE', required=True)

    args = parser.parse_args()

    TOTAL_SEQUENCES = args.total_seqs
    MIN_SIZE = args.min_seq_size
    MAX_SIZE = args.max_seq_size
    output_file_name = args.output


def new_rnd_seq(seq_len):
    """
    Generate a random DNA sequence with a sequence length of "sl" (int).
    return: A string with a DNA sequence."""
    s = ''
    while len(s) < seq_len:
        s += random.choice('ATCG')
    return s


with open(output_file_name + '.fasta', 'w') as new_fh:
    for i in range(1, TOTAL_SEQUENCES + 1):
        # Select a random number between MIN_SIZE and MAX_SIZE
        rsl = random.randint(MIN_SIZE, MAX_SIZE)
        # Generate the random sequence
        raw_seq = new_rnd_seq(rsl)
        # Generate a correlative name
        seq_name = 'Sequence_number_{0}'.format(i)
        rec = SeqRecord(Seq(raw_seq), id=seq_name, description='')
        SeqIO.write([rec], new_fh, 'fasta')
