from app.models.database import db, Paciente
from sqlalchemy import case

class NoPaciente:
    def __init__(self, paciente):
        self.paciente = paciente
        self.proximo = None

class GerenciadorPacientes:
    def __init__(self):
        self.lista_especialidade = {
            'Clinico Geral': list(range(3   , 0, -1)),
            'Ginecologia': list(range(30, 0, -1)),
            'Pediatria': list(range(30, 0, -1)),
            'Geriatria': list(range(30, 0, -1)),
            'Ortopedia': list(range(30, 0, -1))
        }
        self.senhas_esp = {esp: 1 for esp in self.lista_especialidade}
        self.triagem_escolhida = 'triagem 2'

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
        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", nome):
            return "Nome inválido. Use apenas letras e espaços."
        
        if not self.limitar_atendimento(esp):
            return f"Sem vagas para {esp} hoje."

        senha = self.gerar_senha(esp)
        tipo = self.verificar_tipo(idade)
        triagem = self.proxima_triagem()

        novo_paciente = Paciente(
            name=nome,
            age=idade,
            specialty=esp,
            type=tipo,
            password=f"{esp[:3].upper()}-{senha}",
            triage=triagem
        )
        db.session.add(novo_paciente)
        db.session.commit()

        return "Paciente cadastrado com sucesso!"

    def chamar_paciente(self, especialidade):
        paciente = Paciente.query.filter_by(specialty=especialidade, type='Preferencial').order_by(Paciente.id).first()
    
        if not paciente:
            paciente = Paciente.query.filter_by(specialty=especialidade, type='Normal').order_by(Paciente.id).first()

        if paciente:
            dados = {   
            'senha': paciente.password,
            'nome': paciente.name,
            'tipo': paciente.type,
            'triagem': paciente.triage,
            'especialidade': paciente.specialty
            }
            db.session.delete(paciente)
            db.session.commit()
            return dados

        return None


    def listar_pacientes(self):
       return Paciente.query \
        .order_by(
            case(
                (Paciente.type == "Preferencial", 0),
                else_=1
            ),
            Paciente.date_created.asc()
        ).all()