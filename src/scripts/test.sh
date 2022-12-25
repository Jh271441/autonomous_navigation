#!/bin/bash
for i in {0..49} ; do
    n=`expr $i \* 6` # 50 test BARN worlds with equal spacing indices: [0, 6, 12, ..., 294]
        for j in {1..10} ; do            
            # run the test
            python3 run.py --world_idx $n
            ps -ef | grep ros | grep -v grep | awk {'print"kill -9 " $2'} | sh
            sleep 5
        done
done