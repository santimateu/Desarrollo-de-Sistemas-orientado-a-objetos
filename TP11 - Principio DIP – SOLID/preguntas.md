# Respuestas - TP11: Principio de Inversión de Dependencias (DIP)

## Parte 1 – Implementación inicial

**¿Qué sucede si queremos enviar mensajes por WhatsApp?**
No se puede sin tocar el código existente. `NotificacionService` crea adentro suyo un `EmailService` y llama a `enviar_email()`, así que solo sabe mandar correos. Para usar WhatsApp habría que crear una clase `WhatsAppService` y cambiar el servicio para que la use (o agregar un `if` para elegir entre email y WhatsApp).

**¿Qué clase deberíamos modificar?**
`NotificacionService`, que es la lógica principal del sistema. Habría que cambiar su constructor (que hace `EmailService()`) y su método `notificar()` (que llama a `enviar_email()`). Lo mismo pasaría cada vez que se agregue un canal nuevo (SMS, push, etc.).

**¿Qué problema presenta este diseño?**
- **Alto acoplamiento**: la clase de alto nivel (`NotificacionService`) depende de una clase concreta de bajo nivel (`EmailService`).
- **Viola OCP**: para extender el sistema hay que modificar una clase que ya funciona, con riesgo de romperla.
- **Difícil de probar**: no se puede reemplazar `EmailService` por un objeto falso en los tests porque se crea adentro del servicio.
- **Crecimiento con `if`**: si se agregan canales, el servicio termina lleno de condicionales para decidir qué canal usar.

## Parte 4 – Análisis conceptual

**¿Qué establece el principio DIP de SOLID?**
Dice dos cosas: (1) los módulos de alto nivel no deben depender de módulos de bajo nivel; ambos deben depender de abstracciones. (2) Las abstracciones no deben depender de los detalles; los detalles deben depender de las abstracciones. En este TP, `NotificacionService` (alto nivel) y `Email`, `SMS`, `WhatsApp`, `Push` (bajo nivel) dependen todos de `Mensajeria`.

**¿Qué diferencia existe entre depender de una clase concreta y depender de una interfaz?**
Depender de una clase concreta ata el código a una única implementación: si esa clase cambia o se quiere usar otra, hay que modificar el código que la usa. Depender de una interfaz significa depender solo de un "contrato" (qué métodos existen, por ejemplo `enviar(mensaje)`), sin importar quién lo cumple. Así cualquier clase que implemente la interfaz se puede usar en su lugar.

**¿Qué es la inyección de dependencias?**
Es una técnica en la que un objeto no crea sus propias dependencias, sino que se las entregan desde afuera (por constructor, por un método o por un atributo). En el TP, `NotificacionService` no hace `Email()`: el `main.py` crea el canal y se lo pasa al servicio. Es la forma práctica de aplicar DIP.

**¿Qué ventajas tiene utilizar inyección por constructor?**
- El objeto queda **completo y válido desde que se crea**: no puede existir un `NotificacionService` sin canal.
- Las dependencias quedan **explícitas** en la firma del constructor; se ve enseguida qué necesita la clase.
- Permite que la dependencia sea **fija** (no se cambia después por accidente).
- Facilita los **tests**: se puede pasar un objeto falso (mock) que implemente `Mensajeria`.

**¿Por qué el diseño desarrollado facilita agregar nuevas funcionalidades?**
Porque para agregar un canal nuevo alcanza con crear una clase que herede de `Mensajeria` e implemente `enviar()`. No se toca `NotificacionService` ni los canales existentes. Eso se demostró en la Parte 3: `Push` está en un archivo nuevo (`push.py`) y el servicio funcionó sin ningún cambio.

**¿Qué relación existe entre DIP y el principio Open/Closed (OCP)?**
OCP dice que el código debe estar abierto a la extensión pero cerrado a la modificación. DIP es lo que hace posible cumplirlo: como `NotificacionService` depende de la abstracción `Mensajeria`, queda "cerrado" (no se modifica) y el sistema queda "abierto" porque se extiende agregando nuevas implementaciones. Sin DIP (Parte 1), extender el sistema obligaba a modificar la clase principal, violando OCP.
