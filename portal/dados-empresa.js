/* =========================================================================
   DADOS CADASTRAIS — One Group
   Edite SOMENTE este arquivo. Cada item de EMPRESAS[] vira uma opção no
   seletor do portal. Deixe "" nos campos que ainda não tem (aparecem "—").

   Fontes (jun/2026): cartão CNPJ / ficha JUCESP (Drive) + Notion.
   Campos marcados "(a confirmar)" precisam de validação no documento oficial.
   ========================================================================= */
window.DADOS = {
  titulo: "Dados Cadastrais",
  subtitulo: "Dados para cadastro em clientes e fornecedores — uso interno One Group.",

  EMPRESAS: [

    /* ---------------------------------------------------------------- */
    {
      id: "one-work",
      label: "One Work Office",
      empresa: {
        nome_empresarial: "ONE WORK OFFICE ESPAÇOS COMPARTILHADOS LTDA",
        nome_fantasia: "One Work Office",
        cnpj: "35.507.363/0001-00",
        ie: "",                 // não localizada
        im: "",
        natureza: "206-2 — Sociedade Empresária Limitada (Unipessoal / ME)",
        capital: "R$ 100.000,00",
        situacao: "Ativa",
        data_situacao: "13/11/2019",
        cnae_principal: "82.11-3-00 — Serviços combinados de escritório e apoio administrativo",
        cnae_sec: "77.40-3-00 — Gestão de ativos intangíveis não-financeiros; 82.30-0-01 — Organização de feiras, congressos, exposições e festas",
        endereco: "Av. Regente Feijó, nº 944, Conj. 1604A",
        bairro: "Vila Regente Feijó",
        municipio: "São Paulo",
        uf: "SP",
        cep: "03342-000",
        telefone: "(11) 2076-0836",
        email: "contato@oneworkoffice.com.br",
        site: "oneworkoffice.com.br",
      },
      socios: [
        {
          nome: "Gabriel Soares Cassiano de Souza", cpf: "353.812.398-58",
          nascimento: "", estado_civil: "Casado", participacao: "Sócio",
          endereco: "Av. Regente Feijó, 1650, apto 2608, Vila Regente Feijó, São Paulo - SP, CEP 03342-000",
          bairro: "", municipio: "São Paulo", uf: "SP", cep: "03342-000",
          telefone: "", email: "",
        },
        {
          nome: "Jéssica Rocha Ferreira", cpf: "391.467.988-38",
          nascimento: "", estado_civil: "", participacao: "Administradora",
          endereco: "Rua Irapuã Vasco Campos, 55, Pq Maria Luiza, São Paulo - SP, CEP 03450-010",
          bairro: "", municipio: "São Paulo", uf: "SP", cep: "03450-010",
          telefone: "", email: "",
        },
      ],
      bancos: [
        { banco: "Itaú", codigo: "341", tipo: "Conta Corrente", agencia: "2961", conta: "99597-0", pix: "", titular: "One Work Office Espaços Compartilhados LTDA", cnpj: "35.507.363/0001-00" },
        { banco: "Cora", codigo: "403", tipo: "Conta Corrente", agencia: "0001", conta: "3815439-0", pix: "", titular: "One Work Office Espaços Compartilhados LTDA", cnpj: "35.507.363/0001-00" },
        { banco: "C6 Bank", codigo: "336", tipo: "Conta Corrente", agencia: "0001", conta: "18792006-0", pix: "", titular: "One Work Office Espaços Compartilhados LTDA", cnpj: "35.507.363/0001-00" },
      ],
    },

    /* ---------------------------------------------------------------- */
    {
      id: "brmobility",
      label: "BRMobility",
      nota: "Razão social operacional: DEX Veículos. Quadro societário a confirmar no contrato social atualizado.",
      empresa: {
        nome_empresarial: "DEX VEÍCULOS IMPORTAÇÃO COMÉRCIO E LOCAÇÃO LTDA",
        nome_fantasia: "BRMobility",
        cnpj: "20.413.574/0001-07",
        ie: "140.144.290.110",
        im: "",
        natureza: "Sociedade Empresária Limitada (EPP)",
        capital: "R$ 2.000.000,00",
        situacao: "Ativa",
        data_situacao: "18/09/2015",
        cnae_principal: "Locação de outros meios de transporte não especificados anteriormente, sem condutor",
        cnae_sec: "Comércio por atacado de peças e acessórios novos para veículos automotores; Comércio por atacado de pneumáticos e câmaras-de-ar; Comércio por atacado de peças e acessórios para motocicletas; Manutenção e reparação de motocicletas",
        endereco: "Rua Antônio de Barros, nº 2.099",
        bairro: "Vila Carrão (Tatuapé)",
        municipio: "São Paulo",
        uf: "SP",
        cep: "03401-001",
        telefone: "(11) 3995-4766 / (11) 3995-4768",
        email: "coordenador@brmobility.com.br",
        site: "brmobility.com.br",
      },
      socios: [],   // a confirmar — contrato social atualizado
      bancos: [],   // a confirmar
    },

    /* ---------------------------------------------------------------- */
    {
      id: "one-contabil",
      label: "One Contábil",
      nota: "Marca de contabilidade do grupo — sem CNPJ próprio localizado (opera via parceria Trôade / possível 'One Gestão de Negócios LTDA'). Preencher quando confirmado.",
      empresa: {
        nome_empresarial: "", nome_fantasia: "One Contábil", cnpj: "", ie: "", im: "",
        natureza: "", capital: "", situacao: "", data_situacao: "",
        cnae_principal: "", cnae_sec: "",
        endereco: "", bairro: "", municipio: "", uf: "", cep: "",
        telefone: "", email: "", site: "",
      },
      socios: [],
      bancos: [],
    },

    /* ---------------------------------------------------------------- */
    {
      id: "cassiano-martins",
      label: "Cassiano Martins",
      nota: "Advocacia do grupo (Cassiano e Menegare) — sociedade registrada na OAB, sem cartão CNPJ localizado. Preencher quando confirmado.",
      empresa: {
        nome_empresarial: "", nome_fantasia: "Cassiano Martins", cnpj: "", ie: "", im: "",
        natureza: "Sociedade de Advogados", capital: "", situacao: "", data_situacao: "",
        cnae_principal: "", cnae_sec: "",
        endereco: "", bairro: "", municipio: "", uf: "", cep: "",
        telefone: "", email: "", site: "",
      },
      socios: [],
      bancos: [],
    },

  ],
};
