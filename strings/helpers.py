#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """✅**<u>Tüm Komutları:</u>**

/oynat    - şarkıyı oynatır.
/vplay    - video olarak oynatır.
/durdur   - Çalan müziği duraklatın.
/devam    - Duraklatılan müziği devam ettir.
/atla     - Çalmakta olan müziği atla.
/son      - Çalan müziği durdurun.
/karistir - Sıraya alınmış çalma listesini rastgele karıştırır.
/tekrarla - şarkıyı tekrar çalar.
/bul      - şarkıyı/videoyu indirir.
/stream    - canlı yayın akışları oynatır.
"""

HELP_2 = """✅<u>**Sahipler:**</u>

Bot bilgisi için ulaşın - @meyitzade
Bot bilgisi için ulaşın -  @Zg_mali
"""

HELP_3 = """✅<u>**Bilgi:**</u>

Bot hakkında bilgi almak için - @hiraset
/stats - En İyi 10 Parçayı Alın Global İstatistikler, Botun En İyi 10 Kullanıcısı, Botta En İyi 10 Sohbet, Sohbette Oynanan En İyi 10 vb..
"""

HELP_4 = """✅<u>**Sahip/Reklam:**</u>
 
Reklam ve işbirliği için @hiraset
Reklam ve işbirliği için @HirasetTR
"""

HELP_5 = """🔰**<u>Owner komutları :</u>**
/addsudo [Kullanıcı adı veya bir kullanıcıyı yanıtla]
/delsudo [Kullanıcı adı veya bir kullanıcıyı yanıtla]

🤖**<u>BOT KOMUTLARI:</u>**
/restart - Botu Yeniden Başlat. 
/update - Botu Güncelle.
/speedtest - Sunucu hızlarını kontrol edin
/maintenance [enable / disable] 
/logger [enable / disable] - Bot, logger grubundaki aranan sorguları günlüğe kaydeder.
/get_log [Hat Sayısı] - Heroku veya vps'den botunuzun günlüğünü alın. Her ikisi için de çalışır.

📈**<u>STATS KOMUTLARI:</u>**
/activevoice - Botta aktif sesli sohbetleri kontrol edin.
/activevideo - Botta aktif görüntülü aramaları kontrol edin.
/stats - Bot İstatistiklerini Kontrol Edin

⚠️**<u>KARA LİSTE SOHBET FONKSİYONU:</u>**
/blacklistchat [CHAT_ID] - Music Bot kullanarak herhangi bir sohbeti kara listeye alın
/whitelistchat [CHAT_ID] - Music Bot'u kullanarak kara listeye alınmış herhangi bir sohbeti beyaz listeye alın
/blacklistedchat - Kara listeye alınan tüm sohbetleri kontrol edin.

👤**<u>ENGELLİ FONKSİYON:</u>**
/block [Kullanıcı adı veya kullanıcıya yanıt] - Bir kullanıcının bot komutlarını kullanmasını engeller.
/unblock [Kullanıcı adı veya kullanıcıya yanıt] - Bir kullanıcıyı Bot'un Engellenenler Listesinden kaldırma.
/blockedusers - Engellenen Kullanıcı Listelerini Kontrol Edin

👤**<u>GBAN FONKSİYONU:</u>**
/gban [Kullanıcı adı veya kullanıcıya yanıt] - Botun sunduğu sohbetten bir kullanıcıyı Gban ve botunuzu kullanmasını engelleyin.
/ungban [Kullanıcı adı veya kullanıcıya yanıt] - Bir kullanıcıyı Bot'un gbanlı Listesinden çıkarın ve onun botunuzu kullanmasına izin verin
/gbannedusers - Gbanlı Kullanıcı Listelerini Kontrol Edin

🎥**<u>VİDEO ÇAĞRISI İŞLEVİ:</u>**
/set_video_limit [Sohbet Sayısı] - Bir seferde Görüntülü Aramalar için izin verilen maksimum Sohbet Sayısını ayarlayın. Varsayılan olarak 3 sohbet.
/videomode [download|m3u8] - İndirme modu etkinleştirilirse Bot, videoları M3u8 biçiminde oynatmak yerine indirecektir. Varsayılan olarak M3u8'e. Herhangi bir sorgu m3u8 modunda oynatılmadığında indirme modunu kullanabilirsiniz..

⚡️**<u>ÖZEL BOT FONKSİYONU:</u>**
/authorize [CHAT_ID] - Botunuzu kullanmak için bir sohbete izin verin.
/unauthorize [CHAT_ID] - Bir sohbetin botunuzu kullanmasına izin vermeyin.
/authorized - Botunuzun izin verilen tüm sohbetlerini kontrol edin.

🌐**<u>YAYIN FONKSİYONU:</u>**
/reklam [Mesaj Gönder veya Mesaja Cevap Ver] - Bot'un Sunulan Sohbetlerine herhangi bir mesaj yayınlayın.

<u>yayın seçenekleri:</u>
**-pin** : Bu, mesajınızı sabitleyecektir 
**-pinloud** : Bu, mesajınızı yüksek sesli bildirimle sabitleyecektir
**-user** : Bu, mesajınızı botunuzu başlatan kullanıcılara yayınlayacaktır..
**-assistant** : Bu, mesajınızı botunuzun asistan hesabından yayınlayacaktır.
**-nobot** : Bu, botunuzu mesaj yayınlamamaya zorlar

**Örnek :** ` /reklam -user -assistant -pin Merhaba Test'

"""
