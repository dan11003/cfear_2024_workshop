#  Input: pyboreas/eval folder, and folder to evaluation of a method.
#  The script perform the pyboreas odometry evaluation on all sequences (jobs)

boreaspy_eval_folder="/home/daniel/cfear_dev_ws/src/pyboreas/pyboreas/eval"
eval_folder="eval_train_set"
boreas_data_folder="/media/daniel/slow_m2/boreas/boreas_train/"
# Loop through each folder in the root folder
rm -r eval_train_set/*/job_*/est/errors
rm -r eval_train_set/*/job_*/est/plot_error
rm -r eval_train_set/*/job_*/est/plot_path
rm -r eval_test_set/*/job_*/est/errors
rm -r eval_test_set/*/job_*/est/plot_error
rm -r eval_test_set/*/job_*/est/plot_path


for folder in "$eval_folder"/boreas*/*; do
    if [ -d "$folder" ]; then  # Check if it's a directory
        echo "Processing folder: "
        echo "Evaluate: $folder"
        python3 ${boreaspy_eval_folder}/odometry.py --pred $folder/est/boreas --gt $boreas_data_folder --radar
        # Add your commands here to process each folder
        # For example, you can perform operations on each folder
    fi
done

