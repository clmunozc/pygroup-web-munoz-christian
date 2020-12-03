# Descripción - Protocolo HTTP

## Peticiones 

Las peticiones son las estandarizaciones implementadas en la aplicación web de las distintas acciones de los usuarios sobre los elementos del sitio y los datos que ingresa, estos pueden ser de distintos tipos que referencian el propósito de la petición, algunos de los tipos más usados son:


### * GET:

El método GET significa recuperar cualquier información identificada por el Request-URI. Si el Request-URI se refiere a un proceso de producción de datos, son los datos producidos los que se devolverán como entidad en la respuesta.

### * POST:

El método POST es utilizado cuando se quiere enviar una determinada información ingresada por el usuario al servidor web, esto cuando se requiere enviar alguna entidad de datos para ser usada como recurso del sitio web en distintos escenarios.

### * PUT:

El método PUT se usa para indicar cuando se solicita al servidor almacenar una entidad de información en una ubicación específica, la diferencia de este y el método POST es que este método es idempotente, es decir, que una petición de tipo PUT obtiene el mismo resultado sin importar las veces que se envíe.

### * DELETE:

El método DELETE sirve cuando se quiere eliminar una entidad de datos en una ubicación específica del servidor.

## Respuestas

Las respuestas son la salida del sitio web con respecto a una petición anteriormente recibida, las distintas respuestas posibles se clasifican por códigos según su tipo de respuesta, los códigos más importantes son:

### * Respuestas informativas (100-199)

	* 100	Continue: Indica que no hay errores hasta el momento y que el cliente puede continuar con la solicitud o ignorarla

	* 101	Switching Protocol: Responde a una peticion Upgrade e indica que el servidor acepta el cambio de protocolo

### * Respuestas satisfactorias (200-299)

	* 200	OK: Indica solicitud exitosa

	* 201	Created: Responde a la solicitud de creación de un recurso e indica solicitud exitosa 

### * Redirecciones (300-399)

	* 301	Moved Permanently: Indica que la URI del recurso solicitado ha sido cambiado

	* 302	Found: Indica que la URI del recurso solicitado ha sido cambiada temporalmente

### * Errores de los clientes (400-499)

	* 403	Forbidden: Indica que se ha hecho una solicitud que requiere más permisos que los del cliente para ser aceptada

	* 404	Not Found: Indica que no se ha encontrado el recurso solicitado en la URI especificada

### * Errores de los servidores (500-599)

	* 500	Internal Server Error: Indica que, durante la solicitud, el servidor ha enfrentado una situación imprevista

	* 502	Bad Gateway: Indica que el servidor obtuvo una respuesta invalida al actuar como puerta de enlace para recibir una respuesta necesaria



