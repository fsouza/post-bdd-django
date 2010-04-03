#coding:utf-8
from pycukes import *
from should_dsl import *
import set_django

from django.db import IntegrityError
from matricula.models import Aluno

@DadoQue('eu estou cadastrando um aluno')
def iniciar_cadastro_aluno(contexto):
    """docstring for iniciar_cadastro_aluno"""
    contexto._aluno = Aluno()

@Quando('eu não digito o nome')
def aluno_sem_nome(contexto):
    """docstring for aluno_sem_nome"""
    contexto._aluno.nome = None

@Entao('o cadastro não pode ser completado')
def cadastro_nao_pode_ser_completado(contexto):
    """docstring for cadastro_nao_pode_ser_completado"""
    IntegrityError |should_be.thrown_by| contexto._aluno.save
