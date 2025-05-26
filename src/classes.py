class NoPaciente:
    def __init__(self, paciente):
        self.paciente = paciente
        self.proximo = None


class GerenciadorPacientes:
    def __init__(self):
        self.lista_especialidade = {
            'Clinico Geral': list(range(2, 0, -1)),
            'Ginecologia': list(range(30, 0, -1)),
            'Pediatria': list(range(30, 0, -1)),
            'Geriatria': list(range(30, 0, -1)),
            'Ortopedia': list(range(30, 0, -1))
        }
        self.senhas_esp = {esp: 1 for esp in self.lista_especialidade}
        self.triagem_escolhida = 'triagem 2'
        self.inicio = None  
        self.fim = None     
        self.ordenando_lista = 0

    def limitar_atendimento(self, esp):
        if self.lista_especialidade[esp]:
            self.lista_especialidade[esp].pop()
            return True
        return False

    def gerar_senha(self, esp):
        senha = self.senhas_esp[esp]
        self.senhas_esp[esp] += 1
        return senha

    def proxima_triagem(self):
        self.triagem_escolhida = 'triagem 1' if self.triagem_escolhida == 'triagem 2' else 'triagem 2'
        return self.triagem_escolhida

    def verificar_tipo(self, idade):
        return 'Preferencial' if idade > 60 else 'Normal'

    def adicionar_paciente(self, nome, esp, idade):
        if not self.limitar_atendimento(esp):
            return f"Sem vagas para {esp} hoje."

        senha = self.gerar_senha(esp)
        tipo = self.verificar_tipo(idade)
        triagem = self.proxima_triagem()

        paciente = {
            'nome': nome,
            'especialidade': esp,
            'tipo': tipo,
            'senha': senha,
            'triagem': triagem
        }

        novo_no = NoPaciente(paciente)

        if tipo == 'Preferencial':
            novo_no.proximo = self.inicio
            self.inicio = novo_no
            if self.fim is None:
                self.fim = novo_no
        else:
            if self.inicio is None:
                self.inicio = novo_no
                self.fim = novo_no
            else:
                self.fim.proximo = novo_no
                self.fim = novo_no

        return "Paciente cadastrado com sucesso!"

    def listar_pacientes(self):
        pacientes = []
        atual = self.inicio
        while atual:
            pacientes.append(atual.paciente)
            atual = atual.proximo
        return pacientes

    def chamar_paciente(self, especialidade):
        anterior = None
        atual = self.inicio

        while atual:
            if atual.paciente['especialidade'] == especialidade:
                paciente_chamado = atual.paciente
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.inicio = atual.proximo
                if atual == self.fim:
                    self.fim = anterior
                return f"Chamando senha {paciente_chamado['senha']} - {paciente_chamado['nome']} ({paciente_chamado['tipo']}, {paciente_chamado['triagem']})"
            anterior = atual
            atual = atual.proximo

        return f"Não há pacientes aguardando em {especialidade}."
