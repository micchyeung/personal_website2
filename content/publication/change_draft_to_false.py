from glob import glob

flist = glob.glob('*/index.md')

for f in flist:
    with open(f,'
