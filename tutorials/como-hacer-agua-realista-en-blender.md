---
title: Como hacer Agua Realista en Blender
source: YouTube
url: https://www.youtube.com/watch?v=fB_F8x_59LA
author: MinerDesign
ingested: 2026-07-08
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/como-hacer-agua-realista-en-blender/
frame_count: 4
---

# Como hacer Agua Realista en Blender

**Source:** [YouTube](https://www.youtube.com/watch?v=fB_F8x_59LA)
**Author:** MinerDesign
**Duration:** 8m32s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Una gente que mandan el otro día subía esta animación y muchos me comentaron de que les enseñé cómo hacer el agua, así que vamos a hacer eso hoy. Es súper fácil, así que vamos a un archido de blender nuevo, voy a agregar un plano y lo voy a poner un modificador de su división y lo voy a atirlar el adaptativa y lo voy a dejar en simple. ¿Por qué? Para que no se derreonden las ziquinas. Vamos a dejar ahí, nos vamos a la vista render, vamos a ir al mundo y en color vamos a poner un sky texture, así tenemos una iluminación básica. Voy a traer acá el shader editor, hacemos un material nuevo, lo voy a poner agua y esto es súper sencillo. El principal lvdf le vamos a bajar el rófnis a punto 0,5 color. Como gusta un color bastante oscuro y apenas tirado hacia la azul capaz, depende del agua que estén haciendo, este tutorial va a ser como más agua de mar como lo hice en mi animación. Y en todo esto se va a pasar en distintos ruidos, que vamos a ir estaquiendo, o sea, poner uno sobre el otro y van a ir todos conectados al displacement. Así que vamos a poner un modo de displacement, lo vamos a conectar al displacement. Y acá en el hate vamos a conectar todas las nois textures. Hay como ven ya se ha agregado esto. La nois texture, vamos a poner en 4D, porque en 4D nos da este nuevo valor que lo que hace si lo vamos moviendo es que vaya cambiando con el tiempo. Lo voy a subir las calles y podemos hacerlo más. Si yo voy moviendo el wb van a arque, parece que estuera moviendo el agua. Y esto para no animarlo con keyframes que es mucho más fácil, vamos a escribir acá hashtag, beraym, barra, 2000 por ejemplo. Este número cuanto más grande sea menos se va a ir moviendo el número y cuanto menos sea más rápido se va a mover el número. Lo dejará ahí. También depende de los FPS que tengo su escena, yo lo dejaré en 30 y lo voy a dar a play. Ven que ahí se empieza a mover el agua de espacio. Y si yo acá escribo el número menor, por ejemplo 200, cambia más rápido el agua. Así que esto es un valor que lo pueden ajustar a ustedes, de uno que quieran, lo voy a dejar el mil por ahora. Otra cosa que me olvide acá en material properties, vamos a ir a settings y el displacement, acá lo cambiamos a displacement only. Y ahí ya en nuestro agua va a tener más relieve, ¿no? Lo voy a dar a Y esmos, así se ve bien suave. ¿Qué tanto se deforma el agua? Esto lo podemos seleccionar acá con el scale, aunque les voy a mostrar a lo que vamos a ir haciendo con todos los nois textur. Voy a llegar un nodo de más, lo ponemos después de la nois textur, y vamos a poner multiplais. La escala la voy a dejar en un número como punto 0.1, este número no lo voy a tocar más. Y es porque toda la escala de estos rudos la voy a controlar con cada multiplais. En este caso lo voy a subir un poco así se nota más, lo dejaré en 10, poner y voy a poner otra noo de más después de este y lo voy a poner en add. Porque en add, porque lo vamos a sumar a otro nois textur. Así que voy a dar a estos nodos, lo voy a duplicar, y lo voy a sumar con este. Básicamente, esto que hicimos acá es lo que voy a repetir. Todas las que se quiera para darle más detalle a nuestro mar. En este caso, a la segunda nois textur, obviamente no quiero que sea igual porque si no estamos como pacando el mismo ruido. Primero, cuando aplicamos nodos, se nos va a la expresión, así que la voy a volver a poner, la pone más rápida por ende. Y acá voy a subirle las calas, así tenemos un ruido más chico, por ejemplo. Y después, si veo que el ruido chico, este segundo ruido que ha llegado está muy fuerte. Con este multiplais, controlamos la fuerza de este ruido solo. Entonces, si yo le bajo, si yo lo pongo cero, no va a estar haciendo nada, y si le subo un poquito, vamos a servir ahí, que se empieza a notar. Por eso es una forma bastante copada de ir haciendo esto, porque puedo ir arregando todos los rudos que quieras, y vas controlando la fuerza de cada ruido con el multiplais. En vez de poner un número fijo acá. Otra cosa que podemos animar, que es bastante importante, voy a tocar un nodo de Nois Texture, y voy a poner Control T para agregar los nodos de MAPO. Y podemos poner esta misma expresión que hicimos acá, pero en la locación. Si yo animara la locación X, la expresión, vamos a ver que el agua parece que estuviera movéndose para allá. Entonces, podemos acá jugar con esto y hacer que el agua vaya para un lado particular, no? También lo puedes poner en la locación X y en la I, para que vaya en diagonal el agua, por ejemplo. Pero bueno, esto depende de lo que busques hacer, ¿no? La bueno de esto es que es procedural, así que si vos el plano lo necesitas hacer andar, lo va a grandar todo. Póyamente, como vieron ahí, yo lo grande en el modo deitar, y el ruido como que mantiene el mismo tamaño. Así que lo tendrías que volver a ajustar acá con la escala de los rudos. Capaz ahora siento que va muy rápido hacia allá, así que este número lo va a hacer más grande, lo voy a poner 2.000 y 1.000. Y ahora, literalmente, es lo mismo, pero yo he sumando rudos, poner el puedo duplicar este último. Yo los quiero sumar a estos, lo único que va a hacer es agregar un ad, ponerlo después del anterior y volver a conectar así. Entonces, así, poder seguir conectando rudos infinitamente. A este ruido, le voy a animar otra vez el W. Esto yo lo suelo hacer manual uno por uno, pero si quisieramos hacer que todos tengan el mismo, la misma animación, podemos agregar un nodo de válvio, ponerlo en la expresión a este nodo y este nodo conectarlo a 100 valores. Pero como algunos rudos son más grandes que otros, yo quiero controlar el W de cada uno, ¿no? Voy a hacer este bastante más chico, por ejemplo, ven a este, le quiero hacer el W que ha un valor más grande porque se mueve demasiado rápido. Y a lo que voy a hacer con este, por ejemplo, es ponerle los ojos de mapeo y no voy a animar nada de esto, pero voy a escalarlo en un eje para que quede un ruido más estirado. También a lo que pueden hacer es jugar con el nois texto como tal, le pueden poner más detalle, pero bueno, esto a ese genera como demasiado ruido, lo voy a subir a esto un poco más. Así que no solo jugar mucho con el detalle del Rufnes, lo solo dejar en lo base y simplemente jugar con las callas. Entonces, bueno, jugando con esto, nada, literalmente así fue que hice el mar, voy a agregar otro más, realmente hago esto, hago dos rudos base, después uno más chiquito y voy a aplicarlo y hacer uno más marcado, quizás, pero más grande. Recuerden, podemos tocar Control Shift, click en una nois texto para ver qué es lo que estamos haciendo. Algo que quizás a esta nois texto, lo quiero hacer es que tenga más contraste, así que podemos conectar una color RAM y hacer más así, llevar el negro para este lado, así tiene más contraste y a esta, también, animarle el dole V, como siempre. Y ahora tenemos un ruido más grande, que va a como marcar un poco más las zonas grandes, recuerren con este Multipliker, tienen todos los rudos, podemos ajustar las fuerzas, entonces nada, podemos hacer todo con esto, literal. Después, bueno, como es agua, ayuda mucho jugar con el material, o sea, con el material no paro con la luz, siempre recomiendo usar un HR ahí, que va muy lindo. Así que nada, pueden ir jugando con los rudos, ya verán como dos minutos hicimos un shader bastante ocupado. Cuando somos la sud decisión adaptativa, esto bueno, justamente se adapta, que tanto necesita dependiendo de los lejos o cerca de la cámara. Entonces, si yo me alejo mucho, la biché y desmuz para que se actualice esto, va a dar que tiene menos detalle. Si yo me acerco, venga, va creando sudivisiones, entonces depende de dónde lo estén viendo, también o eso. Si no quieren esto, pueden usar las sudiciones como tal del plano, pero bueno, menos óptimo. Voy a mostrarles acá, si yo su debido muchas veces este plano, ya me queda el detalle más marcado, pero es menos óptimo que usar el Adaptive Suddivision. Aunque la sudición adaptativa también es mejor cuando hacemos un render. Miren, los voy a dejar así, mano, mano. Fíjense de cuando hago el render, incluso la sudición adaptativa, que hago más detalle o prácticamente el mismo. Si tienen esta versión de blender, les recomiendo que usen la sudición adaptativa. Y bueno, no sé, me falta mencionar algo, pero es básicamente todo. Como ven el shader, casi que no hay que tocarlo, pueden cambiar los colores si eso si quieren, pero para un mar, ahí me gusta bastante. Así que, manejen ser ahí todo con el displacement. Ibi ya tiene displacement, así que debería funcionar en Ibi de todas formas. Se acá estamos en Ibi y funciona igual. Se ve un poco distinto, obviamente, pero funciona. Así que en la gente espero les haya servido, y cual cosa me consulten, tengo un vídeo más viejo también de cómo hacer agua, con básicamente el mismo procedimiento, pero bueno, se le jodó en la descripción por si les interesa, también. Así que nada, un abrazo a todos y nos vemos en que sigue. Chau-chau.

**Frame:** tutorials\frames\como-hacer-agua-realista-en-blender\frame_000.jpg
**Frame:** tutorials\frames\como-hacer-agua-realista-en-blender\frame_001.jpg
**Frame:** tutorials\frames\como-hacer-agua-realista-en-blender\frame_002.jpg
**Frame:** tutorials\frames\como-hacer-agua-realista-en-blender\frame_003.jpg


---

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### Nodes / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### Blender Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Tutorials
[PENDING EXTRACTION]
