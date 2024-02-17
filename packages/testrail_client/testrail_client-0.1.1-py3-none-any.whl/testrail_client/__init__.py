import logging

from ._testrail_client import TestrailClient

logging.getLogger(__package__).addHandler(logging.NullHandler())

__all__ = ["TestrailClient"]
