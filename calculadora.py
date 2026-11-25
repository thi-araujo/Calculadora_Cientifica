"""Calculadora Científica com interface gráfica.

    python calculadora.py

Abas: Calculadora (teclado científico e histórico), Fórmulas (círculo,
equação do 2º grau, Pitágoras, áreas, função afim, velocidade média...) e
Conversor de unidades.
"""

from __future__ import annotations

import platform
import tkinter as tk
from tkinter import ttk

import conversor as cv
import formulas as fm
from expressao import ErroExpressao, avaliar, formatar

CORES = {
    "fundo": "#0f172a",
    "painel": "#1e293b",
    "borda": "#334155",
    "tecla": "#273449",
    "texto": "#e2e8f0",
    "texto_suave": "#94a3b8",
    "destaque": "#38bdf8",
    "verde": "#22c55e",
    "vermelho": "#ef4444",
    "ambar": "#f59e0b",
}

WINDOWS = platform.system() == "Windows"
FONTE = "Segoe UI" if WINDOWS else "Helvetica"
FONTE_MONO = "Consolas" if WINDOWS else "DejaVu Sans Mono"

# (rótulo, texto inserido ou ação, estilo)
TECLADO = [
    [("sen", "sen(", "f"), ("cos", "cos(", "f"), ("tan", "tan(", "f"), ("√", "√(", "f"), ("xʸ", "^", "f")],
    [("sen⁻¹", "asen(", "f"), ("cos⁻¹", "acos(", "f"), ("tan⁻¹", "atan(", "f"), ("log", "log(", "f"),
     ("ln", "ln(", "f")],
    [("(", "(", "f"), (")", ")", "f"), ("n!", "!", "f"), ("%", "%", "f"), ("π", "π", "f")],
    [("7", "7", "n"), ("8", "8", "n"), ("9", "9", "n"), ("÷", "÷", "o"), ("C", "#limpar", "c")],
    [("4", "4", "n"), ("5", "5", "n"), ("6", "6", "n"), ("×", "×", "o"), ("⌫", "#apagar", "c")],
    [("1", "1", "n"), ("2", "2", "n"), ("3", "3", "n"), ("−", "−", "o"), ("Ans", "#ans", "f")],
    [("0", "0", "n"), (",", ",", "n"), ("e", "e", "f"), ("+", "+", "o"), ("=", "#igual", "=")],
]
ESTILO_TECLA = {"n": (CORES["tecla"], CORES["texto"]), "f": (CORES["painel"], CORES["destaque"]),
                "o": (CORES["borda"], CORES["ambar"]), "c": (CORES["borda"], CORES["vermelho"]),
                "=": (CORES["destaque"], CORES["fundo"])}


def maiuscula(texto: str) -> str:
    return texto[:1].upper() + texto[1:]


