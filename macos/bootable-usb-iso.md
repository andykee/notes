# Making a bootable USB drive from an ISO

Find the device with:
```bash
% diskutil list
```

Unmount the drive:
```bash
% diskutil unmountDisk /dev/disk<N>
```

Dump the ISO to the USB device:
```bash
% sudo dd if=/path/to/image.iso of=/dev/rdisk<N>
```

We’re using the ``/dev/rdisk<N>`` device here rather than ``/dev/disk<N>``. This refers to a “raw device” interface to the same disk, which is faster. The ``bs=4m`` option increases the write performance and it’s optional.


