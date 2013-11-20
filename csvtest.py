import csv

def writeCsvFile(fname, data, *args, **kwargs):
	"""
	@param fname: string, name of file to write
	@param data: list of list of items
	Write data to file
	"""

	mycsv = csv.writer(open(fname, 'wb'), *args, **kwargs)
	for row in data:
		mycsv.writerow(row)

mydat = (
	['filename', 'tokens', 'nertoken'],
	['file1', 200, 7],
	['file2', 300, 17]
)

writeCsvFile(r'test.csv', mydat)
