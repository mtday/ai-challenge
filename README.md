
# Alion Ai Challenge 2109

This document describes how to duplicate the creation of my submission.

## Initial Setup

Initialize the Jetson Nano device using the following procedures:

* Flash the current Jetson Nano developer kit image onto a 64 GB microSD card.
* Use a jumper to short the J48 pins on the device to support powering from the adapter instead of a USB cable. A USB cable does not provide sufficient power to keep the device powered on.
* Connect the necessary peripherals (keyboard, mouse, monitor, USB wifi).
* Boot the device.
* Follow the boot instructions (accept terms of use, configure locale, create user, connect to wifi, etc.).
* Install an `~/.ssh/authorized_keys` file containing a public SSH key to allow passwordless SSH onto the device.
* Add `~/.ssh/id_rsa` and `~/.ssh/id_rsa.pub` files for SSH off the device.

## Update

* The Ubuntu release that comes with the Jetson Nano developer kit image is slightly out-of-date. Updated it via these commands:

```
sudo apt update -y && sudo apt upgrade -y
```

## Personal Setup

Enable vi mode on the terminal command line:

```
echo 'set -o vi' >> ~/.bashrc
```

Use ctrl-l to clear the screen:

```
cat <<EOF > ~/.inputrc
set editing-mode vi
\$if mode=vi

set keymap vi-command
# these are for vi-command mode
Control-l: clear-screen

set keymap vi-insert
# these are for vi-insert mode
Control-l: clear-screen
\$endif
EOF
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



