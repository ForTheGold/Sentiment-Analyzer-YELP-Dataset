import os


with open('electronics10k.json', 'r') as infile:
	with open('electronics10k_formatted.json', 'w') as outfile:

		print('[', file=outfile)

		previous = None
		for line in infile:
			if previous == None:
				outfile.write(line.rstrip('\n'))
				previous = line
			else:
				outfile.write(',\n')
				outfile.write(line.rstrip('\n'))

		outfile.write('\n]')

infile.close()
outfile.close()