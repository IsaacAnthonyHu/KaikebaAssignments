## Pseudocode By Wiki about RANSAC

不会写伪代码，从wiki上复制了一个，现学现卖改一下：

```pseudocode
Given:
    data - a set of observed data points
    model - a model that can be fitted to data points
    n - the minimum number of data values required to fit the model
    k - the maximum number of iterations allowed in the algorithm
    t - a threshold value for determining when a data point fits a model
    d - the number of close data values required to assert that a model fits well to data
Return:
    bestfit - model parameters which best fit the data (or nil if no good model is found)
iterations = 0
bestfit = nil
besterr = something really large
while iterations < k {
    maybeinliers = n randomly selected values from data
    maybemodel = model parameters fitted to maybeinliers
    alsoinliers = empty set
    for every point in data not in maybeinliers {
        if point fits maybemodel with an error smaller than t
             add point to alsoinliers
    }
    if the number of elements in alsoinliers is > d {
        % this implies that we may have found a good model
        % now test how good it is
        bettermodel = model parameters fitted to all points in maybeinliers and alsoinliers
        thiserr = a measure of how well model fits these points
        if thiserr < besterr {
            bestfit = bettermodel
            besterr = thiserr
        }
    }
    increment iterations
}
return bestfit
```



现学现卖：

```pseudocode
Given:
	A - a set of points
	B - a set of points
	AB - matching set of A and B
	n - the minimum number (4) of data values required to fit the model
	k - the maximum number of interations allowed in the algorithm
	t - a threshold value for determinaing when a data point fits a model
	d - the number of close data values required to assert that a model fits well to data
Return:
	bestfit - model parameters which best fit the data (or nil if no good model is found)

iteration = 0
bestfit = nil
besterr = something really large

while iterations < k {
	maybeinliers = 4 random selected values from data 
	% with matched A and B values
	maybemodel = model parameters fitted to maybeinliers
	% use cv2.getPerspectiveTransform
	alsoinliers = empty set
	
	for every point in data not in maybeinliers {
		if point fits maybemodel with an error smaller than t
			add point to alsoinliers
	}
	
	if the number of elements in alsoinliers is > d {
		bettermodel = model parameters fitted to all points in maybeinliers and alsoinliers
		thiserr = a measure of how well model fits these points
		if thiserr < besterr {
			bestfit = bettermodel
			besterr = thiserr
		}
	}
	increment iterations
}
return bestfit
```
