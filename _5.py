import math
data = [
        [1,1],
        [1.5,2],
        [3,4],
        [5,7],
        [3.5,5],
        [4.5,5],
        [3.5,4.5]     
    ]
def eucledian_distance(x1,y1,x2,y2):
    return math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))   
c1 = data[0]
c2 = data[1]
count = 0;
while count < len(data):
    cluster1 = []
    cluster2 = []
    count = count +1
    for point in data:
        x = point[0]
        y = point[1]
        if eucledian_distance(x,y,c1[0],c1[1]) < eucledian_distance(x,y,c2[0],c2[1]):
            cluster1.append(point)
        else:
            cluster2.append(point)
    c1 = [sum(x[0] for x in cluster1)/len(cluster1),sum(x[1] for x in cluster1)/len(cluster1)]
    c2 = [sum(x[0] for x in cluster2)/len(cluster2),sum(x[1] for x in cluster2)/len(cluster2)]    
print("----------------Final Cluster and Center Value")
print("Center1: ",c1 ,"\tCenter2 : ",c2)
print("Cluster1 :",cluster1 , "Cluster : ",cluster2)
