# 在Google Colab上運行mAP使用說明
```
!git clone https://github.com/worldstar/mAP
!pip install scikit-plot
%cd mAP
# 上傳原始標記至input/ground-truth，預測結果至input/detection-results , 預測圖片至input/images-optional
!python main.py 
```

# 指令說明
```
--no-animation --> 計算時關閉動畫功能，在Google Colab上務必使用此參數
--no-plot      --> 不產生classes資料夾、detection-results-info.png、ground-truth-info.png、lamr.png、mAP.png 
```
# 參數說明
```
plt.yticks -> fontsize y軸字樣大小
plt.xticks -> fontsize x軸字樣大小
```

# Roboflow預測結果計算mAP使用說明
因為Roboflow並沒有輸出confidence資訊，因此要刪除相關的confidence內容。
<!-- 1. main 參數說明
- GT_PATH   ground-truth      路徑 ex: "./content/test/labels"
- DR_PATH   detection-results 路徑 ex: "./content/ScaledYOLOv4/inference/output"
- IMG_PATH                圖片路徑 ex: "./content/ScaledYOLOv4/inference/output"             
- main.py 產生 map資料於output/底下
```
範例: 
python main.py "./content/test/labels" "./content/ScaledYOLOv4/inference/output" "./content/ScaledYOLOv4/inference/output"
自定義:
python main.py -GT_PATH <GT_PATH> -DR_PATH <DR_PATH> -IMG_PATH <IMG_PATH>
```
 -->
