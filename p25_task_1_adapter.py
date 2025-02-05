"""Úkol 1 - Adaptér

Pomocí vzoru Adaptér zapište wrapper pro seznam tak,
aby se rozhraní pro klienta skládalo z metod push, pop a is_empty.

Vytvořte dvě implementace:
- založené na objektovém adaptéru - použijte objektové skládání
- na základě adaptéru třídy - pomocí vícenásobné dědičnosti přizpůsobíte
rozhraní seznamu očekávanému rozhraní zásobníku

Vytvořené implementace použijte k výpočtu výrazů uvedených v obrácené polské notaci (RPN):

    '2 7 + 3 / 14 3 - 4 * + 2 /'  -> (((2 + 7) / 3) + ((14 - 3) * 4)) / 2
    '12 2 3 4 * 10 5 / + * +'     -> 12 + (2 * ((3 * 4) + (10 / 5)))
    '5 1 2 + 4 * + 3 -'

Poznámka:
prefixová notace:
+ 2 6  -> 2 + 6
"""