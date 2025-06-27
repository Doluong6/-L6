
import os
import base64
import sendgrid
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition

def gui_mail_sendgrid(file, email_nguoinhan, sobg, ten_khach):
    try:
        from_email = "doluong6.quatest1@gmail.com"
        api_key = os.environ["SENDGRID_API_KEY"]
        sg = sendgrid.SendGridAPIClient(api_key)
        message = Mail(
            from_email=from_email,
            to_emails=email_nguoinhan,
            subject=f"Báo giá thiết bị - {sobg}",
            plain_text_content=f"Kính gửi {ten_khach},\n\nVui lòng xem báo giá đính kèm.\n\nTrân trọng,\nQUATEST 1 - Phòng Đo lường 6"
        )
        file_bytes = file.read()
        encoded = base64.b64encode(file_bytes).decode()
        attachment = Attachment(
            FileContent(encoded),
            FileName(f"{sobg}.xlsx"),
            FileType("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"),
            Disposition("attachment")
        )
        message.attachment = attachment
        sg.send(message)
        return True
    except Exception as e:
        print("❌ Lỗi gửi email:", e)
        return False
