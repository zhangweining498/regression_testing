#! /bin/sh
echo "执行退回宿主机操作"
exit

echo "进入指定目录"
cd /home/jenkins_home/workspace/123456/test

echo "执行python脚本"
source runtest.py
