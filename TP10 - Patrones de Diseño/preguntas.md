## Preguntas

**¿Qué problema resuelve Strategy?**
Permite encapsular distintas reglas o algoritmos (descuentos, envíos, promociones) en clases independientes que comparten una misma interfaz, evitando un gran bloque de `if/elif` dentro de la compra. Cada regla se puede probar por separado y se pueden agregar reglas nuevas (como `DescuentoBlackFriday`) sin modificar las existentes (principio abierto/cerrado).

**¿Por qué una compra puede necesitar varias estrategias?**
Porque el precio final depende de reglas de distinta naturaleza que ocurren al mismo tiempo: el tipo de cliente (VIP), la cantidad de productos, una promoción vigente y la forma de entrega. Ninguna reemplaza a las otras, sino que se combinan: por eso la `Compra` mantiene una lista de estrategias y `calcular_precio_final()` las aplica una tras otra.

**¿Qué problema resuelve Chain of Responsibility?**
Desacopla el emisor de una solicitud de quienes la procesan. El pedido pasa por una cadena de handlers donde cada uno tiene una única responsabilidad (cliente, stock, pago) y no conoce los detalles de los demás. Así se puede agregar, quitar o reordenar controles (como `ValidarLimiteCompra`) solo cambiando cómo se arma la cadena.

**¿Qué sucede cuando un elemento de la cadena rechaza el pedido?**
El procesamiento se detiene en ese elemento: no llama al siguiente handler, por lo que las validaciones posteriores no se ejecutan (por ejemplo, si `Validar Stock` falla, nunca se ejecuta `Validar Pago`). El validador que falló muestra "ERROR" y la cadena termina con "Pedido rechazado".

## Desafío

`DescuentoBlackFriday` (nueva estrategia) y `ValidarLimiteCompra` (nuevo validador) están en `desafio.py` y solo **heredan** de las clases existentes (`Descuento` y `Validador`). `estrategias.py` y `cadena.py` no se modificaron: el código original sigue funcionando (`main.py` no cambia) y los nuevos elementos se agregan al armar la compra y la cadena.
