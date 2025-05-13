# UserTaggerBot 🤖

Telegram grup yöneticileri için özel olarak geliştirilmiş bir kullanıcı etiketleme botu. `usertaggerbot`, belirli komutlar aracılığıyla grup üyelerini topluca etiketlemeye olanak tanır. Sadece yöneticiler tarafından kullanılabilir ve dinamik olarak yönetici listesini güncelleyebilir.

## 🚀 Özellikler
- `/utag mesaj` → Kullanıcıları klasik mention yöntemiyle etiketler.
- `/atag mesaj` → Kullanıcıları sadece isimleriyle etiketler.
- `/btag mesaj` → Kullanıcıları 🚩 bayrak emojisiyle etiketler.
- `/etag mesaj` → Kullanıcıları 🌟 emoji ile etiketler.
- `/reload` → Grup yöneticilerini yeniden tarar ve kayıt eder.

## ⚙️ Kurulum

1. Gerekli bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
