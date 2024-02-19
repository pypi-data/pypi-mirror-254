from pathlib import Path

from oarepo_tools.make_translations import main


def test_cli_with_oarepo_yaml(app, db, cache, extra_entry_points, cli_runner):
    config_file = Path(__file__).parent / "oarepo.yaml"
    try:
        cli_runner(main([str(config_file)]))
    except SystemExit as se:
        assert se.code == 0


def test_cli_with_setup_cfg(app, db, cache, extra_entry_points, cli_runner):
    config_file = Path(__file__).parent / "setup.cfg"
    try:
        cli_runner(main([str(config_file)]))
    except SystemExit as se:
        assert se.code == 0
