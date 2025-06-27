
# 📋 Ứng dụng tạo báo giá - QUATEST 1 (Phòng Đo lường 6)

Hệ thống tạo báo giá tự động từ phiếu yêu cầu, bảng giá thiết bị và hỗ trợ gửi mail hàng loạt cho khách hàng.

## 🔗 Thành phần hệ thống
- **Tích hợp**:
  - Tạo báo giá từ file `.xlsx`
  - Gọi API backend xử lý logic báo giá
  - Tải báo giá đã tạo
  - Gửi mail hàng loạt từ file danh sách

## 🚀 Cách sử dụng
1. Tải file phiếu yêu cầu (hoặc chọn thiết bị thủ công)
2. Nhấn nút "Tạo báo giá"
3. Xem và tải file báo giá tự động sinh
4. Gửi email cho khách hàng nếu cần

## 📦 API backend
- `/tao_baogia_tu_pyc` – Tạo báo giá từ file yêu cầu
- `/tao_baogia_thucong` – Tạo báo giá từ danh sách thiết bị
- `/bang_gia` – Trả danh sách thiết bị + đơn giá
- `/bao_gia_moi_nhat` – Liệt kê báo giá gần đây
- `/gui_mail_hangloat` – Gửi nhiều báo giá qua email

## 📎 Liên hệ
**Trung tâm Kỹ thuật Tiêu chuẩn Đo lường Chất lượng 1**  
Phòng Đo lường 6 – QUATEST 1  
📧 Email: doluong6@quatest1.com.vn  
🌐 Website: https://quatest1.com.vn

