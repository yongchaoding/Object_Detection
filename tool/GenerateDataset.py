import os
from shutil import copyfile


PATH = os.getcwd();
FILENAME = PATH + '/ImageSets/DET/train_1.txt';
DATA_ROOT = PATH + '/Data/DET/train/';
ANNOTATION_ROOT = PATH + '/Annotations/DET/train/';

COPY_ANNOTATION='/home/yongchao/Dataset/ImageNet_Object_Detection/ILSVRC/Annotations/DET/train/';
COPY_DATA='/home/yongchao/Dataset/ImageNet_Object_Detection/ILSVRC/Data/DET/train/';

def ImageSetRead(filename):
	ImageSet = [];
	f = open(filename, 'r');
	while 1:
		line = f.readline();
		if not line:
			break;
		#print(line.split()[0])
		ImageSet.append(line.split()[0]);
	f.close()
	#print(ImageSet);
	return ImageSet;

def ImageDataCopy(ImageSet):
	for Img in ImageSet:
		ImgFile = Img + '.JPEG';
		DistImgFile = DATA_ROOT + ImgFile;
		CopyImgFile = COPY_DATA + ImgFile;
		TrainPath = DATA_ROOT + ImgFile.split('/')[0];
		if os.path.isdir(TrainPath):
			pass;
		else:
			print("mkdir ", TrainPath);
			os.mkdir(TrainPath)
		#print(CopyXMLFile);
		#print(DistXMLFile);
		copyfile(CopyImgFile, DistImgFile);
		print("Copy: ", ImgFile);
	return True;

def ImageAnnotationCopy(ImageSet):
	for XML in ImageSet:
		XMLFile = XML + '.xml';
		DistXMLFile = ANNOTATION_ROOT + XMLFile;
		CopyXMLFile = COPY_ANNOTATION + XMLFile;
		TrainPath = ANNOTATION_ROOT + XMLFile.split('/')[0];
		if os.path.isdir(TrainPath):
			pass;
		else:
			print("mkdir ", TrainPath);
			os.mkdir(TrainPath)
		#print(CopyXMLFile);
		#print(DistXMLFile);
		copyfile(CopyXMLFile, DistXMLFile);
		print("Copy: ", XMLFile);
	return True;

def run():
	ImageSet = ImageSetRead(FILENAME);
	ImageDataCopy(ImageSet);
	ImageAnnotationCopy(ImageSet);
	print("Copy total: ", len(ImageSet))	

if __name__=="__main__":
	run();
