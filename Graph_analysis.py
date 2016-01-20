import pandas as pandas
caption = pandas.read_csv('list.csv')
print len(caption)
import re
import itertools as it
import networkx as nx
proper_noun_regex = r'([A-Z][A-Za-z-]*(,?\s+(\b(and|von|de|van der|van|der)\b))?(\s[A-Z][A-Za-z\'-]*)*)'
List_name=[]

G=nx.MultiGraph()

for i in range(len(caption)):
#for i in range(1000):
    name=[]
    string=caption.ix[i,0]
    if len(string)<250:
       caption_temp=re.findall(proper_noun_regex, string)
    #print string
       for j in range(len(caption_temp)):
           name_temp=caption_temp[j]
           if len(name_temp[0])>5:
               name.append(name_temp[0])
           if 'The' in name:
               name.remove('The')
           if 'Dr' in name:
               name.remove('Dr')
           if 'Verdana'in name:
               name.remove('Verdana')
           if 'Helvetica'in name:
               name.remove('Helvetica')
           if 'Chairman'in name:
               name.remove('Chairman') 
           if 'Director'in name:
               name.remove('Director') 
           if 'Guests'in name:
               name.remove('Guests') 
           if 'President'in name:
               name.remove('President') 
           if 'Hospital' in name:
               name.remove('Hospital')
           if 'Special Surgery' in name:
               name.remove('Special Surgery')
           if 'Executive Director'in name:
               name.remove('Executive Director')
           if 'New York'in name:
               name.remove('New York')
           if 'Museum'in name:
               name.remove('Museum') 
           if 'Photographs'in name:
               name.remove('Photographs') 
           if 'Children'in name:
               name.remove('Children') 
           if 'The Society'in name:
               name.remove('The Society') 
           if 'Dinner'in name:
               name.remove('Dinner') 
           if 'Board Member'in name:
               name.remove('Board Member') 
           if 'Castle'in name:
               name.remove('Castle') 
       if len(name)>2:
           _=[G.add_edge(c[0],c[1],weight=1) for c in it.combinations(name,2)]
       elif len(name)>1: G.add_edge(name[0],name[1],weight=1)   
      
    #make the graph from the multigraph (needed for pagerank)
    Gg = nx.Graph()
    for u,v,data in G.edges_iter(data=True):
        if Gg.has_edge(u,v):
            Gg[u][v]['weight'] += 1
        else:
            Gg.add_edge(u, v, weight=1)
    # get pagerank, 0.85 is default
    pr=nx.pagerank(Gg)
    pranalysis=pd.DataFrame(pr.values(),index=pr.keys()).sort(0,ascending=False)
    #get the degrees for each person
    analysis=pd.DataFrame(G.degree().values(),index=G.degree().keys()).sort(0,ascending=False)
    #find the number of friends each person may have by being in shared pictures
    wedge=[[g[0],g[1],g[2]['weight']] for g in Gg.edges(data=True)]
    friends=pd.DataFrame(wedge,columns=['n1','n2','weight']).sort('weight',ascending=False)
    friends.index=range(len(friends))
