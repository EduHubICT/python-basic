import unittest
from src.main.mail_sender.mail_sender import *


class MailSenderTest(unittest.TestCase):
    def test_send_mail(self):
        user = MailSender("youremail@example.com", "your@password")
        self.assertTrue(user.send_mail("mh.ice.iu@gmail.com", "Testing Mail Sender", "Hi, Mobarak, reply a feedback "
                                                                                       "if you got this mail."))


if __name__ == '__main__':
    unittest.main()
