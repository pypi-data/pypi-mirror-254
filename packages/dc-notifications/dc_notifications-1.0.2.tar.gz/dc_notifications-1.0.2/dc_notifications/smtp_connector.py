import logging
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from email.mime.application import MIMEApplication
from typing import List
import os


class SMTPConnector:
    """Crea la conexion al email con la libreria smtp"""

    def __init__(self, logger=None):
        self._logger = logger
        if self._logger is None:
            self._logger = logging.getLogger("ROBOT.SMTPConnector")
        self._host = os.getenv("MAIL_HOST")
        self._port = os.getenv("MAIL_PORT_SSL")
        self._exchange_sender = os.getenv("MAIL_USER_CON")
        self._exchange_passwd = os.getenv("MAIL_PASSWORD")

    def send_mail_ssl(
        self, destinos: List[List[str]], subject: str, text: str, html: str = None, xlsx_file=None
    ):
        """Envia un email a la lista de destinos.
        destinos debe contener una lista de listas con las direcciones de email
        a las que se debe enviar el mensaje
        (se envia un email por cada lista dentro de destinos).
        """
        mails_sent = []
        # Create a secure SSL context
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self._host, self._port, context=context) as server:
            server.ehlo()
            server.login(self._exchange_sender, self._exchange_passwd)
            message = MIMEMultipart("alternative")
            message["Subject"] = subject
            message["From"] = self._exchange_sender
            message["Date"] = formatdate()
            for destino in destinos:
                message["To"] = str(destino)
                if not html:
                    html = f"""\
                            <html>
                            <body>
                                <p>{text}
                                </p>
                            </body>
                            </html>
                            """
                part1 = MIMEText(text, "plain")
                part2 = MIMEText(html, "html")
                message.attach(part1)
                message.attach(part2)
                if xlsx_file is not None:
                    with open(xlsx_file, "rb") as file_xlsx:
                        part3 = MIMEApplication(file_xlsx.read(), _subtype="xlsx")
                        part3.add_header(
                            "Content-Disposition",
                            "attachment",
                            filename=os.path.basename(file_xlsx.name),
                        )
                    message.attach(part3)
                try:
                    str_message = message.as_string()
                    server.sendmail(self._exchange_sender, destino, str_message)
                    mails_sent.append(f"mail enviado a {destino}")
                except Exception as ex:
                    server.quit()
                    mails_sent.append(f"Error en el envio al correo {destino}")
                    self._logger.critical(ex)
        for mail in mails_sent:
            self._logger.info(mail)