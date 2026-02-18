# JPL IT notes

#### Terminal "login incorrect"
I ran into this some time back. A “trick” is to see if you can change from doing a login shell to running the command ``bash -il``. Not sure why this worked, since bash -il actually does all the login stuff - but for some reason this worked. I use iterm, and this can be changed in the profile, going from “Login shell” to “Command”.

I just tried both ``bash -il`` and ``/bin/zsh -i`` and both worked! So it's apparently something specific to what a "login shell" means... very strange. I also use iTerm2 so now I have alternate profiles I can use when this crops up.


#### USB-C monitor stops working on MacOS

1. Unplug monitor from wall
2. Unplug monitor from computer
3. Plug monitor in to computer
4. Plug monitor back in to wall

Note that steps 2 and 3 may be unnecessary

[Reference](https://www.reddit.com/r/macsysadmin/comments/qgypzy/monterey_external_monitor_issues/hpjdnn9/?context=3)
