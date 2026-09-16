# Profil görselleri

Özel SVG çizimleri; JavaScript, harici görsel API veya zamanlanmış iş kullanmaz.
Açık/koyu tema sürümleri README içindeki `picture` öğesiyle seçilir.
Hareket azaltma tercihi SVG içinde desteklenir. Arayüz çizimleri ürün ekran görüntüsü değildir.

Tipografi: Piklo sitesindeki Geist. Glifler SVG path biçimine dönüştürülür;
ziyaretçinin font indirmesi gerekmez. Lisans: `assets/OFL-Geist.txt`.

Yeniden üretmek için Python 3 ve `fonttools` gerekir. [Geist fontunu](https://github.com/google/fonts/tree/main/ofl/geist) indirip çalıştır:

```sh
python3 design/generate-art.py --font /font/dizini/Geist.ttf --personal
```
