from bassist.util import run


def show(config):
    run(f"ssh {config['host']} quota")
