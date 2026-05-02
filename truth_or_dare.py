import tkinter as tk
from tkinter import messagebox
import random

# ─────────────────────────────────────────────
#  SORU HAVUZU
# ─────────────────────────────────────────────
TRUTH_BASE = [
    "Hiç birine yalan söyledin mi? Ne hakkındaydı?",
    "Hayatında en çok neyi pişman oldun?",
    "En son ne zaman ağladın ve neden?",
    "Şu an kimden özür dilemek istersin?",
    "Hayatında çaldın mı? Anlat.",
    "En büyük korkun ne?",
    "Şu an kimi seviyorsun?",
    "Hiç çok utanç verici bir anın oldu mu?",
    "En çok kime kıskanıyorsun?",
    "Sırrını en çok kime söyledin?",
    "Hiç arkadaşına ihanet ettin mi?",
    "Şu ana kadar yaptığın en aptalca şey neydi?",
    "En sevdiğin ve en nefret ettiğin özelliğin nedir?",
    "Bugüne kadar en büyük yalanın neydi?",
    "Biri hakkında kötü bir şey düşünüp yüzüne söylemedin mi?",
    "Hayalindeki insan nasıl biri?",
    "Bugüne kadar en pahalı aldığın şey neydi ve pişman mısın?",
    "En son kime mesaj attın ve ne yazdın?",
    "Kaç para biriktirdin hiç söyler misin?",
    "Şu an en çok ne hakkında endişelisin?",
    "Sosyal medyada sildiğin bir gönderi var mı? Neydi?",
    "Hayatında en büyük hayal kırıklığını yaşatan kim?",
    "Şu an buradakilerden birini gizlice sevdiniz mi?",
    "En kötü özelliğin ne sence?",
    "Hiç yasadışı bir şey yaptın mı?",
    "Çocukluktan bu yana değişmeyen bir alışkanlığın var mı?",
    "Şu ana kadar en çok para harcadığın şey ne?",
    "Sana en çok kim moral veriyor?",
    "Hiç birine sahte bir hayat anlattın mı?",
    "Şu an telefonda ne var ki kimseye göstermek istemezsin?",
    "Beklediğin ve gerçekleşmeyen en büyük şey neydi?",
    "Şu anda mutlu musun, dürüst cevapla.",
    "Kendini en çok hangi konuda başarısız hissediyorsun?",
    "Birinin sırrını paylaştın mı hiç?",
    "En son ne zaman yalan söyledin?",
    "Şu an kim seni en çok strese sokuyor?",
    "Gençliğinde yaptığın en utanç verici şey neydi?",
    "Sevdiğin biri seni hayal kırıklığına uğrattı mı hiç?",
    "Ailenizden ne saklıyorsunuz?",
    "En büyük kompleksin ne?",
    "Hiç sahte bir hastalık numarası yaptın mı?",
    "Şu an kimin yerine olmak isterdin?",
    "Bugüne kadar aldığın en zor karar neydi?",
    "En son ne için dua ettin?",
    "Seni en çok kim anlıyor?",
    "Şu an ne yapmak istiyor olurdun?",
    "Hayatını değiştiren bir an var mıydı?",
    "En son ne zaman bir arkadaşını hayal kırıklığına uğrattın?",
    "Kendine verdiğin en büyük söz neydi?",
    "Şu an en büyük özlemin ne?",
]

