
# Alion Ai Challenge 2109

This document describes how to duplicate the creation of my submission.

## Setup

Initialize the Jetson Nano device using the following procedures:

* Flash the current Jetson Nano developer kit image onto a 64 GB microSD card.
* Use a jumper to short the J48 pins on the device to support powering from the adapter instead of a USB cable. A USB cable does not provide sufficient power to keep the device powered on.
* Connect the necessary peripherals (keyboard, mouse, monitor, USB wifi).
* Boot the device.
* Follow the boot instructions (accept terms of use, configure locale, create user, connect to wifi, etc.).
* Install an `~/.ssh/authorized_keys` file containing a public SSH key to allow passwordless SSH onto the device.
* The Ubuntu release that comes with the Jetson Nano developer kit image is slightly out-of-date. Updated it via these commands:

```
sudo apt update -y && sudo apt upgrade -y
```

## Source Code

Retrieve the source code from the repository on Github and initialize directory structures:

```
cd /opt
git config --global user.email "mday@eitccorp.com"
git config --global user.name "mday"
sudo git clone https://github.com/mtday/ai-challenge.git
sudo mkdir nexrad-archive
sudo chown mday ai-challenge
sudo chown mday nexrad-archive
```

The rest of this document will assume you are working out of the `ai-challenge` directory.

```
cd ai-challenge
```



