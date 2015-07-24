# Python Raspberry Pi 2 setup

## Installing the Operating System


## Initial setup
### Run updates
<pre><code>
pacman -Syu
reboot
</code></pre>

### Change passwords and add a non-root user
<pre><code>
passwd
useradd -Um natalie
passwd natalie
su - natalie
mkdir .ssh && cd .ssh
nano authorized_keys
</code></pre>

Add your public key to the <code>authorized_keys</code> file.  Don't have one?  [Set it up here!](https://wiki.archlinux.org/index.php/SSH_keys#Generating_an_SSH_key_pair)  It takes 5 minutes, is easier than remembering unique passwords for each machine, and is more secure than passwords alone.


after rebooting, set up ssh,


## Installing additional packages using pacman
<pre><code> pacman -S python-pip tk gcc xorg-xinit xorg-server xorg-server-utils openbox lxde xf86-video-fbdev dbus
ln -s /home/$username/.Xauthority /root/.Xauthority
</code></pre>

The first line installs a basic LXDE desktop, OpenBox window manager, all of the X Window Server packages needed, as well as some Python utilities such as pip and tkinter.

The second line creates a symbolic link between the .Xauthority file in the user's directory to root.  Normally, you don't want to run X as root for security reasons.  However, as this machine has no access to a network outside of my LAN, I figured it was an acceptable risk.  

## Installing additional packages using pip
<pre><code> pip install RPi.GPIO pygubu </code></pre>
