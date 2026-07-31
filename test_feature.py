from src.feature_extraction import FeatureExtractor

url = input("Enter URL : ")

obj = FeatureExtractor(url)

features = obj.extract()

for key, value in features.items():
    print(f"{key} : {value}")