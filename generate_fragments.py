from class_FastA import FastA
from class_FastQ import FastQ
from class_Convert_Sequence import ConvertSequence
import argparse

# # Take care om command line options
#
# parser = argparse.ArgumentParser()
# parser.add_argument('-v','--version', action='version', version='%(prog)s 2.0')
# parser.add_argument('input_file', type=argparse.FileType('r'))
# parser.add_argument('-i','--min', type=int, help="minimum fragment size", default='100')
# parser.add_argument('-x','--max', type=int, help="maximum fragment size", default='100')
# parser.parse_args([C:\\Users\\hpatterton\\Documents\\Genolve\\Notes\\Escherichia coli str K-12 substr MG1655.fasta])
#
# print(end)
#
if __name__ == "__main__":
	input_filename = "C:\\Users\\hpatterton\\Documents\\Genolve\\Notes\\Escherichia coli str K-12 substr MG1655.fasta"
	input_file = FastA()
	number_of_sequences = input_file.ReadFastA(input_filename)
	print("sequences =",number_of_sequences)
	convert_sequence = ConvertSequence()
	path,*remainder = input_filename.rpartition('\\')
	for index,sequence in enumerate(input_file):
		list_of_fragments = convert_sequence.GenerateSequenceReadFragments(sequence,150,150,10)
		list_of_names = []
		for i in range(0,len(list_of_fragments)):
			list_of_names.append(input_file.GetContigName(index)+'_'+str(i))
		out_file = input_file.GetContigName(index)
		out_file = path + '\\' + out_file + '.fastq'
		output_file = FastQ()
		output_file.WriteFastQ(out_file, list_of_names, list_of_fragments, len(list_of_fragments), quality='')
		print('written '+str(len(list_of_fragments))+' sequences to',out_file)
		