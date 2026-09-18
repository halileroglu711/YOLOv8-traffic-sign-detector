> Dil: Türkçe  🇹🇷

İngilizce için : [English](README.md)

![Header](https://capsule-render.vercel.app/api?type=waving&height=250&color=185959&text=🚦Trafik%20İşareti%20Dedektörü&section=header&textBg=false&reversal=false&fontAlign=50&fontSize=50&animation=fadeIn&rotate=0&desc=YOLOv8%20ile%20&descAlignY=69&fontColor=EBF2F2)
# 💭Tanım
Bu Fully Convolutional Network kullanılarak fine-tune edilmiş bir YOLOv8 (YOLOv8n.pt) modeli içeren bir Derin Öğrenme projesidir. Daha önceden eğitilmiş bir YOLOv8 modeli yeni bir veri setiyle tekrar eğitilir. Eğitim süreci boyunca  [🔍Traffic sign dataset](https://universe.roboflow.com/university-km5u7/traffic-sign-detection-yolov8-awuus/dataset/11) kullanılmıştır. Modelin final versiyonu bir görsel içerisindeki trafik işareti objelerini epey doğru bir şekilde tespit edebilir. Tahmin örnekleri ve daha fazla detay takip eden başlıkların altında görülebilir.
## Eğitim Süreci Detayları
**Model:** `YOLOv8n.pt(Nano)` <br>
 **Yöntem:** `Fine-tuning` <br>
 **Görev:** `Trafik işaretleri tespiti` <br>
 **Eğitim Epoch miktarı:** `10` <br>
 **Veri seti:** [🔍Traffic sign dataset](https://universe.roboflow.com/university-km5u7/traffic-sign-detection-yolov8-awuus/dataset/11) <br>
 **Girdi görseli boyutu:** `640x640` <br>
**Teknoloji Yığını:** ![Python](https://img.shields.io/badge/Python-black?style=flat-square&logo=python&logoColor=%23EBDD1A),
![PyTorch](https://img.shields.io/badge/PyTorch-black?style=flat-square&logo=pytorch) , 
![OpenCV](https://img.shields.io/badge/OpenCV-black?style=flat-square&logo=opencv&logoColor=%231A29EB),![Static Badge](https://img.shields.io/badge/Ultralytics-black?style=flat-square&logo=ultralytics&logoColor=%236119B3),
![Static Badge](https://img.shields.io/badge/YOLOv8-black?style=flat-square&logo=yolo&logoColor=%2319A1B3)
> [!NOTE]
> Veri Çeşitliliği eğitim süreci için çok önemlidir. Eğitimden önce veri setine bir dizi augmentation işlemi uygulanmalıdır. Bu augmentation işlemleri verilen veri setinde hali hazırda uygulanmıştır.
# 👀Çıktılar
Modelin doğruluğu model tarafından daha önce görülmemiş iki görsel üzerinde test edilmiştir. İşte sonuçlar:
| **Test Görseli**    | **Modelin Tahmini**    |
|            :---:    |  :---:    |
|   ![Test 1](assets/test1.jpg "ilk test görseli")    |  ![tahmin 1](assets/prediction-result-1.jpg "ilk tahmin")  |
|   ![Test 2](assets/test2.jpg "ikinci test görseli") | ![Prediction 2](assets/prediction-result-2.jpg "tahmin 2")  |
- Conf değeri tahmin görsellerinde nesnenin etiketinin hemen yanında görülebilir. Bu değer, model tarafından belirlenen özgüven skorunu temsil eder. 
## Performans Değerlendirmesi
- Model 10 epoch boyunca eğitildi ve her epoch sonunda doğrulama veri setiyle test edildi. Aşağıdaki görsel modelin zaman içinde eğitim ve doğrulama kaybı değerlerindeki değişiklikleri sergiliyor.
![results](results.png "results" )
- Görüldüğü üzere, modelin performansı eğitim ve doğrulama kaybı değerlerindeki düşüşe karşılık kademeli olarak artmıştır.
### 🤔Bu nasıl yorumlanmalı?
- Model eğitiminde her şeyden önce kontrol edilmesi gereken en kritik nokta aşırı öğrenme (overfitting) yada az öğrenme (underfitting) gerçekleşip gerçekleşmediğidir.
- Bunu sağlayan şey **train/box_loss** ve **val/box_loss** arasındaki uyumdur. Overfitting durumunda **train/box_loss** düşerken, **val/box_loss** düşmek yerine aynı seviyede kalır. Ve underfitting gerçekleştiğinde,modelin öğrenmediği ve veri setinin veri çeşitliliği bakımından yetersiz olduğu anlamına gelen **train/box_loss** aynı seviyede kalır.
- **Recall** grafiği nesnelerin yüzde kaçının tespit edildiğini gösterirken, **Precision** grafiği modelin tahmin doğruluğunu temsil eder.
- *mAP50(B*) grafiği modelin performansını bir tahminin IoU (kesişim/birleşim) değerinin 0.50'den daha yüksek olması gerektiği katı bir kurala göre değerlendirdiği için en önemli ölçümdür. Ayrıca `best.pt` en yüksek *map50* değerine sahip olan ağırlık olarak seçilir. *mAP50-95(B)* grafiği modelin performansını daha katı bir kurala göre değerlendirir. Bu grafik modelin tahminlerini 50'den 95'e kadar *mAP* değerlerine göre değerlendirir ve sonuçların ortalamasını alır.

# 📥Kurulum
- Repoyu ve kütüphaneleri yüklemek ve kendi yerel bilgisayarınızda kullanmak için, aşağıdaki adımları takip edin: <br>

1-
```bash
# Repoyu yerel bilgisayarınıza klonlayın
git clone https://github.com/halileroglu711/YOLOv8-traffic-sign-detector.git

```
2-
```bash
# Proje dosyasına girin
cd traffic-sign-detector
```

3-
```bash
# Gerekli kütüphaneleri yükleyin.
pip install -r requirements.txt
```

4-
```bash
# Modeli test etmek için 
python test.py
```


# 📂 Proje Yapısı

```text
traffic-sign-detector/
│
├── assets/
│   ├── prediction-result-1.jpg
|   ├── prediction-result-2.jpg
|   ├── test1.jpg
|   └── test2.jpg
│
├── weights/
│   └── best.pt             
│
├── .gitignore              
├── README.md
└── README_tr.md            
├── requirements.txt        
├── results.png               
├── test.py             
├── train.py                

```

## ✍🏻Lisans
-Bu proje MIT lisansı ile lisanslıdır..<br>daha fazla detay için [LICENCE](LICENCE) dosyasını inceleyin.


## 📬 İletişim
- Herhangi bir hatam varsa bana bildirin. Bana buradan ulaşabilirsiniz:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](www.linkedin.com/in/halil-eroğlu-5505783a1)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/halileroglu711)
[![Gmail](https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:halileroglu711@gmail.com)

