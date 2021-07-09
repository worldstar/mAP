import glob
import os
import xml.etree.ElementTree as ET
xmlpath = "D:/ga/yolov3/Data/Annotations20210413/"
mAPtxtfile="./mAPTxt_Pre/TWCC-yolov5/output14/mAPTxt_Pre_num_normal"
savefile = "./mAPTxt_Pre/TWCC-yolov5/output14/mAPTxt_Pre_class_no-normal/"
def file_lines_to_list(path):
    # open txt file lines to a list
    with open(path) as f:
        content = f.readlines()
    # remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    
    return content

# ground_truth_files_list = glob.glob(mAPtxtfile + '/*.txt')
# for txt_file in ground_truth_files_list:
# 	file_id = txt_file.split(".txt", 1)[0]
# 	file_name = os.path.basename(os.path.normpath(file_id))
# 	lines_list = file_lines_to_list(txt_file)
# 	# print(file_name,'-',lines_list)
# 	for line in lines_list:

# 		file_box = line.split(" ")
# 		# print(file_box)
# 		if file_box[0] == "0" :
# 			fr = "ASDType2"+" "+file_box[1]+" "+file_box[2]+" "+file_box[3]+" "+file_box[4]+"\n"
# 		elif file_box[0] == "1" :
# 			fr = "VSDType1"+" "+file_box[1]+" "+file_box[2]+" "+file_box[3]+" "+file_box[4]+"\n"
# 		elif file_box[0] == "2" :
# 			fr = "VSDType2"+" "+file_box[1]+" "+file_box[2]+" "+file_box[3]+" "+file_box[4]+"\n"
# 		elif file_box[0] == "3" :
# 			fr = "VSDType4"+" "+file_box[1]+" "+file_box[2]+" "+file_box[3]+" "+file_box[4]+"\n"
# 		elif file_box[0] == "4" :
# 			fr = "PS"+" "+file_box[1]+" "+file_box[2]+" "+file_box[3]+" "+file_box[4]+"\n"
# 		elif file_box[0] == "5" :
# 			fr = "PDA"+" "+file_box[1]+" "+file_box[2]+" "+file_box[3]+" "+file_box[4]+"\n"

# 		f = open(savefile+file_name+".txt", 'a')
# 		f.write(fr)
# 		print(file_name)


# def ground_truth_files_list(mAPtxtfile):
# 	ground_truth_files_list = glob.glob(mAPtxtfile + '/*.txt')
# 	for txt_file in ground_truth_files_list:
# 		file_id = txt_file.split(".txt", 1)[0]
# 		file_name = os.path.basename(os.path.normpath(file_id))
# 		lines_list = file_lines_to_list(txt_file)

# 	return file_name

def xml_files_list(xmlpath,file_name):
	xml_files_list = glob.glob(xmlpath + file_name + '.xml')

	for xml_txt_file in xml_files_list:
		xml_file_id = xml_txt_file.split(".xml", 1)[0]
		xml_file_name = os.path.basename(os.path.normpath(xml_file_id))

		xmlFile = open(xmlpath + file_name + '.xml') 
		xmlTree = ET.parse(xmlFile)
		xmlRoot = xmlTree.getroot()
		width,height,depth = -1,-1,-1
		for xmlObj in xmlRoot.iter('size'):
		    width = xmlObj.find('width').text.replace(" ", "").replace("\t", "").replace("\n", "")
		    height = xmlObj.find('height').text.replace(" ", "").replace("\t", "").replace("\n", "")
			
		# print(width,'-',height)

	return width,height



ground_truth_files_list = glob.glob(mAPtxtfile + '/*.txt')
for txt_file in ground_truth_files_list:
	file_id = txt_file.split(".txt", 1)[0]
	file_name = os.path.basename(os.path.normpath(file_id))
	
	lines_list = file_lines_to_list(txt_file)

	width,height = xml_files_list(xmlpath,file_name)

	for line in lines_list:
		file_box = line.split(" ")
		# print(file_box)
		frr = str(int(float(file_box[1])*int(width)))+" "+str(int(float(file_box[2])*int(height)))+" "+str(int(float(file_box[3])*int(width)))+" "+str(int(float(file_box[4])*int(height)))+"\n"
		if file_box[0] == "0" :
			fr = "ASDType2"+" "+frr
		elif file_box[0] == "1" :
			fr = "VSDType1"+" "+frr
		elif file_box[0] == "2" :
			fr = "VSDType2"+" "+frr
		elif file_box[0] == "3" :
			fr = "VSDType4"+" "+frr
		elif file_box[0] == "4" :
			fr = "PS"+" "+frr
		elif file_box[0] == "5" :
			fr = "PDA"+" "+frr

	f = open(savefile+file_name+".txt", 'a')
	f.write(fr)
	print(file_name)



# file_name = ground_truth_files_list(mAPtxtfile)


# if file_name == xml_file_name :

# print(xml_file_name)