def configurar_estilo(raiz: tk.Tk) -> None:
    estilo = ttk.Style(raiz)
    estilo.theme_use("clam")
    sem_borda = dict(bordercolor=CORES["painel"], lightcolor=CORES["painel"], darkcolor=CORES["painel"])
    fundo_sem_borda = dict(bordercolor=CORES["fundo"], lightcolor=CORES["fundo"], darkcolor=CORES["fundo"])
    estilo.configure(".", background=CORES["fundo"], foreground=CORES["texto"], font=(FONTE, 10))
    estilo.configure("Painel.TFrame", background=CORES["painel"])
    estilo.configure("Painel.TLabel", background=CORES["painel"])
    estilo.configure("PainelSuave.TLabel", background=CORES["painel"], foreground=CORES["texto_suave"])
    estilo.configure("Suave.TLabel", foreground=CORES["texto_suave"])
    estilo.configure("TNotebook", background=CORES["fundo"], borderwidth=0, tabmargins=(16, 8, 16, 0),
                     **fundo_sem_borda)
    estilo.configure("TNotebook.Tab", background=CORES["painel"], foreground=CORES["texto_suave"],
                     padding=(16, 7), borderwidth=0, font=(FONTE, 10, "bold"), **fundo_sem_borda)
    estilo.map("TNotebook.Tab", background=[("selected", CORES["borda"])],
               foreground=[("selected", CORES["destaque"])], expand=[("selected", (0, 0, 0, 0))])
    estilo.configure("TButton", background=CORES["borda"], foreground=CORES["texto"], borderwidth=0,
                     padding=(12, 6), font=(FONTE, 10, "bold"))
    estilo.map("TButton", background=[("active", "#475569")])
    estilo.configure("Destaque.TButton", background=CORES["destaque"], foreground=CORES["fundo"])
    estilo.map("Destaque.TButton", background=[("active", "#0ea5e9")])
    estilo.configure("TRadiobutton", background=CORES["fundo"], foreground=CORES["texto"],
                     indicatorbackground=CORES["fundo"], indicatorforeground=CORES["destaque"],
                     upperbordercolor=CORES["borda"], lowerbordercolor=CORES["borda"])
    estilo.map("TRadiobutton", background=[("active", CORES["fundo"])],
               indicatorforeground=[("selected", CORES["destaque"]), ("!selected", CORES["fundo"])])
    campo = dict(fieldbackground=CORES["fundo"], foreground=CORES["texto"], insertcolor=CORES["texto"],
                 bordercolor=CORES["borda"], lightcolor=CORES["fundo"], darkcolor=CORES["fundo"])
    estilo.configure("TEntry", **campo)
    estilo.configure("TCombobox", arrowcolor=CORES["texto"], background=CORES["borda"], **campo)
    estilo.map("TCombobox", fieldbackground=[("readonly", CORES["fundo"])],
               foreground=[("readonly", CORES["texto"])], selectbackground=[("readonly", CORES["fundo"])],
               selectforeground=[("readonly", CORES["texto"])])
    raiz.option_add("*TCombobox*Listbox.background", CORES["painel"])
    raiz.option_add("*TCombobox*Listbox.foreground", CORES["texto"])
    raiz.option_add("*TCombobox*Listbox.selectBackground", CORES["borda"])
    estilo.configure("Treeview", background=CORES["painel"], fieldbackground=CORES["painel"],
                     foreground=CORES["texto"], borderwidth=0, rowheight=26, **sem_borda)
    estilo.configure("Treeview.Heading", background=CORES["borda"], foreground=CORES["texto_suave"],
                     borderwidth=0, font=(FONTE, 9, "bold"))
    estilo.map("Treeview.Heading", background=[("active", CORES["borda"])])
    estilo.map("Treeview", background=[("selected", CORES["borda"])],
               foreground=[("selected", CORES["destaque"])])


