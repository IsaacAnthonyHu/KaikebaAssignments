import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

def randDotInCir(centre, radius, dots_num=500):
    '''
    create random dots set in a circle with given circle centre
    '''
    dots_list = []
    for x in range(dots_num):
        random_angle = 2 * np.pi * np.random.rand()
        random_radius = radius * np.random.rand()
        x_axis = random_radius * np.sin(random_angle)
        y_axis = random_radius * np.cos(random_angle)
        coord = [centre[0] + x_axis, centre[1] + y_axis]
        dots_list.append(coord)
    return np.array(dots_list)


def geneTestClus():
    '''
    generate random test cluster dataset and return their concatenation
    '''
    cluster1 = randDotInCir([-10, -10], 5)
    cluster2 = randDotInCir([12,13], 6)
    cluster3 = randDotInCir([-20, 15], 4)

    return np.concatenate((cluster1, cluster2, cluster3))


def dotDis(dot1, dot2):
    '''
    calculate distance between two dots
    '''
    return np.sqrt((dot1[0]-dot2[0])**2 + (dot1[1]-dot2[1])**2)


def initiate_centroids(k, test_list):
    '''
    Generate centroids supported by K Means ++
    '''
    # Select First Core Randomly
    core_list = []
    first_core = test_list[np.random.randint(len(test_list))]
    core_list.append(first_core)
    # Other centroids
    def range_search(prob, prob_list):
        '''
        search prob from prob_list
        '''
        for x in range(len(prob_list)):
            if prob >= prob_list[x]:
                continue
            else:
                return x
        return len(prob_list)-1
    
    def other_cores():
        '''
        Repeatable method in other cores
        '''
        dotsDisSqToCores = [min([dotDis(core, dots)**2 for core in core_list]) for dots in test_list]
        dotsProb = [x/sum(dotsDisSqToCores) for x in dotsDisSqToCores]
        dotsAccumuProb = [sum(dotsProb[:x]) for x in range(1, len(dotsProb)+1)]
        randomProb = np.random.rand()
        core_index = range_search(randomProb, dotsAccumuProb)
        new_core = test_list[core_index]
        core_list.append(new_core)
    
    for x in range(k-1):
        other_cores()
    print(core_list)
    return core_list


def assignment(df, centroids, colmap):
    '''
    '''
    for x in centroids.keys():
        df['distance_%r'%x] = np.sqrt((df['x'] - centroids[x][0])**2 + (df['y'] - centroids[x][1])**2)
    distance_columns = ['distance_%r'%x for x in centroids.keys()]
    df['closest_centroids'] = df[distance_columns].idxmin(axis=1)
    df['closest_centroids'] = df['closest_centroids'].map(lambda x: int(x.lstrip('distance_')))
    df['color'] = df['closest_centroids'].map(lambda x: colmap[x])
    return df


def update(df, centroids):
    '''
    '''
    for x in centroids.keys():
        centroids[x] = np.array((np.mean(df[df['closest_centroids'] == x]['x']), np.mean(df[df['closest_centroids'] == x]['y'])))
    return centroids


def main():
    '''
    '''
    test_list = geneTestClus()
    dot_df = pd.DataFrame(data=test_list, columns=['x', 'y'])
    centroids_list = initiate_centroids(3, test_list)
    centroids = {x[0]:x[1] for x in list(enumerate(centroids_list))}
    colmap = {0: 'r', 1: 'g', 2: 'b'}
    dot_df = assignment(dot_df, centroids, colmap)
    plt.scatter(dot_df['x'], dot_df['y'], color=dot_df['color'], alpha=0.5, edgecolor='k')
    for i in centroids.keys():
        plt.scatter(*centroids[i], color=colmap[i], linewidths=7)
    plt.savefig('init_image.jpg')
    
    for i in range(10):
        plt.close()
        
        closest_centroids = dot_df['closest_centroids'].copy(deep=True)
        centroids = update(dot_df, centroids)
        
        plt.scatter(dot_df['x'], dot_df['y'], color=dot_df['color'], alpha=0.5, edgecolor='k')
        for i in centroids.keys():
            plt.scatter(*centroids[i], color=colmap[i], linewidths=7)
        plt.savefig('%r.jpg'%i)
        df = assignment(dot_df, centroids, colmap)
        
        if closest_centroids.equals(df['closest_centroids']):
            break


if __name__ == '__main__':
    main()