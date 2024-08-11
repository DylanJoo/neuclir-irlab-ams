#!/bin/sh
# The following lines instruct Slurm to allocate one GPU.
#SBATCH --job-name=std-doc
#SBATCH --partition gpu
#SBATCH --gres=gpu:nvidia_rtx_a6000:1
#SBATCH --mem=32G
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=48:00:00
#SBATCH --output=logs/%x-%j.out

# Set-up the environment.
source ${HOME}/.bashrc
conda activate rag
cd ~/neuclir-irlab-ams

# Start the experiment.

## std-doc: standard rag
# for split in test dev; do
#     python standard.py \
#         --config configs/neuclir.llama3-8b-chat.std-doc.0shot.yaml  \
#         --split ${split} \
#         --eval_file data/requests-${split}-all.jsonl \
#         --candidates_tsv data/hits-${split}-all-translate.tsv \
#         --used_field translation
# done

run_id=irlab-ams-std-translate-llama-8B
for split in dev test; do
    python tools/convert_output_to_submission.py  \
        --report_json results/report-std-doc-${split}-all.json  \
        --run_id ${run_id} \
        --submission submissions/submission-${split}-all-${run_id} \
        --quick_test
done
# submission-dev-all-irlab-ams-poscite.json
# submission-dev-all-irlab-ams-postcite-v.json
