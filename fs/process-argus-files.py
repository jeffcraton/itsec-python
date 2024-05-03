#!/usr/bin/python
import os 

# source directory
srcfiles = r'C:\devtools\fs\ArgusAPIPrices'

# target directory
dstfiles = r'C:\devtools\fs\ArgusAPIPricesFiltered'

# list of ids in argus to filter for
ids = ['24356','24126','24217','24361','24380','24439','24443','24383','26614',
       '24245','24131','24098','24096','24258','26622','24222','23967','24270',
       '24254','23956','24415','24240','24386','24279','24112','24294','24300',
       '24272','24247','24354','24393','24364','24399','24402','24266','24412',
       '24395','24138','23825','23595','23686','23830','23849','23908','23912',
       '23852','26613','23714','23600','23567','23565','23727','26621','23691',
       '23436','23739','23723','23425','23884','23709','23855','23748','23581',
       '23763','23769','23741','23716','23823','23862','23833','23868','23871',
       '23735','23881','23864','23607']

#
# ierate through directory.
#
print("Start")
for subdir, dirs, files in os.walk(srcfiles):

    for file in files:
        # for each file, open and search for mapped ids

        print("processing file: {0}".format(file))
        finput=open(srcfiles + '\\' + file,'r')
        foutput=open(dstfiles + '\\' + file,'w')
        print(os.path.basename(finput.name))
        filteredfname = dstfiles + os.path.basename(finput.name)
        print(filteredfname)
        for priceline in finput:
            linearr = priceline.split(',')

            if linearr[3] in ids:
                foutput.write(priceline)

        finput.close()
        foutput.close()
#
# create versions of file in other directory where matches are found. stream out matching lines
#

print("End")