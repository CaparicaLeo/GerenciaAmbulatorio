import tkinter as tk
from tkinter import messagebox

# Classe Paciente
class Paciente:
    def __init__(self, nome, cpf, idade, endereco, telefone, historico_medico, emergencia=False):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        self.historico_medico = historico_medico
        self.emergencia = emergencia
        self.em_atendimento = False

    def __str__(self):
        return f"{self.nome} - {self.cpf} {'(Emergência)' if self.emergencia else ''}"

# Classe Médico
class Medico:
    def __init__(self, nome, crm, especialidade, telefone, ocupado=False):
        self.nome = nome
        self.crm = crm
        self.especialidade = especialidade
        self.telefone = telefone
        self.ocupado = ocupado

    def __str__(self):
        return f"{self.nome} - {self.crm} ({'Ocupado' if self.ocupado else 'Disponível'})"

# Classe para a janela inicial
class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestão Hospitalar")
        self.root.geometry("600x400")

        self.label = tk.Label(root, text="Sistema de Gestão Hospitalar")
        self.label.pack(pady=10)

        self.button_pacientes = tk.Button(root, text="Cadastro de Pacientes", command=self.abrir_tela_pacientes)
        self.button_pacientes.pack(pady=5)

        self.button_consulta_pacientes = tk.Button(root, text="Consulta de Pacientes", command=self.abrir_tela_consulta_pacientes)
        self.button_consulta_pacientes.pack(pady=5)

        self.button_medicos = tk.Button(root, text="Gestão de Médicos", command=self.abrir_tela_medicos)
        self.button_medicos.pack(pady=5)

        self.button_consultas_cirurgias = tk.Button(root, text="Gerenciar Consultas e Cirurgias", command=self.abrir_tela_consultas_cirurgias)
        self.button_consultas_cirurgias.pack(pady=5)

        self.label_fila_pacientes = tk.Label(root, text="Fila de Pacientes:")
        self.label_fila_pacientes.pack(pady=5)

        self.listbox_pacientes = tk.Listbox(root)
        self.listbox_pacientes.pack(pady=5)

        self.label_lista_medicos = tk.Label(root, text="Lista de Médicos:")
        self.label_lista_medicos.pack(pady=5)

        self.listbox_medicos = tk.Listbox(root)
        self.listbox_medicos.pack(pady=5)

        self.atualizar_listas()

    def abrir_tela_pacientes(self):
        self.new_window = tk.Toplevel(self.root)
        PacientesWindow(self.new_window, self)

    def abrir_tela_consulta_pacientes(self):
        self.new_window = tk.Toplevel(self.root)
        ConsultaPacientesWindow(self.new_window)

    def abrir_tela_medicos(self):
        self.new_window = tk.Toplevel(self.root)
        MedicosWindow(self.new_window, self)

    def abrir_tela_consultas_cirurgias(self):
        self.new_window = tk.Toplevel(self.root)
        ConsultasCirurgiasWindow(self.new_window, self)

    def atualizar_listas(self):
        self.listbox_pacientes.delete(0, tk.END)
        pacientes_ordenados = sorted(PacientesWindow.pacientes, key=lambda p: p.emergencia, reverse=True)
        for paciente in pacientes_ordenados:
            self.listbox_pacientes.insert(tk.END, str(paciente))

        self.listbox_medicos.delete(0, tk.END)
        for medico in MedicosWindow.medicos:
            self.listbox_medicos.insert(tk.END, str(medico))

