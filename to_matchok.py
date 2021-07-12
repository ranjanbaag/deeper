import os
import face_recognition
import sys

ref_dir = sys.argv[1]
src_dir = sys.argv[2]
tolerance = 0.55 #sys.argv[3]
#src_dir = sys.argv[3]

print ("Args:",ref_dir,src_dir,tolerance)

ref_imgs = os.listdir(ref_dir)
src_imgs = os.listdir(src_dir)
#src_imgs = [f for f in os.listdir(src_dir) if os.path.isfile(f)]

#if not os.path.exists(src_dir+"/_0n"):
os.makedirs(src_dir+"/_0n",exist_ok = True)
#if not os.path.exists(src_dir+"/_ok0/_"):
os.makedirs(src_dir+"/_ok0/_/_",exist_ok = True)
#if not os.path.exists(src_dir+"/_ok1/_/_"):
os.makedirs(src_dir+"/_ok1/_/_",exist_ok = True)
#if not os.path.exists(src_dir+"/_ok2/_/_"):
os.makedirs(src_dir+"/_ok2/_/_",exist_ok = True)
#if not os.path.exists(src_dir+"/_ok3/_"):
os.makedirs(src_dir+"/_ok3/_/_",exist_ok = True)
#if not os.path.exists(src_dir+"/_ok4/_"):
os.makedirs(src_dir+"/_ok4/_/_",exist_ok = True)
os.makedirs(src_dir+"/_ok5/_/_",exist_ok = True)
os.makedirs(src_dir+"/_ok6/_/_",exist_ok = True)
os.makedirs(src_dir+"/_ok7/_/_",exist_ok = True)
os.makedirs(src_dir+"/_ok8/_/_",exist_ok = True)
os.makedirs(src_dir+"/_ok9/_/_",exist_ok = True)
os.makedirs(src_dir+"/_ok99/",exist_ok = True)
#if not os.path.exists(src_dir+"/_nok"):
os.makedirs(src_dir+"/_okn/",exist_ok = True)
os.makedirs(src_dir+"/_nok",exist_ok = True)

#distances_list = [0.3, 0.4, 0.45 ,0.5, 0.54, 0.58, 0.6 ,0.62, 0.66, 0.7, 0.8]
distances_list = [0.29, 0.39, 0.44 ,0.49, 0.59, 0.69, 0.79]
distances_list_actual = []

def compare_move_file(ref_faces,src_faces, tolerance, src_file, new_file,new_file2,new_file3,result,override=False):
	#crt_distance = get_distance(ref_faces, src_faces)
	#result['distance'] = crt_distance
	crt_distance = result['distance']
	if crt_distance > tolerance:
		return False
	if os.path.isfile(new_file):
		if override == True:
			os.remove(new_file)
		elif not os.path.isfile(new_file2+".png"):
			os.rename(new_file, new_file2+".png") #44#52
		else:
			os.rename(new_file, new_file3+".png")#new_file2+".png"
	print("+  ", crt_distance, "->",new_file)
	os.rename(src_file, new_file) #44#52
	return True

def compare_move_file_replace(ref_faces,src_faces, tolerance, src_file, new_file,new_file2,new_file3,result,override):
	crt_distance = get_distance(ref_faces, src_faces,tolerance)
	if crt_distance <= tolerance:
		#new_file = src_dir + "/_ok1/"+ srcn_img
		print("+  ======",crt_distance)
		distances_list_actual.append(crt_distance);
		if os.path.isfile(new_file): # File Already Exists
			old_crt_srcn_img = face_recognition.load_image_file(new_file)
			old_crt_srcn_img_encodeds = face_recognition.face_encodings(old_crt_srcn_img)  
			old_distance = get_distance(crt_ref_img_encodeds_list, old_crt_srcn_img_encodeds,tolerance)
			if (crt_distance < old_distance) or (override == True): # Current File is Better than existing
				print("+  ->",new_file)
				os.rename(src_file, new_file) #44#52				
				return True
			if crt_distance == old_distance: # Current File is Same As existing
				print("+  ->>",new_file2)
				os.rename(new_file, new_file2) #44#52
				os.rename(src_file, new_file2+".png") #44#52				
				return True
			else: # Existing File is Better than Current
				print("+  ->",new_file2)
				os.rename(src_file, new_file3+".png") #44#52			
				return True
		else:
			print("+  ->",new_file)
			os.rename(src_file, new_file) #44#52
			return True
	return False

def get_distance(ref_faces,src_faces):
	for distance in distances_list:
		match = compare_faces(crt_ref_img_encodeds_list, crt_srcn_img_encodeds,distance)
		if match == True:
			return distance
	return 0.9

def compare_faces(ref_faces,src_faces, tolerance):
	for src_face in src_faces:
		result = face_recognition.compare_faces(ref_faces, src_face,tolerance)
		if any(result):
			return True
	return False


for src_img in src_imgs:
	if os.path.islink(src_dir + "/"+ src_img):
		continue
	if os.path.isfile(src_dir + "/"+ src_img) and ( src_img.endswith(".png") or src_img.endswith(".jpg") or src_img.endswith(".jpeg")):
		os.rename(src_dir + "/"+ src_img, src_dir + "/_0n/"+ src_img)

