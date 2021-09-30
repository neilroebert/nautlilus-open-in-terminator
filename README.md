
# Open in terminator

A plugin for Nautilus that allows you to open the directory in the current window, in terminator.

I use GNOME as my linux distro flavour, but I don't really like the default _gnome-terminal_. Nautilus contains a contextual menu option that opens the current directory in terminal, but this opens it in the default teminal. I read a couple of guides on how to change this, but none of them ever worked. So I wrote a plugin for Nautilus that adds a menu item that allows you to open the current working directory in terminator.

## Installation

### Prerequisites
This assumes you already have terminator installed on your system. The only dependancy that you would need is the Nautilus Python module. This can be installed by using the followng command:

```sh
sudo apt install python3-nautilus 
```
Next you would need to create a directory for the plugin. This can be be done by running the following command:

```sh
mkdir -p ~/.local/share/nautilus-python/extensions 
```
### Download the module

This can be downloaded by using git, or just by downloading it as a zip.
```sh
git clone https://github.com/neilroebert/nautlilus-open-in-terminator.git
```
Move the files to the correct directory.
```sh
cd nautlilus-open-in-terminator
cp nautilus-terminator.p* ~/.local/share/nautilus-python/extensions/
```

To get it working you have to restart Nautilus. Just kill the process and open it up again.
```sh
killall nautilus
```
I hope this helps you :+1:
