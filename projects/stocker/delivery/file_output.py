import os
from datetime import datetime
from utils.config import Config
from utils.logger import setup_logger

logger = setup_logger("file_output")

class FileDelivery:
    def __init__(self):
        self.reports_dir = Config.REPORTS_DIR
        if not os.path.exists(self.reports_dir):
            os.makedirs(self.reports_dir)

    def save_report(self, content):
        date_str = datetime.now().strftime("%Y-%m-%d_%H-%M")
        filename = f"report_{date_str}.md"
        filepath = os.path.join(self.reports_dir, filename)
        
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            
            # Also save as latest.md for the UI dashboard
            latest_path = os.path.join(self.reports_dir, "latest.md")
            with open(latest_path, "w", encoding="utf-8") as f:
                f.write(content)
                
            logger.info(f"Report saved to {filepath} and latest.md")
            return filepath
        except Exception as e:
            logger.error(f"Error saving report: {e}")
            return None
