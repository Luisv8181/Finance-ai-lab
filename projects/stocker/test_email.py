from delivery.emailer import EmailDelivery
from utils.logger import setup_logger

logger = setup_logger("test_email")

def send_test():
    emailer = EmailDelivery()
    subject = "⚠️ STOCKER AI — SYSTEM TEST"
    content = """
    Holographic Neural Link Established.
    
    This is a test of the Stocker AI Agent reporting system.
    If you are reading this, your email delivery is fully operational.
    
    Status: SECURED
    Encryption: AES-256
    System: Stocker v4.1
    """
    
    print("\n[!!!] ATTEMPTING TO SEND TEST EMAIL...")
    success = emailer.send_email(subject, content)
    if success:
        print("[SUCCESS] Test email dispatched to your inbox!")
    else:
        print("[FAILURE] Could not send email. Check your password or App Password settings.")

if __name__ == "__main__":
    send_test()
