# wifi-quality-ml

## Hướng dẫn sử dụng

#### Lưu ý: Để có trải nghiêm tốt nh

### Theo dõi từng bước của quá trình học máy
- Bước 0 (Không bắt buộc): Xóa 


các `notebooks` là chú giải của các file, đi qua lần lượt các bước 

| Notebook      | Nội dung |
| ------------- | ---------:|
| `01_data_cleaning.ipynb`   | Quá trình xử lý dữ liệu để sẵn sàng cho khám phá dữ liệu |
| `02_eda.ipynb`      | Quá trình Phân tích khám phá dữ liệu (EDA - Exploratory Data Analysis)       |  
| `03_preprocessing.ipynb` | Quá trình xử lý dữ liệu để sẵn sàng cho các bước học máy |
| `04_baseline.ipynb` | Quá trình tạo ra mô hình Baseline |
| `05_linear_regression.ipynb` | Quá trình tạo ra và train mô hình Linear Regression |
| `06_analysis.ipynb` | Phân tích và so sánh kết quả dự đoán giữa hai mô hình với nhau và với đáp án đúng   |

### Cách 2: Sử dụng mô hình đã train trước để dự đoán băng thông bằng cách nhập biến đầu vào
- Bước 1: Tải `uv` [link]
- Bước 2: Trong terminal, chạy `uv run app.py`
- Bước 3: Điền lần lượt các biến đầu vào