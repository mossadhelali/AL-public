#!usr/bin/bash

sudo apt install curl
sudo apt install -y virtualbox

curl -O https://releases.hashicorp.com/vagrant/2.2.14/vagrant_2.2.14_x86_64.deb

sudo apt install ./vagrant_2.2.14_x86_64.deb

rm vagrant_2.2.14_x86_64.deb

vagrant plugin install vagrant-disksize