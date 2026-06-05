/* =========================================================================
   DADOS CADASTRAIS DA EMPRESA  —  edite SOMENTE este arquivo.
   Cada empresa do grupo = uma cópia desta pasta com este arquivo preenchido.
   Deixe "" nos campos que ainda não tem; eles aparecem como "—" no portal.
   ========================================================================= */
window.DADOS_EMPRESA = {
  // Identificação do portal (cabeçalho)
  unidade: "Cassiano Martins",
  subtitulo: "Dados cadastrais para cadastro em clientes e fornecedores",

  empresa: {
    nome_empresarial: "",     // Razão Social
    nome_fantasia: "",
    cnpj: "",
    ie: "",                   // Inscrição Estadual
    im: "",                   // Inscrição Municipal
    natureza: "",             // Natureza Jurídica
    capital: "",              // Capital Social (R$)
    cnae_principal: "",
    cnae_sec: "",
    situacao: "Ativa",
    data_situacao: "",
    // Endereço
    endereco: "",             // logradouro, número, complemento
    bairro: "",
    municipio: "",
    uf: "",
    cep: "",
    // Contato
    telefone: "",
    email: "",
    site: "",
  },

  socios: [
    {
      nome: "", cpf: "", nascimento: "", estado_civil: "", participacao: "",
      endereco: "", bairro: "", municipio: "", uf: "", cep: "",
      telefone: "", email: "",
    },
  ],

  bancos: [
    {
      banco: "", codigo: "", tipo: "", agencia: "", conta: "",
      pix: "", titular: "", cnpj: "",
    },
  ],
};
