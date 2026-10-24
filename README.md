# referrer-attribution-bounds

## Français

Borner l’attribution possible des visites quand seules les marges sont connues.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m referrer_attribution_bounds examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

À partir de deux marges agrégées cohérentes, calcule les bornes de Fréchet de chaque intersection et fournit les couplages extrêmes agrégés. Montre ce qui reste impossible à attribuer sans jointure événementielle.

### Limites

Les deux marges doivent décrire le même total d’événements partitionnés. Aucune identité humaine, conversion causale ou adoption déduite de vues/téléchargements ; catégories inconnues à fournir explicitement.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Bound possible visit attribution when only aggregate margins are known.

Synthetic data; no network access or secret required.

```sh
python -m referrer_attribution_bounds examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

From consistent aggregate margins, computes Fréchet bounds for each intersection and supplies extreme collapsed couplings. Shows what cannot be attributed without event-level joins.

### Limits

Both margins must partition the same event total. No human identity, causal conversion or adoption inferred from views/downloads; unknown categories must be supplied explicitly.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Acotar atribución de visitas cuando solo se conocen marginales agregados.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m referrer_attribution_bounds examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Con márgenes agregados coherentes, calcula cotas de Fréchet para intersecciones y acoplamientos extremos agregados. Muestra lo que no puede atribuirse sin unión de eventos.

### Límites

Ambos márgenes deben particionar el mismo total de eventos. No infiere identidad humana, conversión causal o adopción de vistas/descargas; categorías desconocidas explícitas.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.itl.nist.gov/div898/handbook/eda/section3/eda35b.htm