DARE_BASE = [
    "Şu an yanındaki kişiyi gıdıkla.",
    "En komik yüzünü yap ve 30 sn öyle kal.",
    "Bir komşunun kapısını çal ve 'merhaba' de.",
    "Odada kör adam cambazı oyna.",
    "Bir dans hareketi icat et ve herkese öğret.",
    "Telefon rehberinden rastgele birini ara ve şarkı söyle.",
    "10 şınav yap.",
    "Ağzında patates cipsi varken konuş.",
    "Herkesin önünde şarkı söyle.",
    "Bir dakika boyunca robot gibi konuş.",
    "Sağ elinle sol kulağına dokun.",
    "Evde bulduğun ilk nesneyi başına tak ve 1 dk öyle kal.",
    "En iyi taklid ettiğin kişiyi taklit et.",
    "Kendini bir ürün gibi tanıt, satmaya çalış.",
    "Merdivenden aşağı inin yukarı çıkın 3 kez.",
    "Bir dakika boyunca sürekli gül.",
    "Söylediğin son cümleyi tersten söyle.",
    "Yüzünü buruşturup 30 saniye öyle kal.",
    "Herkesin önünde 30 saniye dans et.",
    "Bir sahne oyunu gibi 'hayır!' diye bağır.",
    "Bir hayvana benzediğini düşündüğün kişiye hayvan sesini çıkar.",
    "Gözlerin kapalı su iç.",
    "Tüm sesleri taklit ederek bir şarkıyı anlat.",
    "Annen gibi konuş 1 dakika.",
    "Bir şeyi yanlış elle yap (yaz, iç, vb.).",
    "Herkese tek tek el sık ve 'merhaba patron' de.",
    "Alnına kaşık yapıştırmaya çalış.",
    "Kendinle röportaj yap.",
    "Bir dakika boyunca çok yavaş konuş.",
    "Komşularını uyandırmadan bağır.",
    "Bir film karakterini oyna, kimsenin anlamaması gerek.",
    "Telefonundan rastgele bir şarkı çal ve dans et.",
    "En iyi aktörlük yeteneğini sergilererek ağla.",
    "Ellerini kullanmadan bir şey ye.",
    "Odadaki en tuhaf nesneyi bul ve kullan.",
    "Şarkı söylerken yürü, hem de hızlı.",
    "Ters otur bir dakika.",
    "Bir şeyi ters çevir ve öyle kullan.",
    "Kendinle selfie çek ve 5 yıl sonraki halini anlat.",
    "Herkesin gözünün içine bakarak 30 sn dur.",
    "Yüzüne komik bir ifade takıp fotoğraf çektir.",
    "Odanın etrafında tavuk gibi yürü.",
    "Bir nesneyi söz kullanmadan anlat.",
    "Bir şarkının sadece nakaratını 3 kez tekrarla.",
    "Herkesin önünde egzersiz yap.",
    "Gözlerin kapalı bir şey çiz.",
    "Sahte bir haber yazar gibi canlı yayın aç.",
    "En sevdiğin yemeği anlatırken dans et.",
    "Bir dakika boyunca kelime üretemezsin.",
    "Arkadaşlarından birine sahte itirafta bulun.",
]


def generate_questions():
    """Her oyun için soruları karıştır ve yeni seç."""
    truth = TRUTH_BASE.copy()
    dare = DARE_BASE.copy()
    random.shuffle(truth)
    random.shuffle(dare)
    return truth[:50], dare[:50]


