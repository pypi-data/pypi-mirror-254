import base64
import datetime
import os
import traceback
import uuid
from pathlib import Path
from typing import Optional, Union

import requests
from smtpymailer import SmtpMailer

__version__ = "0.0.5"

class ArchedEmailer:
    """
    A class for sending emails.
    ARCHED.DEV
    """
    error_log: dict
    app_name: str = "ArchedErrors"
    app_author: str = "Arched"
    error_sender: str = "errors@arched.dev"
    error_sender_name: str = "Error Bot"
    success_sender: str = "success@arched.dev"
    success_sender_name: str = "Arched Notifications"
    errors_name_time: dict = dict()
    connection_details: str
    arched_api_key: str
    temp_app: Optional[str] = None
    def __init__(self, app: str, api_key: Optional[str] = None, mail_connection_string: Optional[str] = None):

        self.app = app
        self.arched_api_key = os.getenv("ARCHED_API_KEY") or api_key
        self.connection_details = os.getenv("MAIL_CONNECTION_STRING") or mail_connection_string
        self._load_env()
        self.mailer = SmtpMailer(self.error_sender, self.error_sender_name)
        self.success_mailer = SmtpMailer(self.success_sender, self.success_sender_name)

    def _load_env(self):
        """
        Load environment variables from encoded connection details.

        This method decodes the given connection details, splits it into key-value pairs,
        and sets the corresponding environment variables.

        Returns:
            None
        """
        decoded_bytes = base64.b64decode(self.connection_details)
        decoded_string = decoded_bytes.decode("utf-8")
        for val in decoded_string.split(";"):
            if "=" in val:
                key, value = val.split("=")
                os.environ[key] = value

    def _get_create_data_dir(self):
        """
        Gets or creates a directory for storing data specific to the application.

        Returns:
            str: The path to the data directory.

        """

        import appdirs
        app_data_dir = Path(appdirs.user_data_dir(self.app_name, self.app_author))
        app_data_dir.mkdir(parents=True, exist_ok=True)
        return str(app_data_dir)

    def _get_error_email_path(self):
        """
        Fetches the error email template from the API and saves it to a local file.

        Returns:
            str: The path to the saved email template file.

        Raises:
            None.

        Example usage:
            email_path = _get_error_email_path()
        """
        resp = requests.get(
            f"https://arched.dev/email/error?api_key={self.arched_api_key}")
        data_dir = self._get_create_data_dir()
        email_path = os.path.join(data_dir, "error.html")
        if resp.status_code == 200:
            with open(email_path, "w") as f:
                f.write(resp.text)

        return email_path

    def _get_success_email_path(self):
        """
        Fetches the success email template from the API and saves it to a local file.

        Returns:
            str: The path to the saved email template file.

        Raises:
            None.

        Example usage:
            email_path = _get_error_email_path()
        """
        resp = requests.get(
            f"https://arched.dev/email/success?api_key={self.arched_api_key}")
        data_dir = self._get_create_data_dir()
        email_path = os.path.join(data_dir, "success.html")
        if resp.status_code == 200:
            with open(email_path, "w") as f:
                f.write(resp.text)

        return email_path


    def send_email(self, sender_email: str, sender_name: str, recipients: Union[str, list], subject: str,
                   cc_recipients: Optional[Union[str, list]] = None, bcc_recipients: Optional[Union[str, list]] = None,
                   dkim_selector: Optional[str] = "default", template: Optional[str] = None, **kwargs):
        """
        Args:
            sender_email: The email address of the sender.
            sender_name: The name of the sender.
            recipients: The email address(es) of the recipient(s). Can be a string or a list of strings.
            subject: The subject of the email.
            cc_recipients: Optional. The email address(es) of the CC recipient(s). Can be a string or a list of strings.
            bcc_recipients: Optional. The email address(es) of the BCC recipient(s). Can be a string or a list of strings.
            dkim_selector: Optional. The DKIM selector. Default is "default".
            template: Optional. The template for the email.
            **kwargs: Additional keyword arguments for the `send_email` method.

        Returns:
            bool: True if the email was sent successfully, False otherwise.
        """


        try:
            os.environ["MAIL_DKIM_SELECTOR"] = dkim_selector
            self.mailer = SmtpMailer(sender_email, sender_name)
            return self.mailer.send_email(recipients, cc_recipients=cc_recipients, bcc_recipients=bcc_recipients,
                                          subject=subject,
                                          template=template, **kwargs)
        except:
            return False

    def _allowed_to_send(self, exception: Union[str, Exception], allowed_minutes: int = 60):
        """
        Args:
            exception: The exception or error message to be checked.
            allowed_minutes: The number of minutes within which the exception is allowed to be sent again. Default is 60 minutes.

        Returns:
            True if the exception is allowed to be sent, False otherwise.

        """
        exception_text = str(exception)
        if allowed_minutes:
            if exception_text in self.errors_name_time:
                if (datetime.datetime.now() - self.errors_name_time[
                    exception_text]).total_seconds() < allowed_minutes * 60:
                    return False
            self.errors_name_time[exception_text] = datetime.datetime.now()
            return True
        return True

    def send_success_email(self, recipients: Union[str, list], success_text: Optional[str] = None, dkim_selector: str = "default", sender: Optional[str] = None, sender_name: Optional[str] = None, allowed_minutes: Optional[int] = 60, app: Optional[str] = None, **kwargs):
        """
        Sends an error email.

        Args:
            recipients: The recipients of the error email. Can be a string or a list of strings.
            success_text: The text describing the error.
            dkim_selector: The DKIM selector to use for sending emails from the server. Default is "default".
            sender: The email address of the sender. If provided, it will be used as the sender of the email.
            sender_name: The name of the sender. Used only if sender is provided.
            app: The name of the application. If provided, it will be used as the application name in the email.
            **kwargs: Additional keyword arguments for the `send_email` method.
        """
        try:
            if sender:
                self.success_mailer = SmtpMailer(sender, sender_name)

            # gets and creates the email template
            email_path = self._get_success_email_path()

            # sets the DKIM selector, needed for sending emails from the server
            os.environ["MAIL_DKIM_SELECTOR"] = dkim_selector
            date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
            job_id = uuid.uuid4()

            if success_text:
                app_name = app if app else self.app
                self.success_mailer.send_email(recipients, subject=f"Success: {app_name} - ID: {job_id}", template=email_path, date=date, app=app_name, success_text=success_text, **kwargs)

        except:
            pass

    def send_error_email(self, recipients: Union[str, list], error_text: Optional[str] = None,
                         exception: Optional[Exception] = None, include_tb: bool = True, dkim_selector: str = "default",
                         sender: Optional[str] = None,
                         sender_name: Optional[str] = None,
                         allowed_minutes: Optional[int] = 60,
                         app: Optional[str] = None):
        """
        Sends an error email.

        Args:
            recipients: The recipients of the error email. Can be a string or a list of strings.
            error_text: The text describing the error.
            exception: The exception object associated with the error.
            include_tb: A boolean value indicating whether to include the traceback in the email. Default is True.
            dkim_selector: The DKIM selector to use for sending emails from the server. Default is "default".
            sender: The email address of the sender. If provided, it will be used as the sender of the email.
            sender_name: The name of the sender. Used only if sender is provided.
            allowed_minutes: The number of minutes to wait before sending another email of the same exception. Default is 60. 0 means no limit.
            app: The name of the application. If provided, it will be used as the application name in the email.
        """
        try:
            if sender:
                self.mailer = SmtpMailer(sender, sender_name)

            # gets and creates the email template
            email_path = self._get_error_email_path()

            # sets the DKIM selector, needed for sending emails from the server
            os.environ["MAIL_DKIM_SELECTOR"] = dkim_selector
            date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
            error_id = uuid.uuid4()

            template_data = {}
            if include_tb:
                template_data["traceback"] = traceback.format_exc()

            issue = str(exception) or str(error_text) or str(traceback.format_exc())
            if issue:
                if self._allowed_to_send(issue, allowed_minutes=allowed_minutes):
                    app_name = app if app else self.app
                    self.mailer.send_email(recipients, subject=f"Error: {app_name} - ID: {error_id}",
                                           template=email_path, date=date, app=app_name, error_text=error_text,
                                           error_id=error_id, exception=exception, **template_data)

        except:
            pass
