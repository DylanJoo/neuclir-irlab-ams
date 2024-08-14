
source ${HOME}/.bashrc
cd ~/neuclir-irlab-ams/submissions

for file in submission-test*jsonl;do 
    # neuclir/1/fas
    cat ${file} | grep neuclir/1/fas  > flatten/${file/submission-/fas_}
    # neuclir/1/zho
    cat ${file} | grep neuclir/1/zho  > flatten/${file/submission-/zho_}
    # neuclir/1/rus
    cat ${file} | grep neuclir/1/rus  > flatten/${file/submission-/rus_}
done
