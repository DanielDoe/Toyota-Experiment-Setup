#!/bin/bash 
for entry in "assets/test_data"/*
do
  python tools/demo.py image -n yolox-x -c yolox_x.pth --path $entry --conf 0.25 --nms 0.45 --tsize 640 --save_result --device [gpu]  
done

#python tools/demo.py image -n yolox-x -c yolox_x.pth --path assets/view1.jpg --conf 0.25 --nms 0.45 --tsize 640 --save_result --device [gpu]
#python tools/demo.py image -n yolox-x -c yolox_x.pth --path assets/view2.jpg --conf 0.25 --nms 0.45 --tsize 640 --save_result --device [gpu]
#python tools/demo.py image -n yolox-x -c yolox_x.pth --path assets/view3.jpg --conf 0.25 --nms 0.45 --tsize 640 --save_result --device [gpu]
#python tools/demo.py image -n yolox-x -c yolox_x.pth --path assets/view4.jpg --conf 0.25 --nms 0.45 --tsize 640 --save_result --device [gpu]
#python tools/demo.py image -n yolox-x -c yolox_x.pth --path assets/view5.jpg --conf 0.25 --nms 0.45 --tsize 640 --save_result --device [gpu]
