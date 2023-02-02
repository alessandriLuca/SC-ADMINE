## Sparsely Connected Autoencoder 4 Single Cell Rna-sEq dAta Mining
The package is organised in R functions controlling the execution of docker containers embedding the Sparsely Connected Autoencoder (SCA).
The package also provides a version with jupyter lab interface.
To know more about the SCA please refer to the following papers:
  1: Alessandri L, Calogero RA. Functional-Feature-Based Data Reduction Using Sparsely Connected Autoencoders. Methods Mol Biol. 2023;2584:231-240. doi 10.1007/978-1-0716-2756-3_11. PMID: 36495453.
  2: Alessandri et al. Sparsely Connected Autoencoders: A Multi-Purpose Tool for Single Cell omics Analysis. Int J Mol Sci. 2021 Nov 25;22(23):12755. doi: 10.3390/ijms222312755. PMID: 34884559.
  3: Alessandri et al. Sparsely-connected autoencoder (SCA) for single cell RNAseq data mining. NPJ Syst Biol Appl. 2021 Jan 5;7(1):1. doi:10.1038/s41540-020-00162-6. PMID: 33402683.
The R functions required to execute the SCA are located in RFunction folder and organised in the following folders:
  - 1_AE: Run a sparsely connected autoencoder, which produces as output a cumulative sum of the modelled hidden layer, as well as the matrices of all the modelled hidden layers. The cumulative matrix can be used as input for clustrering algorithms as te one implemented in Seurat software.
  - 2_deepCL: Run a sparsely connected autoencoder embedding a deepclustering algorithm. The output is the latent space on which clustering was performed together with a file providing the association of each cell to a cluster. Cluster can be than visualised on UMAP/tSne representation of the latent space.
  - 3_PB/PB_GPU: Run a sparsely connected autoencoder to the 
In the folder 1_AE, 2_deepCL and 3_PB/PB_GPU are present two folders XX_CPU and XX_GPU. 
In the previoulsy indicated folders is present an examplary folder (ExampleRFunction) providing and example how to run the SCA. 
