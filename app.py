import streamlit as st

st.set_page_config(
    page_title="Baş Etme Stilleri Ölçeği",
    layout="centered"
)

st.title("Baş Etme Stilleri Ölçeği")

st.markdown("""
Aşağıda, stresli veya zorlayıcı durumlarla karşılaştığınızda **genellikle nasıl davrandığınızı**
soran ifadeler yer almaktadır.  

Lütfen her maddeyi dikkatle okuyunuz ve sizi **en iyi yansıtan** seçeneği işaretleyiniz.

**Bu uygulamada verdiğiniz yanıtlar kaydedilmez ve tamamen anonimdir.**
""")

# Cevap seçenekleri
options = {
    "Bunu hiç yapmıyorum": 1,
    "Bunu çok az yapıyorum": 2,
    "Bunu orta düzeyde yapıyorum": 3,
    "Bunu çok sık yapıyorum": 4
}

# Sorular
questions = {
    1: "Sorunla karşılaştığımda moralim bozulur ve duygularımı dışarıya yansıtırım.",
    2: "Bu olay hakkında daha az düşünmek için sinemaya giderim ya da TV seyrederim.",
    3: "Olay hiç olmamış gibi davranırım.",
    4: "Bununla baş edemeyeceğimi kabul eder ve denemekten vazgeçerim.",
    5: "Olayın gerçekten olduğu fikrine kendimi alıştırırım.",
    6: "Allah’tan yardım isterim.",
    7: "Söz konusu sorunla ilgili şakalar yaparım.",
    8: "Şartlar uygun olana kadar bu konuda hiçbir şey yapmam.",
    9: "Ne hissettiğimi birilerine anlatırım.",
    10: "Amacıma ulaşmaya çalışmaktansa hemen vazgeçerim.",
    11: "Soruna odaklanabilmek için diğer etkinliklerimi bir tarafa bırakırım.",
    12: "Alkol ya da sakinleştirici alarak bir süre kendimi kaybedip olanları unutmaya çalışırım.",
    13: "Duygularımı dışarı vururum.",
    14: "Daha olumlu taraflarını görebilmek için sorunu başka bir açıdan ele almaya çalışırım.",
    15: "Sorunla ilgili somut bir şeyler yapabilen kişilerle konuşurum.",
    16: "Ne yapmam gerektiği konusunda bir strateji geliştirmeye çalışırım.",
    17: "Sorunu çözmeye odaklanırım ve gerekirse diğer işleri bir süreliğine bırakırım.",
    18: "Başkasının sempatisini ve anlayışını kazanmaya çalışırım.",
    19: "Sorunla daha az meşgul olmak için alkol ya da ilaç almaya çalışırım.",
    20: "Sorunla ilgili şaka yaparım.",
    21: "Olayların iyi yanını görmeye çalışırım.",
    22: "Sorunun en iyi nasıl ele alınabileceğini düşünürüm.",
    23: "Sorun gerçekte olmamış gibi davranırım.",
    24: "Sorun olan şeyleri aklımdan atmak için başka etkinliklere yönelirim.",
    25: "Böyle bir şeyin olduğu gerçeğini kabul ederim.",
    26: "Benzer durumlarla karşılaşan kişilere ne yaptıklarını sorarım.",
    27: "İnancımda huzur bulmaya çalışırım.",
    28: "Bir şeyler yapmak için doğru zamanı beklerim."
}

responses = {}

# Soruları göster
for i in range(1, 29):
    st.markdown(f"### {i}. {questions[i]}")
    responses[i] = st.radio(
        label="",
        options=options.keys(),
        index=None,
        key=f"q{i}"
    )

# Baş etme stilleri – sabit sıra
coping_styles = [
    ("UYUMLU (GENELDE İŞLEVSEL)", [
        ("Aktif Baş Etme", [2, 11],
         "Stres yaratan durumu doğrudan değiştirmeye yönelik davranışsal çaba."),
        ("Planlama", [16, 22],
         "Sorunu çözmeden önce düşünme, strateji kurma ve adımlara ayırma."),
        ("Araçsal Destek Arama", [15, 26],
         "Bilgi, öneri veya somut yardım talep etme."),
        ("Duygusal Destek Arama", [9, 18],
         "Anlaşılmak ve duygusal rahatlama amacıyla başkalarına yönelme."),
        ("Kabullenme", [5, 25],
         "Değiştirilemeyen durumu olduğu gibi kabul etme."),
        ("Olumlu Yeniden Yorumlama", [14, 21],
         "Yaşantıya daha anlamlı veya geliştirici bir çerçeve kazandırma."),
        ("Dinî / Manevi Baş Etme", [6, 27],
         "İnanç, dua veya teslimiyet yoluyla baş etme."),
        ("Mizah", [7, 20],
         "Duruma mesafe koyarak perspektif değiştirme.")
    ]),
    ("KISA VADEDE RAHATLATICI", [
        ("Kendini Oyalama / Dikkat Dağıtma", [2, 17],
         "Sorundan geçici olarak uzaklaşma; kısa süreli rahatlama sağlayabilir."),
        ("Duyguları Boşaltma", [1, 13],
         "Öfke ve hayal kırıklığını yoğun biçimde dışa vurma.")
    ]),
    ("GENELDE UYUMSUZ", [
        ("İnkâr", [3, 23],
         "Sorunun varlığını veya ciddiyetini reddetme."),
        ("Davranışsal Kaçınma / Vazgeçme", [4, 10],
         "Sorunla baş etme çabasını bırakma."),
        ("Madde Kullanımı", [12, 19],
         "Duyguları alkol veya maddelerle bastırma."),
        ("Kendini Suçlama", [24, 28],
         "Yaşanan durumdan kendini aşırı sorumlu tutma.")
    ])
]

def usage_label(score):
    if score <= 3:
        return "Daha az kullanılıyor"
    elif score <= 5:
        return "Zaman zaman"
    else:
        return "Sık kullanılıyor"

# Sonuç butonu
if st.button("Sonuçları Göster"):
    if None in responses.values():
        st.warning("Lütfen tüm soruları yanıtlayınız.")
        st.stop()

    st.markdown("---")
    st.markdown(
        "**Bu puanlar doğru–yanlış ya da iyi–kötü anlamına gelmez; "
        "sadece hangi baş etme stratejilerinin sizde daha baskın olduğunu gösterir.**"
    )

    for category, styles in coping_styles:
        st.subheader(category)
        for name, items, desc in styles:
            score = sum(options[responses[i]] for i in items)
            st.markdown(
                f"**{name}** — {score}/8  \n"
                f"_{usage_label(score)}_  \n"
                f"{desc}"
            )
