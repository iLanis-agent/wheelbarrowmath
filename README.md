# Wheelbarrow math

Wheelbarrow math plans the haul before the first shovel: the pile's
dimensions become liters by a labeled cone rule, the liters become the
trip count with the last load honest, and the barrow with a labeled
density becomes the kilograms each trip carries.

Live site: https://ilanis-agent.github.io/wheelbarrowmath/

## The three tools

- **Pile plan** - `length x width x height / 3` (the labeled cone
  rule) in liters, with a weekend / truckload / fleet pile verdict.
- **Trip plan** - `ceil(pile / barrow)` trips and the load on the last
  trip, with a one trip / short haul / long haul verdict.
- **Load plan** - `barrow x density` kilograms a trip, with a light /
  working / heavy load verdict.

## Limits

Every default is labeled and illustrative. Real piles slump and settle,
and real material changes with moisture. This is planning arithmetic,
not a weighing or a strength rating: lift within your own comfort and
the barrow's rated capacity.

## Files

- `index.html` - landing page with the labeled norms
- `app.html` - the three calculators
- `engine.js` - shared calculation and render logic (browser + node)
- `oracle.py` - python mirror of the engine, writes `expected.json`
- `test.js` - runs the engine against `expected.json` (30 cases, 137 checks)

Run the tests: `python3 oracle.py && node test.js`
