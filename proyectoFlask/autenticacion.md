# Descripción y funcionamiento - Frameworks de autorización y autenticación

## * OAuth:

OAuth 2 es un framework de autorización, que permite a las aplicaciones obtener acceso (limitado) a las cuentas de usuario de determinados servicios, como Facebook, GitHub, Twitter, Steam, BitBucket, LinkedIn y muchos más. Este consiste en delegar la autenticación de usuario al servicio que gestiona las cuentas, de modo que sea éste quien otorgue el acceso para las aplicaciones de terceros.

En el funcionamiento, se desarrolla la siguiente secuencia de pasos:

### * Un usuario entra a nuestra página (digamos que nuestra página se llama PYM), y hace clic en "Ingresar usando Facebook".

### *Nuestra aplicación lo va a redirigir a una URL como la siguiente: facebook.com/oauth2/auth?client_id=ABC&redirect_uri=programacionymas.com/oauth_response

### *Ésta URL contiene los siguientes parámetros: un client_id, una redirect_uri y opcionalmente un parámetro scopes (para indicar a qué información queremos acceder).

### *Facebook primero va a ver si nuestro client_id es válido (comparándolo con la lista de oauth_client permitidos).

### *Si todo está correcto, entonces define una variable de sesión que guarda nuestro client_id y redirect_uri. Y entonces:

### * * Redirige al usuario a facebook.com/login (muestra un formulario de inicio de sesión) si el usuario aún no ha iniciado sesión.
### * * O avanza directamente al siguiente paso si ya hay una sesión activa en Facebook.

### * Facebook muestra el logo de PYM y el nombre de la app (lo reconoce a partir del client_id), indicando al usuario: "Esta app quiere acceder a tus datos de Facebook, ¿le das permiso?" (según el scope indicado previamente).

Al aceptar:

### * Facebook genera un código (que tiene un sólo uso válido para PYM, el usuario en cuestión y el scope solicitado). Facebook redirige al usuario según la redirect_uri indicada al inicio.

### * Es decir, esta redirect_uri es una ruta usada como callback en nuestra aplicación para recibir el permiso otorgado por Facebook y hacer posible el inicio de sesión.

### * Entonces Facebook enviará el código generado hacia la aplicación PYM: programacionymas.com/oauth_response?code=aqui_un_codigo_extenso.

### * PYM toma el código que recibe de Facebook y vuelve a hacer una petición a Facebook, incluyendo ahora su client_secret.

### * Esta última petición no se trata de una redirección a nivel de navegador, sino más bien de una solicitud de servidor a servidor.

### * Para probar su identidad, PYM hace una petición de la siguiente forma: facebook.com/oauth2/token?client_id=ABC&client_secret=XYZ&code=aqui_un_codigo_extenso

### * Facebook verifica que el código sea válido, y así mismo lo invalida en ese instante (recordar que son de uso único).

### * Entonces Facebook responde con un AccessToken, que PYM podrá usar (hasta que expire) para hacer peticiones a la API, en nombre del usuario que ha otorgado los permisos. Por ejemplo, con este token podemos acceder a la información básica del usuario, y usar estos datos para crear una cuenta en nuestra aplicación. Pero un token, dependiendo de la API, nos permite también realizar acciones en nombre del usuario, en función a los permisos otorgados (el parámetro scope usado inicialmente determina los permisos que estamos solicitando al usuario).

## * OpenID:

Es una tecnología centrada en el usuario, basada en el protocolo OAuth, que te permite tener control sobre cómo tu identidad se maneja y se utiliza en línea. Por ser descentralizado, no hay un servidor específico para cada servicio que permite OpenID, al que debas estar registrado, sino que el usuario elige el proveedor donde desea alojar su identidad.

En el funcionamiento, se desarrolla la siguiente secuencia de pasos:

### * Creas una cuenta en un servidor de confianza.

### * Opcionalmente, añades un par de líneas a tu web personal, para poder usarla como identificación.

### * Al entrar en un servicio web que soporte OpenID, introduces la URL de tu perfil OpenID o, si has seguido el paso 2, la URL de tu web personal.

### * Este dato se envía hasta el servidor que elegiste, mostrándote un formulario de entrada en el que tendrás que introducir tu contraseña.

### * Acto seguido, debes autorizar los datos que quieres compartir con el servicio.

### * El servidor devuelve el control al servicio web, que ya conoce quién eres.

La próxima vez que inicies sesión en ese u otro servicio web que acepte OpenID no tendrás que volver a introducir tu contraseña, ya que esos datos se guardarán temporalmente en tu navegador, evitándote más identificaciones innecesarios

## * SAML Authentication:

SAML (Security Assertion Markup Language) es un estándar de código abierto basado en XML que permite el intercambio de información, tanto de autenticación como de autorización entre diferentes partes: un identity provider (proveedor de identidad) y un service provider (proveedor de servicios).

Por un lado, un proveedor de servicios necesita la autenticación del proveedor de identidad para otorgar autorización al usuario. Un proveedor de servicios dependen de un proveedor de identidad para la autenticación del usuario. Por otro lado, un proveedor de identidad realiza la autenticación de que el usuario final es quien dice ser y envía esos datos al proveedor del servicio junto con los derechos de acceso del usuario al servicio.

Así, la autenticación SAML es el proceso por el cual se verifica la identidad y las credenciales del usuario (contraseña, autenticación de dos factores, etc.). La autorización SAML es la que le dice al proveedor de servicios qué acceso otorga al usuario autenticado.

En el funcionamiento, se desarrolla la siguiente secuencia de pasos:

### * Intenta acceder al recurso en el servidor, que, en la terminología de SAML, es un proveedor de servicios. El proveedor de servicios verifica si ya está autenticado dentro del sistema. Si es así, salta al paso 7; si no lo está, el proveedor del servicio inicia el proceso de autenticación.

### * El proveedor del servicio determina el proveedor de identidad apropiado para usted, y lo redirige a ese proveedor -en este caso, el servicio de inicio de sesión único.

### * Su navegador envía una solicitud de autenticación al servicio SSO; el servicio luego lo identifica.

### * El servicio SSO devuelve un documento XHTML, que incluye la información de autenticación que necesita el proveedor de servicios en un parámetro de respuesta de SAML.

### * El parámetro de respuesta de SAML llega al proveedor de servicios.

### * El proveedor de servicios procesa esta respuesta y crea un contexto de seguridad para usted -básicamente, lo registra-, y luego le indica dónde se encuentra el recurso solicitado.

### * Con esta información, ahora puede solicitar el recurso que le interesa nuevamente.

### * El recurso finalmente le es devuelto

