import smtplib
from src.main.logger.py_logger import PyLogger

logger = PyLogger.get_configured_logger()


class MailSender:

    def __init__(self, _from, password):
        """

        :param _from: Gmail account from where mail will be sent
        :param password: If your gmail has two step verification enabled use App password
        otherwise you can use your plain password.
        To create app password follow the link
        https://myaccount.google.com/apppasswords
        """

        self.__from = _from
        self.__password = password

    def send_mail(self, _to, subject, body):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.__from, self.__password)

        msg = f'Subject: {subject}\n\n{body}'
        server.sendmail(self.__from, _to, msg)
        server.close()
        logger.info('You mail has been sent successfully to {}'.format(_to))
        return True
