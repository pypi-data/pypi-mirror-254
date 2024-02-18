# TkLiteUI

`TkLiteUI` kütüphanesi, Python'un Tkinter kütüphanesi kullanılarak grafik kullanıcı arayüzleri (GUI) geliştirirken kod kalabalığını azaltmayı ve arayüz tasarımını kolaylaştırmayı amaçlar. Temel Tkinter widget'ları üzerine inşa edilmiş bu kütüphane, daha az kod ile daha hızlı ve okunaklı GUI uygulamaları oluşturmanıza olanak tanır.

## Özellikler

- **Pencere Yönetimi:** Kolayca ana pencere veya yardımcı pencereler oluşturun.
- **Widget Yönetimi:** Butonlar, etiketler ve giriş alanları gibi temel widget'ları hızlıca ekleyin.
- **Kullanıcı Etkileşimi:** Basit bir API ile widget'ların etkileşimlerini yönetin.
- **Esneklik:** Uygulamanızın ihtiyaçlarına göre özelleştirilebilir widget özellikleri.

## Kurulum

`TkLiteUI` kütüphanesini Python `pip` aracılığıyla aşağıdaki komutu kullanarak kurabilirsiniz:

pip install TkLiteUI


## Kullanım

Kütüphaneyi kullanmaya başlamak için, ilk önce `ui` sınıfını projenize dahil edin:

```python
import TkLiteUI as tl

#Ardından, ui sınıfının bir örneğini oluşturarak bir pencere ve bazı widget'lar ekleyebilirsiniz:

# UI örneğini oluştur
ui = tl.ui()

# Pencere oluştur
pencere = ui.create_window(title="Merhaba TkLiteUI", width=800, height=600)

# Buton ekle
buton = ui.add_button(pencere=pencere, text="Buton", button_x=100, button_y=50)

# Uygulamayı başlat
pencere.mainloop()
```

Geliştirme
Bu kütüphane açık kaynaklıdır ve geliştirme için katkıda bulunabilirsiniz. GitHub üzerinden TkLiteUI reposuna giderek issue açabilir, pull request gönderebilir ve kütüphanenin gelişimine yardımcı olabilirsiniz.

Lisans
Bu proje `MIT` Lisansı altında lisanslanmıştır.

Yazar
Adem Ulker


`TkLiteUI` ile hızlı ve etkili GUI geliştirmenin keyfini çıkarın!