# ─────────────────────────────────────────────
#  UYGULAMA
# ─────────────────────────────────────────────
class TruthOrDareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Doğruluk mu Cesaret mi?")
        self.root.geometry("700x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#0d0d1a")

        self.players = []
        self.truth_q, self.dare_q = generate_questions()
        self.truth_idx = 0
        self.dare_idx = 0
        self.current_q_type = None  # 'truth' or 'dare'

        self._setup_fonts()
        self._show_setup_screen()

    # ── Fontlar ─────────────────────────────
    def _setup_fonts(self):
        import tkinter.font as tkfont
        self.font_title  = tkfont.Font(family="Georgia", size=26, weight="bold")
        self.font_sub    = tkfont.Font(family="Georgia", size=14)
        self.font_body   = tkfont.Font(family="Georgia", size=16)
        self.font_btn    = tkfont.Font(family="Georgia", size=13, weight="bold")
        self.font_small  = tkfont.Font(family="Georgia", size=11)

    # ── Ekranı temizle ───────────────────────
    def _clear(self):
        for w in self.root.winfo_children():
            w.destroy()

    # ── Buton fabrikası ──────────────────────
    def _btn(self, parent, text, cmd, bg="#c0392b", fg="white", width=22):
        return tk.Button(
            parent, text=text, command=cmd,
            bg=bg, fg=fg, font=self.font_btn,
            relief="flat", cursor="hand2",
            width=width, pady=10,
            activebackground="#e74c3c", activeforeground="white",
            bd=0
        )

    # ══════════════════════════════════════════
    #  EKRAN 1 — Oyuncu Kurulum
    # ══════════════════════════════════════════
    def _show_setup_screen(self):
        self._clear()
        self.players = []
        self.truth_q, self.dare_q = generate_questions()
        self.truth_idx = 0
        self.dare_idx = 0

        # Arkaplan gradient efekti (canvas)
        canvas = tk.Canvas(self.root, width=700, height=600, bd=0, highlightthickness=0)
        canvas.place(x=0, y=0)
        for i in range(60):
            shade = int(13 + i * 1.2)
            color = f"#{shade:02x}{shade:02x}{min(shade+30,80):02x}"
            canvas.create_rectangle(0, i*10, 700, (i+1)*10, fill=color, outline="")

        # Başlık
        tk.Label(self.root, text="🎲 Doğruluk mu Cesaret mi?",
                 font=self.font_title, bg="#0d0d1a", fg="#e74c3c").place(relx=0.5, y=40, anchor="center")
        tk.Label(self.root, text="Oyunculeri ekle, oyunu başlat!",
                 font=self.font_small, bg="#0d0d1a", fg="#888").place(relx=0.5, y=80, anchor="center")

        # İsim giriş alanı
        frame = tk.Frame(self.root, bg="#0d0d1a")
        frame.place(relx=0.5, y=130, anchor="center")

        tk.Label(frame, text="Oyuncu İsmi:", font=self.font_sub,
                 bg="#0d0d1a", fg="#ccc").grid(row=0, column=0, padx=5)
        self.name_entry = tk.Entry(frame, font=self.font_sub, width=18,
                                   bg="#1a1a2e", fg="white", insertbackground="white",
                                   relief="flat", bd=5)
        self.name_entry.grid(row=0, column=1, padx=5)
        self.name_entry.bind("<Return>", lambda e: self._add_player())

        self._btn(frame, "➕ Ekle", self._add_player, bg="#2980b9", width=10).grid(row=0, column=2, padx=5)

        # Oyuncu listesi
        list_frame = tk.Frame(self.root, bg="#0d0d1a")
        list_frame.place(relx=0.5, y=300, anchor="center")

        tk.Label(list_frame, text="Oyuncular:", font=self.font_sub,
                 bg="#0d0d1a", fg="#aaa").pack()

        self.player_listbox = tk.Listbox(
            list_frame, font=self.font_body, width=28, height=8,
            bg="#1a1a2e", fg="#f0e6d3", selectbackground="#c0392b",
            relief="flat", bd=0, highlightthickness=0
        )
        self.player_listbox.pack(pady=5)

        # Alt butonlar
        btn_frame = tk.Frame(self.root, bg="#0d0d1a")
        btn_frame.place(relx=0.5, y=530, anchor="center")

        self._btn(btn_frame, "🗑️ Seçiliyi Sil", self._remove_player, bg="#7f8c8d", width=14).grid(row=0, column=0, padx=6)
        self._btn(btn_frame, "🎮 Oyunu Başlat", self._start_game, bg="#27ae60", width=14).grid(row=0, column=1, padx=6)

    def _add_player(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Uyarı", "Lütfen bir isim girin!")
            return
        if name in self.players:
            messagebox.showwarning("Uyarı", "Bu isim zaten ekli!")
            return
        self.players.append(name)
        self.player_listbox.insert(tk.END, f"  👤  {name}")
        self.name_entry.delete(0, tk.END)
        self.name_entry.focus()

    def _remove_player(self):
        sel = self.player_listbox.curselection()
        if not sel:
            return
        idx = sel[0]
        self.player_listbox.delete(idx)
        self.players.pop(idx)

    def _start_game(self):
        if len(self.players) < 2:
            messagebox.showwarning("Uyarı", "En az 2 oyuncu gerekli!")
            return
        self._show_game_screen()

    # ══════════════════════════════════════════
    #  EKRAN 2 — Oyun Ekranı
    # ══════════════════════════════════════════
    def _show_game_screen(self):
        self._clear()
        self._pick_players()
        self._build_game_ui()

    def _pick_players(self):
        picked = random.sample(self.players, 2)
        self.asker  = picked[0]
        self.answerer = picked[1]

    def _build_game_ui(self):
        # Arkaplan
        canvas = tk.Canvas(self.root, width=700, height=600, bd=0, highlightthickness=0)
        canvas.place(x=0, y=0)
        for i in range(60):
            shade = int(13 + i * 1.2)
            color = f"#{shade:02x}{shade:02x}{min(shade+30,80):02x}"
            canvas.create_rectangle(0, i*10, 700, (i+1)*10, fill=color, outline="")

        # Başlık
        tk.Label(self.root, text="🎲 Doğruluk mu Cesaret mi?",
                 font=self.font_title, bg="#0d0d1a", fg="#e74c3c").place(relx=0.5, y=35, anchor="center")

        # Oyuncular
        player_frame = tk.Frame(self.root, bg="#1a1a2e", bd=0, relief="flat")
        player_frame.place(relx=0.5, y=100, anchor="center", width=620, height=70)

        tk.Label(player_frame, text=f"❓ Soran: ", font=self.font_sub,
                 bg="#1a1a2e", fg="#aaa").place(x=20, y=10)
        self.asker_lbl = tk.Label(player_frame, text=self.asker, font=self.font_sub,
                                   bg="#1a1a2e", fg="#f39c12")
        self.asker_lbl.place(x=105, y=10)

        tk.Label(player_frame, text=f"💬 Cevaplayan: ", font=self.font_sub,
                 bg="#1a1a2e", fg="#aaa").place(x=20, y=38)
        self.answerer_lbl = tk.Label(player_frame, text=self.answerer, font=self.font_sub,
                                      bg="#1a1a2e", fg="#2ecc71")
        self.answerer_lbl.place(x=160, y=38)

        # Soru kartı
        self.q_frame = tk.Frame(self.root, bg="#1a1a2e", relief="flat")
        self.q_frame.place(relx=0.5, y=280, anchor="center", width=620, height=150)

        self.q_type_lbl = tk.Label(self.q_frame, text="", font=self.font_title,
                                    bg="#1a1a2e", fg="#e74c3c")
        self.q_type_lbl.place(relx=0.5, y=18, anchor="center")

        self.q_text = tk.Label(self.q_frame, text="↓ Aşağıdan seçim yap",
                                font=self.font_body, bg="#1a1a2e", fg="#ddd",
                                wraplength=560, justify="center")
        self.q_text.place(relx=0.5, y=90, anchor="center")

        # Seçim butonları
        choice_frame = tk.Frame(self.root, bg="#0d0d1a")
        choice_frame.place(relx=0.5, y=400, anchor="center")

        self._btn(choice_frame, "🔍 DOĞRULUK", self._show_truth, bg="#2471a3", width=16).grid(row=0, column=0, padx=10)
        self._btn(choice_frame, "⚡ CESARET",  self._show_dare,  bg="#c0392b", width=16).grid(row=0, column=1, padx=10)

        # Değiştir & Yeni Tur butonları
        action_frame = tk.Frame(self.root, bg="#0d0d1a")
        action_frame.place(relx=0.5, y=465, anchor="center")

        self._btn(action_frame, "🔄 Soruyu Değiştir", self._change_q, bg="#8e44ad", width=16).grid(row=0, column=0, padx=10)
        self._btn(action_frame, "🎲 Yeni Tur", self._new_round, bg="#27ae60", width=16).grid(row=0, column=1, padx=10)

        # Yeni Oyun / Çıkış
        bottom_frame = tk.Frame(self.root, bg="#0d0d1a")
        bottom_frame.place(relx=0.5, y=535, anchor="center")

        self._btn(bottom_frame, "🏠 Ana Menü", self._show_setup_screen, bg="#555", width=14).grid(row=0, column=0, padx=8)
        self._btn(bottom_frame, "❌ Çıkış", self.root.quit, bg="#333", width=14).grid(row=0, column=1, padx=8)

    # ── Soru göster ─────────────────────────
    def _show_truth(self):
        self.current_q_type = "truth"
        if self.truth_idx >= len(self.truth_q):
            random.shuffle(self.truth_q)
            self.truth_idx = 0
        q = self.truth_q[self.truth_idx]
        self.truth_idx += 1
        self.q_type_lbl.config(text="🔍 DOĞRULUK", fg="#2471a3")
        self.q_text.config(text=q)

    def _show_dare(self):
        self.current_q_type = "dare"
        if self.dare_idx >= len(self.dare_q):
            random.shuffle(self.dare_q)
            self.dare_idx = 0
        q = self.dare_q[self.dare_idx]
        self.dare_idx += 1
        self.q_type_lbl.config(text="⚡ CESARET", fg="#c0392b")
        self.q_text.config(text=q)

    def _change_q(self):
        if self.current_q_type == "truth":
            self._show_truth()
        elif self.current_q_type == "dare":
            self._show_dare()
        else:
            messagebox.showinfo("Bilgi", "Önce Doğruluk veya Cesaret seç!")

    def _new_round(self):
        self._pick_players()
        self.asker_lbl.config(text=self.asker)
        self.answerer_lbl.config(text=self.answerer)
        self.q_type_lbl.config(text="")
        self.q_text.config(text="↓ Aşağıdan seçim yap")
        self.current_q_type = None


# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = TruthOrDareApp(root)
    root.mainloop()
