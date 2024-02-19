from argparse import ArgumentParser as _ArgumentParser
from os import mkdir as _mkdir
from os.path import exists as _exists
from sys import exit as _exit, version as _version

from leads import register_controller as _register_controller, MAIN_CONTROLLER as _MAIN_CONTROLLER, \
    initialize_main as _initialize_main, L as _L
from leads_dashboard import get_system_platform as _get_system_platform, load_config as _load_config, \
    DEFAULT_CONFIG as _DEFAULT_CONFIG

if __name__ == '__main__':
    parser = _ArgumentParser(prog="LEADS VeC",
                             description="Lightweight Embedded Assisted Driving System VeC",
                             epilog="ProjectNeura: https://projectneura.org"
                                    "GitHub: https://github.com/ProjectNeura/LEADS")
    parser.add_argument("action", choices=("info", "run"))
    parser.add_argument("-r", "--register", choices=("systemd", "config"), default=None, help="service to register")
    parser.add_argument("-c", "--config", default=None, help="specified configuration file")
    args = parser.parse_args()
    if args.action == "info":
        from leads_vec.__version__ import __version__

        _L.info(f"LEADS Version: {__version__}",
                f"System Platform: {_get_system_platform()}",
                f"Python Version: {_version}",
                sep="\n")
        _exit()
    if args.register == "systemd":
        if _get_system_platform() != "linux":
            _exit("Error: Unsupported operating system")
        if not _exists("/usr/local/leads/config.json"):
            _L.info("Config file not found. Creating \"/usr/local/leads/config.json\"...")
            _mkdir("/usr/local/leads")
            with open("/usr/local/leads/config.json", "w") as f:
                f.write(str(_DEFAULT_CONFIG))
            _L.info("Using \"/usr/local/leads/config.json\"")
        from ._bootloader import create_service

        create_service()
        _L.info("Service registered")
    elif args.register == "config":
        if _exists("config.json"):
            r = input("\"config.json\" already exists. Overwrite? (y/N) >>>").lower()
            if r.lower() != "y":
                _exit("Error: Aborted")
        with open("config.json", "w") as f:
            f.write(str(_DEFAULT_CONFIG))
        _L.info("Configuration file saved to \"config.json\"")
    config = _load_config(args.config) if args.config else _DEFAULT_CONFIG
    from leads_vec.cli import main

    try:
        from leads_vec.controller import _
    except ImportError:
        _L.warn("`leads_vec.controller` is not available, using emulation module instead...")
        try:
            from leads_emulation import SRWRandom as _Controller

            _register_controller(_MAIN_CONTROLLER, _Controller())
        except ImportError:
            raise ImportError("At least one adapter has to be installed")

    _initialize_main()
    _exit(main(config))
