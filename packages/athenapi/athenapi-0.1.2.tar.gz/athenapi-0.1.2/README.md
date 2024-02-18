# Athena Pi


## Setup

### Hardwares

You need to buy the following board + components and assemble them together

+ Main board
  - https://thepihut.com/products/raspberry-pi-zero-2?variant=41181426942147
  - Make sure you buy the one with GPIO headers
+ Batter hut for 0
  - https://thepihut.com/products/uninterruptible-power-supply-ups-hat-for-raspberry-pi-zero
+ Audio hut
  - https://thepihut.com/products/iqaudio-codec-zero
+ Speaker
  - https://thepihut.com/products/mini-oval-speaker-with-short-wires-8-ohm-1-watt
+ sd card
  - any micro sd card > 50 GB is fine.
  

### OS Image

Download Raspberry Pi Imager. Then choose Raspberry pi *lite* OS. (without desktop).

Make sure you have hostname, wifi and ssh setup correctly in your default config.


### Service setup

1. Install [ansible](https://github.com/ansible/ansible) on your laptop.
1. Start your AthenaPi by turning on the power switch button. It will take 10 minutes for the first boot.
1. Make sure you can run `ssh pi@hostname` before you do the following
1. Change ./device/inventory to replace `rpi0-1` with your pi's hostname
1. Run the following command and enter your open ai key as prompt instructed.

```
cd device
ansible-playbook -i inventory playbook.yml"
```