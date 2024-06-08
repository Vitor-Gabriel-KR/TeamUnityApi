from extensão.models import Funcionario

def criar_funcionario(dados_essenciais, dados_opcionais=None):
    novo_funcionario = Funcionario.objects.create(
        nome_completo=dados_essenciais['nome_completo'],
        data_nascimento=dados_essenciais['data_nascimento'],
        rg=dados_essenciais['rg'],
        cpf=dados_essenciais['cpf'],
        endereco_residencial=dados_essenciais['endereco_residencial'],
        telefone=dados_essenciais['telefone'],
        email=dados_essenciais['email'],
        documento_identidade=dados_essenciais.get('documento_identidade', None),
        carteira_trabalho=dados_essenciais.get('carteira_trabalho', None),
        estado_civil=dados_essenciais.get('estado_civil', None),
        dependentes=dados_essenciais.get('dependentes', None),
        alergias=dados_essenciais.get('alegias', None),
        condicoes_medicas=dados_essenciais.get('condicoes_medicas', None),
        cargo=dados_essenciais.get('cargo', None),
        salario=dados_essenciais.get('salario', None),
    )
    if dados_opcionais:
        for chave, valor in dados_opcionais.items():
            setattr(novo_funcionario, chave, valor)
        novo_funcionario.save()

    return novo_funcionario

dados_essenciais = {
    'nome_completo': 'Fulano de Tal',
    'data_nascimento': '1990-01-01',
    'rg': '123456789',
    'cpf': '123.456.789-00',
    'endereco_residencial': 'Rua Exemplo, 123',
    'telefone': '(00) 1234-5678',
    'email': 'fulano@example.com',
    'documento_identidade': '987654321',
    'carteira_trabalho': '1234567890',
    'numero_conta_bancaria': '987654',
    'agencia_bancaria': '1234',
    'banco': 'Banco Exemplo',
    'estado_civil': 'Solteiro',
    'dependentes': 0,
    'alergias': 'Nenhuma',
    'condicoes_medicas': 'Nenhuma',
    'cargo': 'Desenvolvedor',
    'salario': 5000.00,
}

# Dados opcionais genéricos
dados_opcionais = {
    'comprovante_residencia': 'Conta de Luz',
    'contato_emergencia_nome': 'Cicrano de Tal',
    'contato_emergencia_relacao': 'Parente',
    'contato_emergencia_telefone': '(00) 9876-5432',
    'formacao_academica': 'Graduação',
    'historico_profissional': 'Experiência Profissional',
    'foto': None,  
    'profissao': 'Engenheiro',
    'departamento': 'TI',
    'data_inicio_profissao': '2010-01-01',
    'data_termino_profissao': None,
    'trabalhando_em': 'Empresa Exemplo',
    'horario_de_trabalho_inicio': '08:00:00',
    'horario_de_trabalho_fim': '17:00:00',
    'intervalo': '01:00:00',
    'numero_casa': '123',
    'carteira_de_trabalho': '123456',
    'passaporte': 'ABC123',
}

# novo_funcionario = criar_funcionario(dados_essenciais, dados_opcionais)

criar_funcionario(dados_essenciais, dados_opcionais)