class Aplicativo(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Calculadora Científica")
        self.geometry("860x640")
        self.minsize(820, 600)
        self.configure(bg=CORES["fundo"])
        configurar_estilo(self)
        self.ultimo_resultado: float | None = None
        self.acabou_de_calcular = False  # depois do "=", digitar um número começa uma conta nova

        self.abas = ttk.Notebook(self)
        self.abas.pack(fill="both", expand=True, pady=(4, 12))
        for titulo, montar in (("Calculadora", self._aba_calculadora), ("Fórmulas", self._aba_formulas),
                               ("Conversor", self._aba_conversor)):
            aba = ttk.Frame(self.abas, padding=16)
            montar(aba)
            self.abas.add(aba, text=titulo)

    # ------------------------------------------------------------------ Calculadora

    def _aba_calculadora(self, aba: ttk.Frame) -> None:
        esquerda = ttk.Frame(aba)
        esquerda.pack(side="left", fill="both", expand=True)

        visor = tk.Frame(esquerda, bg=CORES["painel"], padx=14, pady=10)
        visor.pack(fill="x")
        self.var_expressao = tk.StringVar()
        self.var_expressao.trace_add("write", lambda *_: self._previa())
        self.entrada = tk.Entry(visor, textvariable=self.var_expressao, font=(FONTE_MONO, 22), justify="right",
                                bg=CORES["painel"], fg=CORES["texto"], insertbackground=CORES["texto"],
                                relief="flat", highlightthickness=0)
        self.entrada.pack(fill="x")
        self.lbl_resultado = tk.Label(visor, text=" ", font=(FONTE_MONO, 14), anchor="e", bg=CORES["painel"],
                                      fg=CORES["texto_suave"])
        self.lbl_resultado.pack(fill="x")
        self.entrada.bind("<Return>", lambda _e: self._igual())
        self.entrada.bind("<KP_Enter>", lambda _e: self._igual())
        self.entrada.bind("<Escape>", lambda _e: self.var_expressao.set(""))
        self.entrada.bind("<Key>", self._tecla_fisica)
        self.entrada.focus_set()

        modo = ttk.Frame(esquerda)
        modo.pack(fill="x", pady=(8, 6))
        self.var_graus = tk.BooleanVar(value=True)
        ttk.Radiobutton(modo, text="Graus", variable=self.var_graus, value=True,
                        command=self._previa).pack(side="left")
        ttk.Radiobutton(modo, text="Radianos", variable=self.var_graus, value=False,
                        command=self._previa).pack(side="left", padx=12)
        ttk.Label(modo, text="Digite pelo teclado também. Enter calcula, Esc limpa.",
                  style="Suave.TLabel", font=(FONTE, 9)).pack(side="right")

        teclado = tk.Frame(esquerda, bg=CORES["fundo"])
        teclado.pack(fill="both", expand=True)
        for i, linha in enumerate(TECLADO):
            teclado.rowconfigure(i, weight=1, uniform="linha")
            for j, (rotulo, acao, tipo) in enumerate(linha):
                teclado.columnconfigure(j, weight=1, uniform="coluna")
                fundo, cor = ESTILO_TECLA[tipo]
                botao = tk.Button(teclado, text=rotulo, bg=fundo, fg=cor, activebackground=CORES["borda"],
                                  activeforeground=cor, relief="flat", bd=0, highlightthickness=0,
                                  font=(FONTE, 14 if tipo in "no=" else 11, "bold"), cursor="hand2",
                                  command=lambda a=acao: self._tecla(a))
                botao.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)

        direita = tk.Frame(aba, bg=CORES["painel"], padx=12, pady=10, width=250)
        direita.pack(side="left", fill="y", padx=(14, 0))
        direita.pack_propagate(False)
        cabeca = tk.Frame(direita, bg=CORES["painel"])
        cabeca.pack(fill="x")
        tk.Label(cabeca, text="Histórico", font=(FONTE, 11, "bold"), bg=CORES["painel"],
                 fg=CORES["destaque"]).pack(side="left")
        tk.Button(cabeca, text="Limpar", bg=CORES["painel"], fg=CORES["texto_suave"], relief="flat", bd=0,
                  activebackground=CORES["painel"], highlightthickness=0, cursor="hand2",
                  command=lambda: self.historico.delete(0, "end")).pack(side="right")
        self.historico = tk.Listbox(direita, bg=CORES["painel"], fg=CORES["texto"], relief="flat",
                                    highlightthickness=0, font=(FONTE_MONO, 10), selectbackground=CORES["borda"],
                                    activestyle="none")
        self.historico.pack(fill="both", expand=True, pady=(8, 0))
        self.historico.bind("<Double-1>", self._usar_historico)
        tk.Label(direita, text="Duplo clique reutiliza o resultado", font=(FONTE, 8), bg=CORES["painel"],
                 fg=CORES["texto_suave"]).pack(anchor="w")

    def _tecla(self, acao: str) -> None:
        if acao == "#limpar":
            self.var_expressao.set("")
        elif acao == "#apagar":
            posicao = self.entrada.index("insert")
            if posicao > 0:
                self.entrada.delete(posicao - 1)
        elif acao == "#igual":
            self._igual()
        elif acao == "#ans":
            if self.ultimo_resultado is not None:
                self.entrada.insert("insert", formatar(self.ultimo_resultado))
        else:
            if self.acabou_de_calcular and acao not in ("+", "−", "×", "÷", "^", "!", "%"):
                self.var_expressao.set("")
            self.entrada.insert("insert", acao)
        if acao != "#igual":
            self.acabou_de_calcular = False
        self.entrada.focus_set()

    def _tecla_fisica(self, evento) -> None:
        if evento.keysym in ("Return", "KP_Enter", "Escape"):
            return
        if self.acabou_de_calcular and evento.char and evento.char not in "+-*/^!%":
            self.var_expressao.set("")
        if evento.char or evento.keysym in ("BackSpace", "Delete"):
            self.acabou_de_calcular = False

    def _previa(self) -> None:
        texto = self.var_expressao.get()
        if not texto.strip():
            self.lbl_resultado.configure(text=" ", fg=CORES["texto_suave"])
            return
        try:
            self.lbl_resultado.configure(text=f"= {formatar(avaliar(texto, self.var_graus.get()))}",
                                         fg=CORES["texto_suave"])
        except ErroExpressao:
            self.lbl_resultado.configure(text=" ")

    def _igual(self) -> None:
        texto = self.var_expressao.get()
        if not texto.strip():
            return
        try:
            resultado = avaliar(texto, self.var_graus.get())
        except ErroExpressao as erro:
            self.lbl_resultado.configure(text=maiuscula(str(erro)), fg=CORES["vermelho"])
            return
        self.ultimo_resultado = resultado
        texto_resultado = formatar(resultado)
        self.historico.insert(0, f"{texto} = {texto_resultado}")
        self.var_expressao.set(texto_resultado)
        self.entrada.icursor("end")
        self.lbl_resultado.configure(text=f"{texto} =", fg=CORES["verde"])
        self.acabou_de_calcular = True

    def _usar_historico(self, _evento) -> None:
        selecao = self.historico.curselection()
        if selecao:
            resultado = self.historico.get(selecao[0]).rsplit(" = ", 1)[-1]
            self.entrada.insert("insert", resultado)
            self.entrada.focus_set()

    # ------------------------------------------------------------------ Fórmulas

    def _aba_formulas(self, aba: ttk.Frame) -> None:
        self.arvore = ttk.Treeview(aba, show="tree", selectmode="browse", height=18)
        self.arvore.column("#0", width=250)
        self.arvore.pack(side="left", fill="y")
        grupos: dict[str, str] = {}
        for i, formula in enumerate(fm.FORMULAS):
            if formula.grupo not in grupos:
                grupos[formula.grupo] = self.arvore.insert("", "end", text=formula.grupo, open=True)
            self.arvore.insert(grupos[formula.grupo], "end", iid=str(i), text=formula.nome)
        self.arvore.bind("<<TreeviewSelect>>", lambda _e: self._mostrar_formula())

        self.painel_formula = tk.Frame(aba, bg=CORES["painel"], padx=22, pady=18)
        self.painel_formula.pack(side="left", fill="both", expand=True, padx=(14, 0))
        self.arvore.selection_set("2")  # equação do 2º grau

    def _mostrar_formula(self) -> None:
        selecao = self.arvore.selection()
        if not selecao or not selecao[0].isdigit():
            return
        formula = fm.FORMULAS[int(selecao[0])]
        for filho in self.painel_formula.winfo_children():
            filho.destroy()
        p = self.painel_formula
        tk.Label(p, text=formula.nome, font=(FONTE, 16, "bold"), bg=CORES["painel"], fg=CORES["texto"],
                 anchor="w").pack(fill="x")
        tk.Label(p, text=formula.expressao, font=(FONTE_MONO, 13), bg=CORES["painel"], fg=CORES["destaque"],
                 anchor="w").pack(fill="x", pady=(2, 16))
        self.campos_formula: dict[str, tk.StringVar] = {}
        for chave, rotulo in formula.campos:
            linha = tk.Frame(p, bg=CORES["painel"])
            linha.pack(fill="x", pady=3)
            tk.Label(linha, text=rotulo, width=16, anchor="w", bg=CORES["painel"], fg=CORES["texto_suave"],
                     font=(FONTE, 10)).pack(side="left")
            var = tk.StringVar()
            entrada = ttk.Entry(linha, textvariable=var, font=(FONTE_MONO, 12), width=16)
            entrada.pack(side="left", ipady=2)
            entrada.bind("<Return>", lambda _e: self._calcular_formula(formula))
            self.campos_formula[chave] = var
        tk.Label(p, text="Os campos aceitam expressões, como 2π ou √2.", font=(FONTE, 9), bg=CORES["painel"],
                 fg=CORES["texto_suave"], anchor="w").pack(fill="x", pady=(6, 0))
        ttk.Button(p, text="Calcular", style="Destaque.TButton",
                   command=lambda: self._calcular_formula(formula)).pack(anchor="w", pady=14)
        self.quadro_resultado = tk.Frame(p, bg=CORES["painel"])
        self.quadro_resultado.pack(fill="x")

    def _calcular_formula(self, formula: fm.Formula) -> None:
        for filho in self.quadro_resultado.winfo_children():
            filho.destroy()
        valores = {}
        try:
            for chave, rotulo in formula.campos:
                texto = self.campos_formula[chave].get().strip()
                if not texto and chave in formula.opcionais:
                    valores[chave] = 0.0
                    continue
                if not texto:
                    raise fm.ErroFormula(f"preencha o campo \"{rotulo}\"")
                try:
                    valores[chave] = avaliar(texto)
                except ErroExpressao as erro:
                    raise fm.ErroFormula(f"{rotulo}: {erro}") from None
            linhas = formula.calcular(valores)
        except fm.ErroFormula as erro:
            tk.Label(self.quadro_resultado, text=maiuscula(str(erro)), font=(FONTE, 11), bg=CORES["painel"],
                     fg=CORES["vermelho"], anchor="w").pack(fill="x")
            return
        for rotulo, valor in linhas:
            linha = tk.Frame(self.quadro_resultado, bg=CORES["painel"])
            linha.pack(fill="x", pady=2)
            tk.Label(linha, text=rotulo, width=18, anchor="w", font=(FONTE, 11), bg=CORES["painel"],
                     fg=CORES["texto_suave"]).pack(side="left")
            tk.Label(linha, text=valor, anchor="w", font=(FONTE_MONO, 15, "bold"), bg=CORES["painel"],
                     fg=CORES["verde"]).pack(side="left")

    # ------------------------------------------------------------------ Conversor

    def _aba_conversor(self, aba: ttk.Frame) -> None:
        topo = tk.Frame(aba, bg=CORES["painel"], padx=22, pady=18)
        topo.pack(fill="x")
        self.var_categoria = tk.StringVar(value="Dados")
        self.var_valor = tk.StringVar(value="1")
        self.var_de = tk.StringVar()
        self.var_para = tk.StringVar()

        linha = tk.Frame(topo, bg=CORES["painel"])
        linha.pack(fill="x")
        tk.Label(linha, text="Categoria", bg=CORES["painel"], fg=CORES["texto_suave"]).pack(side="left")
        categoria = ttk.Combobox(linha, textvariable=self.var_categoria, values=list(cv.CATEGORIAS),
                                 state="readonly", width=16)
        categoria.pack(side="left", padx=10)
        categoria.bind("<<ComboboxSelected>>", lambda _e: self._trocar_categoria())

        linha2 = tk.Frame(topo, bg=CORES["painel"])
        linha2.pack(fill="x", pady=(16, 0))
        entrada = ttk.Entry(linha2, textvariable=self.var_valor, font=(FONTE_MONO, 16), width=12, justify="right")
        entrada.pack(side="left", ipady=3)
        self.cmb_de = ttk.Combobox(linha2, textvariable=self.var_de, state="readonly", width=24)
        self.cmb_de.pack(side="left", padx=10)
        tk.Button(linha2, text="⇄", font=(FONTE, 14, "bold"), bg=CORES["borda"], fg=CORES["destaque"],
                  relief="flat", bd=0, padx=10, highlightthickness=0, activebackground=CORES["tecla"], cursor="hand2",
                  command=self._inverter).pack(side="left")
        self.cmb_para = ttk.Combobox(linha2, textvariable=self.var_para, state="readonly", width=24)
        self.cmb_para.pack(side="left", padx=10)
        self.lbl_conversao = tk.Label(topo, font=(FONTE_MONO, 20, "bold"), bg=CORES["painel"], fg=CORES["verde"],
                                      anchor="w")
        self.lbl_conversao.pack(fill="x", pady=(16, 0))

        for var in (self.var_valor, self.var_de, self.var_para):
            var.trace_add("write", lambda *_: self._converter())

        ttk.Label(aba, text="O mesmo valor em todas as unidades da categoria", style="Suave.TLabel").pack(
            anchor="w", pady=(14, 6))
        self.tabela_conversao = ttk.Treeview(aba, columns=("valor", "unidade"), show="headings", height=10,
                                             selectmode="none")
        self.tabela_conversao.heading("valor", text="Valor", anchor="e")
        self.tabela_conversao.heading("unidade", text="Unidade", anchor="w")
        self.tabela_conversao.column("valor", width=220, anchor="e")
        self.tabela_conversao.column("unidade", width=300, anchor="w")
        self.tabela_conversao.pack(fill="both", expand=True)
        self._trocar_categoria()
        self.var_de.set("Gigabyte (GB)")
        self.var_para.set("Gibibyte (GiB)")

    def _trocar_categoria(self) -> None:
        unidades = list(cv.CATEGORIAS[self.var_categoria.get()])
        self.cmb_de.configure(values=unidades)
        self.cmb_para.configure(values=unidades)
        self.var_de.set(unidades[0])
        self.var_para.set(unidades[1])

    def _inverter(self) -> None:
        de, para = self.var_de.get(), self.var_para.get()
        self.var_de.set(para)
        self.var_para.set(de)

    def _converter(self) -> None:
        categoria, de, para = self.var_categoria.get(), self.var_de.get(), self.var_para.get()
        unidades = cv.CATEGORIAS.get(categoria, {})
        if de not in unidades or para not in unidades:
            return
        self.tabela_conversao.delete(*self.tabela_conversao.get_children())
        try:
            valor = avaliar(self.var_valor.get())
            resultado = cv.converter(valor, categoria, de, para)
        except (ErroExpressao, ValueError) as erro:
            self.lbl_conversao.configure(text=maiuscula(str(erro)), fg=CORES["vermelho"], font=(FONTE, 12))
            return
        self.lbl_conversao.configure(text=f"= {formatar(resultado, 6)}  {para.split('(')[-1].rstrip(')')}",
                                     fg=CORES["verde"], font=(FONTE_MONO, 20, "bold"))
        for unidade in unidades:
            self.tabela_conversao.insert("", "end", values=(formatar(cv.converter(valor, categoria, de, unidade), 6),
                                                            unidade))


def main() -> None:
    Aplicativo().mainloop()


if __name__ == "__main__":
    main()
