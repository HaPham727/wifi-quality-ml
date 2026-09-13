# wifi-quality-ml

Repo này là phần Học máy (Machine Learning) của nhóm 7, thuộc lớp COSH201(2627-HK1)GD1.1

| Thành viên            |     MSSV     |
| --------------------- | ------------ |
| `Trần Thị Ngọc Ánh`   | `2519960007` |
| `Phạm Thị Ngọc Minh`  | `2519960037` |  
| `Phạm Vũ Hoàng Hà`    | `2519960014` |
| `Hán Huy Gia Bảo`     | `2519960008` |
| `Khúc Văn Tuấn Anh`   | `X` |

---

## Tổng quan 

Repo có cấu trúc như sau:

```text
wifi-quality-ml/
│
├── data/
│   ├── raw/
│   │   └── data-raw.csv
│   │
│   ├── cleaned/
│   │   └── data-cleaned
│   │
│   ├── preprocessed/
│   │   ├── data_train.csv
│   │   └── data_test.csv
│   │
│   ├── prediction-baseline/
│   │   └── prediction_baseline.csv
│   │
│   └── prediction-linear-regression/
│       └── prediction_linear_regression.csv
│
├── media/
│   └── 02_05.png
│   └── ...
│
├── models/
│   └── linear_regression_model.joblib
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_preprocessing.ipynb
│   ├── 04_baseline.ipynb
│   ├── 05_linear_regression.ipynb
│   └── 06_analysis.ipynb
│
├── app.py
├── optional.py
├── requirements.txt
└── README.md
```


Repo này có workflow như sau:

```text
                  Dữ liệu thô
                       │
                       ▼
             Làm sạch dữ liệu trong
             01_data_cleaning.ipynb
                       │
                       ▼
           Exploratory Data Analysis
              trong 02_eda.ipynb
                       │
                       ▼
              Preprocessing trong
             03_preprocessing.ipynb
             (Gồm Train/Test Split)
                       │
               ┌───────┴───────┐
               ▼               ▼
        Dự đoán bằng         Dự đoán bằng
        Mean Baseline     Linear Regression
           trong                trong
     04_baseline.ipynb   05_linear_regression.ipynb
               │               │
               └───────┬───────┘
                       │
                       ▼
                  Phân tích và    
                   so sánh hai     
                  mô hình trong
                06_analysis.ipynb
                       │
                       ▼
                  Streamlit App
                  trong app.py
```
---
## Hướng dẫn sử dụng

#### Lưu ý: Để có trải nghiêm tối ưu, hãy đảm bảo trên máy tính có:
- Python
- pip
- Một ứng dụng có thể mở file `.ipynb` như PyCharm hoặc Jupyter Lab/Notebook

### Theo dõi từng bước của quá trình học máy
- Bước 0 (Không bắt buộc): Trong directory, mở Terminal và chạy `python optional.py`
→ Mục đích: Xóa các file dữ liệu đã qua xử lý, để lại duy nhất dữ liệu thô
- Bước 1: Trong directory, mở Terminal và chạy `pip install -r requirements.txt`
- Bước 2: Theo thứ tự đánh số trong tên các file `.ipynb` ở folder `notebooks`, mở các file này và chạy lần lượt các cell

Giải thích nội dung các notebook:

| Notebook      | Nội dung |
| ------------- | ---------|
| `01_data_cleaning.ipynb`   | Quá trình xử lý dữ liệu để sẵn sàng cho khám phá dữ liệu |
| `02_eda.ipynb`      | Quá trình Phân tích khám phá dữ liệu (EDA - Exploratory Data Analysis)       |  
| `03_preprocessing.ipynb` | Quá trình xử lý dữ liệu để sẵn sàng cho các bước học máy |
| `04_baseline.ipynb` | Quá trình tạo ra mô hình Baseline |
| `05_linear_regression.ipynb` | Quá trình tạo ra và train mô hình Linear Regression |
| `06_analysis.ipynb` | Phân tích và so sánh kết quả dự đoán giữa hai mô hình với nhau và với đáp án đúng   |

### Sử dụng mô hình đã train trước để dự đoán băng thông bằng cách nhập biến đầu vào
- Bước 1: Trong directory, mở Terminal và chạy `pip install -r requirements.txt`
- Bước 2: Mở lại Terminal và chạy `streamlit run app.py`
- Bước 3: Điền lần lượt các biến đầu vào và 