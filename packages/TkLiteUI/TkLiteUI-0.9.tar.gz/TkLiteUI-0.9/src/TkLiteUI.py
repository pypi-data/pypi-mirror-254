"""
TkLiteUI as tl
    Öncelikle tl modülünden ui sınıfını kullanarak bir örnek oluşturun
----------------
ui = tl.ui()
----------------
.
.
--------------------
Yazar: Adem Ulker
--------------------
"""
import tkinter as tk


class ui:
    """
        UI sınıfı, Tkinter tabanlı bir grafik kullanıcı arayüzü (GUI) uygulaması için temel işlevler sağlar.
        Bu sınıfın bir örneği, farklı GUI bileşenleri oluşturmak için kullanılır.

        Özellikler:
        ----------------
        - FirstWindow (bool): İlk Tkinter penceresinin oluşturulup oluşturulmadığını takip eder.
                              Bu, birden fazla pencere yönetiminde kullanılır.

        Bu sınıf, pencere oluşturma, buton ekleme ve diğer widget yönetimi gibi işlevleri içerir.

        --------------------
        Yazar: Adem Ulker
        --------------------
    """

    def __init__(self):
        self.FirstWindow = False

    # region Pencere Ekleme
    # Bu fonksiyon ile yeni pencereler oluşturabiliriz
    # İlk pencere oluşturuldu mu diye kontrol etmek için bir flag (işaretçi) kullanın
    def create_window(self, **kwargs):
        """
            Belirtilen özelliklere göre bir Tkinter penceresi oluşturur ve konumlandırır. Bu fonksiyon,
            kullanıcıya pencere boyutu, başlık, arka plan rengi, opaklık, ikon ve diğer birçok özellik
            üzerinde kontrol sağlar. İlk pencere daha önce oluşturulmuşsa, bir 'Toplevel' penceresi
            oluşturur ve gerekirse gizler. İlk pencere henüz oluşturulmamışsa, bir 'Tk' ana penceresi oluşturur.

            Parametreler:
            -------------

            width (int, opsiyonel): Pencerenin genişliği. Varsayılan değer 400.
            height (int, opsiyonel): Pencerenin yüksekliği. Varsayılan değer 300.
            title (str, opsiyonel): Pencerenin başlığı. Varsayılan değer 'Türkiye'.
            bg (str, opsiyonel): Pencerenin arka plan rengi. Varsayılan değer 'beige'.
            is_primary (bool, opsiyonel): Eğer True ise, yardımcı pencere başlangıçta gizlenir. Varsayılan değer False.
            fullscreen (bool, opsiyonel): Eğer True ise, pencereyi tam ekran modunda başlatır. Varsayılan değer False.
            topmost (bool, opsiyonel): Eğer True ise, pencereyi her zaman üstte tutar. Varsayılan değer False.
            opacity (float, opsiyonel): Pencerenin opaklık değeri (1.0 tam opak, 0.0 tam şeffaf). Varsayılan değer 1.0.
            icon (str, opsiyonel): Pencere için kullanılacak ikonun dosya yolu. Varsayılan değer None.
            resizable_width (bool, opsiyonel): Pencerenin genişliğinin ayarlanabilir olup olmadığı. Varsayılan True.
            resizable_height (bool, opsiyonel): Pencerenin yüksekliğinin ayarlanabilir olup olmadığı. Varsayılan True.
            overrideredirect (bool, opsiyonel): Pencere kenarlıkları ve başlık çubuğunu gizler. Varsayılan değer False.

            Örnek Kullanım:
            ---------------
            # Temel pencere oluşturma
            pencere = create_window(width=500, height=400, title="Örnek Pencere", bg='light blue')

            # Detaylı özelliklere sahip pencere oluşturma
            pencere = create_window(width=600, height=500, title="Örnek Pencere", bg='light grey',
                                            fullscreen=True, topmost=True, opacity=0.95, icon='icon.ico',
                                            resizable_width=False, resizable_height=False, overrideredirect=False)

            Notlar:
            -------
            - `overrideredirect(True)` kullanıldığında, işletim sistemi tarafından sağlanan pencere yönetimi
              özellikleri (örneğin, sürükleme ile taşıma) kullanılamaz hale gelir.
            - Pencere ikonu, sadece '.ico' formatını destekleyen işletim sistemlerinde etkilidir.

            --------------------
            Yazar: Adem Ulker
            --------------------
        """

        # İlk pencere oluşturulduysa Toplevel kullan, değilse Tk
        if self.FirstWindow:
            root = tk.Toplevel()
        else:
            root = tk.Tk()
            self.FirstWindow = True

        # Pencere özelliklerini ayarla
        width = kwargs.get('width', 400)
        height = kwargs.get('height', 300)
        title = kwargs.get('title', 'Türkiye')
        bg = kwargs.get('bg', 'beige')
        is_fullscreen = kwargs.get('fullscreen', False)
        is_topmost = kwargs.get('topmost', False)
        opacity = kwargs.get('opacity', 1.0)  # Opaklık değeri: 1.0 tam opak, 0.0 tam şeffaf

        root.iconbitmap(kwargs.get('icon', None))
        root.geometry(f"{width}x{height}+{(root.winfo_screenwidth() - width) // 2}+{(root.winfo_screenheight() - height) // 2}")
        root.title(title)
        root.configure(bg=bg)
        root.attributes('-topmost', is_topmost)
        root.attributes('-alpha', opacity)
        root.attributes('-fullscreen', is_fullscreen)

        root.resizable(width=kwargs.get('resizable_width', True), height=kwargs.get('resizable_height', True))

        if kwargs.get('overrideredirect', False):
            root.overrideredirect(True)

        return root

    # endregion

    # region Buton Ekleme

    # Bu fonksiyon ile yeni butonlar oluşturabiliriz
    def add_button(self, **kwargs):
        """
            Belirtilen özelliklere göre Tkinter kütüphanesi kullanılarak bir buton oluşturur ve bu butonu
            kullanıcı tarafından belirtilen konuma yerleştirir. Fonksiyon, butonun görsel özelliklerini
            özelleştirmek için arka plan rengi, yazı rengi, yazı tipi, çerçeve özellikleri ve imleç stili gibi
            parametreleri destekler.

            Temel Kullanım:
            ---------------
            En basit formda, bir buton için sadece zorunlu parametreler sağlanarak hızlı bir şekilde buton eklemek mümkündür.

            Örnek:
            Buton_Name = ui.add_button(pencere=WindowName, text="Buton", button_x=10, button_y=20,on_click=lambda: Buton_Event(Buton_Name))

            Detaylı Kullanım:
            -----------------
            Detaylı kullanımda, butonun görsel özelliklerini ve davranışlarını özelleştirmek için mevcut tüm parametreler
            kullanılabilir. Bu, daha kontrollü ve özelleştirilmiş bir buton oluşturmanıza olanak tanır.

            Örnek:
            Buton_Name = ui.add_button(pencere=WindowName, text="Buton", bg="lightblue", fg="darkblue",
                                       font=("Helvetica", 14), button_x=50, button_y=100, button_width=200, button_height=50,
                                       bw=2, rf="ridge", cr="hand2", on_click={'action': lambda: Buton_Event(Buton_Name)})

            Parametreler:
            -------------
            pencere (tk.Tk veya tk.Toplevel): Butonun ekleneceği pencere veya frame.
            text (str): Buton üzerinde görünecek metin.
            button_x (int): Butonun x koordinatı.
            button_y (int): Butonun y koordinatı.
            button_width (int, opsiyonel): Butonun genişliği.
            button_height (int, opsiyonel): Butonun yüksekliği.
            bg (str, opsiyonel): Butonun arka plan rengi.
            fg (str, opsiyonel): Buton metninin rengi.
            font (tuple, opsiyonel): Buton metninin yazı tipi ve boyutu.
            bw (int, opsiyonel): Butonun kenarlık genişliği. ('borderwidth' için kısaltma)
            rf (str, opsiyonel): Butonun kenarlık stilini belirler. ('relief' için kısaltma)
            cr (str, opsiyonel): Üzerine gelindiğinde imlecin alacağı şekil. ('cursor' için kısaltma)
            on_click (callable, opsiyonel): Butona tıklandığında çağrılacak fonksiyon.

            Dönüş Değeri:
            --------------
            tk.Button: Oluşturulan ve konumlandırılan Tkinter butonu.

            --------------------
            Yazar: Adem Ulker
            --------------------
        """

        root = kwargs.get('pencere')
        text = kwargs.get('text', 'Buton')
        button_x = kwargs.get('button_x', 0)
        button_y = kwargs.get('button_y', 0)
        button_width = kwargs.get('button_width', None)
        button_height = kwargs.get('button_height', None)
        click_event = kwargs.get('on_click')

        # Varsayılan buton konfigürasyonları
        default_button_config = {

            'bg': kwargs.get('bg', 'gray'),
            'fg': kwargs.get('fg', 'white'),
            'font': kwargs.get('font', ('Helvetica', 12)),
            'anchor': kwargs.get('anc', 'center'),
            'borderwidth': kwargs.get('bw', 3),
            'relief': kwargs.get('rf', 'ridge'),
            'cursor': kwargs.get('cr', None)
        }

        # Buton oluştur ve konfigüre et
        button = tk.Button(root, text=text)
        button.config(default_button_config)
        button.place(x=button_x, y=button_y, width=button_width, height=button_height)

        # Buton komutunu ayarla
        if click_event and 'action' in click_event:
            button.config(command=click_event['action'])

        return button

    # endregion

    # region Label Ekleme

    def add_label(self, **kwargs):
        """
            Belirtilen özelliklere göre Tkinter kütüphanesi kullanılarak bir etiket (Label) oluşturur ve bu Label'i
            kullanıcı tarafından belirtilen konuma yerleştirir. Fonksiyon, etiketin görsel özelliklerini özelleştirmek
            için arka plan rengi, yazı rengi, yazı tipi ve çerçeve özellikleri gibi parametreleri destekler.

            Temel Kullanım:
            ---------------
            En basit formda, etiket için sadece zorunlu parametreler sağlanarak hızlı bir şekilde Label eklemek mümkündür.

            Örnek:
            Label_1 = ui.add_label(pencere=WindowName, text="Label", label_x=10, label_y=20)

            Detaylı Kullanım:
            -----------------
            Detaylı kullanımda, Label'in görsel özelliklerini ve davranışlarını özelleştirmek için mevcut tüm parametreler
            kullanılabilir. Bu, daha kontrollü ve özelleştirilmiş bir etiket oluşturmanıza olanak tanır.

            Örnek:
            Label_1 = ui.add_label(pencere=WindowName, text="Label", bg="lightblue", fg="darkblue",
                                   font=("Helvetica", 14), label_x=50, label_y=100, label_width=200, label_height=50,
                                   bw=2, hbg='red', anc='center')

            Parametreler:
            -------------
            pencere (tk.Widget): Label'in ekleneceği pencere.
            text (str): Label üzerinde görünecek metin.
            label_x (int): Label x koordinatı.
            label_y (int): Label y koordinatı.
            label_width (int, opsiyonel): Label genişliği.
            label_height (int, opsiyonel): Label yüksekliği.
            bg (str, opsiyonel): Arka plan rengi.
            fg (str, opsiyonel): Yazı rengi.
            font (tuple, opsiyonel): Yazı tipi ve boyutu.
            bw (int, opsiyonel): Çerçeve kalınlığı. Belirtilmezse, çerçeve eklenmez.
            hbg (str, opsiyonel): Çerçeve rengi. Belirtilmezse, çerçeve eklenmez.
            anc (str, opsiyonel): Label metninin konumunu belirler. Varsayılan 'center'.

            --------------------
            Yazar: Adem Ulker
            --------------------
        """

        root = kwargs.get('pencere')
        text = kwargs.get('text', '')
        label_x = kwargs.get('label_x', 0)
        label_y = kwargs.get('label_y', 0)
        label_width = kwargs.get('label_width', None)
        label_height = kwargs.get('label_height', None)

        # Varsayılan label konfigürasyonları
        default_label_config = {
            'bg': kwargs.get('bg', 'Black'),
            'fg': kwargs.get('fg', 'black'),
            'font': kwargs.get('font', ('Arial', 12)),
            'anchor': kwargs.get('anc', 'center'),

            'borderwidth': kwargs.get('bw', None),
            'highlightbackground': kwargs.get('hbg', None)
        }

        # kwargs içinde belirtilen özelliklerle varsayılanları birleştir
        label_config = {**default_label_config}

        # Label oluştur ve konfigüre et
        label = tk.Label(root, text=text)
        label.config(label_config)

        label.place(x=label_x, y=label_y, width=label_width, height=label_height)

        return label

    # endregion

    # region Entry Ekleme
    def add_entry(self, **kwargs):
        """
            Belirtilen özelliklere göre Tkinter kütüphanesi kullanılarak bir giriş kutusu (Entry) oluşturur ve
            bu giriş kutusunu kullanıcı tarafından belirtilen konuma yerleştirir. Fonksiyon, giriş kutusunun
            görsel özelliklerini özelleştirmek için arka plan rengi, yazı rengi ve yazı tipi gibi parametreleri
            destekler. Ayrıca, giriş kutusundaki veri her değiştiğinde tetiklenecek bir callback fonksiyonunu
            tanımlamak için bir mekanizma sağlar.

            Temel Kullanım:
            ---------------
            En temel düzeyde, sadece zorunlu parametreleri belirterek giriş kutusu oluşturabilirsiniz.
            Bu, hızlı ve kolay bir şekilde giriş kutusu eklemenizi sağlar.

            Örnek:
            EntryName = ui.add_entry(pencere=WindowName, entry_x=50, entry_y=100, entry_width=150)

            Detaylı Kullanım:
            -----------------
            Detaylı kullanımda, giriş kutusunun görsel özelliklerini ve davranışlarını özelleştirmek için
            mevcut tüm parametreler kullanılabilir. Bu, daha kontrollü ve özelleştirilmiş bir giriş kutusu
            oluşturmanıza olanak tanır.

            Örnek:
            EntryName = ui.add_entry(pencere=WindowName, entry_x=50, entry_y=100, entry_width=150,
                                     bg="lightyellow", fg="darkblue", font=("Helvetica", 14),
                                     callback=lambda value: print("Giriş değişti:", value))

            Parametreler:
            -------------
            pencere (tk.Tk veya tk.Toplevel): Giriş kutusunun ekleneceği pencere veya frame.
            entry_x (int): Giriş kutusunun x koordinatı.
            entry_y (int): Giriş kutusunun y koordinatı.
            entry_width (int): Giriş kutusunun genişliği.
            bg (str, opsiyonel): Giriş kutusunun arka plan rengi.
            fg (str, opsiyonel): Giriş kutusundaki yazı rengi.
            font (tuple, opsiyonel): Giriş kutusundaki yazı tipi ve boyutu.
            callback (callable, opsiyonel): Giriş kutusundaki veri her değiştiğinde çağrılacak fonksiyon.

            --------------------
            Yazar: Adem Ulker
            --------------------
        """
        root = kwargs['pencere']
        entry_x = kwargs.get('entry_x', 0)
        entry_y = kwargs.get('entry_y', 0)
        entry_width = kwargs.get('entry_width', 20)
        # Entry widget için 'height' parametresi doğrudan kullanılmaz, bu yüzden buradan kaldırıldı.
        callback = kwargs.get('callback', None)  # Kullanıcı tarafından sağlanan callback fonksiyonu

        default_entry_config = {
            'bg': kwargs.get('bg', 'White'),
            'fg': kwargs.get('fg', 'black'),
            'font': kwargs.get('font', ('Arial', 12))
        }

        # Entry için StringVar oluştur ve değişiklikleri izle
        entry_var = tk.StringVar()
        entry = tk.Entry(root, textvariable=entry_var, **{k: v for k, v in kwargs.items() if k in ['bg', 'fg', 'font']})
        entry.config(default_entry_config)
        entry.place(x=entry_x, y=entry_y, width=entry_width)

        # Kullanıcı tarafından callback fonksiyonu sağlanmışsa, değişiklikleri izle
        if callback:
            def on_change(*args):
                callback(entry_var.get())

            entry_var.trace_add("write", on_change)

        return entry

    # endregion

    # region Pencere Aç, Kapat, Gizle
    def StartMainWindow(self, Pencere):
        """
        Ana pencereyi başlatır.

        Parametreler:
        ----------------
        StartMainWindow(windowName): Başlatılacak ana Tkinter penceresi.

        Örnek Kullanım:
        ----------------
        ui.StartMainWindow(MainWindowName)

        --------------------
        Yazar: Adem Ulker
        --------------------
        """
        Pencere.mainloop()

    def CloseMainWindow(self, Pencere):
        """
        Ana pencereyi kapatır ve kaynakları serbest bırakır.

        Parametreler:
        ----------------
        CloseMainWindow(windowName): Kapatılacak ana Tkinter penceresi.

        Örnek Kullanım:
        ----------------
        ui.CloseMainWindow(MainWindowName)

        --------------------
        Yazar: Adem Ulker
        --------------------
        """
        Pencere.destroy()

    def ShowSubWindow(self, pencere):
        """
        Yardımcı pencereyi gösterir.

        Parametreler:
        ----------------
        pencere (windowName): Gösterilecek yardımcı Tkinter penceresi.

        Örnek Kullanım:
        ----------------
        ui.ShowSubWindow(SubWindowName)

        --------------------
        Yazar: Adem Ulker
        --------------------
        """
        pencere.deiconify()

    def HideSubWindow(self, pencere):
        """
        Yardımcı pencereyi gizler.

        Parametreler:
        ----------------
        ui.HideSubWindow(windowName): Gizlenecek yardımcı Tkinter penceresi.

        Örnek Kullanım:
        ----------------
        HideSubWindow(SubWindowName)

        --------------------
        Yazar: Adem Ulker
        --------------------
        """
        pencere.withdraw()
    # endregion
