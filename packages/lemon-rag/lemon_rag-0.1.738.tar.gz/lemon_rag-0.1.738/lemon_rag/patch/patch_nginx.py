def get_current_config() -> str:
    with open('/etc/nginx/sites-enabled/app', 'r') as f:
        return f.read()


def write_config(new_config: str):
    with open('/etc/nginx/sites-enabled/app', 'w') as f:
        f.write(new_config)


def patch_nginx() -> bool:
    config = get_current_config()
    if "($request_method = OPTIONS)" in config:
        return False
    config = config.replace(
        "add_header Access-Control-Allow-Origin $http_origin always;",
        "add_header Access-Control-Allow-Origin '*';"
    )
    config = config.replace(
        "proxy_set_header  X-Real-IP        $remote_addr;",
        """proxy_set_header  X-Real-IP        $remote_addr;
        if ($request_method = OPTIONS) {
            return 200;
        }
        proxy_http_version 1.1;"""
    )
    write_config(config)
    return True


def restart_nginx() -> None:
    import subprocess

    command = "nginx -s reload"
    subprocess.run(command, shell=True)


def patch_and_restart_nginx():
    if patch_nginx():
        restart_nginx()


if __name__ == '__main__':
    patch_nginx()