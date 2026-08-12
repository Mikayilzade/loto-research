# Azərlotereya archive/API discovery

Updated: 2026-08-12
Status: **endpoint not discovered; do not guess undocumented URLs**

## Objective
Recover the official historical payload behind client-rendered draw archive pages so 4+4 draw/payout history can be collected reproducibly without relying on search-engine indexing or secondary archives.

## Confirmed frontend behavior
Primary operator pages show two different behaviors:

- `https://www.azerlotereya.com/lotereya-neticeleri` renders current draw data server/index-visible, including draw number, date and winning numbers.
- `https://www.azerlotereya.com/neticeler/4-4` renders the archive shell but crawler-visible output contains `Tiraj undefined`.
- the current 4+4 game page has also intermittently exposed `Invalid Date` / missing latest-result values in crawler output while the dedicated current-results page remains populated.

This strongly suggests that at least part of the archive/game-state data is loaded client-side or through a request path not executed by the search crawler.

## Bounded discovery attempts completed
The following avenues were tried and should not simply be repeated in a future chat without new tooling/evidence:

1. official-domain search for likely strings:
   - `api`
   - `drawNo`
   - `lotteryId`
   - `fourplus`
   - exact current draw numbers such as 26312/26332
2. attempts to surface `robots.txt`, `sitemap.xml`, and sitemap-index endpoints through the web-search/open interface;
3. inspection of parsed current-results and archive pages for exposed links/endpoints;
4. search for likely hostnames such as `api.azerlotereya.com`, Swagger references and `/api/` URLs;
5. public GitHub repository search for `azerlotereya` and `Kartega Azerlotereya`;
6. local/container direct-network approach was previously blocked by DNS/network limitations in this environment.

No authoritative archive endpoint or request schema was recovered.

## Infrastructure clue
A public post by a participant in the website revamp credits Şanstech and Kartega Yazılım ve Danışmanlık A.Ş. for the new Azerlotereya.com implementation and separately mentions CMS/design architecture. This is only an implementation lead; it does **not** identify the data endpoint and should not be treated as a primary rule/data source.

## Important current-results observation
The primary current-results page remains useful as an official reconciliation anchor. On 2026-08-12 it exposed the latest televised draw as draw **26332**, dated **11.08.2026 18:45**, including 4+4 A/B winning numbers.

Historical archive ingestion still requires another route.

## Recommended next technical route
Do not continue blind URL guessing. High-leverage options are:

1. inspect browser DevTools Network requests manually during archive search, then provide the request URL/response shape to the repo;
2. use a future browser/network-capable tool that can expose script/XHR/fetch calls from the live page;
3. obtain a saved HAR/network log from a normal browser session;
4. recover historical results through secondary archives in a normalized dataset, then reconcile sampled rows against official current/winner/news pages until the primary endpoint is available.

## Research consequence
Until the official archive payload is found:
- secondary historical draw tables may be used as **reconstruction evidence**, not authoritative truth;
- primary official winner stories/news/current results should be used for cross-checks;
- no guessed endpoint should be committed as a collector dependency.
