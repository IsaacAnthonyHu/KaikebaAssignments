# Algorithm
def medianBlur(img, kernel, padding_way):
    '''
    @param img single channel image np.array type list
    @param kernel np.array type list
    @param padding_way string
    '''
    im_shape = img.shape
    k_shape = max(kernel.shape) # expand kernel
    expand_lines = int(k_shape/2)
    if padding_way == 'REPLICA':
        top_pad = tuple((img[0] for x in range(expand_lines)))
        end_pad = tuple((img[-1] for x in range(expand_lines)))
        expand_img = np.vstack((top_pad, img, end_pad))
    elif padding_way == 'ZERO':
        zero = np.zeros((img.shape[0]+expand_lines*2, img.shape[1]), dtype=int)
        zero[expand_lines:-expand_lines] += img
        expand_img = zero
    else:
        return "Padding Way Wrong Input!"
    blank_img = np.zeros(expand_img.shape, dtype='uint8')
    for x in range(expand_lines, img.shape[0]+expand_lines):
        for y in range(img.shape[1]):
            if y>=expand_lines:
                area = expand_img[x-expand_lines:x+expand_lines,y-expand_lines:y+expand_lines]
            else:
                area = expand_img[x-expand_lines:x+expand_lines, 0:y+expand_lines]
            
            area_list = np.ravel(area)
            median = int(np.median(area_list))
            blank_img[x,y] = median
        
    return blank_img[expand_lines:-expand_lines].astype('uint8')
