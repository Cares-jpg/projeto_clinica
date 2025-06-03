from app.models.database import db, Paciente
import re
from sqlalchemy import case
import logging
from logger_config import *

class ValidadorPaciente:
    @staticmethod
    def validar_nome(nome):
        logging.debug(f"Validando nome: {nome}")
        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", nome):
            logging.warning(f"Nome inválido detectado: {nome}")
            return False, "Nome inválido. Use apenas letras e espaços."
        logging.debug(f"Nome {nome} validado com sucesso")
        return True, None
    
    @staticmethod
    def validar_idade(idade):
        if idade < 0 or idade > 110:
            logging.warning(f"Idade inválida detectada: {idade}")
            return False, "Idade inválida. Deve estar entre 0 e 110 anos."
        logging.debug(f"Idade {idade} validada com sucesso")
        return True, None

class GerenciadorTipo:
    IDADE_PREFERENCIAL = 60
    
    @staticmethod
    def verificar_tipo(idade):
        tipo = 'Preferencial' if idade >= GerenciadorTipo.IDADE_PREFERENCIAL else 'Normal'
        logging.debug(f"Tipo determinado: {tipo}")
        return tipo

class GerenciadorTriagem:
    def __init__(self):
        self.triagem_atual = 'triagem 2'
    
    def proxima_triagem(self):
        try:
            self.triagem_atual = 'triagem 1' if self.triagem_atual == 'triagem 2' else 'triagem 2'
            logging.info(f"Triagem alterada para: {self.triagem_atual}")
            return self.triagem_atual
        except Exception as e:
            logging.critical(f"Erro crítico na operação proxima_triagem: {str(e)}")
            raise

class GerenciadorEspecialidades:
    def __init__(self):
        self.lista_especialidade = {
            'Clinico Geral': list(range(3, 0, -1)),
            'Ginecologia': list(range(30, 0, -1)),
            'Pediatria': list(range(30, 0, -1)),
            'Geriatria': list(range(30, 0, -1)),
            'Ortopedia': list(range(30, 0, -1))
        }
        logging.debug("GerenciadorEspecialidades inicializado com lista de especialidades")
    
    def tem_vaga(self, especialidade):
        logging.info(f"Verificando vagas para especialidade: {especialidade}")
        
        try:
            if especialidade not in self.lista_especialidade:
                logging.warning(f"Tentativa de acesso a especialidade inexistente: {especialidade}")
                return False
                
            if self.lista_especialidade[especialidade]:
                vagas_restantes = len(self.lista_especialidade[especialidade]) - 1
                self.lista_especialidade[especialidade].pop()
                logging.info(f"Vaga alocada para {especialidade}. Vagas restantes: {vagas_restantes}")
                return True
                
            logging.warning(f"Sem vagas disponíveis para {especialidade}")
            return False
        except Exception as e:
            logging.error(f"Erro ao verificar vagas: {str(e)}")
            raise
    
    def get_especialidades(self):
        return list(self.lista_especialidade.keys())

class GerenciadorSenhas:
    def __init__(self, especialidades):
        self.senhas_esp = {esp: 1 for esp in especialidades}
    
    def gerar_senha(self, especialidade):
        logging.info(f"Gerando senha para especialidade: {especialidade}")
        
        try:
            senha = self.senhas_esp[especialidade]
            self.senhas_esp[especialidade] += 1
            logging.info(f"Senha gerada: {especialidade[:3].upper()}-{senha}")
            return senha
        except KeyError as e:
            logging.error(f"Especialidade não encontrada ao gerar senha: {str(e)}")
            raise
        except Exception as e:
            logging.critical(f"Erro crítico ao gerar senha: {str(e)}")
            raise

class GerenciadorPacientes:
    def __init__(self):
        self.gerenciador_especialidades = GerenciadorEspecialidades()
        self.gerenciador_senhas = GerenciadorSenhas(self.gerenciador_especialidades.get_especialidades())
        self.gerenciador_triagem = GerenciadorTriagem()
        self.validador = ValidadorPaciente()
        self.gerenciador_tipo = GerenciadorTipo()

    def adicionar_paciente(self, nome, esp, idade):
        logging.info(f"Iniciando cadastro de paciente - Nome: {nome}, Especialidade: {esp}, Idade: {idade}")
        
        try:
            valido, erro = self.validador.validar_nome(nome)
            if not valido:
                logging.warning(f"Validação de nome falhou: {erro}")
                return erro
                
            valido, erro = self.validador.validar_idade(idade)
            if not valido:
                logging.warning(f"Validação de idade falhou: {erro}")
                return erro
            
            if not self.gerenciador_especialidades.tem_vaga(esp):
                msg = f"Sem vagas para {esp} hoje."
                logging.warning(msg)
                return msg

            senha = self.gerenciador_senhas.gerar_senha(esp)
            tipo = self.gerenciador_tipo.verificar_tipo(idade)
            triagem = self.gerenciador_triagem.proxima_triagem()

            novo_paciente = Paciente(
                name=nome,
                age=idade,
                specialty=esp,
                type=tipo,
                password=f"{esp[:3].upper()}-{senha}",
                triage=triagem
            )
            
            logging.debug(f"Tentando salvar paciente no banco de dados: {nome}")
            db.session.add(novo_paciente)
            db.session.commit()

            logging.info(f"Paciente {nome} cadastrado com sucesso")
            return "Paciente cadastrado com sucesso!"
            
        except Exception as e:
            logging.critical(f"Erro crítico ao cadastrar paciente: {str(e)}")
            db.session.rollback()
            return f"Erro ao cadastrar paciente: {str(e)}"

    def chamar_paciente(self, especialidade):
        logging.info(f"Chamando próximo paciente para {especialidade}")
        
        try:
            paciente = Paciente.query.filter_by(
                specialty=especialidade, 
                type='Preferencial'
            ).order_by(Paciente.id).first()
        
            if not paciente:
                paciente = Paciente.query.filter_by(
                    specialty=especialidade, 
                    type='Normal'
                ).order_by(Paciente.id).first()

            if paciente:
                dados = {   
                    'senha': paciente.password,
                    'nome': paciente.name,
                    'tipo': paciente.type,
                    'triagem': paciente.triage,
                    'especialidade': paciente.specialty
                }
                logging.debug(f"Removendo paciente {paciente.name} do banco de dados")
                db.session.delete(paciente)
                db.session.commit()
                
                return dados

            logging.warning(f"Nenhum paciente encontrado para a especialidade {especialidade}")
            return None
            
        except Exception as e:
            logging.critical(f"Erro crítico ao chamar paciente: {str(e)}")
            db.session.rollback()
            raise Exception(f"Erro ao chamar paciente: {str(e)}")

    def listar_pacientes(self):
        logging.info("Listando todos os pacientes")
        
        try:
            logging.debug("Executando query para listar pacientes ordenados")
            pacientes = Paciente.query \
                .order_by(
                    case(
                        (Paciente.type == "Preferencial", 0),
                        else_=1
                    ),
                    Paciente.date_created.asc()
                ).all()
                
            qtd_pacientes = len(pacientes)
            logging.info(f"Lista de {qtd_pacientes} pacientes obtida com sucesso")
            logging.debug(f"Pacientes encontrados: {[p.name for p in pacientes]}")
            return pacientes
            
        except Exception as e:
            logging.critical(f"Erro crítico ao listar pacientes: {str(e)}")
            raise Exception(f"Erro ao listar pacientes: {str(e)}")