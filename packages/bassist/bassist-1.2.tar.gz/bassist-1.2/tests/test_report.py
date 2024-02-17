import os
from unittest.mock import MagicMock, patch

import pytest

from bassist.config import Config
from bassist.report import report

CONFIGFILE = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "configs", "reporttest.toml"
)


@pytest.fixture
def config() -> Config:
    return Config(CONFIGFILE)


LOG_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "logs")
SUCCESS_LOG = os.path.join(LOG_DIR, "success.log")
# A log is deemed a failure when it contains 'fail' in the body
FAILURE_LOG = os.path.join(LOG_DIR, "failure.log")


@patch("bassist.report.SMTP")
@patch("bassist.report.open")
def test_logfile_not_emptied(open_mock, smtp, config: Config):
    report(config, SUCCESS_LOG)

    assert open_mock.call_count == 1
    open_mock.assert_called_with(SUCCESS_LOG)


@patch("bassist.report.SMTP")
@patch("bassist.report.open")
def test_logfile_emptied(open_mock, smtp, config: Config):
    report(config, SUCCESS_LOG, empty_logfile=True)

    assert open_mock.call_count == 2
    open_mock.assert_called_with(SUCCESS_LOG, "w")


class TestEmail:
    @patch("bassist.report.SMTP")
    @patch("bassist.report.MIMEMultipart")
    @patch("bassist.report.MIMEText")
    def test_report_calls_smtp(self, text, multipart, smtp, config: Config):
        smtp_mock = MagicMock()
        smtp.return_value = smtp_mock
        multipart_mock = MagicMock()
        multipart.return_value = multipart_mock
        text_mock = MagicMock()
        text.return_value = text_mock

        report(config, SUCCESS_LOG)

        emailconf = config["email"]
        smtp.assert_called_once_with(
            emailconf["smtp"]["host"], emailconf["smtp"]["port"]
        )
        smtp_mock.starttls.assert_called_once()
        smtp_mock.login.assert_called_once_with(
            emailconf["auth"]["username"], emailconf["auth"]["password"]
        )

        subject = "Borg backup success"
        multipart.assert_called_once_with()
        multipart_mock.__setitem__.assert_any_call("From", emailconf["email"]["from"])
        multipart_mock.__setitem__.assert_any_call("To", emailconf["email"]["to"])
        multipart_mock.__setitem__.assert_any_call("Subject", subject)
        multipart_mock.attach.assert_called_once_with(text_mock)

        with open(SUCCESS_LOG, "r") as f:
            text.assert_called_once_with(f.read())

            smtp_mock.sendmail.assert_called_once_with(
                emailconf["email"]["from"],
                emailconf["email"]["to"],
                multipart_mock.as_string(),
            )
            smtp_mock.quit.assert_called_once()

    @patch("bassist.report.SMTP")
    @patch("bassist.report.MIMEMultipart")
    @patch("bassist.report.requests")
    def test_report_correct_subject_failure(
        self, requests, multipart, smtp, config: Config
    ):
        smtp_mock = MagicMock()
        smtp.return_value = smtp_mock
        multipart_mock = MagicMock()
        multipart.return_value = multipart_mock

        report(config, FAILURE_LOG)

        subject = "Borg backup FAILURE"
        multipart.assert_called_once_with()
        multipart_mock.__setitem__.assert_any_call("Subject", subject)


class TestTelegram:
    @patch("bassist.report.SMTP")
    @patch("bassist.report.requests")
    def test_report_doesnt_call_telegram_success(self, requests, smtp, config: Config):
        report(config, SUCCESS_LOG)
        requests.post.assert_not_called()

    @patch("bassist.report.SMTP")
    @patch("bassist.report.requests")
    def test_report_calls_telegram_failure(self, requests, smtp, config: Config):
        report(config, FAILURE_LOG)

        subject = "Borg backup FAILURE"
        conf = config["telegram"]
        requests.post.assert_called_once_with(
            f"https://api.telegram.org/bot{conf['token']}/sendMessage",
            data=dict(chat_id=conf["chat_id"], text=subject),
        )
