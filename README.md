## Sparsely Connected Autoencoder for Data Mining in Single Cell RNAseq
The package is organized into R functions that control the execution of docker containers that embed the Sparsely Connected Autoencoder (SCA). To learn more about the SCA, please refer to the following papers:

- Alessandri L, Calogero RA. Functional-Feature-Based Data Reduction Using Sparsely Connected Autoencoders. Methods Mol Biol. 2023;2584:231-240. doi 10.1007/978-1-0716-2756-3_11. PMID: 36495453.
- Alessandri et al. Sparsely Connected Autoencoders: A Multi-Purpose Tool for Single Cell omics Analysis. Int J Mol Sci. 2021 Nov 25;22(23):12755. doi: 10.3390/ijms222312755. PMID: 34884559.
- Alessandri et al. Sparsely-connected autoencoder (SCA) for single cell RNAseq data mining. NPJ Syst Biol Appl. 2021 Jan 5;7(1):1. doi:10.1038/s41540-020-00162-6. PMID: 33402683.

## R Functions for SCA
The R functions needed to perform the SCA can be found in the `RFunction` folder, which is organized into the following sub-folders:

## 1_AE
Runs a sparse autoencoder that produces a cumulative sum of the modeled hidden layer and the matrices of all modeled hidden layers as output. The cumulative matrix can be used as input for clustering algorithms such as the one implemented in the Seurat software.

## 2_deepCL
Runs a sparse autoencoder with a deep clustering algorithm embedded. The output is the latent space on which clustering was performed, along with a file indicating the cluster association for each cell. The clusters can be visualized on UMAP/tSne representations of the latent space.

## 3_PB/PB_GPU
Runs a sparse autoencoder on the output from 2_deepCL to produce a pseudo-bulk RNAseq experiment.

## 4_DPV
Runs a Dense Projection + Visualization using either the tSne or UMAP algorithm.

For functions 1, 2, and 3, you can choose to run them on a GPU or CPU (docker and functions for both options are provided).

The `docker` folder contains all the necessary files to build each docker from scratch. You can choose to build your own docker, modify it, or use the docker available on our repository (`repbioinfo/`). Only modify and use the folder if you want to use a different/modified docker than the one on the repository.
