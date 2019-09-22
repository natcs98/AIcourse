from PIL import Image
import numpy as np

def stereo_matching_f(left_img,right_img,disparity_range):
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
    for y in range(height):
        for x in range(width):
            # khởi tạo cost ban đầu
            cost=(left[y,x]-right[y,x])**2
            disparity=0
            # tìm min cost
            for d in range(1,disparity_range):
                tmp=(left[y,x]-right[y,x-d])**2
                if tmp<cost :
                    cost=tmp
                    disparity=d
            # gán vị trí vào ảnh chứa khoảng cách=d
            depth[y,x]=disparity*scale
    #chuyển về dạng ảnh
    Image.fromarray(depth).save('disparity_map.png')

#main

disparity_range=16
stereo_matching_f('left.png','right.png',disparity_range)


