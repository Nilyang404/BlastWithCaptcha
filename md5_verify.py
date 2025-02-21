import hashlib

# 假设我们要测试 "password123" 是否生成了这个 MD5
test_string = "quest1"
md5_hash = hashlib.md5(test_string.encode()).hexdigest()

print(md5_hash)  # 计算 MD5 值