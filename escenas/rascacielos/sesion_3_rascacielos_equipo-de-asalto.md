# Equipo de asalto

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Consideraciones](#consideraciones)
- [Descripcion del edificio](#descripcion-del-edificio)
- [Planta 0](#planta-0)
- [Planta 1-43](#planta-1-43)
- [Planta 44](#planta-44)
- [Planta 45](#planta-45)
- [Planta 46](#planta-46)
- [Eventos Críticos](#eventos-cr%C3%ADticos)
  - [Evento critico de alarma](#evento-critico-de-alarma)
- [PNJs](#pnjs)
  - [Recepcion](#recepcion)
      - [C, Personal de recepcion (humano)](#c-personal-de-recepcion-humano)
      - [B1, Personal de Seguridad 1 (Ghoul)](#b1-personal-de-seguridad-1-ghoul)
      - [B2, Personal de Seguridad 2 (Ghoul)](#b2-personal-de-seguridad-2-ghoul)
      - [Coberturas (Para enemigos)](#coberturas-para-enemigos)
  - [Planta 44](#planta-44-1)
    - [Carne de cañon](#carne-de-ca%C3%B1on)
      - [H1, Soldados tipo 1](#h1-soldados-tipo-1)
      - [H2, Soldados tipo 2](#h2-soldados-tipo-2)
      - [H3, Soldados tipo 3](#h3-soldados-tipo-3)
    - [Lugartenientes Vampiros](#lugartenientes-vampiros)
      - [G1, NON MELEE, Vampiro tipo 1](#g1-non-melee-vampiro-tipo-1)
      - [G2, MELEE, Vampiro tipo 2](#g2-melee-vampiro-tipo-2)
      - [G3, MELEE, Vampiro tipo 3](#g3-melee-vampiro-tipo-3)
      - [Features](#features)
  - [Planta 45](#planta-45-1)
    - [Equipo Elite de seguridad](#equipo-elite-de-seguridad)
    - [Lugartenientes Vampiros (melee)](#lugartenientes-vampiros-melee)
      - [K1, NON MELEE,  Vampiro tipo 1](#k1-non-melee--vampiro-tipo-1)
      - [K2, NON MELEE, Vampiro tipo 2](#k2-non-melee-vampiro-tipo-2)
      - [K3, MELEE, Vampiro tipo 3](#k3-melee-vampiro-tipo-3)
      - [Features](#features-1)
  - [Planta 46](#planta-46-1)
    - [Hombres lobo](#hombres-lobo)
      - [M1, Hombre lobo elite 1](#m1-hombre-lobo-elite-1)
      - [M2, Hombre lobo elite 2](#m2-hombre-lobo-elite-2)
      - [Features](#features-2)
    - [Concubines](#concubines)
      - [L, Concubina 1](#l-concubina-1)
      - [L, Concubina 2](#l-concubina-2)
      - [L, Concubino 1](#l-concubino-1)
      - [L, Concubino 2](#l-concubino-2)
      - [Features](#features-3)
    - [X, Helmut Neumeyer (aka Kuzma El Empalador)](#x-helmut-neumeyer-aka-kuzma-el-empalador)
      - [Features](#features-4)
- [Mapa](#mapa)
- [Equipo](#equipo)
- [Mesh](#mesh)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Consideraciones

* La idea original es rollo SWAT
* Dejar a los PJs decidir como proceder
* En un principio deberia ser algo asi:
    * **Muy importante:** Esperar en un furgon a que el equipo de mantenimiento desactive comunicaciones internas
    * Entrar en plan *The Matrix*
        * Cada X turnos evento de refuerzos **TODO: Revisar**
    * **TODO: Revisar** Ir subiendo:
        * Del tiron si el equipo de mantenimiento apaño los ascensores
        * Poco a poco si va mas lento
        * **Opcional** Los ascensores tienen GRIT, como mucho pueden recibir X ataques?

## Descripcion del edificio

* Edificio acristalado
* Cristales bastante opacos de visibilidad (transparente pero oscuros)

## Planta 0

* Los PJs tienen que entrar a saco
* **A**, La puerta giratoria 
    * Solo permite el paso de 2 en 2
    * Pueden volarla con una granada y entonces podran entrar los 4 a la vez
        * Esto se les tiene que ocurrir a los PJs, si hacen esto, pillaran por sorpresa al personal del piso y podran hacer 1 accion con +1 los 4 (piece of cake)
* Segun pasen de la puerta
    * El de seguridad les empezara a disparar
    * El de recepcion gastara reaction para llamar refuerzos
        * **Ventaja: Si las comunicaciones internas no funcionan, NO PODRA LLAMAR REFUERZOS**
    * Si el de recepcion llama a refuerzos cada 5 turnos (revisar cuanto les cuesta matar a los PJs), vendran 2 guardas por las escaleras **F**
    * Si el de recepcion no puede llamar a refuerzos pero estan las camaras de seguridad activas vendran cada 5 + 2 turnos por las escaleras **F**
    * Si el de recepcion no puede llamar a refuerzos y no estan las camaras de seguridad activas vendran cada 5 + 2 + 2 turnos por las escaleras **F**
* En el ascensor
    * Las plantas hasta 44 funcionan normalmente
    * La planta 45 es un boton especial: Los personajes tiran `FOCUS + DETECT CRITICAL`
        * Requiere una autenticacion biometrica
        * Si no han superado la tirada y a los pjs se les ocurre pulsar al boton a ver que pasa, o intentan hackearlo (`FOCUS + FIX IMPOSIBLE`), sonara una alarma y dispararan **Evento critico de alarma**
        * **Ventaja: Solo pueden subir directamente si se han hecho con el control de la sala de mantenimiento**
* **Avisar al equipo de mantenimiento**

## Planta 1-43

* Oficinas sin interes, un par de agentes del servicio de seguridad, personal administrativo

## Planta 44

* **Ventaja: Si las comunicaciones internas no funcionan, les pillaran desprevenidos**
    * **2 X Action Roll** antes del primer **Reaction Roll**
* **H1**, **Carne de cañon** soldados tipo 1
* **H2**, **Carne de cañon** soldados tipo 2
* **H3**, **Carne de cañon** soldados tipo 3
    * **Ventaja: Reduce cantidad si mantenimiento se ha ocupado de las camaras**
* **G1**, Lugarteniente Vampiro tipo 1
* **G2**, Lugarteniente Vampiro tipo 2 
* **G3**, Lugarteniente Vampiro tipo 3 
    **Solo si se disparo el `Evento critico de alarma`**
* **Avisar al equipo de mantenimiento**

## Planta 45

**Nota: Aqui deberian estar ya los 8 juntos si mantenimiento ha conseguido solucionar rapido**

* Enemigos esperando **SIEMPRE**
* **J1**, Equipo elite de seguridad
* **J2**, Equipo elite de seguridad
* **J3**, Equipo elite de seguridad
    * **Solo si se disparo el `Evento critico de alarma`** ó estan los 8 personajes juntos
* **J4**, Equipo elite de seguridad
    * **Solo si se disparo el `Evento critico de alarma`** ó estan los 8 personajes juntos
* **K1**, Lugarteniente Vampiro tipo 1
* **K2**, Lugarteniente Vampiro tipo 2
* **K3**, Lugarteniente Vampiro tipo 3 
    * **Solo si se disparo el `Evento critico de alarma`** ó estan los 8 personajes juntos

## Planta 46

**Nota: Aqui deberian estar ya los 8 juntos SIEMPRE (Si no lo estan, tienen que esperar)**

* **X**, **Kuzma** se encuentra debajo de una cascada de sangre (+12 a adrenalina) con una espada en una mano desnudo de cintura para arriba, pelo largo negro, diversos tatuajes tribales por el pecho, en la espalda unas alas de murcielago recogidas
* En cuanto lleguen los pjs:
    * Dialogo cool
    * Atacar (priorizando al pj con el fenix de jade) a uno de ellos con la espada
    * Despues ir salteando entre las features y special actions que tiene segun convenga
* **M1**, Hombre lobo elite 1
* **M2**, Hombre lobo elite 2
* **L1**, Concubina Vampiro 1
* **L2**, Concubina Vampiro 2
* **L3**, Concubino Vampiro 1
* **L4**, Concubino Vampiro 2

## Eventos Críticos

### Evento critico de alarma

Si se dispara este evento, los enemigos estaran preparados esperando en la salida de los ascensores y las escaleras estaran bloqueadas.

Ademas añade un lugarteniente vampiro a las plantas 44 y 45

## PNJs

### Recepcion

##### C, Personal de recepcion (humano)

**(Cobertura mostrador de recepcion)**

- **ATTACK**: `BASIC`
- **DEFENSE**: `BASIC`
- **GRIT**: `[ ]-[ ]-[ ]-[ ]`

##### B1, Personal de Seguridad 1 (Ghoul)

**(Cobertura Arco de deteccion y escaneo de maletas)**

- **ATTACK**: `CRITICAL`
- **DEFENSE**: `BASIC`
- **GRIT**: `[ ]-[ ]-[ ]-[ ]-[ ]`

##### B2, Personal de Seguridad 2 (Ghoul)

- **ATTACK**: `CRITICAL`
- **DEFENSE**: `BASIC`
- **GRIT**: `[ ]-[ ]-[ ]-[ ]-[ ]`

##### Coberturas (Para enemigos)

**Nota: No muy ituitivo pero es igual que si fuera para amigos**

* +1 Reaction
* -1 Action

### Planta 44

#### Carne de cañon

##### H1, Soldados tipo 1

- **ATTACK**: `2 BASIC`
- **DEFENSE**: `BASIC`
- **GRIT**: `[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]`

##### H2, Soldados tipo 2

- **ATTACK**: `2 BASIC`
- **DEFENSE**: `BASIC`
- **GRIT**: `[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]`

##### H3, Soldados tipo 3

- **ATTACK**: `2 BASIC`
- **DEFENSE**: `BASIC`
- **GRIT**: `[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]`

#### Lugartenientes Vampiros

##### G1, NON MELEE, Vampiro tipo 1

- **ATTACK**: `CRITICAL`
- **DEFENSE**: `CRITICAL`
- **GRIT**: `[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]`

##### G2, MELEE, Vampiro tipo 2

- **ATTACK**: `CRITICAL`
- **DEFENSE**: `CRITICAL`
- **GRIT**: `[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]`

##### G3, MELEE, Vampiro tipo 3

- **ATTACK**: `CRITICAL`
- **DEFENSE**: `CRITICAL`
- **GRIT**: `[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]`

##### Features

**MELEE: FIGHTERS (ENEMY FEATS, 1 FP)**

The Enemies are experts in hand-to-hand combat.

Heroes suffer -1 when rolling to hit the Enemy without firearms or ranged weapons.

**NON MELEE: AUTOMATIC WEAPONS (ENEMY FEATS, 1 FP)**

The Enemies are armed with tommy guns or similar automatic weapons.

Heroes who fail to score at least a Basic Success during their Reaction Turn become Nervous. If they are already Nervous, they lose 1 additional Grit.

**BEAST (MIDNIGHT WARS, ENEMY FEATS, 2 FP)**

The Enemy are werewolves in their beast form, or other similar wild creatures.

Attacking the Enemy while in Melee or Close Range requires an Action Roll (💀).

Heroes suffer -1 when rolling to hit the Enemy with firearms or ranged weapons.


### Planta 45

#### Equipo Elite de seguridad

**J1, Elite de seguridad 1**

- **ATTACK**: `CRITICAL`
- **DEFENSE**: `CRITICAL`
- **GRIT**: `[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]`

**J2, Elite de seguridad 2**

- **ATTACK**: `CRITICAL`
- **DEFENSE**: `CRITICAL`
- **GRIT**: `[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]`

**J3, Elite de seguridad 3**

- **ATTACK**: `CRITICAL`
- **DEFENSE**: `CRITICAL`
- **GRIT**: `[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]`

**J4, Elite de seguridad 4**

- **ATTACK**: `CRITICAL`
- **DEFENSE**: `CRITICAL`
- **GRIT**: `[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]`


#### Lugartenientes Vampiros (melee)

##### K1, NON MELEE,  Vampiro tipo 1

- **ATTACK**: `CRITICAL`
- **DEFENSE**: `CRITICAL`
- **GRIT**: `[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]`

##### K2, NON MELEE, Vampiro tipo 2

- **ATTACK**: `CRITICAL`
- **DEFENSE**: `CRITICAL`
- **GRIT**: `[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]`

##### K3, MELEE, Vampiro tipo 3

- **ATTACK**: `CRITICAL`
- **DEFENSE**: `CRITICAL`
- **GRIT**: `[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]`

##### Features

**MELEE: FIGHTERS (ENEMY FEATS, 1 FP)**

The Enemies are experts in hand-to-hand combat.

Heroes suffer -1 when rolling to hit the Enemy without firearms or ranged weapons.

**NON MELEE: AUTOMATIC WEAPONS (ENEMY FEATS, 1 FP)**

The Enemies are armed with tommy guns or similar automatic weapons.

Heroes who fail to score at least a Basic Success during their Reaction Turn become Nervous. If they are already Nervous, they lose 1 additional Grit.

**BEAST (MIDNIGHT WARS, ENEMY FEATS, 2 FP)**

The Enemy are werewolves in their beast form, or other similar wild creatures.

Attacking the Enemy while in Melee or Close Range requires an Action Roll (💀).

Heroes suffer -1 when rolling to hit the Enemy with firearms or ranged weapons.

#### Atsumi Kia

- **ATTACK**: CRITICAL
- **DEFENSE**: CRITICAL
- **GRIT**: `[ ]-[ ]-[ ]-< >-[ ]-[ ]-[ ]-< >-[ ]`

TODO: Completar habilidades

### Planta 46

#### Hombres lobo

##### M1, Hombre lobo elite 1

- **ATTACK**: `CRITICAL`
- **DEFENSE**: `CRITICAL`
- **GRIT**: `[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]`

##### M2, Hombre lobo elite 2

- **ATTACK**: `CRITICAL`
- **DEFENSE**: `CRITICAL`
- **GRIT**: `[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]-[ ]`

##### Features

**TACTICS (ENEMY FEATS, 1 FP)**

The Enemies are well trained individuals who skillfully move through the battlefield. Real pros.

When a Hero wants to use a Quick Action to get closer or farther from the Enemy, they must flip a coin. 
* Heads: the Enemy anticipates the move, the range doesn’t change, and the Hero loses their action.
* Tails: the Hero repositions successfully.

**MARTIAL ARTS (ENEMY FEATS, 2 FP)**

The Enemies are skilled martial artists who perform acrobatic kicks and menacing war-cries.

All Heroes who cannot rely on the Martial Arts Feat suffer -1 to their Action and Reaction Rolls against the Enemy while in Melee or Close Range.

**BEAST (MIDNIGHT WARS, ENEMY FEATS, 2 FP)**

The Enemy are werewolves in their beast form, or other similar wild creatures.

Attacking the Enemy while in Melee or Close Range requires an Action Roll (💀).

Heroes suffer -1 when rolling to hit the Enemy with firearms or ranged weapons.

#### Concubines

* Atacan en formacion despues de kuzma
* Se curan entre ellos
* Ataca a los pjs con menos lucha (son debiles)

##### L, Concubina 1

- **ATTACK**: `CRITICAL`
- **DEFENSE**: `BASIC`
- **GRIT**: `[ ]-[ ]-[ ]-[ ]`

##### L, Concubina 2

- **ATTACK**: `CRITICAL`
- **DEFENSE**: `BASIC`
- **GRIT**: `[ ]-[ ]-[ ]-[ ]`


##### L, Concubino 3

- **ATTACK**: `CRITICAL`
- **DEFENSE**: `BASIC`
- **GRIT**: `[ ]-[ ]-[ ]-[ ]`


##### L, Concubino 4

- **ATTACK**: `CRITICAL`
- **DEFENSE**: `BASIC`
- **GRIT**: `[ ]-[ ]-[ ]-[ ]`

##### Features

**MEDKIT (ENEMY FEATS, 2 FP)**

The Enemies carry experimental medicines, combat drugs, or syringes of adrenaline. Just a “little help” to keep on fighting.

When they lose all Grit, the Enemies immediately gain 1 additional Grit and get back into the fray.

**ONE STEP AHEAD (ENEMY FEATS, 2 FP)**

The Enemies are in perfect formation and can always rely on each-other, or they are fighting on their home-turf and know the lay of the land. 

They leave nothing to chance.

The Enemies have no Weak Spot. If a Hero tries to find the Enemy’s Weak Spot and succeeds, they immediately realize there is none and lose 1 Grit due to the disheartening discovery.

#### X, Helmut Neumeyer (aka Kuzma El Empalador)

* Boss final
* Viejo y poderoso vampiro ucraniano.  
* Vampiro espadachín.  
* Está detrás de múltiples empresas internacionales.
* Vampiro que tiene una habilidad de control mental.

Empieza con 16 ⚡

- **ATTACK**: 2 CRITICAL
- **DEFENSE**: 2 CRITICAL
- **GRIT**: `[ ]-[ ]-[ ]-< >-[ ]-[ ]-< >-[ ]-< >-[ ]-< >-[ ]`

##### Features

**IMMORTAL (MIDNIGHT WARS, ENEMY FEATS, 3 FP)**

The Enemy is an ancient being, almost impossible to kill.

Common weapons and bare-handed attacks have no effect on the Enemy.

The Heroes can only wound them when using weapons or bullets the Enemy is vulnerable to.


**SHARP BLADES (ENEMY FEATS, 1 FP)**

The Enemies are armed with knives, claws, or sharp swords.

Heroes who fail to score at least a Basic Success during their Reaction Turn become Hurt. If they are already Hurt, they lose 1 additional Grit.

Heroes with kives or swords ignore this Feat.


**DARK GIFT (MIDNIGHT WARS, SPECIAL ACTION, Cost 3 ⚡)**

The Enemy infects a Hero with their curse. Maybe as a punishment, maybe by mistake. The Hero adds 2 Lethal Bullets to their Death Roulette, and they must take a spin on the Death Roulette.

If the Hero survives, they immediately gain the Damned Feat.

**DARK INFLUENCE (MIDNIGHT WARS, SPECIAL ACTION, Cost 2 ⚡)**

The Enemy locks eyes with a Hero or charms a Hero with the sound of their voice.

The Director rolls a numeric die:
1. The Hero is locked in a waking nightmare. (They skip the next Action Turn and become Nervous.)
2. The Hero becomes Angry and attacks an ally. (Another Hero risks losing 3 Grit.)
3. The Hero is charmed. (They become Distracted and suffer -1 when attacking the Enemy.)
4. The Hero has flashing visions. (They skip the next Action Turn and become Confused.)
5. The Hero is paralyzed by panic. (They skip the next Action Turn and become Scared.)
6. The Hero cannot control their body and is forced to harm themselves. (They become Hurt.)

**BLOODSUCKING (MIDNIGHT WARS, SPECIAL ACTION, Cost 2 ⚡)**

**Nota: si van muy sobrados para que dure algo mas**

The Enemy grabs a Hero and drains them of blood or vital energy.

The Director rolls a numeric die. A Hero loses an amount of Grit equal to the result of the roll, and the Enemy recovers the same amount of Grit.

## Resumen de combate del 23 de julio de 2024, como se cargaron a Kuzma en un turno
* Segun subieron los 4 heroes por las escaleras ataco a *Brenan* (que era la que tenia el amuleto)
* *Palomo III*, se dio cuenta que tenia **Get Down** y gasto un punto de adrenalina para salvar a *Brenan* (**PALOMO!!!!**)
* *Subotai*, gasto spotlight y gasto 2 de adrenalina para hacer daño extra **Total 11 (deja a Kuzma a 1 punto de vida)**
* *Jessica* ataca a *Kuzma*:
    * lanza una tirada **2 basic**, 
    * hace free re-roll **critical + basic**
    * all in **extreme + basic**
* Kuzma muere

## Mapa

![Mapa plantas superiores](./imgs/rascacielos_niveles_superiores.png)

* **A**: puerta giratoria (bastante opaca... no veran a nadie entrar hasta que este dentro, pueden ir de 2 en 2)
* **B1**: Personal de Seguridad CRITICAL
    * Arco de deteccion y escaneo de maletas (cobertura)
* **B2**: Personal de Seguridad CRITICAL
* **C**: Personal de Recepcion BASIC
    * Mostrador de recepcion (cobertura)
* **D**: Ascensores de subida
* **E**: Ascensores de mantenimiento y servicio
* **F**: Escaleras
* **G**: Lugar teniente vampiro 
* **H1**: Soldados tipo 1
* **H2**: Soldados tipo 2
* **H3**: Soldados tipo 3
* **I**: Escaleras que conectan plantas 45 y 46
* **J**: Equipo elite de seguridad
* **K1**: Lugarteniente vampiro 1
* **K2**: Lugarteniente vampiro 2
* **K3**: Lugarteniente vampiro 3
* **L**: Cama de Kuzma con sus concubines
* **M1**: Hombre lobo elite 1
* **M2**: Hombre lobo elite 2
* **X**: Kuzma

## Equipo

* Kevlar `BRAWN 2`
* Armas automaticas `todos` anti vampiros
* Cargadores
    * 3 + 1 en el arma `BRAWN 2`
    * 5 + 1 en el arma `BRAWN 3`
* 2x Granadas de fragmentacion
* 2x Granadas de conmocion? (flash light granade)

## Mesh

* AK-47 - Wikipedia, la enciclopedia libre
    * Especificaciones ; Peso, 3,8 kg (descargado) 4,3 kg (cargado) ; Longitud, 870 mm ; Longitud del cañón, 415 mm ; Munición · 7,62 x 39 .22 Long Rifle
