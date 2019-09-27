
# Alion Ai Challenge 2019

This document describes how to duplicate the creation of my submission.

## Initial Setup

Initialize the Jetson Nano device using the following procedures:

* Flash the current Jetson Nano developer kit image onto a 64 GB microSD card.
* Use a jumper to short the J48 pins on the device to support powering from the adapter instead of a USB cable. A USB cable does not provide sufficient power to keep the device powered on.
* Connect the necessary peripherals (keyboard, mouse, monitor, USB wifi).
* Boot the device.
* Follow the boot instructions (accept terms of use, configure locale, create user, connect to wifi, etc.).
* Install an `~/.ssh/authorized_keys` file containing a public SSH key to allow passwordless SSH into the device.
* Add `~/.ssh/id_rsa` and `~/.ssh/id_rsa.pub` files for SSH off the device.
* Add `~/.gitconfig` for common git aliases and user info.
* Add this line to `/etc/sudoers` to allow `sudo` without a password: `mday ALL=(ALL) NOPASSWD:ALL`

## Update

The Ubuntu release that comes with the Jetson Nano developer kit image is slightly out-of-date. Update it via these commands:

```
sudo apt update -y && sudo apt upgrade -y
sudo apt autoremove -y
```

## Software Installs

Install additional required software packages:

```
sudo apt-get install -y python3-pip
sudo apt-get install -y libhdf5-serial-dev
sudo apt-get install -y netcdf-bin libnetcdf-dev
sudo apt-get install -y libblas-dev liblapack-dev gfortran
sudo apt-get install -y libfreetype6-dev
```


## Source Code

Initialize directory structures and retrieve the source code from the repository on Github:

```
cd /opt
sudo mkdir ai-challenge
sudo mkdir nexrad-archive
sudo chown mday ai-challenge
sudo chown mday nexrad-archive
git clone git@github.com:mtday/ai-challenge.git
```

The rest of this document will assume you are working out of the `ai-challenge` directory.

```
cd ai-challenge
```

## Python Module Install

Install the necessary python modules. This will take a long time so plan accordingly.

```
pip3 install boto3==1.9.236 matplotlib==3.1.1 netCDF4==1.5.2 numpy==1.17.2 scipy==1.3.1 xarray==0.13.0
pip3 install arm-pyart==1.10.2
```


