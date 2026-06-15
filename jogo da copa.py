import tkinter as tk
from tkinter import font as tkfont
import random

# Lista de perguntas: cada uma tem o texto, as opções e o índice da resposta correta
PERGUNTAS = [
    {
        "pergunta": "Qual seleção tem o maior número de títulos da Copa do Mundo?",
        "opcoes": ["Alemanha", "Argentina", "Brasil", "Itália"],
        "resposta": 2
    },
    {
        "pergunta": "Em que país foi disputada a Copa do Mundo de 2014?",
        "opcoes": ["Brasil", "Rússia", "Catar", "África do Sul"],
        "resposta": 0
    },
    {
        "pergunta": "Quem foi o artilheiro da Copa do Mundo de 2022?",
        "opcoes": ["Lionel Messi", "Kylian Mbappé", "Neymar", "Cristiano Ronaldo"],
        "resposta": 1
    },
    {
        "pergunta": "Qual jogador é conhecido como 'O Rei do Futebol' e venceu 3 Copas do Mundo?",
        "opcoes": ["Pelé", "Ronaldinho", "Romário", "Zico"],
        "resposta": 0
    },
    {
        "pergunta": "Em que ano o Uruguai sediou e venceu a primeira Copa do Mundo?",
        "opcoes": ["1928", "1930", "1934", "1950"],
        "resposta": 1
    },
    {
        "pergunta": "Qual país sediará a Copa do Mundo de 2026?",
        "opcoes": ["Catar", "Brasil", "EUA, México e Canadá", "Espanha e Portugal"],
        "resposta": 2
    },
    {
        "pergunta": "Quantas vezes a seleção brasileira foi campeã da Copa do Mundo?",
        "opcoes": ["3", "4", "5", "6"],
        "resposta": 2
    },
    {
        "pergunta": "Qual seleção venceu a Copa do Mundo de 2018?",
        "opcoes": ["Croácia", "Bélgica", "França", "Inglaterra"],
        "resposta": 2
    },
]

# Cores do tema
COR_FUNDO = "#0b3d2e"
COR_CARTAO = "#ffffff"
COR_TEXTO = "#0b3d2e"
COR_BOTAO = "#1e7d4f"
COR_BOTAO_HOVER = "#25a064"
COR_CERTO = "#2e7d32"
COR_ERRADO = "#c62828"
COR_DESTAQUE = "#ffd700"


