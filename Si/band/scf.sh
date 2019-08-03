#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=40
#SBATCH --time=00:30:00
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=slurmnotifs@gmail.com
#SBATCH --account=def-maassenj
#SBATCH --job-name=Si_scf_test
#SBATCH --mem=80G

module purge 
module load nixpkgs/16.09 
module load gcc/7.3.0 
module load openmpi/3.1.2 
module load quantumespresso/6.4 

srun pw.x < scf.in > scf.out