crt_ref_img_encodeds_list = []
for ref_img in ref_imgs:
	print ("Ref Image ", ref_dir + "/" + ref_img)
	try:
		crt_ref_img = face_recognition.load_image_file(ref_dir + "/" + ref_img)
		crt_ref_img_encodeds = face_recognition.face_encodings(crt_ref_img)
		if len(crt_ref_img_encodeds) < 1:
			continue
		crt_ref_img_encodeds_list.append(crt_ref_img_encodeds[0]);
	except:
		print ("Ref Image Error:",ref_dir + "/" + ref_img)


srcn_imgs = os.listdir(src_dir+"/_0n/")
for srcn_img in srcn_imgs:
	try:
		crt_srcn_file = src_dir + "/_0n/" + srcn_img
		#print ("crt_srcn_file : " + crt_srcn_file)
		crt_srcn_img = face_recognition.load_image_file(crt_srcn_file)
		crt_srcn_img_encodeds = face_recognition.face_encodings(crt_srcn_img)  
		if len(crt_srcn_img_encodeds) > 0:
			print("+ ",crt_srcn_file)
			#for crt_ref_img_encodeds in crt_ref_img_encodeds_list:
			crt_distance = get_distance(crt_ref_img_encodeds_list, crt_srcn_img_encodeds)
			result = { 'moved' : False, 'distance' : crt_distance  }
			try:
				moved = compare_move_file(crt_ref_img_encodeds_list, crt_srcn_img_encodeds, 0.3,
						crt_srcn_file, src_dir + "/_ok0/_/"+ srcn_img, src_dir + "/_ok0/_/_/"+ srcn_img,
						src_dir + "/_ok0/_/_/"+ srcn_img,result)
				if moved == True:
					continue
				moved = compare_move_file(crt_ref_img_encodeds_list, crt_srcn_img_encodeds, 0.45,
						crt_srcn_file, src_dir + "/_ok1/_/"+ srcn_img, src_dir + "/_ok1/_/_/"+ srcn_img,
						src_dir + "/_ok1/_/_/"+ srcn_img,result)
				if moved == True:
					continue
				moved = compare_move_file(crt_ref_img_encodeds_list, crt_srcn_img_encodeds, 0.55,
						crt_srcn_file, src_dir + "/_ok2/"+ srcn_img, src_dir + "/_ok2/_/"+ srcn_img,
						src_dir + "/_ok2/_/_/"+ srcn_img,result)
				if moved == True:
					continue
				moved = compare_move_file(crt_ref_img_encodeds_list, crt_srcn_img_encodeds, 0.75,
						crt_srcn_file, src_dir + "/_ok3/"+ srcn_img, src_dir + "/_ok3/_/"+ srcn_img,
						src_dir + "/_ok3/_/_/"+ srcn_img,result, True)
				if moved == True:
					continue
				moved = compare_move_file(crt_ref_img_encodeds_list, crt_srcn_img_encodeds, 0.8,
						crt_srcn_file, src_dir + "/_ok4/"+ srcn_img, src_dir + "/_ok4/_/"+ srcn_img,
						src_dir + "/_ok4/_/_/"+ srcn_img,result,True)
				if moved == True:
					continue
				"""	
				moved = compare_move_file(crt_ref_img_encodeds_list, crt_srcn_img_encodeds, 0.80,
						crt_srcn_file, src_dir + "/_ok5/"+ srcn_img, src_dir + "/_ok5/_/"+ srcn_img,
						src_dir + "/_ok5/_/_/"+ srcn_img,result,True)
				if moved == True:
					continue
				moved = compare_move_file(crt_ref_img_encodeds_list, crt_srcn_img_encodeds, 0.7,
						crt_srcn_file, src_dir + "/_ok6/"+ srcn_img, src_dir + "/_ok6/_/"+ srcn_img,
						src_dir + "/_ok6/_/_/"+ srcn_img,result,True)
				if moved == True:
					continue
				moved = compare_move_file(crt_ref_img_encodeds_list, crt_srcn_img_encodeds, 0.8,
						crt_srcn_file, src_dir + "/_ok7/"+ srcn_img, src_dir + "/_ok7/_/"+ srcn_img,
						src_dir + "/_ok7/_/_/"+ srcn_img,result,True)
				if moved == True:
					continue
				moved = compare_move_file(crt_ref_img_encodeds_list, crt_srcn_img_encodeds, 0.8,
						crt_srcn_file, src_dir + "/_ok8/"+ srcn_img, src_dir + "/_ok8/_/"+ srcn_img,
						src_dir + "/_ok8/_/_/"+ srcn_img,result,True)
				if moved == True:
					continue
				moved = compare_move_file(crt_ref_img_encodeds_list, crt_srcn_img_encodeds, 0.9,
						crt_srcn_file, src_dir + "/_ok9/"+ srcn_img, src_dir + "/_ok9/_/"+ srcn_img,
						src_dir + "/_ok9/_/_/"+ srcn_img,result,True)
				if moved == True:
					continue
				"""
				os.rename(src_dir + "/_0n/"+ srcn_img, src_dir + "/_ok99/"+ srcn_img)
			except:
				print ("Src Image Compare Error:",crt_srcn_file)
				print("Oops!",sys.exc_info(),"occured.")
		else:
			print ("Src Image Empty:",src_dir + "/" + srcn_img)
			os.rename(src_dir + "/_0n/"+ srcn_img, src_dir + "/_nok/"+ srcn_img)
	except:
		#print ("Src Image Encoding Error:",src_dir + "/" + srcn_img)
		print("Src Image Encoding Error:", sys.exc_info()," for ",srcn_img)


counters = { (x, distances_list_actual.count(x)) for x in distances_list }
for (x, count) in counters:
    print("%f: %d" % (x, count))







