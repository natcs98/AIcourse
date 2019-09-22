from PIL import Image
import numpy as np

def stereo_matching_f(left_img,right_img,kernel_size,disparity_range):
    # dọc ảnh ,chuyển ảnh về ảnh xám,đưa về dạng ảnh số trong numpy
    left_img=Image.open(left_img).convert('L')
    left=np.asarray(left_img)
    right_img=Image.open(right_img).convert('L')
    right=np.asarray(right_img)

    # kích thước ảnh
    height=288
    width=384

    # tao ảnh disparity map
    depth=np.zeros((height,width),np.uint8)
    scale=255/disparity_range
    kernel_hafl=int((kernel_size-1)/2)
    for y in range(kernel_hafl,height-kernel_hafl):
        for x in range(kernel_hafl,width-kernel_hafl):
            disparity=0
            cost=123131
            for d in range(0,disparity_range):

                tong=0
                for u in range(-kernel_hafl,kernel_hafl):
                    for v in range(-kernel_hafl,kernel_hafl):
                        tong+=(left[y+u,x+v]-right[y+u,x+v-d])**2
                if tong< cost:
                    cost=tong
                    disparity=d
            depth[y,x]=disparity*scale
    Image.fromarray(depth).save('disparity_map.png')
disparity_range=16
stereo_matching_f('left.png','right.png',5,disparity_range)