__author__ = 'zekiye'

from .. import BaseProvider

class Provider(BaseProvider):
    lectures = (
                 'Yazılım Mühendisliğine Giriş', 'Genel Kimya', 'İngilizcede Akademik Beceriler', 'Almanca',
                 'Türk Dİli', 'Genel Matematik', 'Prograamlamaya Giriş', 'Akademik ve SOsyal Oryantasyon',
                 'Atatürk İlkeleri ve İnkılap Tarihi', 'Genel Fizik', 'Bilgisayar Bilimlerinde Ayrık Yapılar',
                 'Veri Yapıları ve Algoritmalar', 'Mühendisler İçin Doğrusal Cebir ve Türevsel Denklemler',
                 'Fransızca', 'İspanyolca', 'Almanca', 'İtalyanca', 'Japonca', 'Çince', 'Portekizce', 'Arapça',
                 'Yunanca', 'Latince', 'Yazılım Belirtim ve Tasarım', 'Yazılım Proje Yönetimi',
                 'Veri Tabanı Sİstemleri', 'Mühendisler İçin Olasılık', 'Programlama Dilleri Kavramları',
                 'Sanat ve İletişim', 'Yazılım Mimarisi', 'Yazılım Sınama ve Doğrulama', 'Hesaplama Kuramı',
                 'İnsan ve Toplum', 'Toplumsal Bilinç ve Etik Değerler', 'Bitirme Projesi', 'Staj',
                 'İnovasyon ve Girişimcilik', 'İşletim Sİstemleri', 'İşletim Sİstemleri Güvenliği',
                 'Bilgisayar Ağları ve İletişimi', 'Kriptografi ve Ağ Güvenliği',
                 'Linux Araçları ve Kabuk Programlama', 'Kablosuz İletişim', 'Dağıtık Veri Tabanı Sistemleri',
                 'Hesaplamalı Geometri', 'Algoritma Analizi', 'Algoritma Tasarımı',
                 'Bilgisayar Mimarisi ve Organizasyon', 'Bulut Bilişim Temelleri',
                 'Dağıtık Sistemler ve Paralel Hesaplama', 'Yapay Sinir Ağlarına Giriş', 'Müzik ve Bilgisayar',
                 'Dijital Görüntü İşlemeye Giriş', 'Mühendislik Sistemleri Analizi',
                 'Üretim Planlama,Tasarım ve Kontrol', 'Tedarik Zincirlerinin Modellenmesi ve Analizi',
                 'Endüstride Benzetim Uygulamaları', 'Matematiksel Modelleme Sanatı',
                 'Üretim ve Hizmet Sistemleri Yönetimi', 'Proje Yönetimi', 'Üretim Yönetiminde Özel Konular',
                 'İmalat Sistemlerinde Rassal Modeller', 'Optimizasyonda Sezgisel Yöntemler', 'Optimizasyon',
                 'Endüstride Bilgisayar Uygulamaları', 'Uygulamalı Üretim Sistemleri', 'Ağ Optimizasyonu',
                 'Oyun Kuramı', 'İmalat Dinamikleri ve Denetimi', 'Kuyruk Sistemleri',
                 'Rassal Süreçlere Giriş', 'İnsan Faktörleri Mühendisliği', 'Karar Teorisi',
                 'Tesis ve Malzeme Nakil Tasarımı', 'Sıralama ve Çizelgeleme', 'Finansal Mühendislik',
                 'Veri Analizi', 'Yazılım Mühendisliğinin İlkeleri', 'Veri Tabanı Yönetim Sistemleri',
                 'Nesnel Tabanlı Programlamanın Kavramları', 'İleri C++: Şablonlar ve Soysal Programlama',
                 'Bilgisayar Grafiği', 'Bilgisayar Oyunlarına Giriş', 'İleri Düzeyde Oyun Geliştirme',
                 'Yazılım Testi', 'Oyun Tasarımı', 'Bilgisayar Oyunlarında Ağ Programlama',
                 'Bilgisayar Oyunlarında Yapay Zeka', 'Yazılım Geliştirmede İlerlemeler',
                 'Sunucu-Taraflı Skript Dilleri', 'Sayısal Çözümleme', 'Web Servisleri Programlaması',
                 'Web Sayfası Tasarımı:HTML5', 'Mobil Uygulama Geliştirme',
                 'Mobil Cihazlar için Yazılım Mühendisliği', 'Yapay Zeka ve Uzman Sistemler',
                 'Bilgisayar Oyunlarında 3B Modelleme', 'Bilgisayar Oyunlarında 3B Animasyon',
                 'Yazılım Ölçümü', 'Yazılım Bakımı', 'İstemci-Taraflı Skript Dilleri',
                 'E-iş: Yönetim, Güvenlik, Pazarlama', 'İşletmeciliğe Giriş', 'Mikroekonominin İlkeleri',
                 'Makroekonominin İlkeleri', 'Ekonomi Tarihi', 'Modern Dünya Ekonomisi', 'Sağlık Ekonomisi',
                 'Uluslararası Politik Ekonomi', 'Türk Mutfak Kültürü',
                 'Karşılaştırmalı Dil ve Kültür Çalışmaları', 'Eleştirel Okuma', 'Dil ve Toplum',
                 'Uygarlık Tarihi', 'Sosyal Bilimin İlkeleri', 'Etik ve Politika: Modern Siyasi Düşünce',
                 'Siyaset Bilimine Giriş', 'Dünya Siyasetinde Güncel Konular', 'Çağdaş Dünya Tarihi',
                 'Sosyal Psikoloji', 'Sosyolojiye Giriş', 'Temel Felsefe', 'Toplumsal Sorunlar',
                 'Gündelik Yaşam ve Sosyoloji', 'Sesler, Görüntüler, Kültürler',
                 'Film Semineri: Gölgede Kalan Sinema', 'Edebiyatta Temel Kavramlar', 'Müzik ve Edebiyat',
                 'Müziğin Başyapıtları', 'Müzikte Dönemler Besteciler',
                 'Geç 20.yy Film Müzikleri ve Bestecileri', 'Filmlerde Giysiler',
                 'İletişim, Edebiyat ve Felsefe', 'Türk Sineması', 'Toplumsal Cinsiyet ve Medya',
                 'Sosyal Medya', 'Çağdaş Dünya Sineması', 'Fotoğrafta Güncel Tartışmalar ve Uygulamalar',
                 'Popüler Kültür', 'Kültürlerarası İletişim', 'Temel Fotoğrafçılık',
                 'Görsel Kültür Analizi', 'Beslenme İlkeleri ve Menü Planlama', 'Çevre Ekonomisi',
                 'Yoksulluk ve Eşitsizlik', 'İlaç ve Toplum', 'Halk Sağlığı',
                 'Sürdürülebilirlik için Tasarım', 'İnsan Hakları Siyaseti', 'Teknoloji İktisadı',
                 'Yenilikçi Tasarım Stratejileri', 'İş Hukuku', 'Analiz', 'Analitik Geometri',
                 'Stokastik Süreçlere Giriş', 'Kompleks Analiz', 'Lineer Cebir', 'Olasılık Teorisine Giriş',
                 'İleri Matematik', 'Diferansiyel Denklemlere Giriş', 'Fonksiyonel Analiz', 'Topoloji',
                 'Nümerik Analiz', 'İstatistik Teorisi', 'Psikolojide Niceliksel Yöntemler',
                 'İnsan Davranışının Biofizyolojik Temelleri', 'Görsel Algı ve Sanat',
                 'Gelişim Psikolojisine Giriş', 'Sosyal Psikoloji', 'Psikolojide Araştırma Yöntemleri',
                 'Kişilik Kuramları', 'Sağlık Psikolojisi', 'Endüstriyel Psikoloji', 'Klinik Psikoloji',
                 'Öğrenme Psikolojisi', 'Bilişsel Psikoloji', 'Psikopatoloji', 'Psikolojide Okuma ve Yazma',
                 'Psikolojik Danışmanlık ve Rehberliğin İlkeleri', 'Psikometri', 'Algı Psikolojisi',
                 'Psikolojik Danışmanlık Uygulamaları', 'Evrimsel Psikoloji',
                 'Sosyal Psikolojide Çağdaş Gelişmeler', 'İleri Fizyolojik Psikoloji',
                 'Kültürler Arası Psikoloji', 'Çocuk ve Ergen Psikopatolojisi', 'Adli Psikoloji',
                 'Psikolojide Ölçme Araçları Geliştirme', 'Psikolojinin Felsefi Temelleri',
                 'Psikoterapilere Giriş', 'Uygulamalı Psikolojik Testler', 'İnsan Cinselliği',
                 'Sistemler ve Kuramlar Yaklaşımıyla Psikoloji Tarihi', 'Dil ve Düşünce',
                 'Nöropsikolojik Değerlendirme', 'Trafik Psikolojisi', 'Motivasyon', 'Bireysel Farklılıklar',
                 'Sosyal Davranışta Bireysel Farklılıklar', 'Psikolojide Araştırma Projesi Geliştirme',
                 'Psikolojide Araştırma Projesi Uygulama ve Raporlama', 'Hukuk İngilizcesi', 'Anayasa Hukuku',
                 'Hukuka Giriş ve Hukuk Felsefesi', 'Medeni Hukuka Giriş ve Kişiler Hukuku', 'Aile Hukuku',
                 'Roma Hukuku', 'Borçlar Hukuku Genel Hükümler', 'Ticari İşletme Hukuku',
                 'Ceza Hukuku Genel Hükümler', 'İdare Hukuku', 'Ortaklıklar Hukuku', 'İdari Yargılama Hukuku',
                 'Medeni Usul Hukuku', 'Eşya Hukuku', 'Borçlar Özel Hukuku', 'Kıymetli Evrak Hukuku',
                 'Miras Hukuku', 'Ceza Özel Hukuku', 'İş Hukuku', 'Deniz Ticaret Hukuku', 'Ceza Usul Hukuku',
                 'Sosyal Güvenlik Hukuku', 'Mahkeme Uygulamaları', 'İcra ve İflas Hukuku', 'Sigorta Hukuku',
                 'Spor Hukuku', 'Hukuk Stajı', 'Çeviriye Giriş', 'Sözcükbilimi', 'Dilbilime Giriş',
                 'Medya ve İletişim Metinleri Çevirisi', 'Bilgisayar Destekli Çeviri Çalışmaları',
                 'Eleştirel Okuma', 'İngilizce-Türkçe Karşıtsal Çözümleme Çalışmaları',
                 'Edebiyatta Temel Kavramlar', 'Hukuk Metinleri Çevirisi', 'Yazılı Metinden Sözlü Çeviri',
                 'Ardıl Çeviri', 'Çeviri Tarihi', 'Eşzamanlı Çeviri', 'Ekonomi Metinleri Çevirisi',
                 'Ticaret ve Finans Metinleri Çevirisi', 'Çağdaş Batı Edebiyatına Giriş',
                 'Kültürel Yönleriyle Yazılı ve Sözlü Çeviri', 'Özel Alan Çevirisi', 'Edimbilim ve Çeviri',
                 'Yabancı Dil Olarak İngilizce Öğretimi', 'Çeviri Eleştirisi', 'Toplum Çevirmenliği',
                 'Konferans Çevirmenliğinde Terminoloji Çalışmaları', 'Konferans Ortamında Eşzamanlı Çeviri',
                 'Çevirmenler İçin Profesyonel İletişim', 'Siyaset Bilimi Metinleri Çevirisi',
                 'Metin Düzeltme ve Yayına Hazırlama', 'Görsel-İşitsel Çeviri', 'Çeviride Alan Çalışması',
                 'Yaratıcı Yazma', 'Çeviride Kaybolmamak', 'Tüketici Davranışları',
                 'Yönetim ve Maliyet Muhasebesi', 'İşletme Finansmanı', 'İnsan Kaynakları Yönetimi',
                 'Pazarlama İlkeleri', 'İç Mekanları Duyumsamak', 'Sanat ve Tasarım Tarihi', 'Maket Yapımı',
                 'İçmimarlık ve Çevre Tasarımı için Çevresel Kontrol Sistemleri', 'Yapım ve Malzemeler',
                 'Mobilya Tasarımı', 'Geleceğe Yönelik İç Mimarlık Çalışmaları', 'Evrensel Tasarım',
                 'Portfolio Tasarımı', '3 Boyutlu Mimari Tasarım', 'Akıllı ve Etkileşimli Mekanlar',
                 'Osmanlı Döneminden Modern Türkiyeye Güzel Sanatlar', 'Ekolojik ve Biyo-iklimsel Tasarım',
                 'Çağdaş Peyzaj Tasarımına Giriş', 'Sağlık Bilimleri ve Hemşireliğe Giriş', 'Anatomofizyoloji',
                 'Biyokimya', 'Hemşirelik Esasları', 'Sağlığın Değerlendirilmesi',
                 'Klinik Mikrobiyoloji ve Enfeksiyon Hastalıkları', 'İç Hastalıkları Hemşireliği',
                 'Cerrahi Hastalıkları Hemşireliği', 'Hemşireliğe Özel Farmakoloji', 'Patoloji',
                 'Bilgisayar Uygulamalı Biyoistatistik', 'Kadın Sağlığı ve Hastalıkları Hemşireliği',
                 ' Çocuk Sağlığı ve Hastalıkları Hemşireliği', 'Sağlık Bilimlerinde Araştırma Yöntemleri',
                 'Sağlık Bilimlerinde Etik', 'Epidemiyoloji', 'İlk Yardım', 'Hemşirelikte Yönetim',
                 'Lojistik İlkeleri', 'Lojistik Yönetimi için Akademik Beceriler', 'Pazarlama Yönetimi',
                 'Taşımacılık Yönetimi ve Yasal Çerçeve', 'Lojistik Planlama ve Modelleme',
                 'Perakendeciliğe Giriş', 'İşletme Finansmanı', 'Küresel Lojistik Yönetimi',
                 'Satınalma ve Envanter Yönetimi', 'Lojistikte Simülasyon', 'Gemi Kiralama ve Acenteliği',
                 'Tedarik Zinciri Stratejileri', 'Kaynak Planlama Tabanlı Tedarik Zinciri Yönetimi',
                 'Uluslararası Karayolu Yük Taşımacılığı', 'Kentsel Lojistik', 'Ters Lojistik',
                 'Yalın Tedarik Zinciri Yönetimi', 'Tedarik Zincirinde Risk Yönetimi',
                 'Yönlendirilmiş Araştırma', 'Bilgi Güvenliği Yönetimi', 'Depo Yönetimi',
                 'Demiryolu Taşımacılığı', 'Tehlikeli Madde Lojistiği', 'Matematik ve İstatistiğe Giriş',
                 'İletişim Çalışmalarına Giriş', 'İletişimde Sunum Becerileri', 'İletişim ve Etik',
                 'Halkla İlişkilerin İlkeleri', 'Reklamcılığın İlkeleri', 'Kişilerarası İletişim',
                 'Halkla İlişkiler ve Reklamcılıkta Yaratıcılık', 'Medya Planlama ve Satın Alma',
                 'Halkla İlişkiler ve Reklam Yazarlığı', 'Marka Yönetimi', 'Stratejik Reklam Analizi',
                 'Kurum Kültürü', 'Kurumsal İletişim', 'Etkinlik Yönetimi',
                 'Halkla İlişkilerde Güncel Eğilimler', 'Marka İletişiminde Yaratıcılık', 'Habercilik',
                 'Film Çalışmaları', 'Türk Medya Tarihi', 'Görsel Gazetecilik', 'Senaryo Yazımı',
                 'İleri Senaryo Yazımı', 'Belgesel Yapımı', 'İletişimde Dil ve Diksiyon',
                 'Küreselleşme ve Medya', 'Radyo Program Yapımı', 'İnternet Gazeteciliği',
                 'Sinemada Müzik ve Ses Tasarımı', 'Sinema Akımları', 'Medya, Kültür ve Teknoloji',
                 'Gündelik Hayat ve İletişim', 'Tıbbi Bilimlere Giriş',
                 'Normal Yapı ve Fonksiyon: Solunum, Dolaşım, Kan-Lenfoid, Boşaltım',
                 'Normal Yapı ve Fonksiyon: Sindirim, Metabolizma',
                 'Normal Yapı ve Fonksiyon: Hareket ve Sinir Sistemleri',
                 'Normal Yapı ve Fonksiyon: Hayatın Evreleri',
                 'Patolojik ve Klinik Bilimlere Giriş', 'Sistem Patolojileri: Hayatın Evreleri', 'Tıp Stajı'
                )









