from abc import ABC, abstractmethod


class CanalConfirmacion(ABC):
    @abstractmethod
    def enviar_confirmacion(self, destinatario: str, mensaje: str) -> None:
        pass

class EmailCanal(CanalConfirmacion):
    def enviar_confirmacion(self, destinatario: str, mensaje: str) -> None:
        print(f"[EMAIL] Enviando email a {destinatario} con mensaje: {mensaje}")
       

class SmsCanal(CanalConfirmacion):
    def enviar_confirmacion(self, destinatario: str, mensaje: str) -> None:
        print(f"[SMS] Enviando SMS a {destinatario} con mensaje: {mensaje}")

class WhatsAppCanal(CanalConfirmacion):
    def enviar_confirmacion(self, destinatario: str, mensaje: str) -> None:
        print(f"[WHATSAPP] Enviando WhatsApp a {destinatario} con mensaje: {mensaje}")

class LlamadaCanal(CanalConfirmacion):
    def enviar_confirmacion(self, destinatario: str, mensaje: str) -> None:
        print(f"[LLAMADA] Realizando llamada a {destinatario} con mensaje: {mensaje}")


class FabricaCanalesConfirmacion:
    @staticmethod
    def crear_canal(tipo: str) -> CanalConfirmacion:
        tipo_normalizado = tipo.lower()
        if tipo_normalizado == "email":
            return EmailCanal()
        if tipo_normalizado == "sms":
            return SmsCanal()
        if tipo_normalizado == "whatsapp":
            return WhatsAppCanal()
        if tipo_normalizado == "llamada":
            return LlamadaCanal()
        raise ValueError(f"Tipo de canal desconocido: {tipo}")


class AgendaMedica:
    def __init__(self) -> None:
        self.horarios_disponibles = {
            "2026-05-10 09:00",
            "2026-05-10 11:00",
            "2026-05-11 16:00",
            "2026-05-12 18:00",
        }

    def horario_disponible(self, horario: str) -> bool:
        print(f"Revisando disponibilidad para {horario}...")
        return horario in self.horarios_disponibles

    def apartar_horario(self, horario: str) -> None:
        self.horarios_disponibles.remove(horario)
        print(f"Horario {horario} apartado correctamente.")

class RegistroCitas:
    def __init__(self) -> None:
        self.citas: list[dict[str, str]] = []

    def registrar(self, paciente: str, medico: str, horario: str) -> str:
        folio = f"CITA-{len(self.citas) + 1:03d}"
        self.citas.append(
            {
                "folio": folio,
                "paciente": paciente,
                "medico": medico,
                "horario": horario,
            }
        )
        print(f"Cita {folio} registrada para {paciente} con {medico} en {horario}.")
        return folio

class ServicioRecordatorios:
    def preparar_mensaje(
        self, paciente: str, medico: str, horario: str, folio: str
    ) -> str:
        return f"Hola {paciente}, tu cita {folio} con {medico} fue agendada para {horario}."


class AgendamientoFacade:
    def __init__(
        self,
        agenda: AgendaMedica,
        registro: RegistroCitas,
        recordatorios: ServicioRecordatorios,
    ) -> None:
        self.agenda = agenda
        self.registro = registro
        self.recordatorios = recordatorios

    def agendar_cita(
        self,
        paciente: str,
        contacto: str,
        medico: str,
        horario: str,
        canal: CanalConfirmacion,
    ) -> str:  
       
        if not self.agenda.horario_disponible(horario):
            raise ValueError(f"Horario no disponible: {horario}")
        
        self.agenda.apartar_horario(horario)
        folio = self.registro.registrar(paciente, medico, horario)
        mensaje = self.recordatorios.preparar_mensaje(paciente, medico, horario, folio)
        canal.enviar_confirmacion(contacto, mensaje)
        
        print(f"Cita agendada exitosamente para {paciente}.")
        return folio


def main() -> None:
    agenda = AgendaMedica()
    registro = RegistroCitas()
    recordatorios = ServicioRecordatorios()

    # Fachada
    fachada = AgendamientoFacade(agenda, registro, recordatorios)

    # Canales
    canal_email = FabricaCanalesConfirmacion.crear_canal("email")
    canal_sms = FabricaCanalesConfirmacion.crear_canal("sms")

    # Pruebas
    try:
        fachada.agendar_cita(
            "Ana Torres",
            "ana@correo.com",
            "Dra. Ruiz",
            "2026-05-10 09:00",
            canal_email,
        )
        print("-" * 30)
        fachada.agendar_cita(
            "Luis Perez",
            "+5215551234567",
            "Dr. Mora",
            "2026-05-10 11:00",
            canal_sms,
        )
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()