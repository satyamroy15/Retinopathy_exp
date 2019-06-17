from skimage.transform import resize
from skimage.io import imread, imsave
from glob import glob

def make_resize(origin_path, dest_path, x = 255, y = 255, z = 3):
    
    for img_name in glob(origin_path + '/*'):
        img = imread(img_name)
        result = resize(img, (x, y, z))
        fname  = img_name.split('/')[2]
        imsave(dest_path + '/'+ fname, result)
        
       
nodr, dr  = glob('data_main/*')
make_resize(nodr, "dataset_225_225_3/nosymptoms")
make_resize(dr, "dataset_225_225_3/symptoms")