# Classe para a tela de cadastro de pacientes
class PacientesWindow:
    pacientes = []

    def __init__(self, root, main_window):
        self.root = root
        self.main_window = main_window
        self.root.title("Cadastro de Pacientes")
        self.root.geometry("400x400")

        self.label_nome = tk.Label(root, text="Nome:")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(root)
        self.entry_nome.pack()

        self.label_cpf = tk.Label(root, text="CPF:")
        self.label_cpf.pack()
        self.entry_cpf = tk.Entry(root)
        self.entry_cpf.pack()

        self.label_idade = tk.Label(root, text="Idade:")
        self.label_idade.pack()
        self.entry_idade = tk.Entry(root)
        self.entry_idade.pack()

        self.label_endereco = tk.Label(root, text="Endereço:")
        self.label_endereco.pack()
        self.entry_endereco = tk.Entry(root)
        self.entry_endereco.pack()

        self.label_telefone = tk.Label(root, text="Telefone:")
        self.label_telefone.pack()
        self.entry_telefone = tk.Entry(root)
        self.entry_telefone.pack()

        self.label_historico = tk.Label(root, text="Histórico Médico:")
        self.label_historico.pack()
        self.entry_historico = tk.Entry(root)
        self.entry_historico.pack()

        self.emergencia_var = tk.BooleanVar()
        self.check_emergencia = tk.Checkbutton(root, text="Emergência", variable=self.emergencia_var)
        self.check_emergencia.pack(pady=5)

        self.button_adicionar = tk.Button(root, text="Adicionar Paciente", command=self.adicionar_paciente)
        self.button_adicionar.pack(pady=10)

    def adicionar_paciente(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        idade = self.entry_idade.get()
        endereco = self.entry_endereco.get()
        telefone = self.entry_telefone.get()
        historico = self.entry_historico.get()
        emergencia = self.emergencia_var.get()

        paciente = Paciente(nome, cpf, idade, endereco, telefone, historico, emergencia)
        PacientesWindow.pacientes.append(paciente)
        messagebox.showinfo("Paciente Adicionado", f"Paciente {nome} adicionado com sucesso!")
        self.main_window.atualizar_listas()

# Classe para a tela de consulta de pacientes
class ConsultaPacientesWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Consulta de Pacientes")
        self.root.geometry("400x400")

        self.listbox_pacientes = tk.Listbox(root)
        self.listbox_pacientes.pack(pady=10)

        self.button_mostrar = tk.Button(root, text="Mostrar Pacientes", command=self.mostrar_pacientes)
        self.button_mostrar.pack(pady=10)

    def mostrar_pacientes(self):
        self.listbox_pacientes.delete(0, tk.END)
        pacientes_ordenados = sorted(PacientesWindow.pacientes, key=lambda p: p.emergencia, reverse=True)
        for paciente in pacientes_ordenados:
            self.listbox_pacientes.insert(tk.END, str(paciente))

# Classe para a tela de gestão de médicos
class MedicosWindow:
    medicos = []

    def __init__(self, root, main_window):
        self.root = root
        self.main_window = main_window
        self.root.title("Gestão de Médicos")
        self.root.geometry("400x400")

        self.label_nome = tk.Label(root, text="Nome:")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(root)
        self.entry_nome.pack()

        self.label_crm = tk.Label(root, text="CRM:")
        self.label_crm.pack()
        self.entry_crm = tk.Entry(root)
        self.entry_crm.pack()

        self.label_especialidade = tk.Label(root, text="Especialidade:")
        self.label_especialidade.pack()
        self.entry_especialidade = tk.Entry(root)
        self.entry_especialidade.pack()

        self.label_telefone = tk.Label(root, text="Telefone:")
        self.label_telefone.pack()
        self.entry_telefone = tk.Entry(root)
        self.entry_telefone.pack()

        self.button_adicionar = tk.Button(root, text="Adicionar Médico", command=self.adicionar_medico)
        self.button_adicionar.pack(pady=10)

        self.listbox_medicos = tk.Listbox(root)
        self.listbox_medicos.pack(pady=10)

        self.button_mostrar = tk.Button(root, text="Mostrar Médicos", command=self.mostrar_medicos)
        self.button_mostrar.pack(pady=10)

    def adicionar_medico(self):
        nome = self.entry_nome.get()
        crm = self.entry_crm.get()
        especialidade = self.entry_especialidade.get()
        telefone = self.entry_telefone.get()

        medico = Medico(nome, crm, especialidade, telefone)
        MedicosWindow.medicos.append(medico)
        messagebox.showinfo("Médico Adicionado", f"Médico {nome} adicionado com sucesso!")
        self.main_window.atualizar_listas()

    def mostrar_medicos(self):
        self.listbox_medicos.delete(0, tk.END)
        for medico in MedicosWindow.medicos:
            self.listbox_medicos.insert(tk.END, str(medico))

# Classe para a tela de gestão de consultas e cirurgias
class ConsultasCirurgiasWindow:
    def __init__(self, root, main_window):
        self.root = root
        self.main_window = main_window
        self.root.title("Gestão de Consultas e Cirurgias")
        self.root.geometry("400x400")

        self.label_pacientes = tk.Label(root, text="Pacientes:")
        self.label_pacientes.pack()
        self.listbox_pacientes = tk.Listbox(root)
        self.listbox_pacientes.pack(pady=5)

        self.label_medicos = tk.Label(root, text="Médicos:")
        self.label_medicos.pack()
        self.listbox_medicos = tk.Listbox(root)
        self.listbox_medicos.pack(pady=5)

        self.button_atender = tk.Button(root, text="Atender Paciente", command=self.atender_paciente)
        self.button_atender.pack(pady=10)

        self.atualizar_listas()

    def atualizar_listas(self):
        self.listbox_pacientes.delete(0, tk.END)
        pacientes_ordenados = sorted(PacientesWindow.pacientes, key=lambda p: p.emergencia, reverse=True)
        for paciente in pacientes_ordenados:
            if not paciente.em_atendimento:
                self.listbox_pacientes.insert(tk.END, str(paciente))

        self.listbox_medicos.delete(0, tk.END)
        for medico in MedicosWindow.medicos:
            if not medico.ocupado:
                self.listbox_medicos.insert(tk.END, str(medico))

    def atender_paciente(self):
        paciente_index = self.listbox_pacientes.curselection()
        medico_index = self.listbox_medicos.curselection()

        if paciente_index and medico_index:
            paciente = PacientesWindow.pacientes[paciente_index[0]]
            medico = MedicosWindow.medicos[medico_index[0]]

            paciente.em_atendimento = True
            medico.ocupado = True

            messagebox.showinfo("Atendimento Iniciado", f"O paciente {paciente.nome} está sendo atendido pelo médico {medico.nome}.")
            self.main_window.atualizar_listas()
            self.atualizar_listas()
        else:
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione um paciente e um médico.")

# Criação da janela principal
root = tk.Tk()
app = MainWindow(root)
root.mainloop()
