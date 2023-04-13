# Gameda Games

<img src="../images/logo.png" width = "100px">


## Índice
- [Introducción](#introducción).
- [Descripción](#descripción).
- [Diagrama de Casos de Uso](#diagrama-de-casos-de-uso).
- [Especificación de Actores](#especificación-de-actores).
- [Especificación de Casos de Uso](#especificación-de-casos-de-uso).

### Introducción

El presente documento especifica el __diagrama de casos de uso__ de la aplicación Gameda Games solicitada por varias empresas que se encargan de la venta de productos relacionados al mundo de los videojuegos. Este documento trata a grandes rasgos, el diagrama de casos de uso, los casos de uso identificados, así como los actores que intervienen en ellos.

### Descripción

El objetivo es realizar una aplicación con la que gestionar los productos que se venden en la tienda, la venta de los mismos y aquellas personas que trabajan para la empresa.

### Diagrama de Casos de Uso

<img src="../images/diagrama-casos-uso.png">

### Especificación de Actores

En el presente documento se realiza la especificación de los diferentes actores que intervienen en la solución propuesta.

#### Empleado

| Actor | Empleado |
|---|---|
| Descripción  | El empleado podrá realizar las tareas comunes de un sistema de estas características, gestionar ventas, gestionar productos, etc.  |
| Características  | Comparte casos de uso con el actor "Encargado" |
| Relaciones | - |
| Referencias | Autenticarse, Gestionar Venta, Listar Venta, Realizar Venta, Gestionar Cliente, Insertar Cliente, Modificar Cliente, Eliminar Cliente, Listar Cliente, Gestionar Producto, Insertar Producto, Modificar Producto, Eliminar Producto, Listar Producto.  |   
|  Notas | - |
| Autor  | _Abián Gustavo Castañeda Méndez y Diego Peraza Cabo_ |
|Fecha | _30/03/2023_ |

#### Encargado

| Actor | Encargado |
|---|---|
  | Descripción  | El encargado podrá realizar las mismas acciones que el empleado pero tendrá acceso a la supervisión de sus trabajadores mediante la "Gestionar Empleado". |
  | Características  | Comparte casos de uso con el actor "Empleado". |
  | Relaciones | El encargado puede hacer todas las acciones que realiza el actor "Empleado".  |
  | Referencias | Autenticarse, Gestionar Venta, Listar Venta, Realizar Venta, Gestionar Cliente, Insertar Cliente, Modificar Cliente, Eliminar Cliente, Listar Cliente, Gestionar Producto, Insertar Producto, Modificar Producto, Eliminar Producto, Listar Producto, Gestionar Empleado, Listar Empleado, Eliminar Empleado, Modificar Empleado, Insertar Empleado.  |   
  |  Notas | - |
  | Autor  | _Abián Gustavo Castañeda Méndez y Diego Peraza Cabo_ |
  |Fecha | _30/03/2023_ |

### Especificación de Casos de Uso

#### Autenticarse

|  Caso de Uso	CU.1 | Autenticarse |
|---|---|
| Fuentes  | El caso de uso se sustenta en [este documento](https://github.com/AbianGustavo/proyecto-ets/blob/feature_10/doc/diagrama-casos-uso.md).|
| Actor  | Empleado, Encargado |
| Descripción | Tanto el empleado como el encargado deben autenticarse antes de poder realizar alguna de las acciones. |
| Flujo básico | - |
| Pre-condiciones | - |  
| Post-condiciones  | - |  
|  Requerimientos | - |
|  Notas | - |
| Autor  | _Abián Gustavo Castañeda Méndez y Diego Peraza Cabo_ |
|Fecha | _30/03/2023_ |

#### Gestionar Venta

|  Caso de Uso	CU.2 | Gestionar Venta |
|---|---|
| Fuentes  | El caso de uso se sustenta en [este documento](https://github.com/AbianGustavo/proyecto-ets/blob/feature_10/doc/diagrama-casos-uso.md).|
| Actor  | Empleado, Encargado |
| Descripción | Tanto el empleado como el encargado podrán gestionar todo lo relacionado a las ventas. |
| Flujo básico | Autenticarse --> Gestionar Venta |
| Pre-condiciones | - |  
| Post-condiciones  | - |  
|  Requerimientos | Haberse autenticado. |
|  Notas | - |
| Autor  | _Abián Gustavo Castañeda Méndez y Diego Peraza Cabo_ |
|Fecha | _30/03/2023_ |

#### Listar Venta

|  Caso de Uso	CU.3 | Listar Venta |
|---|---|
| Fuentes  | El caso de uso se sustenta en [este documento](https://github.com/AbianGustavo/proyecto-ets/blob/feature_10/doc/diagrama-casos-uso.md).|
| Actor  | Empleado, Encargado |
| Descripción | Tanto el empleado como el encargado podrán listar y comprobar las ventas que se hayan realizado. |
| Flujo básico | Autenticarse --> Gestionar Venta --> Listar Venta |
| Pre-condiciones | - |  
| Post-condiciones  | - |  
|  Requerimientos | Haber seleccionado "Gestionar Venta" y autenticarse. |
|  Notas | - |
| Autor  | _Abián Gustavo Castañeda Méndez y Diego Peraza Cabo_ |
|Fecha | _30/03/2023_ |


#### Realizar Venta

|  Caso de Uso	CU.4 | Realizar Venta |
|---|---|
| Fuentes  | El caso de uso se sustenta en [este documento](https://github.com/AbianGustavo/proyecto-ets/blob/feature_10/doc/diagrama-casos-uso.md).|
| Actor  | Empleado, Encargado |
| Descripción | Tanto el empleado como el encargado podrán realizar ventas. |
| Flujo básico | Autenticarse --> Gestionar Venta --> Realizar Venta |
| Pre-condiciones | - |  
| Post-condiciones  | - |  
|  Requerimientos | Haber seleccionado "Gestionar Venta" y autenticarse. |
|  Notas | - |
| Autor  | _Abián Gustavo Castañeda Méndez y Diego Peraza Cabo_ |
|Fecha | _30/03/2023_ |

#### Gestionar Cliente

|  Caso de Uso	CU.5 | Gestionar Cliente |
|---|---|
| Fuentes  | El caso de uso se sustenta en [este documento](https://github.com/AbianGustavo/proyecto-ets/blob/feature_10/doc/diagrama-casos-uso.md).|
| Actor  | Empleado, Encargado |
| Descripción | Tanto el empleado como el encargado podrán gestionar todo lo realizado a sus clientes. |
| Flujo básico | Autenticarse --> Gestionar Cliente |
| Pre-condiciones | - |  
| Post-condiciones  | - |  
|  Requerimientos | Haberse autenticado. |
|  Notas | - |
| Autor  | _Abián Gustavo Castañeda Méndez y Diego Peraza Cabo_ |
|Fecha | _30/03/2023_ |

#### Insertar Cliente

|  Caso de Uso	CU.6 | Insertar Cliente |
|---|---|
| Fuentes  | El caso de uso se sustenta en [este documento](https://github.com/AbianGustavo/proyecto-ets/blob/feature_10/doc/diagrama-casos-uso.md).|
| Actor  | Empleado, Encargado |
| Descripción | Tanto el empleado como el encargado podrán insertar en el sistema nuevos clientes y sus datos. |
| Flujo básico | Autenticarse --> Gestionar Cliente --> Insertar Cliente |
| Pre-condiciones | - |  
| Post-condiciones  | - |  
|  Requerimientos | Haber seleccionado "Gestionar Cliente" y autenticarse. |
|  Notas | - |
| Autor  | _Abián Gustavo Castañeda Méndez y Diego Peraza Cabo_ |
|Fecha | _30/03/2023_ |

#### Modificar Cliente

|  Caso de Uso	CU.7 | Modificar Cliente |
|---|---|
| Fuentes  | El caso de uso se sustenta en [este documento](https://github.com/AbianGustavo/proyecto-ets/blob/feature_10/doc/diagrama-casos-uso.md).|
| Actor  | Empleado, Encargado |
| Descripción | Tanto el empleado como el encargado podrán modificar en el sistema la información de sus clientes. |
| Flujo básico | Autenticarse --> Gestionar Cliente --> Modificar Cliente |
| Pre-condiciones | - |  
| Post-condiciones  | - |  
|  Requerimientos | Haber seleccionado "Gestionar Cliente" y autenticarse. |
|  Notas | - |
| Autor  | _Abián Gustavo Castañeda Méndez y Diego Peraza Cabo_ |
|Fecha | _30/03/2023_ |

#### Eliminar Cliente

|  Caso de Uso	CU.8 | Eliminar Cliente |
|---|---|
| Fuentes  | El caso de uso se sustenta en [este documento](https://github.com/AbianGustavo/proyecto-ets/blob/feature_10/doc/diagrama-casos-uso.md).|
| Actor  | Empleado, Encargado |
| Descripción | Tanto el empleado como el encargado podrán eliminar en el sistema clientes y sus datos. |
| Flujo básico | Autenticarse --> Gestionar Cliente --> Eliminar Cliente |
| Pre-condiciones | - |  
| Post-condiciones  | - |  
|  Requerimientos | Haber seleccionado "Gestionar Cliente" y autenticarse. |
|  Notas | - |
| Autor  | _Abián Gustavo Castañeda Méndez y Diego Peraza Cabo_ |
|Fecha | _30/03/2023_ |

#### Listar Cliente

|  Caso de Uso	CU.9 | Listar Cliente |
|---|---|
| Fuentes  | El caso de uso se sustenta en [este documento](https://github.com/AbianGustavo/proyecto-ets/blob/feature_10/doc/diagrama-casos-uso.md).|
| Actor  | Empleado, Encargado |
| Descripción | Tanto el empleado como el encargado podrán listar en el sistema a sus clientes y datos. |
| Flujo básico | Autenticarse --> Gestionar Cliente --> Listar Cliente |
| Pre-condiciones | - |  
| Post-condiciones  | - |  
|  Requerimientos | Haber seleccionado "Gestionar Cliente" y autenticarse. |
|  Notas | - |
| Autor  | _Abián Gustavo Castañeda Méndez y Diego Peraza Cabo_ |
|Fecha | _30/03/2023_ |

#### Gestionar Producto

|  Caso de Uso	CU.10 | Gestionar Producto |
|---|---|
| Fuentes  | El caso de uso se sustenta en [este documento](https://github.com/AbianGustavo/proyecto-ets/blob/feature_10/doc/diagrama-casos-uso.md).|
| Actor  | Empleado, Encargado |
| Descripción | Tanto el empleado como el encargado podrán gestionar todo lo realizado a sus productos. |
| Flujo básico | Autenticarse --> Gestionar Producto |
| Pre-condiciones | - |  
| Post-condiciones  | - |  
|  Requerimientos | Haberse autenticado. |
|  Notas | - |
| Autor  | _Abián Gustavo Castañeda Méndez y Diego Peraza Cabo_ |
|Fecha | _30/03/2023_ |

#### Insertar Producto

|  Caso de Uso	CU.11 | Insertar Producto |
|---|---|
| Fuentes  | El caso de uso se sustenta en [este documento](https://github.com/AbianGustavo/proyecto-ets/blob/feature_10/doc/diagrama-casos-uso.md).|
| Actor  | Empleado, Encargado |
| Descripción | Tanto el empleado como el encargado podrán insertar en el sistema nuevos productos. |
| Flujo básico | Autenticarse --> Gestionar Producto --> Insertar Producto|
| Pre-condiciones | - |  
| Post-condiciones  | - |  
|  Requerimientos | Haber seleccionado "Gestionar Producto" y autenticarse. |
|  Notas | - |
| Autor  | _Abián Gustavo Castañeda Méndez y Diego Peraza Cabo_ |
|Fecha | _30/03/2023_ |

#### Modificar Producto

|  Caso de Uso	CU.12 | Modificar Producto |
|---|---|
| Fuentes  | El caso de uso se sustenta en [este documento](https://github.com/AbianGustavo/proyecto-ets/blob/feature_10/doc/diagrama-casos-uso.md).|
| Actor  | Empleado, Encargado |
| Descripción | Tanto el empleado como el encargado podrán modificar los productos que hay en el sistema. |
| Flujo básico | Autenticarse --> Gestionar Producto --> Modificar Producto|
| Pre-condiciones | - |  
| Post-condiciones  | - |  
|  Requerimientos | Haber seleccionado "Gestionar Producto" y autenticarse. |
|  Notas | - |
| Autor  | _Abián Gustavo Castañeda Méndez y Diego Peraza Cabo_ |
|Fecha | _30/03/2023_ |

#### Listar Producto

|  Caso de Uso	CU.13 | Listar Producto |
|---|---|
| Fuentes  | El caso de uso se sustenta en [este documento](https://github.com/AbianGustavo/proyecto-ets/blob/feature_10/doc/diagrama-casos-uso.md).|
| Actor  | Empleado, Encargado |
| Descripción | Tanto el empleado como el encargado podrán listar los productos que hay en el sistema. |
| Flujo básico | Autenticarse --> Gestionar Producto --> Listar Producto|
| Pre-condiciones | - |  
| Post-condiciones  | - |  
|  Requerimientos | Haber seleccionado "Gestionar Producto" y autenticarse. |
|  Notas | - |
| Autor  | _Abián Gustavo Castañeda Méndez y Diego Peraza Cabo_ |
|Fecha | _30/03/2023_ |

#### Eliminar Producto

|  Caso de Uso	CU.14 | Eliminar Producto |
|---|---|
| Fuentes  | El caso de uso se sustenta en [este documento](https://github.com/AbianGustavo/proyecto-ets/blob/feature_10/doc/diagrama-casos-uso.md).|
| Actor  | Empleado, Encargado |
| Descripción | Tanto el empleado como el encargado podrán eliminar los productos que hay en el sistema. |
| Flujo básico | Autenticarse --> Gestionar Producto --> Eliminar Producto |
| Pre-condiciones | - |  
| Post-condiciones  | - |  
|  Requerimientos | Haber seleccionado "Gestionar Producto" y autenticarse. |
|  Notas | - |
| Autor  | _Abián Gustavo Castañeda Méndez y Diego Peraza Cabo_ |
|Fecha | _30/03/2023_ |

#### Gestionar Empleado

|  Caso de Uso    CU.15 | Gestionar Empleado |
|---|---|
| Fuentes  | El caso de uso se sustenta en [este documento](https://github.com/AbianGustavo/proyecto-ets/blob/feature_10/doc/diagrama-casos-uso.md).|
| Actor  | Encargado |
| Descripción | El encargado podrá gestionar todo lo relacionado a sus empleados. |
| Flujo básico | Autenticarse --> Gestionar Empleado |
| Pre-condiciones | - |
| Post-condiciones  | - |
|  Requerimientos | Haberse autenticado. |
|  Notas | - |
| Autor  | _Abián Gustavo Castañeda Méndez y Diego Peraza Cabo_ |
|Fecha | _30/03/2023_ |

#### Listar Empleado

|  Caso de Uso    CU.16 | Listar Empleado |
|---|---|
| Fuentes  | El caso de uso se sustenta en [este documento](https://github.com/AbianGustavo/proyecto-ets/blob/feature_10/doc/diagrama-casos-uso.md).|
| Actor  | Encargado |
| Descripción | El encargado podrá listar a sus empleados y sus datos. |
| Flujo básico | Autenticarse --> Gestionar Empleado --> Listar Empleado |
| Pre-condiciones | - |
| Post-condiciones  | - |
|  Requerimientos | Haber seleccionado "Gestionar Empleado" y autenticarse. |
|  Notas | - |
| Autor  | _Abián Gustavo Castañeda Méndez y Diego Peraza Cabo_ |
|Fecha | _30/03/2023_ |

#### Eliminar Empleado

|  Caso de Uso    CU.17 | Eliminar Empleado |
|---|---|
| Fuentes  | El caso de uso se sustenta en [este documento](https://github.com/AbianGustavo/proyecto-ets/blob/feature_10/doc/diagrama-casos-uso.md).|
| Actor  | Encargado |
| Descripción | El encargado podrá eliminar empleados y sus datos. |
| Flujo básico | Autenticarse --> Gestionar Empleado --> Eliminar Empleado |
| Pre-condiciones | - |
| Post-condiciones  | - |
|  Requerimientos | Haber seleccionado "Gestionar Empleado" y autenticarse. |
|  Notas | - |
| Autor  | _Abián Gustavo Castañeda Méndez y Diego Peraza Cabo_ |
|Fecha | _30/03/2023_ |

#### Modificar Empleado

|  Caso de Uso    CU.18 | Modificar Empleado |
|---|---|
| Fuentes  | El caso de uso se sustenta en [este documento](https://github.com/AbianGustavo/proyecto-ets/blob/feature_10/doc/diagrama-casos-uso.md).|
| Actor  | Encargado |
| Descripción | El encargado podrá modificar la información de sus empleados. |
| Flujo básico | Autenticarse --> Gestionar Empleado --> Modificar Empleado |
| Pre-condiciones | - |
| Post-condiciones  | - |
|  Requerimientos | Haber seleccionado "Gestionar Empleado" y autenticarse. |
|  Notas | - |
| Autor  | _Abián Gustavo Castañeda Méndez y Diego Peraza Cabo_ |
|Fecha | _30/03/2023_ |

#### Insertar Empleado

|  Caso de Uso    CU.19 | Insertar Empleado |
|---|---|
| Fuentes  | El caso de uso se sustenta en [este documento](https://github.com/AbianGustavo/proyecto-ets/blob/feature_10/doc/diagrama-casos-uso.md).|
| Actor  | Encargado |
| Descripción | El encargado podrá insertar nuevos empleados y sus datos. |
| Flujo básico | Autenticarse --> Gestionar Empleado --> Insertar Empleado |
| Pre-condiciones | - |
| Post-condiciones  | - |
|  Requerimientos | Haber seleccionado "Gestionar Empleado" y autenticarse. |
|  Notas | - |
| Autor  | _Abián Gustavo Castañeda Méndez y Diego Peraza Cabo_ |
|Fecha | _30/03/2023_ |
