from imagecluster import main
import sys
img_dir = sys.argv[1]
print(img_dir)
main.main(img_dir, sim=0.5)
