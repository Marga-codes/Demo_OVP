# Guía de Estilos — Rediseño Web OVP (Concepto)

- **Preparado por:** Marga Mbande
- **Fecha:** 26 de agosto de 2026
- **Fuente de marca:** OVP Logo Guideline, versión 1.0, 6 de septiembre de 2017 (documento oficial del cliente)
- **Propósito:** reunir en un solo documento las reglas de marca oficiales de OVP y las decisiones de diseño tomadas en la demo del rediseño, para poder (1) mantener consistencia al seguir iterando el diseño, (2) darle a cualquier IA de diseño (Fable, Stitch, opencode) instrucciones coherentes, y (3) explicar al cliente con seguridad por qué cada decisión se tomó así.

---

## 1. Paleta de color oficial

Estos son los tres únicos colores de marca definidos en el documento oficial de OVP. No se añaden colores nuevos: toda la paleta "extendida" de la demo (fondos claros/oscuros, grises de texto) se construye como variaciones de neutro alrededor de estos tres, nunca sustituyéndolos.

| Muestra | Nombre | HEX | RGB | CMYK |
| --- | --- | --- | --- | --- |
| 🟢 | Verde OVP | `#00B700` | 0, 183, 0 | 79%, 0%, 100%, 0% |
| 🔵 | Azul OVP | `#7AE3FC` | 122, 227, 252 | 42%, 0%, 3%, 0% |
| ⚪ | Gris OVP | `#848484` | 132, 132, 132 | 51%, 42%, 42%, 6% |

## 2. Cómo se usa cada color en la interfaz

| Color de marca | Uso en la demo (rol de UI) | Motivo |
| --- | --- | --- |
| Verde `#00B700` | Acento principal: enlaces activos, botones primarios (CTA), subrayados de foco, iconografía de check/aprobado. | Es el color más reconocible de la marca; se reserva para acciones y puntos de máxima atención, **nunca como fondo extenso** (fatiga visual). |
| Azul `#7AE3FC` | Acento secundario: chips de credenciales (sector público), detalles decorativos, estados "pending" en la franja de gobierno, gráficos de datos. | Aporta variedad sin competir con el verde; funciona bien sobre fondos oscuros (franja "gov-band"), coherente con estética de confianza/tecnología. |
| Gris `#848484` | Texto secundario, etiquetas ("eyebrow"), bordes, fondos neutros de tarjetas. | Es el color de marca menos saturado; ideal para jerarquía tipográfica sin introducir un color nuevo no oficial. |

**Regla práctica:** si dudas qué color usar en un elemento nuevo, por defecto usa gris para texto/estructura y reserva el verde para una sola acción por pantalla (el CTA principal). Evita usar verde y azul juntos en un mismo bloque pequeño: en la marca no aparecen combinados, y generar demasiado contraste de color entre ellos puede leerse como no oficial.

## 3. Tipografía

| Uso | Tipografía oficial de marca | Sustituto usado en la demo digital |
| --- | --- | --- |
| Texto general / titulares | Proxima Nova Light | Work Sans (Google Fonts) — grotesca geométrica de peso ligero, la alternativa gratuita más cercana al carácter de Proxima Nova. |
| Acento / display | Monoton | No utilizada en la demo — Monoton es muy decorativa (estilo neón/retro) y no es legible en textos de negocio; se sustituyó su función de "acento" por IBM Plex Mono en mayúsculas, usada solo en etiquetas cortas y datos. |
| Etiquetas / datos | — (no especificada) | IBM Plex Mono — añadida para dar un aire técnico/"panel de control" a cifras, kickers y credenciales, en línea con referencias del cliente (Guidehouse). |

**Nota importante sobre licencias:** Proxima Nova es una fuente comercial (no está en Google Fonts). Si OVP puede facilitar el archivo con licencia de uso web (por ejemplo, vía Adobe Fonts o Fontspring), se debe sustituir Work Sans por Proxima Nova real antes de pasar a producción. La demo usa Work Sans únicamente como aproximación visual honesta, declarada así en el propio prototipo, nunca de forma oculta.

