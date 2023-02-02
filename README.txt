Sparsely Connected Autoencoder 4 Single Cell Rna-sEq dAta Mining
The package is organised in R functions controlling the execution of docker containers embedding the Sparsely Connected Autoencoder (SCA).
The package also provides a version with jupyter lab interface.
To know more about the SCA please refer to the following papers:
  1: Alessandri L, Calogero RA. Functional-Feature-Based Data Reduction Using Sparsely Connected Autoencoders. Methods Mol Biol. 2023;2584:231-240. doi 10.1007/978-1-0716-2756-3_11. PMID: 36495453.
  2: Alessandri et al. Sparsely Connected Autoencoders: A Multi-Purpose Tool for Single Cell omics Analysis. Int J Mol Sci. 2021 Nov 25;22(23):12755. doi: 10.3390/ijms222312755. PMID: 34884559; PMCID: PMC8657975.
  3: Alessandri et al. Sparsely-connected autoencoder (SCA) for single cell RNAseq data mining. NPJ Syst Biol Appl. 2021 Jan 5;7(1):1. doi:10.1038/s41540-020-00162-6. PMID: 33402683; PMCID: PMC7785742.
The R functions required to execute the SCA are located in RFunction folder and organised in the following folders:
  - 1_AE
  - 2_deepCL
  - 3_PB/PB_GPU
In the folder 1_AE are present two folders AE_CPU and AE_GPU. In the previoulsy indicated folders are present and an examplary folder (ExampleRFunction) providing and example how to run the SCA. 
