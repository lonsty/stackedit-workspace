# Install from NVM ( Node Version Manager )

### Install & Update script

To  **install**  or  **update**  nvm, you should run the  [install script](https://github.com/nvm-sh/nvm/blob/v0.35.1/install.sh). To do that, you may either download and run the script manually, or use the following cURL or Wget command:
```
$ curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.1/install.sh | bash

$ wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.1/install.sh | bash
```
Running either of the above commands downloads a script and runs it. The script clones the nvm repository to  `~/.nvm`, and adds the source lines from the snippet below to your profile (`~/.bash_profile`,  `~/.zshrc`,  `~/.profile`, or  `~/.bashrc`).

```
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
```

### Install Node.js and NPM

Instal the **Long-term support** verison
```
$ nvm install --lts
```

### npm set proxy

List npm config
```
$ npm config list
```

Set npm via proxy
```
$ npm config set proxy http://proxy.company.com:8080
$ npm config set https-proxy http://proxy.company.com:8080
```

*config file `~/.npmrc`*
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTM1NzU4MTg0MV19
-->