## 4. Reglas de uso del logotipo

Tal y como se especifica en la guía oficial de OVP, el logotipo tiene versiones para distintos fondos (a color, sobre fondo de color, en "knockout"/blanco, y en versión insignia/badge) y **no debe alterarse**:

- Sin patrones detrás del logotipo.
- Sin distorsión ni inclinación (skew).
- Sin alteraciones de color.
- Sin gradientes.
- Sin rotación.

**Estado actual en la demo:** el logotipo oficial ya está incorporado (`assets/OVP-mark.png`), extraído del archivo de marca del cliente (`assets/OVPLogoRGB.jpg`) y recortado con fondo transparente para uso web, conservando los colores oficiales exactos (verde `#00B700` y azul `#7AE3FC`). El texto "Management Consulting Group" se sigue renderizando como texto real en el HTML junto al isotipo, nunca incrustado en la imagen, para que siga siendo seleccionable y accesible. Las fotografías del equipo y de la galería también son ya reales, facilitadas por el cliente.

## 5. Estructura y patrones de la demo (Main.dc.html)

La demo sigue un orden de secciones pensado para un comprador de perfil gobierno/enterprise, siguiendo la recomendación de combinar los cinco sitios de referencia del cliente (Eagle Hill, Fors Marsh, MGT, Guidehouse, NSP & Co.):

1. Cinta de aviso superior — deja explícito que es un concepto con copy real pero fotos/logo pendientes de OVP.
2. Navegación fija con marca.
3. Hero con la declaración de misión real de OVP (sin titulares inventados).
4. Franja de "engagements" con nombres reales de clientes (sin casos de éxito ficticios).
5. Servicios — las descripciones reales y verbatim, con un aviso aparte, de borde discontinuo, aclarando qué partes son propuesta propia y no contenido actual del cliente.
6. Franja oscura "Built for public-sector & strategic-partner buyers" con credenciales marcadas como "pending" (no certificaciones inventadas).
7. Equipo — biografías reales, con marcadores de foto pendientes.
8. Testimonios — citas reales y verbatim.
9. Franja de confianza/seguridad y pie de página con crédito y nota de sustitución de tipografía/paleta.

**Convención de marcadores (placeholders):** cualquier elemento que falte (logo, fotos) se muestra como una caja con icono + leyenda explicativa, nunca como texto entre corchetes tipo `[TBD]` ni como un hueco vacío — así el cliente entiende de un vistazo qué falta y por qué, sin que parezca un error.

**Patrón de contraste (franja oscura):** la franja "gov-band" usa un juego de tokens de color fijos (fondo/texto/borde de contraste) que no cambian con el modo claro/oscuro del navegador, para garantizar que el texto siga siendo legible en ambos modos. Si se añaden más secciones de fondo oscuro, se reutiliza este mismo patrón en vez de los colores base de texto/fondo del sitio.

## 6. Reglas de contenido

- Todo el copy de cliente (misión, servicios, biografías, testimonios) debe ser texto real tomado de la web o los documentos de OVP — **nunca redactado desde cero por una IA**.
- Cualquier propuesta que reestructure o reagrupe contenido real (por ejemplo, la idea de 4 pilares de servicio) debe marcarse visualmente como propuesta, distinta del contenido actual del cliente.
- No se inventan casos de éxito, cifras de resultados, certificaciones ni logos de cliente que no estén confirmados.

## 7. Cómo usar esta guía

- **Para seguir iterando el diseño tú misma:** usa las tablas de color y tipografía como referencia directa de qué valores no se pueden cambiar.
- **Para briefear a Stitch o a Fable:** pega las secciones 1 a 5 como contexto de marca antes de pedir variaciones nuevas, así cualquier resultado nuevo se mantiene dentro del sistema visual de OVP.
- **Para explicarle a Alejandro o Ebony una decisión de diseño:** esta guía da la justificación (sección "Motivo"/"Uso") lista para convertir en una frase de respuesta si preguntan "¿por qué este color aquí?" o "¿por qué esta tipografía?".