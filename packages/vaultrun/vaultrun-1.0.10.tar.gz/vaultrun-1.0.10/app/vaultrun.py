import hvac

from app.login import vault_login
from app.utils import call_rofi_dmenu, parse_user_config, which, copy_to_clipboard
from rich import print, pretty


def parse_vault_path(client: hvac.Client, mount_point: str, secret_path: str) -> str:
    all_secrets = client.secrets.kv.v2.list_secrets(mount_point=mount_point, path=secret_path)
    _selected = call_rofi_dmenu(options=all_secrets.get("data", {}).get("keys"), abort=True, prompt=None)
    if _selected.endswith("/"):
        all_secrets = client.secrets.kv.v2.list_secrets(mount_point=mount_point, path=f"{secret_path}/{_selected}")
        selected = call_rofi_dmenu(options=all_secrets.get("data", {}).get("keys"), abort=True, prompt=None)
        if selected.endswith("/"):
            _secret_path = f"{_selected}/{selected}"
            return parse_vault_path(client=client, mount_point=mount_point, secret_path=_secret_path)
        else:
            return f"{_selected}/{selected}"
    else:
        return _selected


def main():
    pretty.install()
    _mount_point, _secret_path = parse_user_config()
    client = vault_login()
    if client and client.is_authenticated():
        user_selection = parse_vault_path(client=client, mount_point=_mount_point, secret_path=_secret_path)
        _secret = client.secrets.kv.v2.read_secret_version(
            mount_point=_mount_point,
            path=f"{_secret_path}/{user_selection}",
            raise_on_deleted_version=False,
        )["data"]["data"]
        key_selected = call_rofi_dmenu(options=["All"] + [*_secret], abort=True, prompt=None)
        if key_selected == "All":
            print(_secret)
        else:
            secret_for_user = _secret[key_selected]
            if which("xsel"):
                copy_to_clipboard(str.encode(secret_for_user))

            print(secret_for_user)


if __name__ == "__main__":
    main()
