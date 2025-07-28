import sklearn.datasets


digits =  sklearn.datasets.load_digits()

print("データの個数=`",len(digits.images))
print("画像データ=\n",digits.images[-3])
print("何の数字か=",digits.target[-3])
