(function (root) {
  "use strict";
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }
  function round1(x) { return Math.round(x * 10) / 10; }

  function pilePlan(lengthCm, widthCm, heightCm) {
    if (!(lengthCm > 0) || !(widthCm > 0) || !(heightCm > 0)) return { error: "the pile dimensions must be positive" };
    var liters = round1(lengthCm * widthCm * heightCm / 3 / 1000);
    var verdict;
    if (liters < 500) verdict = "a weekend pile";
    else if (liters <= 2000) verdict = "a truckload pile";
    else verdict = "a fleet pile";
    return { liters: liters, verdict: verdict };
  }

  function tripPlan(pileLiters, barrowLiters) {
    if (!(pileLiters > 0) || !(barrowLiters > 0)) return { error: "the pile and the barrow must be positive" };
    var trips = Math.ceil(pileLiters / barrowLiters);
    var lastLoad = round1(pileLiters - (trips - 1) * barrowLiters);
    var verdict;
    if (trips === 1) verdict = "one trip";
    else if (trips <= 6) verdict = "a short haul";
    else verdict = "a long haul";
    return { trips: trips, lastLoad: lastLoad, verdict: verdict };
  }

  function loadPlan(barrowLiters, densityKgPerL) {
    if (!(barrowLiters > 0) || !(densityKgPerL > 0)) return { error: "the barrow and the density must be positive" };
    var kg = round1(barrowLiters * densityKgPerL);
    var verdict;
    if (kg < 25) verdict = "a light load";
    else if (kg <= 60) verdict = "a working load";
    else verdict = "a heavy load";
    return { kg: kg, verdict: verdict };
  }

  function renderPile(r, lengthCm, widthCm, heightCm) {
    return "A pile " + lengthCm + " cm by " + widthCm + " cm by " + heightCm + " cm holds " + r.liters + " liters by the labeled cone rule - " + r.verdict + ".";
  }

  function renderTrip(r, pileLiters, barrowLiters) {
    return "A pile of " + pileLiters + " liters in a labeled " + barrowLiters + " liter barrow takes " + plural(r.trips, "trip") + ", the last one carrying " + r.lastLoad + " liters - " + r.verdict + ".";
  }

  function renderLoad(r, barrowLiters, densityKgPerL) {
    return "A labeled " + barrowLiters + " liter barrow at " + densityKgPerL + " kg a liter carries " + r.kg + " kg - " + r.verdict + ".";
  }

  var api = { pilePlan: pilePlan, tripPlan: tripPlan, loadPlan: loadPlan, renderPile: renderPile, renderTrip: renderTrip, renderLoad: renderLoad };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.WheelbarrowMath = api;
})(this);
