# 🌮 Sistema de Gestión de Tamales (ProgramandoTamales) 🫔

## 📝 Descripción del Proyecto

ProgramandoTamales es una aplicación de consola desarrollada en Python, diseñada para centralizar y simplificar la **gestión de ventas e inventario** en un negocio de tamales con **múltiples puntos de venta (Puestos)**. Permite a los empleados registrar ventas en tiempo real y a los administradores obtener reportes de desempeño y reabastecer el stock.

## ✨ Características Clave

* **Gestión Multi-Puesto:** Manejo de inventario independiente para Puesto 1, Puesto 2 y Puesto Demo (Puesto 3).
* **Roles de Usuario:**
    * **Administrador:** Acceso a reportes de venta, inventario global y reabastecimiento de stock.
    * **Empleado/Vendedor:** Funcionalidad para registrar ventas y consultar el inventario de su puesto.
* **Control de Stock:** Actualización automática del inventario tras cada venta y validación de stock para prevenir ventas con existencias insuficientes.
* **Persistencia de Datos:** El inventario se almacena y actualiza en archivos de texto (`.txt`) específicos para cada puesto, asegurando que los datos se conserven entre sesiones.
* **Reportes de Contabilidad:** El administrador puede calcular las **ventas reales netas** comparando el inventario inicial con el final, permitiendo el manejo de stock sobrante (venta negativa).

## 🚀 Tecnologías Utilizadas

| Tecnología | Descripción |
| :--- | :--- |
| **Python** | Lenguaje de programación principal para la lógica del sistema. |
| **Archivos de Texto (`.txt`)** | Utilizados como base de datos simple para la persistencia del inventario (lectura, parseo, escritura). |
| **Consola/CLI** | Interfaz de usuario básica para la interacción (menus, inputs, outputs). |

## 🛠️ Instalación y Uso

### Requisitos

Necesitas tener Python instalado en tu sistema.
