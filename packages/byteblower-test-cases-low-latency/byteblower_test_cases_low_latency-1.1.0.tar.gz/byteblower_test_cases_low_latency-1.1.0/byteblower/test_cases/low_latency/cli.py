"""Command-line interface."""
import logging

from byteblower_test_framework.logging import configure_logging

from ._arguments import parse_arguments
from ._config_file import load_config_file
from ._definitions import LOGGING_PREFIX
from ._lld import run

__all__ = ('main', )


def cli() -> None:
    """Run the main application.

    Parses command-line arguments, loads the configuration file
    and runs the actual use case.
    """
    logging.info("Initializing Low Latency test case")

    # Load test configuration
    config_file_name, report_path, report_prefix = parse_arguments()
    logging.info(
        '%sLoading configuration file %s', LOGGING_PREFIX, config_file_name
    )
    test_config = load_config_file(config_file_name)
    run(test_config, report_path=report_path, report_prefix=report_prefix)


def main() -> None:
    """Configure logging and start the main application."""
    # 1. Configure logging
    logging.basicConfig(level=logging.INFO)

    framework_level = logging.INFO
    for framework_module in ('byteblower_test_framework', ):
        framework_logger = logging.getLogger(framework_module)
        framework_logger.setLevel(framework_level)

    logging.info("Initializing ByteBlower Test Framework")
    configure_logging()

    # 2. Run the use case
    cli()


if __name__ == '__main__':
    main()
