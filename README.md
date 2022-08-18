# USB FTP Synchronizer

The USB FTP Synchronizer ensures that a removable device, namely a USB, is kept in sync with a local FTP server when connected and merges the data stored in the device, solving any conflicts that may arise from both mediums.


# Planned features

- [x] USB Detection (in progress)
- [ ] FTP Server
- [ ] USB - FTP Synchronizer
- [ ] USB - FTP Conflict Resolution
- [ ] Backup of data
- [ ] GUI
- [ ] Run as a service

## Why

One way to manage one owns files between different devices is via the use of an FTP server. The issue with this is that it may not be possible to easily configure a connection to the server for different reasons, such as using a machine that is not owned by yourself and comes with limited access. Meanwhile, a USB is an easy medium to move data around regardless of the machine used, but can be a hassle to carry around, is bothersome when using multiple devices, and can't be used simultaneously in multiple devices.

To solve this, this utility aims to enable the user to use both the FTP server and USB independently, and when the USB is connected to the machine, both mediums are synced, making the data readily available.
