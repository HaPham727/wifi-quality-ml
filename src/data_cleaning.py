### 1. Import thư viện pandas và load dataset
import pandas as pd

data = pd.read_csv("../data/raw/data-raw.csv")

### 2. Bỏ cột 'observation_id`
data = data.drop(columns=["observation_id"])

### 3. Đổi kiểu giá trị biến `timestamp` thành kiểu số, đồng thời đổi tên thành `seconds_since_midnight`
ts_col = pd.to_datetime(data['timestamp'])

data['timestamp'] = ts_col.dt.hour * 3600 + ts_col.dt.minute * 60 + ts_col.dt.second

data.rename(columns={'timestamp': 'seconds_since_midnight'}, inplace=True)

### 4. Bỏ cột `session_id` và `time_of_day`
data = data.drop(columns=['session_id'])
data = data.drop(columns=['time_of_day'])

### 5. Thay giá trị tương ứng các địa điểm thu dữ liệu thành giá trị khoảng cách, đồng thời đổi tên thành `distance_m`
data['location_id'] = data['location_id'].replace({1: 1, 2: 15, 3: 5})
data.rename(columns={'location_id': 'distance_m'}, inplace=True)

### 6. Đổi tên cột `signal_mean` và `signal_std` thành lần lượt `signal_mean_pct` và `signal_std_pct`
data.rename(columns={'signal_mean': 'signal_mean_pct'}, inplace=True)
data.rename(columns={'signal_std': 'signal_std_pct'}, inplace=True)

### 7. Lưu lại dataset đã qua cleaning
try:
    data.to_csv("../data/cleaned/data.csv", mode="x", index=False)
    print("File created successfully.")
except FileExistsError:
    print("File already exists.")