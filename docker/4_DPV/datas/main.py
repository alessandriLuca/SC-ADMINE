import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import umap
from sklearn.manifold import TSNE
import sys
import os
print(np.asarray(sys.argv).shape[0])
if np.asarray(sys.argv).shape[0] ==1:
    matrixName='latentSpace.csv'
    cloutput='clustering.output.csv'
    sep=","
    perplexity=30
    n_iter=250
    n_neighbors=15
    min_dist=0.1
    tsneplot=1
    umapplot=1
else:
    matrixName=sys.argv[1]
    cloutput=sys.argv[2]
    sep=sys.argv[3]
    perplexity=int(sys.argv[4])
    n_iter=int(sys.argv[5])
    if n_iter<250:
        n_iter=250
    n_neighbors=int(sys.argv[6])
    min_dist=float(sys.argv[7])
    tsneplot=int(sys.argv[8])
    umapplot=int(sys.argv[9])
if sep == "tab":
    sep="\t"
base, ext = os.path.splitext(matrixName)
# Carica i dati dai file csv
latent_space = pd.read_csv("scratch/"+matrixName, header=0, index_col=0,sep=sep)
clustering_output = pd.read_csv("scratch/"+cloutput, header=0, index_col=0,sep=sep)
# Scegliere i colori
colors = ['red', 'blue', 'green', 'purple', 'orange', 'brown', 'pink', 'grey', 'olive', 'cyan']
# Trovare i cluster esistenti
clusters = clustering_output['Belonging_cluster'].unique()

# Eseguire il plot UMAP
if umapplot==1:
    reducer = umap.UMAP(min_dist=min_dist,n_neighbors=n_neighbors)
    umap_embedding = reducer.fit_transform(latent_space.T)
    for cluster in clusters:
        color = colors[cluster]
        plt.scatter(umap_embedding[clustering_output["Belonging_cluster"] == cluster, 0],
                umap_embedding[clustering_output["Belonging_cluster"] == cluster, 1],
                c=color, label=f'Cluster {cluster}',s=2)
    plt.legend()
    plt.savefig("/scratch/"+base+"umap.pdf")
    plt.clf()
if tsneplot==1:
    tsne = TSNE(n_components=2,perplexity=perplexity,n_iter=n_iter)
    projected = tsne.fit_transform(latent_space.T)[:,[0,1]]
    for cluster in clusters:
        color = colors[cluster]
        plt.scatter(projected[clustering_output["Belonging_cluster"] == cluster, 0],
                    projected[clustering_output["Belonging_cluster"] == cluster, 1],
                    c=color, label=f'Cluster {cluster}',s=2)
    plt.legend()
    plt.savefig("/scratch/"+base+"tsne.pdf")
    plt.clf()
os.system("chmod 777 -R /scratch")
# Colorare i punti



