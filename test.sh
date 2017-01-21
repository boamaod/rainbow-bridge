# tested on ubuntu 16.04.1 and raspbian 8.0

# https://github.com/EionRobb/skype4pidgin/tree/master/skypeweb#building-deb-package-for-debianubuntumint

sudo apt-get install libpurple-dev libjson-glib-dev cmake gcc
git clone git://github.com/EionRobb/skype4pidgin.git
cd skype4pidgin/skypeweb
mkdir build
cd build
cmake ..
cpack
sudo dpkg -i skypeweb-1.2.0-Linux.deb
cd ../../..

# https://github.com/dequis/purple-facebook/wiki/Building-on-*NIX

wget https://github.com/dequis/purple-facebook/releases/download/66ee77378d82/purple-facebook-66ee77378d82.tar.gz
tar xvf purple-facebook-66ee77378d82.tar.gz
cd purple-facebook-66ee77378d82/
./configure
make
sudo make install

# https://github.com/majn/telegram-purple#building-from-source

sudo apt-get install libgcrypt20-dev libpurple-dev libwebp-dev gettext
git clone --recursive https://github.com/majn/telegram-purple
cd telegram-purple
./configure
make
sudo make install

# the bridge itself

sudo apt-get install screen finch python-pip python-gobject
pip install pydbus
git clone https://github.com/boamaod/rainbow-bridge.git
cd rainbow-bridge

# to start the relay on terminal
# (configure finch/pidgin and obtain chat names before)

dbus-launch screen -S rainbow -dmLU -t 0 finch
sleep 30
screen -S rainbow -X screen -t 1
screen -S rainbow -p 1 -X stuff $'./rainbow-bridge.py\n'