class QuizCopaDoMundo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz da Copa do Mundo ⚽🏆")
        self.geometry("600x500")
        self.resizable(False, False)
        self.configure(bg=COR_FUNDO)

        # Fontes
        self.fonte_titulo = tkfont.Font(family="Helvetica", size=20, weight="bold")
        self.fonte_pergunta = tkfont.Font(family="Helvetica", size=14, weight="bold")
        self.fonte_opcao = tkfont.Font(family="Helvetica", size=12)
        self.fonte_status = tkfont.Font(family="Helvetica", size=11, weight="bold")

        # Estado do jogo
        self.perguntas = []
        self.indice_atual = 0
        self.pontos = 0
        self.botoes_opcoes = []

        self.criar_tela_inicial()

    # ---------- TELAS ----------
    def limpar_tela(self):
        for widget in self.winfo_children():
            widget.destroy()

    def criar_tela_inicial(self):
        self.limpar_tela()

        titulo = tk.Label(
            self, text="QUIZ DA COPA DO MUNDO",
            font=self.fonte_titulo, bg=COR_FUNDO, fg=COR_DESTAQUE
        )
        titulo.pack(pady=40)

        subtitulo = tk.Label(
            self,
            text="Teste seus conhecimentos sobre a história\nda Copa do Mundo de futebol! ⚽",
            font=self.fonte_opcao, bg=COR_FUNDO, fg="white", justify="center"
        )
        subtitulo.pack(pady=10)

        btn_iniciar = tk.Button(
            self, text="Começar Quiz", font=self.fonte_pergunta,
            bg=COR_BOTAO, fg="white", activebackground=COR_BOTAO_HOVER,
            relief="flat", padx=30, pady=10, cursor="hand2",
            command=self.iniciar_jogo
        )
        btn_iniciar.pack(pady=60)

        rodape = tk.Label(
            self, text=f"{len(PERGUNTAS)} perguntas • Boa sorte!",
            font=("Helvetica", 10), bg=COR_FUNDO, fg="#cccccc"
        )
        rodape.pack(side="bottom", pady=20)

    def iniciar_jogo(self):
        self.perguntas = PERGUNTAS.copy()
        random.shuffle(self.perguntas)
        self.indice_atual = 0
        self.pontos = 0
        self.mostrar_pergunta()

    def mostrar_pergunta(self):
        self.limpar_tela()

        item = self.perguntas[self.indice_atual]

        # Barra de progresso (texto)
        progresso = tk.Label(
            self,
            text=f"Pergunta {self.indice_atual + 1} de {len(self.perguntas)}   |   Pontos: {self.pontos}",
            font=self.fonte_status, bg=COR_FUNDO, fg=COR_DESTAQUE
        )
        progresso.pack(pady=(20, 10))

        # Cartão da pergunta
        cartao = tk.Frame(self, bg=COR_CARTAO, padx=20, pady=20)
        cartao.pack(padx=30, pady=10, fill="both", expand=True)

        pergunta_label = tk.Label(
            cartao, text=item["pergunta"], font=self.fonte_pergunta,
            bg=COR_CARTAO, fg=COR_TEXTO, wraplength=480, justify="left"
        )
        pergunta_label.pack(pady=(10, 20), anchor="w")

        self.botoes_opcoes = []
        for idx, opcao in enumerate(item["opcoes"]):
            btn = tk.Button(
                cartao, text=opcao, font=self.fonte_opcao,
                bg="#f0f0f0", fg=COR_TEXTO, activebackground="#dcdcdc",
                relief="flat", anchor="w", padx=15, pady=10, cursor="hand2",
                command=lambda i=idx: self.verificar_resposta(i)
            )
            btn.pack(fill="x", pady=5)
            self.botoes_opcoes.append(btn)

        # Label de feedback (inicialmente vazio)
        self.feedback_label = tk.Label(
            cartao, text="", font=self.fonte_status, bg=COR_CARTAO
        )
        self.feedback_label.pack(pady=(15, 0))

    def verificar_resposta(self, escolha_idx):
        item = self.perguntas[self.indice_atual]
        resposta_correta = item["resposta"]

        # Desabilita os botões para evitar múltiplos cliques
        for btn in self.botoes_opcoes:
            btn.config(state="disabled")

        if escolha_idx == resposta_correta:
            self.pontos += 1
            self.botoes_opcoes[escolha_idx].config(bg=COR_CERTO, fg="white")
            self.feedback_label.config(text="✅ Resposta correta!", fg=COR_CERTO)
        else:
            self.botoes_opcoes[escolha_idx].config(bg=COR_ERRADO, fg="white")
            self.botoes_opcoes[resposta_correta].config(bg=COR_CERTO, fg="white")
            correta_texto = item["opcoes"][resposta_correta]
            self.feedback_label.config(
                text=f"❌ Errado! A correta era: {correta_texto}", fg=COR_ERRADO
            )

        # Avança para próxima pergunta após uma pausa
        self.after(1400, self.proxima_pergunta)

    def proxima_pergunta(self):
        self.indice_atual += 1
        if self.indice_atual < len(self.perguntas):
            self.mostrar_pergunta()
        else:
            self.mostrar_resultado()

    def mostrar_resultado(self):
        self.limpar_tela()

        total = len(self.perguntas)
        porcentagem = (self.pontos / total) * 100

        if porcentagem == 100:
            mensagem = "🏆 Perfeito! Você é um verdadeiro craque da Copa do Mundo!"
        elif porcentagem >= 70:
            mensagem = "🥈 Muito bem! Você sabe bastante sobre a Copa do Mundo!"
        elif porcentagem >= 40:
            mensagem = "🥉 Não foi mal, mas dá para melhorar!"
        else:
            mensagem = "📚 Bora estudar mais sobre a história da Copa do Mundo!"

        titulo = tk.Label(
            self, text="FIM DO QUIZ!", font=self.fonte_titulo,
            bg=COR_FUNDO, fg=COR_DESTAQUE
        )
        titulo.pack(pady=(50, 20))

        pontuacao = tk.Label(
            self, text=f"Você acertou {self.pontos} de {total} perguntas",
            font=self.fonte_pergunta, bg=COR_FUNDO, fg="white"
        )
        pontuacao.pack(pady=10)

        comentario = tk.Label(
            self, text=mensagem, font=self.fonte_opcao,
            bg=COR_FUNDO, fg="white", wraplength=480, justify="center"
        )
        comentario.pack(pady=20)

        btn_reiniciar = tk.Button(
            self, text="Jogar de novo", font=self.fonte_pergunta,
            bg=COR_BOTAO, fg="white", activebackground=COR_BOTAO_HOVER,
            relief="flat", padx=30, pady=10, cursor="hand2",
            command=self.iniciar_jogo
        )
        btn_reiniciar.pack(pady=30)


if __name__ == "__main__":
    app = QuizCopaDoMundo()
    app.mainloop()