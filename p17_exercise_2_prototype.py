"""Prototype – Klonování uživatelských šablon
Vytvoř systém pro správu uživatelských šablon, kde každá šablona obsahuje
předdefinovaná nastavení (např. barvy, fonty, rozložení).
Použij návrhový vzor Prototype, aby bylo možné efektivně klonovat existující
šablony a upravit jejich parametry bez nutnosti vytvářet je od nuly.

Požadavky:
- Vytvoř třídu Template, která bude obsahovat atributy jako název šablony,
barva pozadí, font, rozložení prvků.
- Implementuj metodu clone(), která vrátí kopii existující šablony s
možností modifikace atributů.
- Ověř, že klonování je hluboké (změna hodnot v kopii neovlivní originál).
- Umožni jednoduchou správu šablon pomocí seznamu (TemplateManager), kde bude
možné šablony vytvářet, klonovat a upravovat."""