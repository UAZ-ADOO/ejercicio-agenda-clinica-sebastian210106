from abc import ABC, abstractmethod


class CanalConfirmacion(ABC):
    @abstractmethod
    def enviar_confirmacion(self, destinatario: str, mensaje: str) -> None:
        pass


class EmailCanal(CanalConfirmacion):
    def enviar_confirmacion(self, destinatario: str, mensaje: str) -> None:
        # TODO: implementar envio por email.
        raise NotImplementedError("Checkpoint 1: implementa el canal de email.")


class SmsCanal(CanalConfirmacion):
    def enviar_confirmacion(self, destinatario: str, mensaje: str) -> None:
        # TODO: implementar envio por SMS.
        raise NotImplementedError("Checkpoint 1: implementa el canal de SMS.")


class WhatsAppCanal(CanalConfirmacion):
    def enviar_confirmacion(self, destinatario: str, mensaje: str) -> None:
        # TODO: implementar envio por WhatsApp.
        raise NotImplementedError("Checkpoint 1: implementa el canal de WhatsApp.")


class LlamadaCanal(CanalConfirmacion):
    def enviar_confirmacion(self, destinatario: str, mensaje: str) -> None:
        # TODO: implementar envio por llamada automatizada.
        raise NotImplementedError("Checkpoint 1: implementa el canal de llamada.")


class FabricaCanalesConfirmacion:
    @staticmethod
    def crear_canal(tipo: str) -> CanalConfirmacion:
        # TODO: regresar el canal correcto segun el tipo recibido.
        raise NotImplementedError("Checkpoint 2: implementa la fabrica de canales.")


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
        self,
        paciente: str,
        medico: str,
        horario: str,
        folio: str,
    ) -> str:
        return (
            f"Hola {paciente}, tu cita {folio} con {medico} fue agendada para {horario}."
        )


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
    ) -> None:
        # TODO: validar disponibilidad, registrar y confirmar la cita.
        raise NotImplementedError("Checkpoint 3: completa la fachada de agendamiento.")


def main() -> None:
    agenda = AgendaMedica()
    registro = RegistroCitas()
    recordatorios = ServicioRecordatorios()

    fachada = AgendamientoFacade(agenda, registro, recordatorios)

    canal_email = FabricaCanalesConfirmacion.crear_canal("email")
    canal_sms = FabricaCanalesConfirmacion.crear_canal("sms")
    canal_whatsapp = FabricaCanalesConfirmacion.crear_canal("whatsapp")
    canal_llamada = FabricaCanalesConfirmacion.crear_canal("llamada")

    fachada.agendar_cita(
        "Ana Torres",
        "ana@correo.com",
        "Dra. Ruiz",
        "2026-05-10 09:00",
        canal_email,
    )
    print()
    fachada.agendar_cita(
        "Luis Perez",
        "+5215551234567",
        "Dr. Mora",
        "2026-05-10 11:00",
        canal_sms,
    )
    print()
    fachada.agendar_cita(
        "Carla Diaz",
        "+5215559876543",
        "Dra. Vega",
        "2026-05-11 16:00",
        canal_whatsapp,
    )
    print()
    fachada.agendar_cita(
        "Rosa Medina",
        "555-0101",
        "Dr. Lara",
        "2026-05-12 18:00",
        canal_llamada,
    )


if __name__ == "__main__":
    main()
