import re
import sys

first_content='''%YAML:1.0
---
opencv_lbphfaces:
   threshold: 1.7976931348623157e+308
   radius: 1
   neighbors: 8
   grid_x: 8
   grid_y: 8
   histograms:
      '''
last='''labels: !!opencv-matrix
        rows: {0}
        cols: 1
        dt: i
        data: [{1}]
    labelsInfo:
        []
'''

file1=open(sys.argv[1],"r")
file2=open(sys.argv[2],"r")

file1_content=file1.read()
file2_content=file2.read()

file1.close()
file2.close()

file1_mid=re.search("(?s)histograms:(?s)(.*)labels:",file1_content).group(1)
file2_mid=re.search("(?s)histograms:(?s)(.*)labels:",file2_content).group(1)
mid_content=file1_mid+file2_mid

file1_data=re.search("data:(?s)(.*)(?s)[[](?s)(.*)(?s)[]](?s)(.*)(?s)labelsInfo:",file1_content).group(2)
file2_data=re.search("data:(?s)(.*)(?s)[[](?s)(.*)(?s)[]](?s)(.*)(?s)labelsInfo:",file2_content).group(2)
data_string=file1_data+","+file2_data
rows=len(data_string.split(","))

last_content=last.format(rows,data_string)

final_content=first_content+mid_content+last_content

newfile=open("New file.yml","w")
newfile.write(final_content)
newfile.close()

print("New file created")
