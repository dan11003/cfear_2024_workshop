# Work in progress -- ICRA radar in robotics workshop 2024
## Present CFEAR evaluation

```
git clone https://github.com/dan11003/cfear_2024_workshop.git # This can take some time
cd cfear_2024_workshop/
python3 cfear_eval.py
```

## (Optional) Rerun experiments
### Install

create catkin_ws
```
git clone cfear (private repo)
git clone github.com:dan11003/radar_kitti_benchmark.git branch export-less
git clone https://github.com/utiasASRL/pyboreas.git

cd ..
catkin build
source devel/setup.bash
```

## Run evaluation
```
roscd cfear_radarodometry/launch/oxford/eval/
./1.1_boreas_baseline_eval 
```
Move evaluation to **cfear_2024_workshop/eval_test_set**

Consistency with pyboreas benchmark can be verified via:
```
eval_all.sh
```

## Prepare submission
./prepare_submission.sh


