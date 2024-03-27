## Install

create catkin_ws
```
Git clone cfear (private repo)
git clone github.com:dan11003/radar_kitti_benchmark.git branch export-less
git clone https://github.com/utiasASRL/pyboreas.git

cd .. catkin build
source devel/setup.bash
```

## Run
```
roscd cfear_radarodometry/launch/oxford/eval/
./1.1_boreas_baseline_eval 
```

## Evaluate
Depends on if **test set** or **training set** is evaluated, see commented lines in 1.1_boreas_baseline_eval.

copy result of evaluation to **eval_test_set** or **eval_train_set**, that should end up in something like:

```
val_train_set/boreas_cfear-3-P2D_2024-03-19_1600/
```


```
./eval_all.sh
```



