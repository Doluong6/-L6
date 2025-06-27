files = {
    "Máy đo pH": "2025 May do pH - B.xlsx",
    "Máy đo độ dẫn": "2025 May do do dan - B.xlsx",
    "Tỷ trọng kế": "2025 Ty trong ke - B.xlsx",
}

# Các trường dùng chung cho tất cả thiết bị
FIELDS_CHUNG = {
    "Z3": "Ngày",
    "AC3": "Tháng",
    "BC3": "Số phiếu yêu cầu",
    "BG3": "Số giấy",
    "I10": "Tên Đơn vị sử dụng",
    "E12": "Địa chỉ",
    "R24": "Nhiệt độ bắt đầu (ºC)",
    "R25": "Độ ẩm bắt đầu (%)",
    "AJ24": "Nhiệt độ kết thúc (ºC)",
    "AJ25": "Độ ẩm kết thúc (%)",
    "A58": "Người thực hiện"  # ✅ Đã thêm dòng này
}

from forms.form_ph import hien_form_rieng as form_ph
from forms.form_ty_trong import hien_form_rieng as form_ty_trong
from forms.form_do_dan import hien_form_rieng as form_do_dan

# thêm các form khác tương tự...

forms_map = {
    "Máy đo pH": "form_ph",
    "Tỷ trọng kế": "form_ty_trong",
    "Máy đo độ dẫn": "form_do_dan"
}
