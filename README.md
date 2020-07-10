## putty에서
sudo apt-get update

sudo apt-get upgrade

sudo apt-get purge realvnc-vnc-server

sudo apt-get install xrdp


## 원격 데스크톱에서
sudo apt-get install build-essential cmake pkg-config

sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev

sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev

sudo apt-get install libxvidcore-dev libx264-dev

sudo apt-get install libgtk2.0-dev libgtk3-dev

sudo apt-get install libatlas-base-dev gfortran

sudo apt-get install python2.7-dev python3.0-dev

sudo apt install libqt4-test

pip3 install numpy

pip3 install opencv-python==3.4.4.19


## raspberry 창에서 tensorflow 다운받기

### get a fresh start
$ sudo apt-get update

$ sudo apt-get upgrade

### remove old versions, if not placed in a virtual environment (let pip search for them)
$ sudo pip uninstall tensorflow

$ sudo pip3 uninstall tensorflow

### install the dependencies (if not already onboard)
$ sudo apt-get install gfortran

$ sudo apt-get install libhdf5-dev libc-ares-dev libeigen3-dev

$ sudo apt-get install libatlas-base-dev libopenblas-dev libblas-dev

$ sudo apt-get install liblapack-dev cython

$ sudo pip3 install pybind11

$ sudo pip3 install h5py

### download the wheel
$ wget https://github.com/Qengineering/Tensorflow-Raspberry-Pi/raw/master/tensorflow-2.1.0-cp37-cp37m-linux_armv7l.whl

### install TensorFlow
$ sudo -H pip3 install tensorflow-2.1.0-cp37-cp37m-linux_armv7l.whl

### and complete the installation by rebooting
$ reboot
