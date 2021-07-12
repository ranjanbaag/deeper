import os
import face_recognition
import sys

src_dir = sys.argv[1]

unclean = 0
if len(sys.argv) >= 3:
    unclean = sys.argv[2]

print ("Args:plu",src_dir)

def makedirs(dir):
	try: 
		os.makedirs(dir)
		print("Directory '%s' can not be created")
	except OSError as error: 
	    print("Directory '%s' can not be created")
#if not os.path.exists(src_dir+"/_0n"):
os.makedirs(src_dir+"/_0n",exist_ok = True)
#if not os.path.exists(src_dir+"/_ok0"):
os.makedirs(src_dir+"/_ok0/_",exist_ok = True)
#if not os.path.exists(src_dir+"/_ok1/_"):
os.makedirs(src_dir+"/_ok1/_",exist_ok = True)
#if not os.path.exists(src_dir+"/_ok2/_"):
os.makedirs(src_dir+"/_ok2/_",exist_ok = True)
#if not os.path.exists(src_dir+"/_ok3/_"):
os.makedirs(src_dir+"/_ok3/_",exist_ok = True)
#if not os.path.exists(src_dir+"/_ok4/_"):
os.makedirs(src_dir+"/_ok4/_",exist_ok = True)
#if not os.path.exists(src_dir+"/_nok"):
os.makedirs(src_dir+"/_nok",exist_ok = True)

folders = ["_ok0", "_ok1", "_ok2", "_ok3", "_ok4", "_ok5", "_ok6", "_ok7", "_ok8", "_ok9"]


def okmatch(ok0,ok1,replace=False):
	imgs = os.listdir(src_dir + "/"+ok0)
	#print(src_dir + "/"+ok0)
	for img in imgs:
		file0 = src_dir + "/"+ok0+"/" + img
		file0_ = src_dir + "/"+ok0+"/_/" + img
		file1 = src_dir + "/"+ok1+"/" + img
		file0_png = src_dir + "/"+ok0+"/_/" + img + ".png"
		if os.path.isfile(file1):
			if replace == True:
				file0_ts = os.path.getmtime(file0)
				file1_ts = os.path.getmtime(file1)
				if (file0_ts < file1_ts):
					os.remove(file0)
					os.rename(file1, file0)
				else:
					os.remove(file1)
			else:
				if not os.path.isfile(file0_):
					os.rename(file0, file0_)
				if not os.path.isfile(file0_png):
					os.rename(file1, file0_png)
				else:
					os.rename(file1, file0_png+".png")
			#print(ok0+img)

for folder in folders:
	folder_path = src_dir+"/"+folder
	os.makedirs(folder_path+"/_",exist_ok = True)
	imgs = os.listdir(folder_path+"/_")
	#print(folder_path+"/_/",len(imgs))
	for img in imgs:
		new_img = img.replace(".png.png",".png").replace(".jpg.png",".jpg").replace(".jpeg.png",".jpeg")
		blured = False
		if (".png.png" in img) or (".jpg.png" in img) or (".jpeg.png" in img):
			blured = True
		exists = False
		if os.path.isfile(folder_path+"/"+new_img):
			exists = True
		exists_ = False
		if os.path.isfile(folder_path+"/_/"+new_img):
			exists_ = True

		if (blured == True) and (exists == False) and (exists_ == False):
			os.rename(folder_path + "/_/"+ img, folder_path + "/"+ new_img)
			print(new_img,'<-',img)
		elif (blured == False) and (exists == False) and (exists_ == True):
			os.rename(folder_path + "/_/"+ img, folder_path + "/"+ new_img)
			print(new_img,'<-',img)
		elif (exists == True) and (exists_ == False) and (unclean == 0):
			os.rename(folder_path+"/"+new_img, folder_path+"/_/"+new_img)
			print(new_img,' -> ',new_img)
		elif (blured == False) and (exists == True) and (exists_ == True) and (unclean == 0):
			os.rename(folder_path+"/_/"+new_img, folder_path+"/_/"+new_img+".png")
			os.rename(folder_path+"/"+new_img, folder_path+"/_/"+new_img)
			print(new_img,' -> ',new_img)
		else:
			print("[*",blured,exists,exists_,"]",folder_path+"/_/"+img,"|", new_img)

	imgs = os.listdir(folder_path)
	for img in imgs:
		if (".png.png" in img) or (".jpg.png" in img) or (".jpeg.png" in img):
			if not os.path.isfile(folder_path+"/_/"+img):
				os.rename(folder_path + "/"+ img, folder_path + "/_/"+ img)
	# 			new_img = img.replace(".png.png",".png").replace(".jpg.png",".png").replace(".jpeg.png",".png")

	# 		if ".jpg.png" in img:
	# 			os.rename(folder_path + "/"+ img, folder_path + "/_/"+ img)
	# 		if ".jpeg.png" in img:
	# 			os.rename(folder_path + "/"+ img, folder_path + "/_/"+ img)

okmatch("_ok0","_ok1")
okmatch("_ok0","_ok2")
okmatch("_ok0","_ok3")
okmatch("_ok0","_ok4")
okmatch("_ok0","_ok5")
okmatch("_ok0","_ok6")
okmatch("_ok0","_ok7")
okmatch("_ok0","_ok8")
okmatch("_ok0","_ok9")
okmatch("_ok0","_nok")

okmatch("_ok1","_ok2")
okmatch("_ok1","_ok3")
okmatch("_ok1","_ok4")
okmatch("_ok1","_ok5")
okmatch("_ok1","_ok6")
okmatch("_ok1","_ok7")
okmatch("_ok1","_ok8")
okmatch("_ok1","_ok9")
okmatch("_ok1","_nok")

okmatch("_ok2","_ok3")
okmatch("_ok2","_ok4")
okmatch("_ok2","_ok5")
okmatch("_ok2","_ok6")
okmatch("_ok2","_ok7")
okmatch("_ok2","_ok8")
okmatch("_ok2","_ok9")
okmatch("_ok2","_nok")

okmatch("_ok3","_ok4",True)
okmatch("_ok3","_ok5",True)
okmatch("_ok3","_ok6",True)
okmatch("_ok3","_ok7",True)
okmatch("_ok3","_ok8",True)
okmatch("_ok3","_ok9",True)
okmatch("_ok3","_0n",True)
okmatch("_ok3","_nok",True)

okmatch("_ok4","_ok5",True)
okmatch("_ok4","_ok6",True)
okmatch("_ok4","_ok7",True)
okmatch("_ok4","_ok8",True)
okmatch("_ok4","_ok9",True)
okmatch("_ok4","_0n",True)
okmatch("_ok4","_nok",True)

okmatch("_ok5","_ok6",True)
okmatch("_ok5","_ok7",True)
okmatch("_ok5","_ok8",True)
okmatch("_ok5","_ok9",True)
okmatch("_ok5","_0n",True)
okmatch("_ok5","_nok",True)

#"""
okmatch("_ok6","_ok7",True)
okmatch("_ok6","_ok8",True)
okmatch("_ok6","_ok9",True)
okmatch("_ok6","_0n",True)
okmatch("_ok6","_nok",True)

okmatch("_ok7","_ok8",True)
okmatch("_ok7","_ok9",True)
okmatch("_ok7","_0n",True)
okmatch("_ok7","_nok",True)

okmatch("_ok8","_ok9",True)
okmatch("_ok8","_0n",True)
okmatch("_ok8","_nok",True)

okmatch("_ok9","_0n",True)
okmatch("_ok9","_nok",True)
#"""




