import numpy as np
from sklearn.ensemble import IsolationForest
import datetime

class CyberSecurityAgent:
    def __init__(self):
        # Sử dụng Isolation Forest - một thuật toán AI rất mạnh để phát hiện phần tử ngoại lai (Anomaly Detection)
        self.model = IsolationForest(contamination=0.01) # Giả định 1% dữ liệu là bất thường
        self.is_trained = False

    def train_agent(self, historical_data):
        """
        Huấn luyện Agent dựa trên dữ liệu lịch sử (Thời gian đăng nhập, Dung lượng file, Địa chỉ IP số hóa)
        """
        print("[*] Agent is learning normal user behavior...")
        self.model.fit(historical_data)
        self.is_trained = True
        print("[+] Training complete. Agent is now active.")

    def monitor_activity(self, current_activity):
        """
        Giám sát và đưa ra quyết định phản ứng
        current_activity: [giờ_đăng_nhập, dung_lượng_tải, id_vùng_địa_lý]
        """
        if not self.is_trained:
            return "Agent needs training first."

        prediction = self.model.predict([current_activity])
        
        if prediction[0] == -1:
            return self.respond_to_threat(current_activity)
        return "[SAFE] Activity matches normal patterns."

    def respond_to_threat(self, data):
        """
        Quy trình phản ứng tự động (Incident Response)
        """
        timestamp = datetime.datetime.now()
        report = f"⚠️ [ALERT] Suspicious activity detected at {timestamp}!\n"
        report += f"Details: Activity Data {data}\n"
        report += "[ACTION] Revoking OAuth Token and notifying HCC IT Admin."
        return report

# --- CHƯƠNG TRÌNH MÔ PHỎNG ---
if __name__ == "__main__":
    agent = CyberSecurityAgent()

    # Giả lập dữ liệu bình thường: [Giờ (0-23), Dung lượng (MB), Vùng (1-10)]
    # Sinh viên thường học từ 8h-22h, tải file nhỏ (1-50MB)
    normal_data = np.random.randint([8, 1, 1], [22, 50, 2], size=(100, 3))
    
    agent.train_agent(normal_data)

    # Tình huống 1: Sinh viên đang học (Bình thường)
    print(agent.monitor_activity([14, 10, 1])) 

    # Tình huống 2: Hacker đang rút dữ liệu lúc 3h sáng, tải 3000MB (Bất thường)
    # Đây là cách chúng ta bắt quả tang ShinyHunters!
    print(agent.monitor_activity([3, 3000, 9])) 
