# mAP使用說明

1. main 參數說明
- GT_PATH   ground-truth      路徑 ex: "./content/test/labels"
- DR_PATH   detection-results 路徑 ex: "./content/ScaledYOLOv4/inference/output"
- IMG_PATH                圖片路徑 ex: "./content/ScaledYOLOv4/inference/output"             
- main.py 產生 map資料於output/底下
```
範例: 
python main.py "./content/test/labels" "./content/ScaledYOLOv4/inference/output" "./content/ScaledYOLOv4/inference/output"
自定義:
python main.py <GT_PATH> <DR_PATH> <IMG_PATH>
```
