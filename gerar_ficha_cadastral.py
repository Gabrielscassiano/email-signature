#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador da Ficha Cadastral - Cassiano Martins / One Group
Layout nas cores da marca (navy #0F1E4F + laranja #FF4400).

Estrutura baseada nos modelos cadastrais oficiais:
  - Dados Empresariais
  - Quadro Societário
  - Dados Bancários
  - Documentos / Anexos

Os campos saem em branco (linha preenchivel), prontos para
preenchimento manual ou digital. Para emitir uma ficha ja
preenchida, edite o dicionario DADOS abaixo.

Uso:  python3 gerar_ficha_cadastral.py
Saida: Ficha_Cadastral_Cassiano_Martins.pdf
"""

from fpdf import FPDF

# ---------------------------------------------------------------------------
# Cores da marca
# ---------------------------------------------------------------------------
NAVY = (15, 30, 79)        # #0F1E4F
ORANGE = (255, 68, 0)      # #FF4400
WHITE = (255, 255, 255)
GRAY_BG = (242, 244, 248)  # fundo claro dos campos
GRAY_LINE = (205, 210, 222)
GRAY_TXT = (90, 96, 110)

LOGO_WHITE = "Logotipo_OneGroup_WHITE.png"

# ---------------------------------------------------------------------------
# Dados (deixe "" para sair como campo em branco preenchivel)
# ---------------------------------------------------------------------------
DADOS = {
    "unidade": "Cassiano Martins",
    "empresa": {},   # ex.: {"CNPJ": "00.000.000/0001-00", ...}
    "socios": [{}, {}],
    "bancos": [{}, {}],
}

PAGE_W = 210
MARGIN = 15
CONTENT_W = PAGE_W - 2 * MARGIN


class Ficha(FPDF):
    def header(self):
        # Faixa navy do topo
        self.set_fill_color(*NAVY)
        self.rect(0, 0, PAGE_W, 34, "F")
        # Detalhe laranja
        self.set_fill_color(*ORANGE)
        self.rect(0, 34, PAGE_W, 1.6, "F")

        # Logo branco
        try:
            self.image(LOGO_WHITE, x=MARGIN, y=9, w=58)
        except Exception:
            self.set_xy(MARGIN, 12)
            self.set_text_color(*WHITE)
            self.set_font("Helvetica", "B", 20)
            self.cell(60, 8, "ONE GROUP")

        # Titulo a direita
        self.set_text_color(*WHITE)
        self.set_font("Helvetica", "B", 17)
        self.set_xy(PAGE_W - MARGIN - 95, 11)
        self.cell(95, 8, "FICHA CADASTRAL", align="R")
        self.set_font("Helvetica", "", 10.5)
        self.set_xy(PAGE_W - MARGIN - 95, 20)
        self.set_text_color(255, 150, 120)
        self.cell(95, 6, f"Unidade: {DADOS['unidade']}", align="R")

        self.set_y(44)

    def footer(self):
        self.set_y(-15)
        self.set_draw_color(*ORANGE)
        self.set_line_width(0.4)
        self.line(MARGIN, self.get_y(), PAGE_W - MARGIN, self.get_y())
        self.ln(1.5)
        self.set_font("Helvetica", "", 7.5)
        self.set_text_color(*GRAY_TXT)
        self.cell(0, 4,
                  "ONE GROUP  -  One Contábil  |  One Work  |  Cassiano Martins  |  BRMobility",
                  align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 4, f"Documento cadastral - página {self.page_no()}", align="C")

    # ---- helpers de layout ------------------------------------------------
    def section_title(self, text):
        if self.get_y() > 250:
            self.add_page()
        self.ln(2)
        self.set_fill_color(*NAVY)
        self.set_text_color(*WHITE)
        self.set_font("Helvetica", "B", 11)
        # marcador laranja
        y = self.get_y()
        self.set_fill_color(*ORANGE)
        self.rect(MARGIN, y, 2.5, 8, "F")
        self.set_fill_color(*NAVY)
        self.set_x(MARGIN + 2.5)
        self.cell(CONTENT_W - 2.5, 8, "   " + text.upper(), fill=True,
                  new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def sub_label(self, text):
        self.ln(1)
        self.set_text_color(*ORANGE)
        self.set_font("Helvetica", "B", 9.5)
        self.cell(0, 5, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(0.5)

    def field(self, label, value="", w=CONTENT_W, h=8.5, new_line=True):
        """Campo rotulado com area de preenchimento."""
        x0, y0 = self.get_x(), self.get_y()
        # caixa do campo (fundo) primeiro
        self.set_fill_color(*GRAY_BG)
        self.set_draw_color(*GRAY_LINE)
        self.set_line_width(0.2)
        self.rect(x0, y0, w, h, "DF")
        # rotulo por cima
        self.set_font("Helvetica", "B", 7.5)
        self.set_text_color(*NAVY)
        self.set_xy(x0 + 2, y0 + 1)
        self.cell(w - 4, 3.2, label.upper())
        # valor
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 35, 50)
        self.set_xy(x0 + 2, y0 + 3.6)
        self.cell(w - 4, 4.5, str(value))
        if new_line:
            self.set_xy(MARGIN, y0 + h + 1.5)
        else:
            self.set_xy(x0 + w + 4, y0)
        return h

    def two_fields(self, l1, v1, l2, v2):
        w = (CONTENT_W - 4) / 2
        y0 = self.get_y()
        self.field(l1, v1, w=w, new_line=False)
        self.set_xy(MARGIN + w + 4, y0)
        self.field(l2, v2, w=w, new_line=True)

    def three_fields(self, items):
        w = (CONTENT_W - 8) / 3
        y0 = self.get_y()
        for i, (lbl, val) in enumerate(items):
            self.set_xy(MARGIN + i * (w + 4), y0)
            self.field(lbl, val, w=w, new_line=False)
        self.set_xy(MARGIN, y0 + 8.5 + 1.5)

    def checklist(self, items):
        self.set_font("Helvetica", "", 9.5)
        for it in items:
            y = self.get_y()
            self.set_draw_color(*NAVY)
            self.set_line_width(0.3)
            self.rect(MARGIN + 1, y + 0.8, 3.8, 3.8)
            self.set_text_color(40, 45, 60)
            self.set_xy(MARGIN + 8, y)
            self.cell(0, 5.4, it, new_x="LMARGIN", new_y="NEXT")
            self.ln(0.8)


def g(d, k):
    return d.get(k, "") if isinstance(d, dict) else ""


def build():
    pdf = Ficha(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.set_margins(MARGIN, 44, MARGIN)
    pdf.add_page()

    emp = DADOS["empresa"]
    socios = DADOS["socios"]
    bancos = DADOS["bancos"]

    # ---------------- DADOS EMPRESARIAIS ----------------
    pdf.section_title("Dados Empresariais")
    pdf.two_fields("Razão Social / Nome Empresarial", g(emp, "nome_empresarial"),
                   "Nome Fantasia", g(emp, "nome_fantasia"))
    pdf.three_fields([("CNPJ", g(emp, "cnpj")),
                      ("Inscrição Estadual", g(emp, "ie")),
                      ("Inscrição Municipal", g(emp, "im"))])
    pdf.field("Endereço (logradouro, número, complemento)", g(emp, "endereco"))
    pdf.three_fields([("Bairro", g(emp, "bairro")),
                      ("Município", g(emp, "municipio")),
                      ("UF", g(emp, "uf"))])
    pdf.three_fields([("CEP", g(emp, "cep")),
                      ("Telefone", g(emp, "telefone")),
                      ("E-mail", g(emp, "email"))])
    pdf.field("Atividade Econômica Principal (CNAE)", g(emp, "cnae_principal"))
    pdf.field("Atividades Econômicas Secundárias (CNAE)", g(emp, "cnae_sec"), h=16)
    pdf.two_fields("Data da Situação Cadastral", g(emp, "data_situacao"),
                   "Situação Cadastral", g(emp, "situacao") or "Ativa")
    pdf.two_fields("Natureza Jurídica", g(emp, "natureza"),
                   "Capital Social (R$)", g(emp, "capital"))

    # ---------------- QUADRO SOCIETARIO ----------------
    pdf.section_title("Quadro Societário")
    for i, s in enumerate(socios, start=1):
        pdf.sub_label(f"Sócio {i}")
        pdf.two_fields("Nome Completo", g(s, "nome"),
                       "CPF", g(s, "cpf"))
        pdf.three_fields([("Data de Nascimento", g(s, "nascimento")),
                          ("Estado Civil", g(s, "estado_civil")),
                          ("Participação (%)", g(s, "participacao"))])
        pdf.field("Endereço", g(s, "endereco"))
        pdf.three_fields([("Bairro", g(s, "bairro")),
                          ("Município", g(s, "municipio")),
                          ("UF", g(s, "uf"))])
        pdf.three_fields([("CEP", g(s, "cep")),
                          ("Telefone", g(s, "telefone")),
                          ("E-mail", g(s, "email"))])

    # ---------------- DADOS BANCARIOS ----------------
    pdf.section_title("Dados Bancários")
    for i, b in enumerate(bancos, start=1):
        pdf.sub_label(f"Conta {i}")
        pdf.three_fields([("Banco", g(b, "banco")),
                          ("Codigo", g(b, "codigo")),
                          ("Tipo de Conta", g(b, "tipo"))])
        pdf.three_fields([("Agência", g(b, "agencia")),
                          ("Conta Corrente", g(b, "conta")),
                          ("Chave PIX", g(b, "pix"))])
        pdf.two_fields("Titular / Nome Empresarial", g(b, "titular"),
                       "CNPJ do Titular", g(b, "cnpj"))

    # ---------------- DOCUMENTOS / ANEXOS ----------------
    pdf.section_title("Documentos e Anexos")
    pdf.set_text_color(*GRAY_TXT)
    pdf.set_font("Helvetica", "", 9)
    pdf.multi_cell(CONTENT_W, 4.6,
                   "Assinale e anexe os documentos que acompanham esta ficha cadastral:")
    pdf.ln(2)
    pdf.checklist([
        "Cartão CNPJ atualizado",
        "Contrato Social / Ato Constitutivo (e última alteração)",
        "Documento de identificação dos sócios (RG / CNH)",
        "CPF dos sócios",
        "Comprovante de endereço da empresa",
        "Certidão Negativa de Débitos (CND) - Receita Federal",
        "Comprovante de dados bancários",
        "Procuração (quando aplicável)",
    ])

    # ---------------- DECLARACAO / ASSINATURA ----------------
    pdf.ln(4)
    pdf.section_title("Declaração e Assinatura")
    pdf.set_text_color(*GRAY_TXT)
    pdf.set_font("Helvetica", "", 8.5)
    pdf.multi_cell(CONTENT_W, 4.4,
                   "Declaro, para os devidos fins, que as informações prestadas nesta ficha "
                   "cadastral são verdadeiras e completas, responsabilizando-me civil e "
                   "criminalmente por sua veracidade.")
    pdf.ln(10)
    w = (CONTENT_W - 10) / 2
    y = pdf.get_y()
    pdf.set_draw_color(*NAVY)
    pdf.set_line_width(0.3)
    pdf.line(MARGIN, y, MARGIN + w, y)
    pdf.line(MARGIN + w + 10, y, MARGIN + CONTENT_W, y)
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*NAVY)
    pdf.set_xy(MARGIN, y + 1)
    pdf.cell(w, 4, "Assinatura do Responsável", align="C")
    pdf.set_xy(MARGIN + w + 10, y + 1)
    pdf.cell(w, 4, "Local e Data", align="C")

    out = "Ficha_Cadastral_Cassiano_Martins.pdf"
    pdf.output(out)
    print("Gerado:", out)


if __name__ == "__main__":
    build()
