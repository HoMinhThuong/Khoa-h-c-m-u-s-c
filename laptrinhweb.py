import streamlit as st
from PIL import Image

# Cấu hình trang
st.set_page_config(
    page_title="Khoa học màu sắc",
    layout="wide",
    page_icon="🎨"
)

# CSS tùy chỉnh
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #e3f2fd, #fce4ec);
        padding: 20px;
        font-family: 'Arial', sans-serif;
    }
    h1, h2, h3 {
        color: #d63384;
    }
    .title-text {
        font-size: 36px;
        font-weight: bold;
        color: #2196f3;
    }
    .sub-text {
        font-size: 20px;
        color: #6a1b9a;
    }
    </style>
""", unsafe_allow_html=True)


# Mở ảnh
image1 = Image.open("Logo HCMUTE Tagline 1_White background.PNG")
st.image(image1, use_container_width=True)

# Hiệu ứng
#st.success("✅ Dự án đã sẵn sàng khởi động!")
st.balloons()

# Tiêu đề & giới thiệu
st.markdown('<div class="title-text">🎨 KHOA HỌC MÀU SẮC TRONG NGÀNH IN ẤN</div>', unsafe_allow_html=True)
st.write("### 👋 Chào mừng bạn đến với project khoa học màu sắc của mình!")
st.write("#### 🎓 Mình tên là **Hồ Minh Thương** - MSSV `21158059`")
st.write("####  Cùng tìm hiểu cách màu sắc hoạt động trong in offset, hệ màu CMYK và những hiện tượng thú vị nhé!")

# === Phần giới thiệu ===
st.markdown("## 🔎 Giới thiệu")
st.write("""
Khoa học màu sắc đóng vai trò then chốt trong ngành in ấn, giúp đảm bảo chất lượng hình ảnh, độ chính xác của màu sắc và sự đồng nhất giữa các thiết bị.
Trong in ấn hiện đại, việc quản lý màu sắc (color management) trở thành yêu cầu bắt buộc để đáp ứng các tiêu chuẩn quốc tế như ISO 12647.
""")
st.write("""
Trang web này nhằm hỗ trợ việc tìm hiểu và thực hành các kiến thức về Khoa học màu sắc trong in ấn, 
đặc biệt liên quan đến quy trình đo, chuyển đổi và mô phỏng không gian màu của các thiết bị in.
""")
# === Các chủ đề chính ===
st.markdown("## 📚 Nội dung chính")

col4, col5 = st.columns(2)

with col4:
    st.markdown("### 1️⃣ Chuyển đổi không gian màu sRGB ↔ XYZ")
    st.write("- Chuyển đổi qua lại giữa hệ màu sRGB và không gian XYZ.")

    st.markdown("### 2️⃣ Tính giá trị X, Y, Z từ file phổ đo")
    st.write("- Xử lý file phổ đo trên máy đo màu của Khoa để tính 3 thành phần X, Y, Z.")

    st.markdown("### 3️⃣ Vẽ biểu đồ CIE hình móng ngựa")
    st.write("- Vẽ biểu đồ CIE xy, còn gọi là biểu đồ hình móng ngựa, hiển thị các màu khả dụng của mắt người.")

with col5:
    st.markdown("### 4️⃣ Vẽ gamut màu của thiết bị RGB")
    st.write("- Minh hoạ dải màu (gamut) của một thiết bị hiển thị RGB trên biểu đồ CIE.")

    st.markdown("### 5️⃣ Vẽ gamut màu của máy in Khoa")
    st.write("- Dựa vào file gamut đo được từ máy in, vẽ dải màu in được trên không gian CIE.")

    st.markdown("### 6️⃣ Đặc tính hoá của máy in nửa tone")
    st.write("- Nghiên cứu và mô phỏng quá trình đặc tính hoá (characterization) máy in nửa tone tại Khoa.")
# === Thêm hàng mới ===
st.markdown("## 🔥 Ngoài ra")
st.write("Ngoài ra còn có các nội dung liên quan đến chủ đề Khoa học màu sắc khác rất hấp dẫn. Hãy trải nghiệm nhé!")
st.image("Bieu do CIE 1931.png", 
             caption="Các hàm phối màu chuẩn CIE 1931 và biểu đồ sắc độ CIE 1931 xy ")
# Hiệu ứng
#st.success("✅ Cùng trải nghiệm với chúng tôi nào!")
st.balloons()
# === Footer ===
st.markdown("---")
#st.markdown("<p style='text-align: center; color: gray;'>© 2025 Đinh Nguyễn Hoài Nhi | Project Khoa học màu sắc</p>", unsafe_allow_html=True)

# Nội dung minh họa

st.markdown("---")
st.markdown("## 🖨️ Một số kiến thức cơ bản về màu sắc trong in ấn")
st.markdown("""
- 🎯 **CMYK** là hệ màu dùng trong in ấn, gồm: Cyan (Xanh lơ), Magenta (Hồng cánh sen), Yellow (Vàng) và Black (Đen).
- 🎨 Mỗi màu trong CMYK được in thành từng lớp riêng biệt, chồng lên nhau để tạo thành hình ảnh đầy màu sắc.""")
image1 = Image.open("He-mau-la-gi-tim-hieu-ve-he-mau-CMYK.PNG")
st.image(image1, use_container_width=True)
st.markdown("## 🖨️ Một số không gia màu phổ biến")

image1 = Image.open("Khong-gian-mau-Lab.PNG")
st.image(image1, use_container_width=True)

st.markdown("""
📺 Hệ màu RGB: Dựa trên ba màu cơ bản là đỏ (Red), xanh lá (Green) và xanh lam (Blue). Được sử dụng rộng rãi trong các thiết bị hiển thị như màn hình máy tính, tivi.

🖨️ Hệ màu CMYK: Dựa trên ba màu mực in là xanh lam (Cyan), hồng (Magenta), vàng (Yellow) và đen (Black). Thường được sử dụng trong ngành in ấn là chủ yếu.

📊 Hệ màu Lab: Mô tả màu sắc dựa trên các thuộc tính cảm nhận của mắt người, bao gồm độ sáng (L), độ đỏ-xanh (a) và độ vàng-lam (b). Là hệ màu được ứng dụng nhiều nhất trong mọi ngành nghề liên quan đến màu sắc.

""")




# Footer
st.markdown("---")
st.write("💡 *Liên hệ nếu bạn cần thêm thông tin hoặc tài liệu về kỹ thuật in!*")

