echo "Copy trajectory text files"
cp eval_test_set/*/job_*/est/boreas/*.txt submission

echo "zip submission"
cd submission
zip -r test-odometry.zip *.txt *.yaml
cd ../

echo "Copy .zip to boreas folder"
cd
cp submission/test-odometry.zip /home/daniel/cfear_dev_ws/src/pyboreas/pyboreas/eval/test-odometry.zip




