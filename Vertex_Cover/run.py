import networkx as nx
from matplotlib.pyplot import pause
import matplotlib.pyplot as plt
import pylab
pylab.ion()

'''######################################################################################################
   #     IF node color is red, that node has been covered.                                              #
   #     IF node color is yellow, that node is the one currently being added to the vertex cover set.   #
   #     IF node color is blue, that node is not part of the vertex cover.                              #   
   #     IF edge color is red, that edge is covered by the choosen vertex.                              #
   #     IF edge color is blue, that edge is not yet colored.                                           #
   #     IN the final output, all the edges have to be in color red.                                    #
   ######################################################################################################'''

def greedy_vc(input_graph, edj,g):
    cover = []
    valid, num_edge = valid_cover(input_graph, cover)
    
    while not valid:
        m = [x for x in range(0, len(num_edge)) if num_edge[x] == max(num_edge)][0]
        #print("m ki value hai")
        #print(m)
        cover.append(m)
        

        
        g.add_node(4)
        
       
        g.add_edges_from(edj)
        pylab.show()
        fig = pylab.figure()


        color_map = []
        color_map_1= []
        flag=0
        for node in g:
            if (node in cover)and(node==m):
                color_map.append('yellow')
            elif(node in cover):
                color_map.append('red')
                
            else: color_map.append('blue')
            print(color_map)
        etcvariable=int(len(edj)/2)
        #print(type(etcvariable))
        etc=[[] for _s in range(etcvariable)] 
        #1. making a list of concerned edges only since we are not having a list of edges(edj counts 1,2 and 2,1 seperately).
        st=0
        #st1=0
        p=0
        fls=0
        for i in range(len(graph)):
            for j in range(len(graph)):
                if(graph[i][j]==1):
                    st+=1
                    if(st==1):
                        etc[p].append(i)
                        etc[p].append(j)
                        p=p+1 
                      
                        #print("bbbbbbbbbbbbbbbbnnnnnnnnnnnnnnmmmmmmmmmmmmmmm")
                        #print(etc)
                        #print(etc[0][1])
                    else:
                        for k in range(p):
                            if(i==etc[k][1] and j==etc[k][0]):
                                fls=1 
                                break
                            
                        if(fls==0):
                            etc[p].append(i)
                            etc[p].append(j)
                            p=p+1 
                    fls=0
        #1.end
        #print("gggggggggggggggggggggggggggggggggggggggggggggggggggggggggg")
        #print(etc)
        #2. Making a list of colors which will be affected by covered node and also non-effected node's color.   
        for i in range(len(etc)):
            for j in range(len(cover)):
                if(cover[j]==etc[i][0] or cover[j]==etc[i][1]):
                    color_map_1.append('red')
                    flag=1
                    break
            if(flag==0):
                color_map_1.append('green') 
            flag=0  
        #nx.draw(g, pos=nx.get_node_attributes(g,'Position'))
        #print("pppppppppppppppppppppppppppppp")
        #2.end
        #3. drawing the network with colors and closing the figure after taking 5s pause.
        nx.draw(g,node_color = color_map,edge_color =color_map_1,with_labels = True)
        #edge_color =color_map_1
       
        #nx.draw(g,edge_color="red",with_labels = True)
        fig.canvas.draw()
        pylab.draw()
        pause(10)
        pylab.close(fig)
        #3.end

        
        valid, num_edge = valid_cover(input_graph, cover)
        
    return cover

def valid_cover(graph, cover):
    valid = True
    num_edge = [0] * len(graph)
    #print("numegde fkffkf")
    #print(num_edge)
    for i in range(0, len(graph)):
        for j in range(i, len(graph)):
            if graph[i][j] == 1:
                if (i not in cover) and (j not in cover):
                    valid = False
                    num_edge[i] += 1
                    num_edge[j] += 1
    return valid, num_edge
list1=[]
n=0
graph = [[0, 1, 1, 1, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [1, 0, 1, 0, 1],
         [1, 1, 1, 1, 0]]

for i in range(len(graph)):
    for j in range(len(graph)):
        if(graph[i][j]==1):
            n=n+1
#print(n)


edj=[[] for _s in range(n)]    #test
z=0
for i in range(len(graph)):
    for j in range(len(graph)):
        if(graph[i][j]==1):
            edj[z].append(i)
            edj[z].append(j)
            z=z+1              #test
#Section for vertex cover
glen=len(graph)
print(glen)
for i in range(glen):
    list1.append(i)
print(list1)        #LIST OF EDGES

g=nx.Graph()
cover = greedy_vc(graph,edj,g) #Function call
print(cover)
