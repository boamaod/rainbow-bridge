# testing on ubuntu 16.04.1

sudo apt-get install libpurple-dev libjson-glib-dev cmake gcc
git clone git://github.com/EionRobb/skype4pidgin.git
cd skype4pidgin/skypeweb
mkdir build
cd build
cmake ..
cpack
sudo dpkg -i skypeweb-1.2.0-Linux.deb
cd ../../..

sudo apt-get install screen python-pip python-gobject
pip install pydbus
git clone https://github.com/boamaod/rainbow-bridge.git
cd rainbow-bridge

# to start the relay on terminal
# (configure finch/pidgin and obtain chat names before)

dbus-launch screen -S rainbow -dmLU -t 0 finch
sleep 30
screen -S rainbow -X screen -t 1
screen -S rainbow -p1 -X stuff $'./rainbow-bridge.py\n'
