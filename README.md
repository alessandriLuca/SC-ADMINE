## Sparsely Connected Autoencoder for Data Mining in Single Cell RNAseq

### Introduction

Single-cell RNA-sequencing (scRNA-seq) provides the ability to profile the entire transcriptome of individual cells. A crucial step in scRNA-seq data analysis is to identify cellular heterogeneity in complex samples or tissues. However, scRNA-seq is characterized by high-dimensional, sparse, and noisy data due to technical noise and a high rate of dropouts which limits its quantitative accuracy [[1](https://pubmed.ncbi.nlm.nih.gov/33959753/)].
Dimensionality reduction plays a critical role in the subsequent analysis of scRNA-seq data [[2](https://pubmed.ncbi.nlm.nih.gov/33833778/)]. By reducing the number of dimensions, it can effectively eliminate noise and improve the results of downstream analyses such as clustering.
Autoencoders, a type of neural network that compresses input into a lower-dimensional representation called a latent-space and then reconstructs the output, have been applied to denoise single cell data. Recently, we introduced a novel class of autoencoder called the sparsely-connected-autoencoder (SCA) [3,4]. This type of autoencoder stands out because it allows direct utilization of the information contained in the latent-space, as each node in the latent-space is connected to a specific set of input/output nodes [4].
The connections between input/output nodes and the latent-space are biologically determined. Each latent-space node represents a biological meta-feature that is modeled based on experimentally verified relationships among input/output genes. Latent-space meta-features can be transcription factors, miRNAs, kinases, pathways, molecular signatures, chromatin compartments, etc. SCA latent space is used to uncover the underlying biological signatures that drive cell subpopulation clustering [4].
Previously, SCA was only available for CPU platforms [3] and the results of SCA analysis required an external clustering tool for further analysis. In this work, we present a GPU-based implementation of SCA, which greatly improves computational performance. Additionally, we have integrated an unsupervised deep clustering procedure directly into SCA [5], which provides a better representation of the underlying biology.

### Implementation

We have developed three tools based on sparsely connected autoencoders, namely AE, PB, and deepCL. The three tools are available at https://github.com/alessandriLuca/SC-ADMINE. Initially, AE and PB were only compatible with CPU architecture, but we have now improved their performance by implementing them for GPU architecture, as shown in Fig. 1A and B. This is the first time deepCL has been introduced.
AE is a tool that performs a sparsely connected autoencoder (SCA), as previously outlined in [6], It takes a matrix of single-cell RNA expression data as input and produces a cumulative sum matrix of the modeled latent spaces. The cumulative matrix can then be utilized for sub-population discovery through clustering [7,4].
DeepCL is a novel tool that can be run on both CPU and GPU architectures, and it incorporates unsupervised deep clustering into the SCA. The technique, called Deep Embedded Clustering, was proposed by Xie and colleagues [8] and involves learning feature representations and cluster assignments simultaneously using a deep neural network. By incorporating this approach into the SCA, deepCL aims to map the data space to a biologically meaningful feature space, iteratively optimizing a clustering objective.
All three tools have been packaged within a Docker container to ensure computational and functional reproducibility. PB is a tool designed to construct pseudo-bulk experiments that serve as pseudo-replicates for cell sub-populations identified through clustering analysis [3]. The concept behind this approach is that genes defining a particular cell cluster will be the non-noise signals captured by the hidden layer of the SCA. By repeating the SCA modelling multiple times, we can create pseudo-bulk RNAseq experiments representing pseudo-replicates for each cluster's gene expression. These pseudo-bulk experiments can then be used to identify cluster-specific genes through differential expression analysis using conventional bulk RNA-seq tools [9].
![image](https://github.com/alessandriLuca/SC-ADMINE/assets/10886147/4a383e47-0d12-495d-90ce-de965c260331)

### AE and deepCL performances

We evaluated the results obtainable using AE and deepCL on the same datasets. We also compared the computing time for AE on CPU and GPU and for deepCL on GPU. The test was carried out using a set of single cell datasets from the colon immune cell atlas (https://www.gutcellatlas.org/, [10]).The evaluation was conducted on HPC4AI University of Torino cloud infrastructure (https://hpc4ai.unito.it/), using an instance with 128 GB RAM, 18 cores and one V100 NVIDIA GPU. 
For AE the advantage of using GPU is getting more evident as the number of cells increases, showing to be 2.56 times faster than CPU implementation at 30,000 cells, with a 33% improvement in speed moving from 10,000 to 30,000 cells, Fig. 1A. DeepCL performances, where evaluated only on GPU, using a fix number of k clusters, i.e. 5 (N.B. the number of clusters defined in deepCL does not affect the computing time, Fig. 1A, squared dots). The integration of the deep clustering in the SCA significantly improves the analysis time, Fig. 1A. The assembly of pseudo-bulk RNAseq experiment using PB [9], Fig. 1B, being less computationally intensive with respect to AE and deepCL, does not show a significant improvement in execution time using a GPU intrastructure with respect to CPU.

### Dimensionality reduction features of AE and deepCL

In the case of AE, 40 latent space model matrices are cumulatively summed to produce the output, which is then subjected to k-means clustering with a value of k=6, Fig. 1C. On the other hand, deepCL incorporates clustering as part of the sparsely connected autoencoder model and the computation terminates once the clustering results converge, Fig. 1D. The clustering generated by deepCL, when compared with the one generated by AE, appears to offer a more comprehensive understanding of the similarities among cell subpopulations, characterizing the different cell lines. Specifically, cluster 5 in Fig. 1D is present across all 5 cell lines, suggesting the existence of a set of cells in each cell line sharing a common set of genomic regions characterized by similar expression.



Fig. 1: Sparsely connected autoencoders dimensionality reduction driven by genes associate to chromosomal cytobands. The purpose of reducing chromosomal cytobands data is to identify genomic loci specific to a particular cell line that result in coordinated gene expression, which cannot be discerned by solely examining individual gene expression. A) Computing time for the execution of sparsely connected autoencoders using AE on CPU, AE on GPU and deepCL GPU, which integrates in one application AE and k-mean deep clustering. B) Computing time for the execution of pseudo-bulk RNAseq, 5 replicates for each cluster, by mean of sparsely connected autoencoders (PB), CPU and GPU implementation. C) AE GPU + K-mean clustering dimensionality data reduction results, k=6. D) deepCL dimensionality data reduction results, k=6.![image](https://github.com/alessandriLuca/SC-ADMINE/assets/10886147/f4c56a33-30b9-450f-b168-a8a5909f0ff0)

### Conclusions

The use of a GPU to implement AE provides substantial time optimization, particularly as there is an increasing need for larger single cell experiments. Moreover, incorporating deep clustering into the sparsely connected autoencoder model can significantly enhance analysis time. Additionally, compared to AE combined with k-means clustering, deepCL appears to offer a more comprehensive understanding of the similarities present among various cell lines.



## About this github

The package is organized into R functions that control the execution of docker containers that embed the Sparsely Connected Autoencoder (SCA). To learn more about the SCA, please refer to the following papers:

- Alessandri L, Calogero RA. Functional-Feature-Based Data Reduction Using Sparsely Connected Autoencoders. Methods Mol Biol. 2023;2584:231-240. doi 10.1007/978-1-0716-2756-3_11. PMID: 36495453.
- Alessandri et al. Sparsely Connected Autoencoders: A Multi-Purpose Tool for Single Cell omics Analysis. Int J Mol Sci. 2021 Nov 25;22(23):12755. doi: 10.3390/ijms222312755. PMID: 34884559.
- Alessandri et al. Sparsely-connected autoencoder (SCA) for single cell RNAseq data mining. NPJ Syst Biol Appl. 2021 Jan 5;7(1):1. doi:10.1038/s41540-020-00162-6. PMID: 33402683.

### R Functions for SCA
The R functions needed to perform the SCA can be found in the `RFunction` folder, which is organized into the following sub-folders:

### 1_AE
Runs a sparse autoencoder that produces a cumulative sum of the modeled hidden layer and the matrices of all modeled hidden layers as output. The cumulative matrix can be used as input for clustering algorithms such as the one implemented in the Seurat software.

### 2_deepCL
Runs a sparse autoencoder with a deep clustering algorithm embedded. The output is the latent space on which clustering was performed, along with a file indicating the cluster association for each cell. The clusters can be visualized on UMAP/tSne representations of the latent space.

### 3_PB/PB_GPU
Runs a sparse autoencoder on the output from 2_deepCL to produce a pseudo-bulk RNAseq experiment.

### 4_DPV
Provides a visualisation of the latent space data using either tSne or UMAP algorithm.

For functions 1, 2, and 3, you can choose to run them on a GPU or CPU (docker and functions for both options are provided).

User might decide to build a new docker, by modify the files available in the docker folder, or use the docker available on our repository on docker hub (`repbioinfo`). 

### INSTALL 
```
install.packages("devtools")
library(devtools)
install_github("alessandriLuca/SC-ADMINE", ref="main")
```
