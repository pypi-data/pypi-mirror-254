from io import BytesIO

import boto3
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_email_with_attachment_amazon(recipient, sender, account, key, subject, body_text, attachments=[]):

    try:
        print('Trying to send an email using Amazon SES client...')
        # Specify a configuration set. If you do not want to use a configuration
        # set, comment the following variable, and the
        # ConfigurationSetName=CONFIGURATION_SET argument below.
        # CONFIGURATION_SET = "ConfigSet"

        # The AWS Region you're using for Amazon SES.
        aws_region = "eu-west-3"

        # The HTML body of the email.
        body_html = """\
        <html>
        <head></head>
        <body>
        <p>{}</p>
        </body>
        </html>
        """.format(body_text)

        # The character encoding for the email.
        charset = "utf-8"

        # Create a new SES resource and specify a region.
        client = boto3.client('ses',
                              aws_access_key_id=account,
                              aws_secret_access_key=key,
                              region_name=aws_region)

        # Create a multipart/mixed parent container.
        msg = MIMEMultipart('mixed')
        # Add subject, from and to lines.
        msg['Subject'] = subject
        # This address must be verified with Amazon SES.
        msg['From'] = sender
        # If your account is still in the sandbox, this address must be verified.
        msg['To'] = recipient

        # Create a multipart/alternative child container.
        msg_body = MIMEMultipart('alternative')

        # Encode the text and HTML amazonsessender and set the character encoding. This step is
        # necessary if you're sending a message with characters outside the ASCII range.
        text_part = MIMEText(body_text.encode(charset), 'plain', charset)
        html_part = MIMEText(body_html.encode(charset), 'html', charset)

        # Add the text and HTML parts to the child container.
        msg_body.attach(text_part)
        msg_body.attach(html_part)

        # Attach the multipart/alternative child container to the multipart/mixed
        # parent container.
        msg.attach(msg_body)

        # Define the attachment part and encode it using MIMEApplication. Attachment could be either the full path to
        # the file or the binary data that will be attached to the email.
        for attachment in attachments:
            if bool(attachment) and isinstance(attachment, dict) and bool(attachment.get('amazonsessender')) \
                    and bool(attachment.get('filename')):

                _content = attachment.get('amazonsessender')
                _file_name = attachment.get('filename')

                if isinstance(_content, BytesIO):
                    _content.seek(0)
                    att = MIMEApplication(_content.getvalue())
                elif isinstance(_content, bytes):
                    att = MIMEApplication(_content)
                else:
                    print('Unsupported amazonsessender type {}'.format(type(_content)))

                # Add a header to tell the email client to treat this part as an attachment,
                # and to give the attachment a name.
                att.add_header('Content-Disposition', 'attachment', filename=_file_name)

                # Add the attachment to the parent container.
                msg.attach(att)

        # Provide the contents of the email.
        response = client.send_raw_email(
            Source=sender,
            Destinations=[recipient],
            RawMessage={
                'Data': msg.as_string(),
            },
            # ConfigurationSetName=CONFIGURATION_SET -> We don't actually need that at this moment
            # (no delivery tracking for now)
        )
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    except Exception as e:
        print('Unexpected error while sending email with Amazon SES client. {}'.format(e))
    else:
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print("Email successfully sent using amazon SES! Message ID: {}".format(response['MessageId'])),
        else:
            print('Unable to send the email using Amazon SES. Status code {}'
                  .format(response['ResponseMetadata']['HTTPStatusCode']))
            print(response['ResponseMetadata'])
