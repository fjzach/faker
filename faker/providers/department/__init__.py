# coding=utf-8
localized = True

from .. import BaseProvider


class Provider(BaseProvider):
	bölüm = (

           'Acil Yardım ve Afet Yönetimi', 'Adli Bilişim Mühendisliği', 'Ağaç İşleri Endüstri Mühendisliği',
           'Aile ve Tüketici Bilimleri', 'Aktüerya', 'Alman Dili ve Edebiyatı', 'Almanca Öğretmenliği',
           'Amerikan Kültürü ve Edebiyatı', 'Animasyon', 'Antropoloji', 'Arap Dili ve Edebiyatı',
           'Arapça Öğretmenliği', 'Arkeoloji', 'Arnavut Dili ve Edebiyatı', 'Astronomi ve Uzay Bilimleri',
           'Avrupa Birliği İlişkileri', 'Azerbaycan Dili ve Edebiyatı', 'Bahçe Bitkileri',
           'Balıkçılık Teknolojisi', 'Bankacılık', 'Bankacılık ve Finans', 'Bankacılık ve Sigortacılık',
           'Bankacılık ve Sigortacılık', 'Basım Yayın Üretim Teknolojileri', 'Basım Yayın Üretim Teknolojileri',
           'Basın ve Yayın', 'Beslenme ve Diyetetik', 'Bilgi ve Belge Yönetimi', 'Basın ve Yayın',
           'Bilgisayar Mühendisliği', 'Bilgisayar Teknolojisi ve Bilişim Sistemleri',
           'Bilgisayar ve Öğretim Teknolojileri Öğretmenliği', 'Bilgisayar-Enformatik', 'Bilim Tarihi',
           'Bilişim Sistemleri Mühendisliği', 'Bilişim Sistemleri ve Teknolojileri', 'Bitki Koruma',
           'Bitkisel Üretim ve Teknolojileri', 'Biyokimya', 'Biyoloji', 'Biyoloji Öğretmenliği',
           'Biyomedikal Mühendisliği', 'Biyomühendislik', 'Biyosistem Mühendisliği', 'Biyoteknoloji',
           'Boşnak Dili ve Edebiyatı', 'Bulgar Dili ve Edebiyatı', 'Cevher Hazırlama Mühendisliği',
           'Coğrafya', 'Coğrafya Öğretmenliği', 'Çağdaş Türk Lehçeleri ve Edebiyatları',
           'Çalışma Ekonomisi ve Endüstri İlişkileri', 'Çerkez Dili ve Edebiyatı', 'Çeviribilim',
           'Çevre Mühendisliği', 'Çin Dili ve Edebiyatı', 'Çocuk Gelişimi ve Eğitimi',
           'Deniz Ulaştırma İşletme Mühendisliği', 'Denizcilik İşletmeleri Yönetimi', 'Deri Mühendisliği',
           'Dijital Oyun Tasarımı', 'Dil ve Konuşma Terapisi', 'Dilbilim', 'Dini İlimler',
           'Diş Hekimliği Fakültesi', 'Doğu Dilleri', 'Ebelik', 'Eczacılık Fakültesi', 'Ekonometri',
           'Ekonomi', 'Ekonomi ve Finans', 'El Sanatları', 'Elektrik Mühendisliği',
           'Elektrik-Elektronik Mühendisliği', 'Elektronik Mühendisliği',
           'Elektronik ve Haberleşme Mühendisliği', 'Endüstri Mühendisliği',
           'Endüstri ve Sistem Mühendisliği', 'Endüstri Ürünleri Tasarımı', 'Endüstriyel Tasarımı',
           'Endüstriyel Tasarım Mühendisliği', 'Enerji Sistemleri Mühendisliği', 'Enerji Yönetimi',
           'Ergoterapi', 'Ermeni Dili ve Edebiyatı', 'Eşit Ağırlıklı Programlar', 'Fars Dili ve Edebiyatı',
           'Felsefe', 'Felsefe Grubu Öğretmenliği', 'Fen Bilgisi Öğretmenliği', 'Film Tasarımı', 'Fizik',
           'Fizik Mühendisliği', 'Fizik Öğretmenliği', 'Fizyoterapi ve Rehabilitasyon', 'Fotoğraf ve Video',
           'Fransız Dili ve Edebiyatı', 'Fransızca Öğretmenliği', 'Gastronomi ve Mutfak Sanatları',
           'Gayrimenkul ve Varlık Değerleme', 'Gazetecilik', 'Geleneksel Türk Sanatları',
           'Gemi ve Deniz Teknolojisi Mühendisliği', 'Gemi ve Yat Tasarımı', 'Genetik ve Biyomühendislik',
           'Geomatik Mühendisliği', 'Gerontoloji', 'Gıda Mühendisliği', 'Gıda Teknolojisi', 'Girişimcilik',
           'Görme Engelliler Öğretmenliği', 'Görsel İletişim Tasarımı', 'Görsel Sanatlar', 'Grafik Tasarımı',
           'Gümrük İşletme', 'Gürcü Dili ve Edebiyatı', 'Güverte', 'Halkbilim', 'Halkla İlişkiler',
           'Halkla İlişkiler ve Reklamcılık', 'Halkla İlişkiler ve Tanıtım', 'Harita Mühendisliği',
           'Havacılık Elektrik ve Elektroniği', 'Havacılık İşletmeciliği', 'Havacılık ve Uzay Mühendisliği',
           'Hayvansal Üretim', 'Hemşirelik', 'Hidrojeoloji Mühendisliği', 'Hindoloji', 'Hititoloji',
           'Hukuk Fakültesi', 'Hungaroloji', 'İbrani Dili ve Edebiyatı', 'İç Mimarlık',
           'İç Mimarlık ve Çevre Tasarımı', 'İktisadi ve İdari Bilimler Programları', 'İktisat',
           'İlahiyat Fakültesi', 'İletişim Bilimleri', 'İletişim Tasarımı',
           'İlköğretim Matematik Öğretmenliği', 'İmalat Mühendisliği', 'İngiliz Dil Bilimi',
           'İngiliz Dili ve Edebiyatı', 'İngiliz Dili ve Karşılaştırmalı Edebiyat', 'İngilizce Öğretmenliği',
           'İnsan Kaynakları Yönetimi', 'İnsan ve Toplum Bilimleri', 'İnşaat Mühendisliği', 'İslami İlimler',
           'İspanyol Dili ve Edebiyatı', 'İstatistik', 'İş Sağlığı ve Güvenliği',
           'İşitme Engelliler Öğretmenliği', 'İşletme', 'İşletme Enformatiği', 'İşletme Mühendisliği',
           'İşletme Yönetimi', 'İşletme Ekonomi', 'İtalyan Dili ve Edebiyatı', 'Japon Dili ve Edebiyatı',
           'Japonca Öğretmenliği', 'Jeofizik Mühendisliği', 'Jeoloji Mühendisliği', 'Kamu Yönetimi',
           'Kanatlı Hayvan Yetiştiriciliği', 'Karşılaştırmalı Edebiyat', 'Kazak Dili ve Edebiyatı',
           'Kentsel Tasarım ve Peyzaj Mimarisi', 'Kimya', 'Kimya Mühendisliği', 'Kimya ve Süreç Mühendisliği',
           'Kimya Biyoloji Mühendisliği', 'Kimya Öğretmenliği', 'Klasik Arkeoloji', 'Konaklama İşletmeciliği',
           'Kontrol ve Otomasyon Mühendisliği', 'Kore Dili ve Edebiyatı', 'Kurgu-Ses ve Görüntü Yönetimi',
           'Kuyumculuk ve Mücevher Tasarımı', 'Kültür Varlıklarını Koruma ve Onarım', 'Kürt Dili ve Edebiyatı',
           'Latin Dili ve Edebiyatı', 'Leh Dili ve Edebiyatı', 'Lojistik Yönetimi', 'Maden Mühendisliği',
           'Makine Mühendisliği', 'Maliye', 'Malzeme Bilimi ve Mühendisliği',
           'Malzeme Bilimi ve Nanoteknoloji Mühendisliği', 'Matematik Bölümü', 'Matematik Mühendisliği',
           'Matematik – Bilgisayar', 'Matematik Öğretmenliği', 'Medya ve İletişim', 'Mekatronik Mühendisliği',
           'Metalurji ve Malzeme Mühendisliği', 'Meteoroloji Mühendisliği', 'Mimarlık',
           'Mobilya Üretimi ve İç Mekan Tasarımı', 'Moda Tasarımı', 'Moleküler Biyoloji ve Genetik',
           'Muhasebe Bölümü', 'Muhasebe Bilgi Sistemleri', 'Muhasebe ve Denetim',
           'Muhasebe ve Finansal Yönetim', 'Mücevherat Mühendisliği',
           'Mühendislik ve Doğa Bilimleri Programları', 'Mühendislik Programları', 'Mütercim Tercümanlık',
           'Müzecilik', 'Nükleer Enerji Mühendisliği', 'Odyoloji', 'Okul Öncesi Öğretmenliği',
           'Optik ve Akustik Mühendisliği', 'Organik Tarım İşletmeciliği', 'Orman Endüstrisi Mühendisliği',
           'Orman Mühendisliği', 'Ortez-Protez', 'Otel Yöneticiliği', 'Otomotiv Mühendisliği',
           'Öğretmenlik Programları', 'Özel Eğitim Öğretmenliği', 'Pazarlama', 'Perfüzyon',
           'Petrol ve Doğalgaz Mühendisliği', 'Peyzaj Mimarlığı', 'Pilotaj', 'Polimer Mühendisliği',
           'Polonya Dili ve Kültürü', 'Protohistorya ve Ön Asya Arkeolojisi', 'Psikoloji',
           'Radyo, Televizyon ve Sinema', 'Raylı Sistemler Mühendisliği',
           'Psikolojik Danışmanlık ve Rehberlik', 'Rehberlik ve Psikolojik Danışmanlık',
           'Reklam Tasarımı ve İletişimi', 'Reklamcılık', 'Rekreasyon Yönetimi',
           'Restorasyon ve Konservasyon', 'Rus Dili Öğretmenliği', 'Rus Dili ve Edebiyatı',
           'Sağlık Yönetimi', 'Sanat Tarihi', 'Sanat ve Kültür Yönetimi',
           'Sanat ve Sosyal Bilimler Programları', 'Sanat Yönetimi', 'Sermaye Piyasası',
           'Seyahat İşletmeciliği', 'Sınıf Öğretmenliği', 'Sigortacılık ve Risk Yönetimi',
           'Sinema ve Dijital Medya', 'Sinema ve Televizyon', 'Sinoloji',
           'Sivil Hava Ulaştırma İşletmeciliği', 'Siyaset Bilimi', 'Siyaset Bilimi ve Kamu Yönetimi',
           'Siyaset Bilimi ve Uluslararası İlişkiler', 'Sosyal Bilgiler Öğretmenliği', 'Sosyal Hizmet',
           'Sosyoloji', 'Spor Yöneticiliği', 'Su Ürünleri Mühendisliği', 'Sümeroloji', 'Süt Teknolojisi',
           'Şehir ve Bölge Planlama', 'Takı Tasarımı', 'Tapu Kadastro', 'Tarım Ekonomisi',
           'Tarım Makineleri ve Teknolojileri Mühendisliği', 'Tarımsal Biyoteknoloji',
           'Tarımsal Genetik Mühendisliği', 'Tarımsal Yapılar ve Sulama', 'Tarih', 'Tarih Öğretmenliği',
           'Tarih Öncesi Arkeolojisi', 'Tarla Bitkileri', 'Teknoloji ve Bilgi Yönetimi',
           'Tekstil Mühendisliği', 'Televizyon Haberciliği ve Programcılığı', 'Tıp Fakültesi',
           'Tıp Mühendisliği', 'Toprak Bilimi ve Bitki Besleme', 'Turizm İşletmeciliği',
           'Turizm Rehberliği', 'Turizm ve Otel İşletmeciliği', 'Türk Dili ve Edebiyatı','Türk Halkbilimi',
           'Türkçe Öğretmenliği', 'Türkoloji', 'Tütün Eksperliği', 'Uçak Elektrik Elektronik',
           'Uçak Gövde – Motor', 'Uçak Mühendisliği', 'Ulaştırma Mühendisliği', 'Uluslararası Finans',
           'Uluslararası Girişimcilik', 'Uluslararası İlişkiler', 'Uluslararası Lojistik ve Taşımacılık',
           'Uluslararası Lojistik Yönetimi', 'Uluslararası Perakende Yönetimi', 'Uluslararası Ticaret',
           'Uluslararası Ticaret ve Finansman', 'Uluslararası Ticaret ve İşletmecilik',
           'Uluslararası Ticaret ve Lojistik', 'Urdu Dili ve Edebiyatı', 'Uzay Mühendisliği',
           'Üstün Zekalılar Öğretmenliği', 'Veterinerlik Fakültesi', 'Yaban Hayatı Ekolojisi ve Yönetimi',
           'Yazılım Mühendisliği', 'Yeni Medya', 'Yerel Yönetimler', 'Yiyecek İçecek İşletmeciliği',
           'Yönetim Bilişim Sistemleri', 'Yunan Dili ve Edebiyatı', 'Zaza Dili ve Edebiyatı',
           'Zihinsel Engelliler Öğretmenliği', 'Zooteknik'
           )

	@classmethod
	def bölüm(cls):
		return cls.random_element(cls.bölüm())
