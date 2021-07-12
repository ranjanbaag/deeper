import os
import face_recognition
import sys

ref_dir = sys.argv[1]
src_dir = sys.argv[2]
tolerance = sys.argv[3]

print ("Args:",ref_dir,src_dir,tolerance)

ref_imgs = os.listdir(ref_dir)
src_imgs = os.listdir(src_dir)
#src_imgs = [f for f in os.listdir(src_dir) if os.path.isfile(f)]

if not os.path.exists(src_dir+"/_0n"):
	os.makedirs(src_dir+"/_0n")

for src_img in src_imgs:
	if os.path.isfile(src_dir + "/"+ src_img) and ( src_img.endswith(".png") or src_img.endswith(".jpg") or src_img.endswith(".jpeg")):
		os.rename(src_dir + "/"+ src_img, src_dir + "/_0n/"+ src_img)

for ref_img in ref_imgs:
	print ("Ref Image ", ref_dir + "/" + ref_img)
	try:
		crt_ref_img = face_recognition.load_image_file(ref_dir + "/" + ref_img)
		crt_ref_img_encodeds = face_recognition.face_encodings(crt_ref_img)
		if len(crt_ref_img_encodeds) < 1:
			continue
		srcn_imgs = os.listdir(src_dir+"/_0n/")
		for srcn_img in srcn_imgs:
			try:
				crt_srcn_img = face_recognition.load_image_file(src_dir + "/_0n/" + srcn_img)
				crt_srcn_img_encodeds = face_recognition.face_encodings(crt_srcn_img)   
				if len(crt_srcn_img_encodeds) > 0:
					try:
						result = face_recognition.compare_faces([crt_ref_img_encodeds[0]], crt_srcn_img_encodeds[0],tolerance)
						if result[0] == True:
							os.rename(src_dir + "/_0n/"+ srcn_img, src_dir + "/"+ srcn_img)
					except:
						print ("Src Image Compare Error:",src_dir + "/" + srcn_img)
				else:
					print ("Src Image Empty:",src_dir + "/" + srcn_img)
			except:
				print ("Src Image Encoding Error:",src_dir + "/" + srcn_img)
	except:
		print ("Ref Image Error:",ref_dir + "/" + ref_img)
