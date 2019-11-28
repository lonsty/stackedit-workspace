# [Install zsh](https://github.com/robbyrussell/oh-my-zsh/wiki/Installing-ZSH)

## Zsh?

Oh-My-Zsh is a framework for  [Zsh](http://www.zsh.org/), the Z shell.

-   In order for Oh-My-Zsh to work, Zsh must be installed.
    -   Please run  `zsh --version`  to confirm.
    -   Expected result:  `zsh 5.1.1`  or more recent
-   Additionally, Zsh should be set as your default shell.
    -   Please run  `echo $SHELL`  from a new terminal to confirm.
    -   Expected result:  `/usr/bin/zsh`  or similar

## Install and set up zsh as default

If necessary, follow these steps to install Zsh:

1.  There are two main ways to install Zsh

-   with the package manager of your choice,  _e.g._  `sudo apt install zsh`  (see  [below for more examples](https://github.com/robbyrussell/oh-my-zsh/wiki/Installing-ZSH#how-to-install-zsh-in-many-platforms))
-   from  [source](http://zsh.sourceforge.net/Arc/source.html), following  [instructions from the Zsh FAQ](http://zsh.sourceforge.net/FAQ/zshfaq01.html#l7)

2.  Verify installation by running  `zsh --version`. Expected result:  `zsh 5.1.1`  or more recent.
3.  Make it your default shell:  `chsh -s $(which zsh)`

-   Note that this will not work if Zsh is not in your authorized shells list (`/etc/shells`) or if you don't have permission to use  `chsh`. If that's the case  [you'll need to use a different procedure](https://www.google.com/search?q=zsh+default+without+chsh).

4.  Log out and login back again to use your new default shell.
5.  Test that it worked with  `echo $SHELL`. Expected result:  `/bin/zsh`  or similar.
6.  Test with  `$SHELL --version`. Expected result: 'zsh 5.1.1' or similar

# Install [Oh-My-Zsh](https://github.com/robbyrussell/oh-my-zsh)

	sh -c "$(wget -O- https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# Set themes and install plugins for zsh

edit  `~/.zshrc`, change theme to

	ZSH_THEME="agnoster"

Log out and log in back.

**NOTE:**  In all likelihood, you will need to install a  [Powerline-patched font](https://github.com/Lokaltog/powerline-fonts)  for this theme to render correctly.

To test if your terminal and font support it, check that all the necessary characters are supported by copying the following command to your terminal:  `echo "\ue0b0 \u00b1 \ue0a0 \u27a6 \u2718 \u26a1 \u2699"`. The result should look like this:

![](https://gist.githubusercontent.com/agnoster/3712874/raw/characters.png)

#### Plugins

- [zsh-autosuggestsions](https://github.com/zsh-users/zsh-autosuggestions)

		git clone https://github.com/zsh-users/zsh-autosuggestions.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

- [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)
		
		git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

- [autojump](https://github.com/wting/autojump)

		git clone https://github.com/wting/autojump.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/autojump
		cd ~/.oh-my-zsh/custom/plugins/autojump
		./install.sh

- [k](https://github.com/rimraf/k)

		git clone https://github.com/rimraf/k.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/k
		
Edit `~/.zshrc`

	plugins=([plugins...] zsh-autosuggestions zsh-syntax-highlighting autojump k)
		
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyMzYyMDg3MzVdfQ==
-->