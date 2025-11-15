import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# 标准化
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    standardized_data = (data - mean) / std
    # 归一化
    min_val = np.min(data, axis=0)
    max_val = np.max(data, axis=0)
    normalized_data = (data - min_val) / (max_val - min_val)
    return standardized_data, normalized_data
#test

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
standardized_data, normalized_data = feature_scaling(data)
print("Standardized Data:\n", standardized_data)
print("Normalized Data:\n", normalized_data)