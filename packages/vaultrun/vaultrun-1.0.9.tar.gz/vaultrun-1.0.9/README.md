# vault-cli
Vault cli helper

# Requirements
[rofi](https://github.com/davatorium/rofi) or [dmenu](https://tools.suckless.org/dmenu/) needs to be installed.

config file should be located at `/home/{user}/.config/vaultrun/config` with:

```
[<NAME>]
mount_point=<Secret mount point>
secret_path=<Secret path to query>
```

# Installation
```bash
python -m pip3 install vaultrun
```

# Usage
```bash
vaultrun
```
