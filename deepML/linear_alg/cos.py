
import numpy as np

def cosine_similarity(v1, v2):
	# 精确到0.001
	norm_v1 = np.linalg.norm(v1)
	norm_v2 = np.linalg.norm(v2)
	if norm_v1 == 0 or norm_v2 == 0:
		return 0
	return round(np.dot(v1, v2) / (norm_v1 * norm_v2), 3)